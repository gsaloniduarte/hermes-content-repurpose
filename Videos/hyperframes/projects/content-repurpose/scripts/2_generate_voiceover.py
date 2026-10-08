#!/usr/bin/env python3
"""Script 2: generate_voiceover — TTS narração PT-BR."""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RENDERS_DIR = BASE_DIR / "renders"

def log(msg):
    print(f"[generate_voiceover] {msg}", flush=True)

def run(cmd, check=True):
    log(f"→ {cmd}")
    result = os.system(cmd)
    if check and result != 0:
        log(f"❌ Erro: {result}")
        sys.exit(1)
    return result

def generate_voiceover(text, output_file, lang="pt-BR"):
    log(f"🎙️  Gerando narração: {len(text)} chars")
    run(f"edge-tts --text '{text}' --voice {lang} --write-media '{output_file}'")
    return output_file

def main():
    log("🚀 Iniciando generate_voiceover")
    import argparse
    parser = argparse.ArgumentParser(description="Generate voiceover")
    parser.add_argument("text", help="Text for narration")
    parser.add_argument("--output", default="renders/voiceover.wav", help="Output file")
    args = parser.parse_args()
    generate_voiceover(args.text, args.output)
    log("✅ Voicer finalizado")

if __name__ == "__main__":
    main()
