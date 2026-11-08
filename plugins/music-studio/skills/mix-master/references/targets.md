# Loudness, true peak and delivery targets (checked 2 Nov 2026)

Sources: research/04_production_and_video.md §1, §5 (claims table there). `tools/loudness.py` TARGETS must match this
table.

| Destination | Integrated | True peak | Status |
|---|---|---|---|
| Spotify | normalises to -14 LUFS (Loud -11, Quiet -19 for Premium users who pick them) | below -1 dBTP; **below -2 dBTP if the master is louder than -14 LUFS** | CONFIRMED (Spotify for Artists) |
| Apple Music | about -16 LUFS (Sound Check) | "at least 1 dB of headroom", check inter-sample clipping on the encode | -16: secondary; headroom: CONFIRMED (Apple Digital Masters) |
| YouTube | about -14 LUFS, only turns loud songs down | n/a | secondary only; no official figure found |
| TikTok, Instagram | no official target found | n/a | not found |
| In-game radio or vehicle | test in the game against voice chat | -1 dBTP | house rule |

**House target:** master between -14 and -10 LUFS integrated; true peak -1 dBTP, or -2 dBTP when louder than -14.
Louder gains nothing on streaming (every platform turns it down) and costs dynamics. The `streaming` target in
loudness.py is -14 +-1; a deliberately louder master uses `--target club` and the -2 dBTP ceiling by hand.

## Measuring
```
ffmpeg -hide_banner -nostats -i song.wav -af ebur128=peak=true:framelog=quiet -f null -
```
- Summary gives I (LUFS), LRA and true peak. loudness.py wraps this and adds the phone-speaker vocal check.
- Measure the ENCODED files too (the MP3/AAC a platform will make): overs that the WAV doesn't show appear after lossy
  encoding (Spotify, Apple). `ffmpeg -i master.wav -c:a aac -b:a 256k check.m4a`, then measure check.m4a.
- ffmpeg's built-in AAC encoder can put single-sample spikes (+2 to +5 dBTP) into a 44.1 kHz float WAV's encode that
  are not in the music (seen 8 Nov 2026 on a guitar master; the MP3 and Opus encodes were clean). Encode-check from
  48 kHz / 24-bit, and if one encode alone fails, look at the spike before lowering the ceiling.
- It happens on 48 kHz / 24-bit sources too (seen 8 Nov 2026): wherever the limiter holds a flat top for 10 or
  more samples, ffmpeg's AAC put a spike up to +1.3 dBTP. Lowering the ceiling from -2.6 to -3.5 made it worse,
  while MP3 and Opus stayed clean (-2.8 and -1.9 dBTP). Treat that as an encoder glitch, not an over in the master.

## loudnorm (a trim, never the mastering limiter)
- Two passes, linear mode only: pass 1 `loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json`, pass 2 with all four
  `measured_*` values plus `offset`, `linear=true`, and **always `-ar 48000`** (dynamic mode silently upsamples to 192 kHz).
- loudnorm falls back to dynamic mode (a compressor that changes the mix) when the target LRA is below the source's
  or the gain would push the peak over TP: set LRA at least the measured LRA, or limit in the DAW first.

## Mastering
- Chain (general practice, INFERRED): corrective EQ, gentle bus compression (1-2 dB gain reduction), tonal EQ,
  optional saturation and width, a true-peak limiter at the ceiling, then measure.
- Matchering 2.0 (GPL-3.0): matches the target's RMS, frequency response, peak and stereo width to a reference song;
  placed 3rd of 12 in a 472-entry blind test behind two pro engineers "by carefully selecting a proper song as
  reference". A starting point; the reference choice is the whole game.
- Pitfalls: louder is not better; don't do all the work in the limiter; ears over meters; -14 is a guideline; not one
  chain for every song.

## Delivery files
- Distributor master: WAV 24-bit at the native session rate (never upsampled; Apple asks for the highest native rate).
- Video: the same master, AAC 48 kHz (YouTube recommends AAC-LC 384 kbps stereo), integrated loudness and true peak
  re-measured in the rendered video file.
