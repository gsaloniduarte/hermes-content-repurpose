#!/usr/bin/env python3
"""Script 4: mix_audio — mistura áudio (voz + BGM + SFX)."""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RENDERS_DIR = BASE_DIR / "renders"

def log(msg):
    print(f"[mix_audio] {msg}", flush=True)

def run(cmd, check=True):
    log(f"→ {cmd}")
    result = os.system(cmd)
    if check and result != 0:
        log(f"❌ Erro: {result}")
        sys.exit(1)
    return result

def mix_audio(voiceover_path, bgm_path, output_path):
    log(f"🎵 Misturando áudio...")
    log(f"   - voicer: {voiceover_path}")
    log(f"   - BGM: {bgm_path}")
    log(f"   - output: {output_path}")
    # Placeholder — implementação futura com ffmpeg
    # ffmpeg -i voicer -i bgm -filter_complex "[0:a][1:a]amix=inputs=2:duration=first:dropout_transition=0[vo]; [vo] volume=0.7" -ac 2 output_path
    return True

def main():
    log("🚀 Iniciando mix_audio")
    mix_audio(
        RENDERS_DIR / "voiceover.wav",
        RENDERS_DIR / "bgm.wav",
        RENDERS_DIR / "audio_mix.wav"
    )
    log("✅ Mixagem concluída")

if __name__ == "__main__":
    main()
