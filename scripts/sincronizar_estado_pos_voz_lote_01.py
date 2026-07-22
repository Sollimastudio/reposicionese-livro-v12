#!/usr/bin/env python3
"""Sincroniza porta principal, Registro Mestre e Matriz após o Lote 01."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_guarded(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise ValueError(f"{label}: esperado um trecho antigo ou a versão nova já aplicada; encontrado {count}.")


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
                "estado da porta principal",
                "**Estado:** manuscrito textual completo; governança reconciliada; auditorias localizadas e especializadas pendentes",
                "**Estado:** manuscrito textual completo; governança e coerência metodológica reconciliadas; voz e ritmo concluídos no Lote 01; especialistas e produção pendentes",
            ),
            (
                "contagem da porta principal",
                "- aproximadamente 36.859 palavras editoriais;",
                "- aproximadamente 37.084 palavras editoriais;",
            ),
            (
                "arquivos de estado da porta principal",
                "- [Validação da reconciliação](revisao-b-global/39_VALIDACAO_RECONCILIACAO_GOVERNANCA.md)",
                "- [Validação da reconciliação](revisao-b-global/39_VALIDACAO_RECONCILIACAO_GOVERNANCA.md)\n- [Rastreabilidade da coerência metodológica](revisao-b-global/40_RASTREABILIDADE_COERENCIA_METODOLOGICA_LOCALIZADA.md)\n- [Rastreabilidade de voz e ritmo — Lote 01](revisao-b-global/42_RASTREABILIDADE_VOZ_RITMO_REPETICAO_LOTE_01.md)\n- [Ponto de retomada — Lote 01](revisao-b-global/43_PONTO_DE_RETOMADA_VOZ_RITMO_LOTE_01.md)",
            ),
            (
                "pendências da porta principal",
                "- coerência metodológica localizada;\n- passagem global de voz, ritmo e repetição;",
                "- passagem global de voz, ritmo e repetição nos Lotes 2–4;",
            ),
            (
                "próxima etapa da porta principal",
                "A **Reconciliação de Governança está concluída**.\n\nA próxima passagem textual autorizável é a **Rodada de Coerência Metodológica Localizada**, limitada aos pontos já auditados e sem reabrir a arquitetura ou as Partes.",
                "A **Reconciliação de Governança** e a **Coerência Metodológica Localizada** estão concluídas.\n\nA passagem global de voz, ritmo e repetição começou em lotes controlados. O **Lote 01 — Pré-livro e Partes I–II** está concluído. A próxima unidade autorizável é o **Lote 02 — Partes III–IV**.",
            ),
        ],
    )

    update(
        ROOT / "direcao-editorial/12_REGISTRO_MESTRE_DE_CONTEXTO.md",
        [
            (
                "versão do Registro Mestre",
                "**Versão:** 3.0 — Reconciliação do Marco 07",
                "**Versão:** 3.1 — Voz e ritmo, Lote 01",
            ),
            (
                "estado do Registro Mestre",
                "**Estado:** Revisão B textual completa; auditorias globais e especializadas em andamento",
                "**Estado:** Revisão B textual completa; governança e coerência metodológica reconciliadas; voz e ritmo concluídos no Lote 01",
            ),
            (
                "contagem do Registro Mestre",
                "- aproximadamente 36.859 palavras editoriais;",
                "- aproximadamente 37.084 palavras editoriais;",
            ),
            (
                "fase do Registro Mestre",
                "- PR #2 em rascunho e sem merge.",
                "- PR #2 em rascunho e sem merge;\n- voz, ritmo e repetição concluídos no Pré-livro e Partes I–II;\n- próximo lote textual: Partes III–IV.",
            ),
        ],
    )

    update(
        ROOT / "direcao-editorial/13_MATRIZ_DE_NAO_PERDA.md",
        [
            (
                "versão da Matriz",
                "**Versão:** 2.0 — Marco 07",
                "**Versão:** 2.1 — Pós-coerência e voz, Lote 01",
            ),
            (
                "estado da Matriz",
                "**Estado:** manuscrito completo em Revisão B; validações especializadas e produção pendentes",
                "**Estado:** manuscrito completo em Revisão B; coerência metodológica reconciliada; voz e ritmo concluídos no Lote 01; validações especializadas e produção pendentes",
            ),
            (
                "status do Mirante",
                "| 24 | Mirante do Discernimento | Ponto metacognitivo | Pré-livro e Suba | CORREÇÃO LOCALIZADA | parecer sistema extra | definir uso visual e checkpoints estratégicos |",
                "| 24 | Mirante do Discernimento | Ponto metacognitivo | Pré-livro e Suba | CANÔNICO | parecer sistema extra | integrado ao comando Suba e à descida; uso visual ainda pendente |",
            ),
            (
                "status do Filtro aplicado à influência",
                "| 35 | Filtro da Influência | Aplicação temática | Parte II/Workbook | CORREÇÃO LOCALIZADA | competir com Filtro oficial | mapear ao oficial, reduzir ou mover instrumento extenso |",
                "| 35 | Filtro da Influência | Aplicação temática | Parte II/Workbook | CANÔNICO | competir com Filtro oficial | aplicação mapeada ao Filtro oficial; sem lista paralela |",
            ),
        ],
    )

    print("Estado sincronizado após voz, ritmo e repetição — Lote 01.")


if __name__ == "__main__":
    main()
