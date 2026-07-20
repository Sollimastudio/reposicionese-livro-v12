#!/usr/bin/env python3
"""Gera o manuscrito consolidado da Revisão Integral A.

O script não edita os módulos. Ele valida a sequência canônica, concatena as
fontes em ordem e grava um único Markdown rastreável.
"""

from __future__ import annotations

import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "manuscrito-canonico-rev-a" / "REPOSICIONESE_REV_A_CONSOLIDADO.md"
SUMMARY = ROOT / "manuscrito-canonico-rev-a" / "SUMARIO_REV_A.md"

SOURCES = [
    Path("revisao-integral/00_PRE_LIVRO_REV_A.md"),
    Path("revisao-integral/01_PARTE_I_REV_A.md"),
    Path("revisao-integral/02_PARTE_II_REV_A.md"),
    Path("revisao-integral/03_PARTE_III_REV_A.md"),
    Path("revisao-integral/04_PARTE_IV_REV_A.md"),
    Path("revisao-integral/05_PARTE_V_REV_A.md"),
    Path("revisao-integral/06_PARTE_VI_REV_A.md"),
    Path("revisao-integral/07_PARTE_VII_REV_A.md"),
    Path("revisao-integral/08_PARTE_VIII_REV_A.md"),
]

CHAPTER_RE = re.compile(r"^# CAP[IÍ]TULO\s+(\d+)\b", re.MULTILINE | re.IGNORECASE)
EPILOGUE_RE = re.compile(r"^# EP[IÍ]LOGO\b", re.MULTILINE | re.IGNORECASE)


def read_utf8(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Fonte ausente: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").strip()
    if not text:
        raise ValueError(f"Fonte vazia: {path.relative_to(ROOT)}")
    return text


def git_sha() -> str:
    sha = os.getenv("GITHUB_SHA")
    if sha:
        return sha
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return "indisponível"


def validate(full_text: str) -> list[int]:
    chapters = [int(value) for value in CHAPTER_RE.findall(full_text)]
    expected = list(range(1, 39))

    if chapters != expected:
        raise ValueError(
            "Sequência de capítulos inválida. "
            f"Esperado: {expected}. Encontrado: {chapters}."
        )

    if len(chapters) != len(set(chapters)):
        raise ValueError("Há capítulos duplicados.")

    if not EPILOGUE_RE.search(full_text):
        raise ValueError("Epílogo não encontrado.")

    return chapters


def build() -> str:
    source_texts: list[tuple[Path, str]] = []
    for relative in SOURCES:
        source_texts.append((relative, read_utf8(ROOT / relative)))

    body_for_validation = "\n\n".join(text for _, text in source_texts)
    chapters = validate(body_for_validation)

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    source_list = "\n".join(f"- `{path.as_posix()}`" for path, _ in source_texts)

    header = f"""# REPOSICIONE-SE™
## Método da Árvore do Discernimento

**Autora:** Sol Lima  
**Estado:** Manuscrito Canônico Consolidado — Revisão Integral A  
**Atenção:** esta não é a edição final aprovada ou diagramada.  
**Gerado em:** {generated_at}  
**Commit de origem:** `{git_sha()}`  
**Capítulos validados:** {len(chapters)}

> Este arquivo foi gerado automaticamente a partir dos módulos da Revisão A. As fontes modulares permanecem canônicas para rastreabilidade. Não editar este arquivo manualmente sem atualizar o processo de consolidação.

### Fontes

{source_list}

---
"""

    summary = read_utf8(SUMMARY)
    pieces = [header, "<!-- INÍCIO DO SUMÁRIO CANÔNICO -->", summary,
              "<!-- FIM DO SUMÁRIO CANÔNICO -->"]

    for relative, text in source_texts:
        pieces.extend(
            [
                "\n---\n",
                f"<!-- FONTE: {relative.as_posix()} -->",
                text,
                f"<!-- FIM DA FONTE: {relative.as_posix()} -->",
            ]
        )

    result = "\n\n".join(pieces).strip() + "\n"
    if len(result) < 1000:
        raise ValueError("Arquivo consolidado ficou inesperadamente pequeno.")
    return result


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build(), encoding="utf-8", newline="\n")
    print(f"Gerado: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
