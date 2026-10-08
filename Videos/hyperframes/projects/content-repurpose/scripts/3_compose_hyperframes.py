#!/usr/bin/env python3
"""Script 3: compose_hyperframes — gera frames do HyperFrames."""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

def log(msg):
    print(f"[compose_hyperframes] {msg}", flush=True)

def run(cmd, check=True):
    log(f"→ {cmd}")
    result = os.system(cmd)
    if check and result != 0:
        log(f"❌ Erro: {result}")
        sys.exit(1)
    return result

def compose_hyperframes():
    log("🎬 Compondo com HyperFrames (npm run build)...")
    run("npm run build")
    return True

def main():
    log("🚀 Iniciando compose_hyperframes")
    compose_hyperframes()
    log("✅ Composição concluída")

if __name__ == "__main__":
    main()
