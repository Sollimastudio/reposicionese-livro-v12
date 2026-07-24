#!/usr/bin/env python3
"""Sincroniza porta principal, Registro Mestre e Matriz após o Lote 02."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_guarded(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise ValueError(f"{label}: esperado trecho antigo ou versão nova; encontrado {count}.")


def update(path: Path, replacements: list[tuple[str, str, str]]) -> None:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    for label, old, new in replacements:
        text = replace_guarded(text, old, new, label)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    update(
        ROOT / "LER_AGORA_REPOSICIONESE_REV_B.md",
        [
            (
                "estado principal",
                "**Estado:** manuscrito textual completo; governança e coerência metodológica reconciliadas; voz e ritmo concluídos no Lote 01; especialistas e produção pendentes",
                "**Estado:** manuscrito textual completo; governança e coerência metodológica reconciliadas; voz e ritmo concluídos nos Lotes 01–02; especialistas e produção pendentes",
            ),
            (
                "contagem principal",
                "- aproximadamente 37.084 palavras editoriais;",
                "- aproximadamente 37.047 palavras editoriais;",
            ),
            (
                "arquivos de voz",
                "- [Ponto de retomada — Lote 01](revisao-b-global/43_PONTO_DE_RETOMADA_VOZ_RITMO_LOTE_01.md)",
                "- [Ponto de retomada — Lote 01](revisao-b-global/43_PONTO_DE_RETOMADA_VOZ_RITMO_LOTE_01.md)\n- [Validação — Lote 01](revisao-b-global/44_VALIDACAO_VOZ_RITMO_LOTE_01.md)\n- [Auditoria de continuidade e pista visual](revisao-b-global/45_AUDITORIA_PRONTIDAO_CONTINUIDADE_E_VISUAL.md)\n- [Rastreabilidade — Lote 02](revisao-b-global/46_RASTREABILIDADE_VOZ_RITMO_REPETICAO_LOTE_02.md)\n- [Ponto de retomada — Lote 02](revisao-b-global/47_PONTO_DE_RETOMADA_VOZ_RITMO_LOTE_02.md)\n- [Validação — Lote 02](revisao-b-global/48_VALIDACAO_VOZ_RITMO_LOTE_02.md)",
            ),
            (
                "pendência de lotes",
                "- passagem global de voz, ritmo e repetição nos Lotes 2–4;",
                "- passagem global de voz, ritmo e repetição nos Lotes 3–4;",
            ),
            (
                "próxima etapa",
                "A passagem global de voz, ritmo e repetição começou em lotes controlados. O **Lote 01 — Pré-livro e Partes I–II** está concluído. A próxima unidade autorizável é o **Lote 02 — Partes III–IV**.",
                "A passagem global de voz, ritmo e repetição avançou em lotes controlados. Os **Lotes 01–02 — Pré-livro e Partes I–IV** estão concluídos. A próxima unidade autorizável é o **Lote 03 — Partes V–VI**. A pista visual permanece separada porque os binários ainda não foram versionados no repositório.",
            ),
        ],
    )

    update(
        ROOT / "direcao-editorial/12_REGISTRO_MESTRE_DE_CONTEXTO.md",
        [
            (
                "versão Registro",
                "**Versão:** 3.1 — Voz e ritmo, Lote 01",
                "**Versão:** 3.2 — Voz e ritmo, Lotes 01–02",
            ),
            (
                "estado Registro",
                "**Estado:** Revisão B textual completa; governança e coerência metodológica reconciliadas; voz e ritmo concluídos no Lote 01",
                "**Estado:** Revisão B textual completa; governança e coerência metodológica reconciliadas; voz e ritmo concluídos nos Lotes 01–02",
            ),
            (
                "contagem Registro",
                "- aproximadamente 37.084 palavras editoriais;",
                "- aproximadamente 37.047 palavras editoriais;",
            ),
            (
                "fase Registro",
                "- voz, ritmo e repetição concluídos no Pré-livro e Partes I–II;\n- próximo lote textual: Partes III–IV.",
                "- voz, ritmo e repetição concluídos no Pré-livro e Partes I–IV;\n- próximo lote textual: Partes V–VI;\n- banco visual registrado por manifesto e hash, mas sem binários versionados.",
            ),
        ],
    )

    update(
        ROOT / "direcao-editorial/13_MATRIZ_DE_NAO_PERDA.md",
        [
            (
                "versão Matriz",
                "**Versão:** 2.1 — Pós-coerência e voz, Lote 01",
                "**Versão:** 2.2 — Pós-coerência e voz, Lotes 01–02",
            ),
            (
                "estado Matriz",
                "**Estado:** manuscrito completo em Revisão B; coerência metodológica reconciliada; voz e ritmo concluídos no Lote 01; validações especializadas e produção pendentes",
                "**Estado:** manuscrito completo em Revisão B; coerência metodológica reconciliada; voz e ritmo concluídos no Pré-livro e Partes I–IV; validações especializadas e produção pendentes",
            ),
        ],
    )

    print("Estado sincronizado após voz, ritmo e repetição — Lote 02.")


if __name__ == "__main__":
    main()
