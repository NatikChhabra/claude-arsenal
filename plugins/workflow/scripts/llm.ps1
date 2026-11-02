# Start a local OpenAI-compatible LLM server (llama.cpp llama-server) for scripts/ask.py and scripts/batch.py.
# Model paths live in a local, untracked presets file (copy llm.presets.example.json to llm.presets.json):
#   .\scripts\llm.ps1 -Preset fast        # a preset from llm.presets.json
#   .\scripts\llm.ps1 -Model D:\m.gguf -Ctx 8192
#   .\scripts\llm.ps1 -Stop               # free the GPU when done (always, before the user games or renders)
# Server exe: -Server, else $env:LLAMA_SERVER, else llama-server on PATH. Serves http://127.0.0.1:<Port>/v1
param(
    [string]$Preset,
    [string]$Model,
    [int]$Ctx = 8192,
    [int]$Port = 8091,
    [string]$Server = $(if ($env:LLAMA_SERVER) { $env:LLAMA_SERVER } else { 'llama-server' }),
    [switch]$Stop
)

# Only one large model fits in VRAM at a time: stop any running server first.
Get-Process llama-server -ErrorAction SilentlyContinue | Stop-Process -Force
if ($Stop) { return }

if ($Preset) {
    $file = Join-Path $PSScriptRoot 'llm.presets.json'
    $p = (Get-Content $file -Raw | ConvertFrom-Json).$Preset
    if ($null -eq $p) { throw "No preset '$Preset' in $file" }
    $Model = $p.m
    if ($p.c) { $Ctx = $p.c }
}
if (-not $Model) { throw 'Give -Preset or -Model' }

& $Server -m $Model -ngl 99 -c $Ctx -fa on --jinja --port $Port --host 127.0.0.1
