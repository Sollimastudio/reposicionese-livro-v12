#!/usr/bin/env python3
"""Atualiza a auditoria técnica para o estado posterior ao Lote 03."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts/auditar_estado_completo_revisao_b.py"


def replace_guarded(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise ValueError(f"{label}: esperado trecho antigo ou versão nova; encontrado {count}.")


def main() -> None:
    text = TARGET.read_text(encoding="utf-8").replace("\r\n", "\n")
    text = replace_guarded(
        text,
        '    last_four_words = sum(part_words[name] for name in ["Parte V", "Parte VI", "Parte VII", "Parte VIII + Epílogo"])',
        '    remaining_voice_words = sum(part_words[name] for name in ["Parte VII", "Parte VIII + Epílogo"])',
        "variável de pendência",
    )
    text = replace_guarded(
        text,
        '        f"As Partes V–VIII e o Epílogo concentram **{fmt_int(last_four_words)} palavras**, equivalentes a **{fmt_pct(percentage(last_four_words, total_words))}%** das fontes vivas. Essas unidades ainda não receberam a passagem completa de voz e ritmo dos Lotes 03–04.",',
        '        f"A Parte VII, a Parte VIII e o Epílogo concentram **{fmt_int(remaining_voice_words)} palavras**, equivalentes a **{fmt_pct(percentage(remaining_voice_words, total_words))}%** das fontes vivas. Essas unidades ainda não receberam a passagem completa de voz e ritmo do Lote 04.",',
        "resumo de volume pendente",
    )
    text = replace_guarded(
        text,
        '        "Esses números não representam erro automático. Servem para localizar risco de fadiga, especialmente nas Partes ainda não submetidas aos Lotes 03–04.",',
        '        "Esses números não representam erro automático. Servem para localizar risco de fadiga, especialmente nas unidades ainda não submetidas ao Lote 04.",',
        "nota de densidade",
    )
    text = replace_guarded(
        text,
        '        "1. Lotes 03–04 de voz, ritmo e repetição;",',
        '        "1. Lote 04 de voz, ritmo e repetição;",',
        "veredito de voz",
    )
    TARGET.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print("Auditoria técnica atualizada para o estado pós-Lote 03.")


if __name__ == "__main__":
    main()
