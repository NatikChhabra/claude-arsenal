#!/usr/bin/env python3
"""listening_taste.py: what the owner really listens to, read from a desktop music player's local cache, so taste
questions ("what kind of music do you play?") are answered from evidence, not from a list typed from memory.
Used by gear-pick (which guitar suits his music).

    python listening_taste.py <feishin-user-data-dir | file ...> [--json out.json] [--top 25]
    (%APPDATA% and ~ are expanded, so "%APPDATA%/feishin" works from any shell when quoted)
    python listening_taste.py --selftest

Reads Feishin (the Navidrome / Jellyfin / Subsonic desktop client). Its user data folder is %APPDATA%\\feishin on
Windows, ~/.config/feishin on Linux, ~/Library/Application Support/feishin on macOS. Two places hold songs:
  - IndexedDB/*.leveldb/*.log|*.ldb  : the play queue as JSON (title, artist, play count, last played, favourite)
  - IndexedDB/*.blob/**              : the query cache (Chromium wraps it as 0xFF 0x11 0x02 + raw Snappy, inside is a
                                       V8-serialized object); its lyrics queries carry artist + title for every song
                                       played with lyrics on, so it is the best "recently played" list
Pass the whole folder (it walks those two places) or single files copied out of it. LevelDB is read properly: .log
records are rejoined across 32 KiB blocks and .ldb tables have their Snappy blocks decoded, so the queue survives a
compaction. The queue JSON is read as the V8 string it is stored as (Latin-1 or UTF-16), so "Peña" and Hindi titles
survive. Stdlib only (a small Snappy decoder is built in). Read-only. Prints songs (play count where known), then artists by number of songs.
Exit 0 when at least one song was found, 1 when none (wrong folder, or the cache was cleared).
Server-side play counts (Navidrome's own database) are better still when the server is reachable; this tool is for
when it is not (a home server over a VPN, a phone, a friend's box).
"""
import json, os, re, sys
from collections import Counter


# ---------- Snappy (raw block format) ----------
def _varint(b, i):
    r = s = 0
    while True:
        x = b[i]
        i += 1
        r |= (x & 0x7F) << s
        s += 7
        if x < 0x80:
            return r, i


class SnappyError(ValueError):
    def __init__(self, msg, partial=b""):
        super().__init__(msg)
        self.partial = partial


def snappy_raw(b):
    """Decode one raw Snappy block. Raises SnappyError (with .partial = bytes decoded so far) on malformed input."""
    out = bytearray()
    try:
        return _snappy(b, out)
    except IndexError:
        raise SnappyError("truncated input", bytes(out))
    except ValueError as e:
        raise SnappyError(str(e), bytes(out))


def _snappy(b, out):
    n, i = _varint(b, 0)
    if n > 512 * 1024 * 1024:
        raise ValueError("implausible length")
    L = len(b)
    while i < L:
        tag = b[i]
        i += 1
        kind = tag & 3
        if kind == 0:  # literal
            ln = tag >> 2
            if ln >= 60:
                k = ln - 59
                if i + k > L:
                    raise ValueError("truncated literal length")
                ln = int.from_bytes(b[i:i + k], "little")
                i += k
            ln += 1
            if i + ln > L:
                out += b[i:L]  # keep what is there, for a partial scan
                raise ValueError("truncated literal")
            out += b[i:i + ln]
            i += ln
            continue
        if kind == 1:
            ln = ((tag >> 2) & 7) + 4
            if i >= L:
                raise ValueError("truncated copy")
            off = ((tag >> 5) << 8) | b[i]
            i += 1
        elif kind == 2:
            ln = (tag >> 2) + 1
            if i + 2 > L:
                raise ValueError("truncated copy")
            off = int.from_bytes(b[i:i + 2], "little")
            i += 2
        else:
            ln = (tag >> 2) + 1
            if i + 4 > L:
                raise ValueError("truncated copy")
            off = int.from_bytes(b[i:i + 4], "little")
            i += 4
        if off == 0 or off > len(out):
            raise ValueError("bad copy offset")
        start = len(out) - off
        if off >= ln:
            out += out[start:start + ln]
        else:  # overlapping copy: byte by byte
            for j in range(ln):
                out.append(out[start + j])
        if len(out) > n:
            raise ValueError("output longer than header")
    if len(out) != n:
        raise ValueError("length mismatch")
    return bytes(out)


def unwrap(b, name="blob"):
    """The bytes worth scanning in an IndexedDB blob. Chromium writes 0xFF <version> 0x02 then raw Snappy; older or
    small values are stored plain. Compressed bytes are never scanned as text (that yields half-literal ghosts such
    as "Sailor Son"): a truncated Snappy body (a copy taken mid-write) is scanned as far as it decodes, with a warning."""
    wrapped = len(b) > 3 and b[0] == 0xFF and b[2] == 0x02
    if wrapped:
        try:
            return snappy_raw(b[3:])
        except SnappyError as e:
            if len(e.partial) > 0:
                print(f"warning: {name}: Snappy body cut short ({e}); scanned the first {len(e.partial)} bytes",
                      file=sys.stderr)
                return e.partial
            print(f"warning: {name}: Snappy body unreadable ({e}); skipped", file=sys.stderr)
            return b""
    for off in range(0, 9):  # unwrapped Snappy (a blob copied without its envelope)
        if off >= len(b):
            break
        try:
            return snappy_raw(b[off:])
        except SnappyError:
            continue
    return b


# ---------- LevelDB (.log write-ahead log and .ldb tables) ----------
LOG_BLOCK = 32768
LDB_MAGIC = bytes.fromhex("57fb808b247547db")


def leveldb_log(b):
    """Whole records from a LevelDB .log: 32 KiB blocks, each record fragment has a 7-byte header (crc32, length,
    type FULL=1 FIRST=2 MIDDLE=3 LAST=4). Fragments are rejoined so a value never has a header inside it."""
    recs, cur, i, L = [], bytearray(), 0, len(b)
    while i + 7 <= L:
        left = LOG_BLOCK - (i % LOG_BLOCK)
        if left < 7:  # block trailer padding
            i += left
            continue
        ln = b[i + 4] | (b[i + 5] << 8)
        typ = b[i + 6]
        frag = b[i + 7:i + 7 + ln]
        i += 7 + ln
        if typ == 0 and ln == 0:  # zero padding (preallocated tail)
            i += LOG_BLOCK - (i % LOG_BLOCK) if i % LOG_BLOCK else 0
            continue
        if typ == 1:
            recs.append(bytes(frag))
            cur = bytearray()
        elif typ == 2:
            cur = bytearray(frag)
        elif typ == 3:
            cur += frag
        elif typ == 4:
            cur += frag
            recs.append(bytes(cur))
            cur = bytearray()
        else:  # unknown type: stop rather than read garbage
            break
    return b"\x00".join(recs)


def _block(b, off, size):
    raw = b[off:off + size]
    if off + size < len(b) and b[off + size] == 1:
        raw = snappy_raw(raw)
    return raw


def _entries(block):
    if len(block) < 4:
        return
    nrest = int.from_bytes(block[-4:], "little")
    end = len(block) - 4 - 4 * nrest
    i, key = 0, b""
    while 0 <= i < end:
        shared, i = _varint(block, i)
        nonshared, i = _varint(block, i)
        vlen, i = _varint(block, i)
        key = key[:shared] + block[i:i + nonshared]
        i += nonshared
        yield key, block[i:i + vlen]
        i += vlen


def leveldb_table(b, name="table"):
    """Every value in a LevelDB .ldb table: footer (last 48 bytes, magic checked) -> index block -> data blocks,
    each Snappy-decoded when its trailer type is 1. Returns the values joined, or b"" when it is not a table."""
    if len(b) < 48 or b[-8:] != LDB_MAGIC:
        return b""
    try:
        f = b[-48:]
        _, i = _varint(f, 0)
        _, i = _varint(f, i)
        ioff, i = _varint(f, i)
        isize, i = _varint(f, i)
        vals = []
        for _, handle in _entries(_block(b, ioff, isize)):
            doff, j = _varint(handle, 0)
            dsize, _ = _varint(handle, j)
            for _, v in _entries(_block(b, doff, dsize)):
                vals.append(v)
        return b"\x00".join(vals)
    except (ValueError, IndexError) as e:
        print(f"warning: {name}: table unreadable ({e}); skipped", file=sys.stderr)
        return b""


# ---------- V8 serialized strings ----------
def v8_string(b, i):
    """Read a V8-serialized string at i (skipping 0x00 padding). Returns (text, next_index) or (None, i)."""
    L = len(b)
    while i < L and b[i] == 0:
        i += 1
    if i >= L:
        return None, i
    t = b[i]
    if t not in (0x22, 0x63, 0x53):  # '"' one-byte latin-1, 'c' two-byte utf-16le, 'S' utf-8
        return None, i
    try:
        n, j = _varint(b, i + 1)
    except IndexError:
        return None, i
    if n > 4096 or j + n > L:
        return None, i
    raw = b[j:j + n]
    if t == 0x22:
        s = raw.decode("latin-1")
    elif t == 0x63:
        s = raw.decode("utf-16-le", "replace")
    else:
        s = raw.decode("utf-8", "replace")
    return s, j + n


KEY_ARTIST = b'"\x06artist'
KEY_NAME = b'"\x04name'


def songs_from_v8(b):
    """(artist, title) pairs from V8 objects that carry an `artist` key followed closely by a `name` key."""
    out = []
    for m in re.finditer(re.escape(KEY_ARTIST), b):
        artist, j = v8_string(b, m.end())
        if not artist:
            continue
        k = b.find(KEY_NAME, j, j + 256)
        if k < 0:
            continue
        title, _ = v8_string(b, k + len(KEY_NAME))
        if title:
            out.append({"artist": artist.strip(), "title": title.strip(), "plays": None, "favourite": None,
                        "last_played": None, "source": "cache"})
    return out


def songs_from_json(b):
    """Songs from Feishin's play-queue JSON ({"default":[...],"songs":{id: song}})."""
    out = []
    dec = json.JSONDecoder()
    texts = []
    # V8 stores the queue string one-byte (Latin-1) when it can, else two-byte (UTF-16LE): read it as stored.
    lat = b.decode("latin-1")
    texts += [(lat, m.start()) for m in re.finditer(r'\{\s*"default"\s*:\s*\[', lat)]
    pat16 = '{"default"'.encode("utf-16-le")
    k = b.find(pat16)
    while k >= 0:
        seg = b[k:k + 16 * 1024 * 1024]
        texts.append((seg[:len(seg) // 2 * 2].decode("utf-16-le", "replace"), 0))
        k = b.find(pat16, k + 2)
    for text, start in texts:
        try:
            obj, _ = dec.raw_decode(text, start)
        except ValueError:
            continue
        songs = obj.get("songs") if isinstance(obj, dict) else None
        if not isinstance(songs, dict):
            continue
        for s in songs.values():
            if not isinstance(s, dict) or not s.get("name"):
                continue
            out.append({"artist": (s.get("artistName") or s.get("albumArtistName") or "").strip(),
                        "title": s["name"].strip(), "plays": s.get("playCount"),
                        "favourite": s.get("userFavorite"), "last_played": s.get("lastPlayedAt"), "source": "queue"})
    return out


def candidate_files(path):
    path = os.path.expanduser(os.path.expandvars(path))
    if os.path.isfile(path):
        return [path]
    if not os.path.isdir(path):
        print(f"no such file or folder: {path}", file=sys.stderr)
        return []
    files = []
    idb = os.path.join(path, "IndexedDB")
    root = idb if os.path.isdir(idb) else path
    for d, _, names in os.walk(root):
        for n in names:
            p = os.path.join(d, n)
            if ".blob" in d or n.endswith((".log", ".ldb")):
                files.append(p)
    return sorted(files)


def collect(paths):
    rows = []
    for p in paths:
        for f in candidate_files(p):
            try:
                with open(f, "rb") as fh:
                    data = fh.read()
            except OSError as e:
                print(f"skip {f}: {e}", file=sys.stderr)
                continue
            if f.endswith(".log"):
                payload = leveldb_log(data)
            elif f.endswith(".ldb"):
                payload = leveldb_table(data, f)
            else:
                payload = unwrap(data, f)
            rows += songs_from_json(payload)
            rows += songs_from_v8(payload)
    return merge(rows)


def merge(rows):
    by = {}
    for r in rows:
        key = (r["artist"].casefold(), r["title"].casefold())
        cur = by.get(key)
        if cur is None:
            by[key] = dict(r)
            continue
        if r["plays"] is not None and (cur["plays"] is None or r["plays"] > cur["plays"]):
            cur["plays"] = r["plays"]
        newer = r["last_played"] is not None and (cur["last_played"] is None or r["last_played"] >= cur["last_played"])
        if newer:  # favourite and last_played come from the newest snapshot (ISO-8601 strings compare in order)
            cur["last_played"] = r["last_played"]
            if r["favourite"] is not None:
                cur["favourite"] = r["favourite"]
        elif cur["favourite"] is None and r["favourite"] is not None:
            cur["favourite"] = r["favourite"]
        if r["source"] == "queue":
            cur["source"] = "queue"
    songs = sorted(by.values(), key=lambda r: (-(r["plays"] or 0), r["artist"].casefold(), r["title"].casefold()))
    return songs


def artist_counts(songs):
    c = Counter()
    for s in songs:
        for a in re.split(r",|;| & | feat\.? | x ", s["artist"]):
            a = a.strip()
            if a:
                c[a] += 1
    return c


def report(songs, top):
    print(f"{len(songs)} songs")
    for s in songs:
        extra = []
        if s["plays"] is not None:
            extra.append(f"{s['plays']} plays")
        if s["favourite"]:
            extra.append("favourite")
        print(f"  {s['artist']} - {s['title']}" + (f"  ({', '.join(extra)})" if extra else ""))
    print("artists by number of songs:")
    for a, n in artist_counts(songs).most_common(top):
        print(f"  {n:3d}  {a}")


# ---------- selftest ----------
def _snappy_literal_only(data):
    """Minimal valid Snappy encoder (literals only) for the selftest."""
    n = len(data)
    head = bytearray()
    while True:
        x = n & 0x7F
        n >>= 7
        head.append(x | (0x80 if n else 0))
        if not n:
            break
    out = bytearray(head)
    for i in range(0, len(data), 60):
        chunk = data[i:i + 60]
        out.append((len(chunk) - 1) << 2)
        out += chunk
    return bytes(out)


def _v8s(s):
    try:
        raw = s.encode("latin-1")
        return b'"' + bytes([len(raw)]) + raw
    except UnicodeEncodeError:
        raw = s.encode("utf-16-le")
        return b"\x00c" + bytes([len(raw)]) + raw


def _vint(n):
    out = bytearray()
    while True:
        x = n & 0x7F
        n >>= 7
        out.append(x | (0x80 if n else 0))
        if not n:
            return bytes(out)


def _v8long(text):
    """A V8 string of any length, stored the way V8 stores it (one-byte when Latin-1 fits, else two-byte)."""
    try:
        raw = text.encode("latin-1")
        return b'"' + _vint(len(raw)) + raw
    except UnicodeEncodeError:
        raw = text.encode("utf-16-le")
        return b"c" + _vint(len(raw)) + raw


def _make_log(records):
    """A LevelDB .log holding these records, split into FIRST/MIDDLE/LAST fragments across 32 KiB blocks."""
    out = bytearray()
    for rec in records:
        pos, first = 0, True
        while True:
            left = LOG_BLOCK - (len(out) % LOG_BLOCK)
            if left < 7:
                out += b"\x00" * left
                left = LOG_BLOCK
            room = left - 7
            frag = rec[pos:pos + room]
            last = pos + len(frag) >= len(rec)
            typ = 1 if first and last else 2 if first else 4 if last else 3
            out += b"\x00\x00\x00\x00" + len(frag).to_bytes(2, "little") + bytes([typ]) + frag
            pos += len(frag)
            first = False
            if last:
                break
    return bytes(out)


def _make_table(values):
    """A LevelDB .ldb with one Snappy data block per value, an index block and a footer."""
    out, index = bytearray(), bytearray()
    for n, v in enumerate(values):
        key = b"k%03d" % n
        block = b"\x00" + _vint(len(key)) + _vint(len(v)) + key + v + (0).to_bytes(4, "little") + (1).to_bytes(4, "little")
        comp = _snappy_literal_only(block)
        handle = _vint(len(out)) + _vint(len(comp))
        out += comp + b"\x01" + b"\x00" * 4
        index += b"\x00" + _vint(len(key)) + _vint(len(handle)) + key + handle
    index += (0).to_bytes(4, "little") + (1).to_bytes(4, "little")
    ioff = len(out)
    out += index + b"\x00" + b"\x00" * 4
    footer = _vint(0) + _vint(0) + _vint(ioff) + _vint(len(index))
    out += footer + b"\x00" * (40 - len(footer)) + LDB_MAGIC
    return bytes(out)


def _queue(name, artist, plays, fav, when, lyrics="x"):
    return json.dumps({"default": ["u1"], "songs": {"u1": {
        "name": name, "artistName": artist, "playCount": plays, "userFavorite": fav, "lastPlayedAt": when,
        "lyrics": lyrics}}}, separators=(",", ":"), ensure_ascii=False)


def selftest():
    import tempfile
    # Snappy: a copy with overlap (offset 1, length 6) after a literal "ab" -> "abbbbbbb"
    assert snappy_raw(bytes([8, 1 << 2]) + b"ab" + bytes([((6 - 4) << 2) | 1, 1])) == b"abbbbbbb"
    long_lit = bytes(range(256)) * 2  # literal longer than 60: length in extra bytes
    assert snappy_raw(_vint(512) + bytes([61 << 2]) + (511).to_bytes(2, "little") + long_lit) == long_lit
    try:
        snappy_raw(bytes([9, 1 << 2]) + b"ab")
        raise AssertionError("length mismatch not caught")
    except SnappyError as e:
        assert e.partial == b"ab"
    # Cache blob: V8 lyrics-query objects, one with a two-byte (Hindi) title
    v8 = (b"\xff\x0fo" + b'"\x05local' + b"o" + KEY_ARTIST + _v8s("Gigi Perez") + b'"\x04lang' + _v8s("xxx")
          + KEY_NAME + _v8s("Sailor Song") + b"{" + b"o" + KEY_ARTIST + _v8s("Pritam, Papon")
          + b'"\x04lang' + _v8s("hi") + KEY_NAME + _v8s("जीयें क्यूँ") + b"{")
    blob = b"\xff\x11\x02" + _snappy_literal_only(v8)
    # Queue in the .log: an old snapshot, then a newer one that crosses a 32 KiB block boundary (long lyrics),
    # stored one-byte (Latin-1: "Peña"); a second song whose lyrics force a two-byte (UTF-16) string.
    old = b"\x01\x00" + _v8long(_queue("A Thousand Years", "Chance Peña", 3, False, "2026-01-01T00:00:00Z"))
    new = b"\x01\x00" + _v8long(_queue("A Thousand Years", "Chance Peña", 15, True, "2026-11-07T11:38:22Z",
                                          "la " * 15000))
    wide = b"\x01\x00" + _v8long(_queue("Raabta", "Pritam", 4, None, "2026-11-05T10:00:00Z", "I’m here, 彻夜"))
    log = _make_log([old, new, wide])
    assert len(log) > LOG_BLOCK and leveldb_log(log).count(b'{"default"') == 2
    table = _make_table([b"\x01\x00" + _v8long(_queue("Iris", "The Goo Goo Dolls", 9, True, "2026-10-01T00:00:00Z"))])
    with tempfile.TemporaryDirectory() as d:
        idb = os.path.join(d, "IndexedDB")
        os.makedirs(os.path.join(idb, "file__0.indexeddb.blob", "1", "7a"))
        os.makedirs(os.path.join(idb, "file__0.indexeddb.leveldb"))
        with open(os.path.join(idb, "file__0.indexeddb.blob", "1", "7a", "7afc"), "wb") as f:
            f.write(blob)
        with open(os.path.join(idb, "file__0.indexeddb.leveldb", "000003.log"), "wb") as f:
            f.write(log)
        with open(os.path.join(idb, "file__0.indexeddb.leveldb", "000005.ldb"), "wb") as f:
            f.write(table)
        songs = collect([d])
        # a blob cut short mid-write still yields what decodes, never compressed-byte ghosts
        with open(os.path.join(idb, "file__0.indexeddb.blob", "1", "7a", "7afc"), "wb") as f:
            f.write(blob[:-12])
        cut = collect([os.path.join(idb, "file__0.indexeddb.blob")])
    got = {(s["artist"], s["title"]): s for s in songs}
    assert ("Gigi Perez", "Sailor Song") in got and ("Pritam, Papon", "जीयें क्यूँ") in got, got
    q = got[("Chance Peña", "A Thousand Years")]
    assert q["plays"] == 15 and q["favourite"] is True and q["last_played"].startswith("2026-11-07"), q
    assert got[("Pritam", "Raabta")]["plays"] == 4, got
    assert got[("The Goo Goo Dolls", "Iris")]["plays"] == 9, got
    assert len(songs) == 5, songs
    assert songs[0]["title"] == "A Thousand Years"  # songs with plays sort first
    assert artist_counts(songs)["Pritam"] == 2 and artist_counts(songs)["Papon"] == 1
    assert [(s["artist"], s["title"]) for s in cut] == [("Gigi Perez", "Sailor Song")], cut
    print("selftest PASS")
    return 0


def main(argv):
    import argparse
    if hasattr(sys.stdout, "reconfigure"):  # a cp1252 Windows console would crash on a Hindi title mid-report
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Songs and artists from a music player's local cache.")
    ap.add_argument("paths", nargs="*", help="Feishin user data folder, or files copied out of it")
    ap.add_argument("--json", help="also write songs and artist counts to this JSON file")
    ap.add_argument("--top", type=int, default=25, help="artists to list (default 25)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.paths:
        ap.print_help()
        return 1
    songs = collect(a.paths)
    if a.json:  # write before printing, so a console problem can never cost the file
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump({"songs": songs, "artists": artist_counts(songs).most_common()}, f, ensure_ascii=False, indent=1)
    report(songs, a.top)
    return 0 if songs else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
