#!/usr/bin/env python3
"""Sincroniza porta principal, Registro Mestre e Matriz após o Lote 03."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def replace_guarded(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise ValueError(f"{label}: esperado trecho antigo ou versão nova; encontrado {count}.")


def replace_regex(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.M)
    if count != 1:
        raise ValueError(f"{label}: esperado 1 trecho; encontrado {count}.")
    return updated


def current_word_count() -> tuple[str, str]:
    report = read(ROOT / "revisao-b-global/16_MEDICAO_EDITORIAL_10_PORCENTO_KINDLE.md")
    match = re.search(r"Total editorial estimado: \*\*([0-9,]+) palavras\*\*", report)
    if not match:
        raise ValueError("Não foi possível recuperar a contagem Kindle atual.")
    comma = match.group(1)
    dot = comma.replace(",", ".")
    return comma, dot


def main() -> None:
    _, words_dot = current_word_count()

    ler_path = ROOT / "LER_AGORA_REPOSICIONESE_REV_B.md"
    ler = read(ler_path)
    ler = replace_guarded(
        ler,
        "**Estado:** manuscrito textual completo; governança e coerência metodológica reconciliadas; voz e ritmo concluídos nos Lotes 01–02; especialistas e produção pendentes",
        "**Estado:** manuscrito textual completo; governança e coerência metodológica reconciliadas; voz e ritmo concluídos nos Lotes 01–03; especialistas e produção pendentes",
        "estado principal",
    )
    ler = replace_regex(
        ler,
        r"^- aproximadamente [0-9.]+ palavras editoriais;$",
        f"- aproximadamente {words_dot} palavras editoriais;",
        "contagem principal",
    )
    ler = replace_guarded(
        ler,
        "- passagem global de voz, ritmo e repetição nos Lotes 3–4;",
        "- passagem global de voz, ritmo e repetição no Lote 4;",
        "pendência de lotes",
    )
    ler = replace_guarded(
        ler,
        "A passagem global de voz, ritmo e repetição avançou em lotes controlados. Os **Lotes 01–02 — Pré-livro e Partes I–IV** estão concluídos. A próxima unidade autorizável é o **Lote 03 — Partes V–VI**. A pista visual permanece separada porque os binários ainda não foram versionados no repositório.",
        "A passagem global de voz, ritmo e repetição avançou em lotes controlados. Os **Lotes 01–03 — Pré-livro e Partes I–VI** estão concluídos. A próxima unidade autorizável é o **Lote 04 — Partes VII–VIII e Epílogo**. A pista visual permanece separada porque os binários ainda não foram versionados no repositório.",
        "próxima etapa",
    )
    write(ler_path, ler)

    registro_path = ROOT / "direcao-editorial/12_REGISTRO_MESTRE_DE_CONTEXTO.md"
    registro = read(registro_path)
    registro = replace_guarded(
        registro,
        "**Versão:** 3.2 — Voz e ritmo, Lotes 01–02",
        "**Versão:** 3.3 — Voz e ritmo, Lotes 01–03",
        "versão Registro",
    )
    registro = replace_guarded(
        registro,
        "**Estado:** Revisão B textual completa; governança e coerência metodológica reconciliadas; voz e ritmo concluídos nos Lotes 01–02",
        "**Estado:** Revisão B textual completa; governança e coerência metodológica reconciliadas; voz e ritmo concluídos nos Lotes 01–03",
        "estado Registro",
    )
    registro = replace_regex(
        registro,
        r"^- aproximadamente [0-9.]+ palavras editoriais;$",
        f"- aproximadamente {words_dot} palavras editoriais;",
        "contagem Registro",
    )
    registro = replace_guarded(
        registro,
        "- voz, ritmo e repetição concluídos no Pré-livro e Partes I–IV;\n- próximo lote textual: Partes V–VI;",
        "- voz, ritmo e repetição concluídos no Pré-livro e Partes I–VI;\n- próximo lote textual: Partes VII–VIII e Epílogo;",
        "fase Registro",
    )
    write(registro_path, registro)

    matriz_path = ROOT / "direcao-editorial/13_MATRIZ_DE_NAO_PERDA.md"
    matriz = read(matriz_path)
    matriz = replace_guarded(
        matriz,
        "**Versão:** 2.2 — Pós-coerência e voz, Lotes 01–02",
        "**Versão:** 2.3 — Pós-coerência e voz, Lotes 01–03",
        "versão Matriz",
    )
    matriz = replace_guarded(
        matriz,
        "**Estado:** manuscrito completo em Revisão B; coerência metodológica reconciliada; voz e ritmo concluídos no Pré-livro e Partes I–IV; validações especializadas e produção pendentes",
        "**Estado:** manuscrito completo em Revisão B; coerência metodológica reconciliada; voz e ritmo concluídos no Pré-livro e Partes I–VI; validações especializadas e produção pendentes",
        "estado Matriz",
    )
    write(matriz_path, matriz)

    print("Estado sincronizado após voz, ritmo e repetição — Lote 03.")


if __name__ == "__main__":
    main()
