#!/usr/bin/env python3
"""Script 5: render_video — render final do vídeo com FFmpeg."""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RENDERS_DIR = BASE_DIR / "renders"

def log(msg):
    print(f"[render_video] {msg}", flush=True)

def run(cmd, check=True):
    log(f"→ {cmd}")
    result = os.system(cmd)
    if check and result != 0:
        log(f"❌ Erro: {result}")
        sys.exit(1)
    return result

def render_video():
    log("🎥 Renderizando vídeo...")
    run("npm run render")
    return True

def main():
    log("🚀 Iniciando render_video")
    render_video()
    log("✅ Render finalizado")

if __name__ == "__main__":
    main()
