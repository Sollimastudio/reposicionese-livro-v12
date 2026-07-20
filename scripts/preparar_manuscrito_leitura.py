#!/usr/bin/env python3
"""Prepara uma versão limpa do manuscrito para exportação editorial.

Remove somente o invólucro técnico criado pela consolidação automática e os
comentários de rastreabilidade. O texto autoral dos módulos não é reescrito.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscrito-canonico-rev-a" / "REPOSICIONESE_REV_A_CONSOLIDADO.md"
OUTPUT_DIR = ROOT / "dist-leitura"
OUTPUT = OUTPUT_DIR / "REPOSICIONESE_MANUSCRITO_COMPLETO_REV_A.md"

START = "<!-- FONTE: revisao-integral/00_PRE_LIVRO_REV_A.md -->"
COMMENT_RE = re.compile(r"<!--\s*(?:FONTE|FIM DA FONTE):.*?-->", re.DOTALL)
CHAPTER_RE = re.compile(r"^# CAP[IÍ]TULO\s+(\d+)\b", re.MULTILINE | re.IGNORECASE)
EPILOGUE_RE = re.compile(r"^# EP[IÍ]LOGO\b", re.MULTILINE | re.IGNORECASE)


def main() -> None:
    raw = SOURCE.read_text(encoding="utf-8").replace("\r\n", "\n")
    if START not in raw:
        raise RuntimeError("Marcador do início do manuscrito não foi encontrado.")

    text = raw.split(START, 1)[1]
    text = COMMENT_RE.sub("", text).strip()

    chapters = [int(n) for n in CHAPTER_RE.findall(text)]
    expected = list(range(1, 39))
    if chapters != expected:
        raise RuntimeError(f"Capítulos inválidos: {chapters}")
    if not EPILOGUE_RE.search(text):
        raise RuntimeError("Epílogo ausente.")

    title_page = """---
title: "REPOSICIONE-SE™"
subtitle: "Método da Árvore do Discernimento"
author: "Sol Lima"
lang: pt-BR
subject: "Manuscrito completo — Revisão Integral A"
keywords:
  - posicionamento
  - discernimento
  - autoria
  - árvore do discernimento
---

> **MANUSCRITO PARA LEITURA AUTORAL — REVISÃO INTEGRAL A**  
> Esta versão contém Pré-livro, Capítulos 1–38 e Epílogo. Ainda passará por aprovação autoral, revisão factual, jurídica, psicológica, teológica, ortotipográfica e projeto gráfico.

\\newpage

"""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(title_page + text + "\n", encoding="utf-8", newline="\n")
    print(f"Gerado: {OUTPUT.relative_to(ROOT)}")
    print(f"Capítulos validados: {len(chapters)}")


if __name__ == "__main__":
    main()
