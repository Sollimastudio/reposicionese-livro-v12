#!/usr/bin/env python3
"""Gera o manuscrito contínuo vivo da Revisão B e o Marco 01.

A Revisão B substitui apenas os blocos já revisados. As Partes ainda não
trabalhadas permanecem herdadas da Revisão A, com marcadores invisíveis de
origem. Nenhum arquivo da Revisão A é alterado.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

B_SOURCES = [
    Path("revisao-b-global/03_ONDA_1_PRE_LIVRO_REV_B.md"),
    Path("revisao-b-global/04_ONDA_1_PARTE_I_REV_B.md"),
    Path("revisao-b-global/05_ONDA_2_PARTE_II_REV_B.md"),
]

A_FALLBACK_SOURCES = [
    Path("revisao-integral/03_PARTE_III_REV_A.md"),
    Path("revisao-integral/04_PARTE_IV_REV_A.md"),
    Path("revisao-integral/05_PARTE_V_REV_A.md"),
    Path("revisao-integral/06_PARTE_VI_REV_A.md"),
    Path("revisao-integral/07_PARTE_VII_REV_A.md"),
    Path("revisao-integral/08_PARTE_VIII_REV_A.md"),
]

CONTINUOUS = ROOT / "manuscrito-revisao-b" / "REPOSICIONESE_REV_B_CONTINUO.md"
MILESTONE = ROOT / "marcos-revisao-b" / "MARCO_01_PRE_LIVRO_PARTES_I_II.md"

CHAPTER_RE = re.compile(r"^# CAP[IÍ]TULO\s+(\d+)\b", re.MULTILINE | re.IGNORECASE)
EPILOGUE_RE = re.compile(r"^# EP[IÍ]LOGO\b", re.MULTILINE | re.IGNORECASE)
TRAILING_RULE_RE = re.compile(r"(?:\n\s*---\s*)+$")


def read(path: Path) -> str:
    full = ROOT / path
    if not full.is_file():
        raise FileNotFoundError(f"Fonte ausente: {path}")
    text = full.read_text(encoding="utf-8").replace("\r\n", "\n").strip()
    text = TRAILING_RULE_RE.sub("", text).rstrip()
    if not text:
        raise ValueError(f"Fonte vazia: {path}")
    return text


def validate_chapters(text: str, expected: list[int], require_epilogue: bool) -> None:
    found = [int(value) for value in CHAPTER_RE.findall(text)]
    if found != expected:
        raise ValueError(f"Sequência inválida. Esperado {expected}; encontrado {found}")
    if len(found) != len(set(found)):
        raise ValueError("Há capítulos duplicados.")
    if require_epilogue and not EPILOGUE_RE.search(text):
        raise ValueError("Epílogo ausente no manuscrito contínuo.")


def marker(path: Path, status: str) -> str:
    return f"<!-- FONTE: {path.as_posix()} | STATUS: {status} -->"


def metadata(subject: str, note: str) -> str:
    generated = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    return f'''---
title: "REPOSICIONE-SE™"
subtitle: "Método da Árvore do Discernimento"
author: "Sol Lima"
lang: pt-BR
subject: "{subject}"
toc-title: "SUMÁRIO"
---

> **{note}**  
> Gerado em {generated}. A Revisão A permanece preservada como referência histórica.

\\newpage
'''


def assemble(sources: list[tuple[Path, str]]) -> str:
    blocks: list[str] = []
    for path, status in sources:
        block = "\n\n".join(
            [
                marker(path, status),
                read(path),
                f"<!-- FIM DA FONTE: {path.as_posix()} -->",
            ]
        )
        blocks.append(block)
    return "\n\n\\newpage\n\n".join(blocks).strip() + "\n"


def main() -> None:
    continuous_sources = [(p, "REVISÃO B") for p in B_SOURCES] + [
        (p, "HERDADO TEMPORARIAMENTE DA REVISÃO A") for p in A_FALLBACK_SOURCES
    ]
    continuous_body = assemble(continuous_sources)
    validate_chapters(continuous_body, list(range(1, 39)), require_epilogue=True)

    milestone_body = assemble([(p, "REVISÃO B") for p in B_SOURCES])
    validate_chapters(milestone_body, list(range(1, 7)), require_epilogue=False)

    CONTINUOUS.parent.mkdir(parents=True, exist_ok=True)
    MILESTONE.parent.mkdir(parents=True, exist_ok=True)

    CONTINUOUS.write_text(
        metadata(
            "Manuscrito contínuo vivo — Revisão B",
            "MANUSCRITO DE TRABALHO — REVISÃO B. Pré-livro e Partes I–II já revisados; Partes III–VIII ainda herdadas da Revisão A.",
        )
        + continuous_body,
        encoding="utf-8",
        newline="\n",
    )

    MILESTONE.write_text(
        metadata(
            "Marco 01 — Pré-livro e Partes I–II — Revisão B",
            "MARCO 01 DA REVISÃO B — Pré-livro, Parte I e Parte II revisados.",
        )
        + milestone_body,
        encoding="utf-8",
        newline="\n",
    )

    print(f"Gerado: {CONTINUOUS.relative_to(ROOT)}")
    print(f"Gerado: {MILESTONE.relative_to(ROOT)}")
    print("Validação: manuscrito contínuo 1–38 + Epílogo; Marco 01 capítulos 1–6.")


if __name__ == "__main__":
    main()
