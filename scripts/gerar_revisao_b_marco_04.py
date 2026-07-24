#!/usr/bin/env python3
"""Gera, integra e valida o manuscrito contínuo da Revisão B e o Marco 04.

O Marco 04 reúne Pré-livro e Partes I–V na Revisão B. As Partes VI–VIII
permanecem herdadas da Revisão A no manuscrito contínuo. Nenhum marco anterior
ou arquivo da Revisão A é alterado. A saída contínua também alimenta a medição
editorial da amostra Kindle.
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
    Path("revisao-b-global/07_ONDA_3_PARTE_III_REV_B.md"),
    Path("revisao-b-global/20_ONDA_4_PARTE_IV_REV_B.md"),
    Path("revisao-b-global/23_ONDA_5_PARTE_V_REV_B.md"),
]

A_FALLBACK_SOURCES = [
    Path("revisao-integral/06_PARTE_VI_REV_A.md"),
    Path("revisao-integral/07_PARTE_VII_REV_A.md"),
    Path("revisao-integral/08_PARTE_VIII_REV_A.md"),
]

CONTINUOUS = ROOT / "manuscrito-revisao-b" / "REPOSICIONESE_REV_B_CONTINUO.md"
MILESTONE = ROOT / "marcos-revisao-b" / "MARCO_04_PRE_LIVRO_PARTES_I_II_III_IV_V.md"

CHAPTER_RE = re.compile(r"^# CAP[IÍ]TULO\s+(\d+)\b", re.MULTILINE | re.IGNORECASE)
EPILOGUE_RE = re.compile(r"^# EP[IÍ]LOGO\b", re.MULTILINE | re.IGNORECASE)


def read(path: Path) -> str:
    full = ROOT / path
    if not full.is_file():
        raise FileNotFoundError(f"Fonte ausente: {path}")
    text = full.read_text(encoding="utf-8").replace("\r\n", "\n").strip()
    if not text:
        raise ValueError(f"Fonte vazia: {path}")
    return text


def validate(text: str, expected: list[int], require_epilogue: bool) -> None:
    found = [int(value) for value in CHAPTER_RE.findall(text)]
    if found != expected:
        raise ValueError(f"Sequência inválida. Esperado {expected}; encontrado {found}")
    if len(found) != len(set(found)):
        raise ValueError("Há capítulos duplicados.")
    if require_epilogue and not EPILOGUE_RE.search(text):
        raise ValueError("Epílogo ausente.")


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
> Gerado em {generated}. A Revisão A e os Marcos 01–03 permanecem preservados.

\\newpage
'''


def assemble(sources: list[tuple[Path, str]]) -> str:
    pieces: list[str] = []
    for index, (path, status) in enumerate(sources):
        if index:
            pieces.append("\n")
        pieces.append(f"<!-- FONTE: {path.as_posix()} | STATUS: {status} -->")
        pieces.append(read(path))
        pieces.append(f"<!-- FIM DA FONTE: {path.as_posix()} -->")
    return "\n\n".join(pieces).strip() + "\n"


def main() -> None:
    continuous_sources = [(path, "REVISÃO B") for path in B_SOURCES] + [
        (path, "HERDADO TEMPORARIAMENTE DA REVISÃO A")
        for path in A_FALLBACK_SOURCES
    ]
    continuous_body = assemble(continuous_sources)
    validate(continuous_body, list(range(1, 39)), require_epilogue=True)

    milestone_body = assemble([(path, "REVISÃO B") for path in B_SOURCES])
    validate(milestone_body, list(range(1, 21)), require_epilogue=False)

    CONTINUOUS.parent.mkdir(parents=True, exist_ok=True)
    MILESTONE.parent.mkdir(parents=True, exist_ok=True)

    CONTINUOUS.write_text(
        metadata(
            "Manuscrito contínuo vivo — Revisão B — Marco 04",
            "MANUSCRITO DE TRABALHO — REVISÃO B. Pré-livro e Partes I–V revisados; Partes VI–VIII ainda herdadas da Revisão A.",
        )
        + continuous_body,
        encoding="utf-8",
        newline="\n",
    )

    MILESTONE.write_text(
        metadata(
            "Marco 04 — Pré-livro e Partes I–V — Revisão B",
            "MARCO 04 DA REVISÃO B — Pré-livro e Partes I, II, III, IV e V revisados.",
        )
        + milestone_body,
        encoding="utf-8",
        newline="\n",
    )

    print(f"Gerado: {CONTINUOUS.relative_to(ROOT)}")
    print(f"Gerado: {MILESTONE.relative_to(ROOT)}")
    print("Validação: contínuo 1–38 + Epílogo; Marco 04 capítulos 1–20.")


if __name__ == "__main__":
    main()
