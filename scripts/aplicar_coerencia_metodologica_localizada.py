#!/usr/bin/env python3
"""Aplica correções metodológicas localizadas já autorizadas na Revisão B.

Escopo:
- distinguir entrada do cultivo e estrutura da Árvore no Pré-livro;
- tornar o Mirante uma função do comando Suba na Árvore;
- substituir o Filtro da Influência por aplicação temática do Filtro oficial;
- padronizar o Checkpoint da Parte III;
- fechar polarização, Fuga Identitária e influência no Capítulo 38;
- manter os geradores dos Marcos 06 e 07 reprodutíveis.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8").replace("\r\n", "\n")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8", newline="\n")


def replace_or_confirm(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{label}: esperado 1 trecho antigo; encontrado {count}.")
    return text.replace(old, new, 1)


def patch_prebook() -> None:
    path = "revisao-b-global/03_ONDA_1_PRE_LIVRO_REV_B.md"
    text = read(path)

    old_map = """- **Mirante do Discernimento:** o ponto metacognitivo de onde você observa sem se reduzir ao fruto e decide quando descer para agir.

A ordem estrutural é:

> **Semente → Solo → Raízes → Tronco → Galhos → Frutos.**"""
    new_map = """- **Mirante do Discernimento:** o ponto metacognitivo de onde você observa sem se reduzir ao fruto e decide quando descer para agir. Não é uma camada da Árvore nem uma ferramenta separada; é o nome do ponto de observação alcançado quando você sobe.

A **Semente** é a entrada do cultivo.

A estrutura da Árvore é:

> **Solo → Raízes → Tronco → Galhos → Frutos.**

A representação editorial completa pode mostrar:

> **Semente → Solo → Raízes → Tronco → Galhos → Frutos.**"""
    text = replace_or_confirm(text, old_map, new_map, "mapa, Semente e Mirante")

    old_command = "- **Suba na Árvore:** amplie o panorama e perceba como está pensando enquanto pensa."
    new_command = "- **Suba na Árvore:** amplie o panorama e perceba como está pensando enquanto pensa. Esse ponto de observação é o Mirante do Discernimento; você não precisa decorá-lo como etapa separada."
    text = replace_or_confirm(text, old_command, new_command, "comando Suba e Mirante")

    write(path, text)


def patch_part_ii() -> None:
    path = "revisao-b-global/05_ONDA_2_PARTE_II_REV_B.md"
    text = read(path)

    old = """## O Filtro da Influência

O Filtro da Influência não é outro método.

É o Filtro da Sensatez aplicado ao momento em que uma voz externa pede acesso.

Pergunte:

1. Percebi que estava sendo influenciada?
2. A fonte distingue fato, opinião, experiência e interpretação?
3. A pessoa possui competência para esta afirmação específica?
4. Posso discordar sem perder meu lugar?
5. Existe pressão de medo, vergonha, urgência ou pertencimento?
6. Aplico o mesmo rigor ao meu grupo e ao grupo oposto?
7. Esta influência amplia minha capacidade de pensar ou oferece respostas para que eu não precise pensar?
8. Que fruto já produz em mim?
9. O que ela me ajudou a compreender com mais clareza?
10. Ainda consigo dizer “não sei”?
11. O que preciso verificar fora desta fonte?
12. Que nível de acesso esta voz realmente merece?

Influência saudável pode confrontar e mudar uma opinião.

Mas devolve você à responsabilidade de discernir.

Influência adoecida precisa que você permaneça dependente da voz que interpreta tudo."""

    new = """## O Filtro da Sensatez aplicado à influência

Não existe um segundo Filtro.

Quando uma voz externa pede acesso, você usa as mesmas doze perguntas oficiais do Filtro da Sensatez, com atenção especial a quatro focos:

- **Verdade e evidência:** qual é a afirmação, o que é fato, qual é a fonte, que competência ela possui e o que precisa ser verificado fora dela?
- **Justiça e simetria:** eu aplicaria o mesmo rigor se a mensagem viesse do meu grupo, do grupo oposto ou de alguém que não admiro?
- **Liberdade e acesso:** consigo discordar, dizer “não sei” e limitar a influência sem perder toda dignidade ou pertencimento? Existe pressão de medo, vergonha, urgência ou lealdade?
- **Fruto e responsabilidade:** esta voz amplia minha capacidade de pensar, que clareza realmente ofereceu, que fruto produz e que nível de acesso merece?

Em decisões de alto custo, volte ao conjunto completo das doze perguntas. Estes focos não formam outra lista oficial; apenas mostram onde o Filtro costuma revelar acesso indevido ou influência saudável.

Influência saudável pode confrontar e mudar uma opinião.

Mas devolve você à responsabilidade de discernir.

Influência adoecida precisa que você permaneça dependente da voz que interpreta tudo."""

    text = replace_or_confirm(text, old, new, "Filtro aplicado à influência")
    write(path, text)


def patch_part_iii() -> None:
    path = "revisao-b-global/07_ONDA_3_PARTE_III_REV_B.md"
    text = read(path)
    text = replace_or_confirm(
        text,
        "## Checkpoint da Parte III",
        "# CHECKPOINT DA PARTE III",
        "hierarquia do Checkpoint da Parte III",
    )
    write(path, text)


def patch_part_vii_and_generator() -> None:
    path = "revisao-b-global/29_ONDA_7_PARTE_VII_REV_B.md"
    text = read(path)

    old = "Metacognição não exige permanecer no Mirante. Também percebe quando pensar deixou de servir à decisão e começou a protegê-la do custo."
    new = "O Mirante não é uma nova camada da Árvore nem um lugar em que você precisa permanecer. É o nome do ponto de observação criado quando você sobe, percebe como está pensando e recupera panorama suficiente para escolher. Metacognição também reconhece quando pensar deixou de servir à decisão e começou a protegê-la do custo."
    text = replace_or_confirm(text, old, new, "função editorial do Mirante na Parte VII")
    write(path, text)

    generator_path = "scripts/gerar_revisao_b_marco_06.py"
    generator = read(generator_path)
    generator = replace_or_confirm(generator, old, new, "reprodutibilidade do Mirante no gerador 06")
    write(generator_path, generator)


def patch_generator_vii() -> None:
    path = "scripts/gerar_revisao_b_marco_07.py"
    text = read(path)

    marker = '''        "cinco convicções finais",\n    )\n\n    text = replace_once(\n        text,\n        "## O ritual final\\n\\n### 1. Observe os Frutos",'''

    inserted = '''        "cinco convicções finais",\n    )\n\n    text = replace_once(\n        text,\n        "Você não precisa viver desconfiando de tudo. Precisa continuar capaz de perguntar por que acredita, quem participa da conclusão, o que ainda precisa verificar e que fruto essa forma de pensar tende a produzir.\\n\\n## A Jaula está aberta",\n        "Você não precisa viver desconfiando de tudo. Precisa continuar capaz de perguntar por que acredita, quem participa da conclusão, o que ainda precisa verificar e que fruto essa forma de pensar tende a produzir.\\n\\n> **Nenhum grupo pensará automaticamente por mim, nem mesmo o grupo que representa meus valores.**\\n\\nQuando a polarização tentar entregar uma sentença antes do exame, quando a Fuga Identitária oferecer um rótulo para substituir a pessoa inteira, ou quando influenciadores e algoritmos repetirem uma voz até ela parecer sua, volte às perguntas: *Estou aprendendo ou entregando o trabalho da minha consciência? Consigo pertencer sem desaparecer? Esta identificação amplia minha consciência ou está substituindo quem sou?*\\n\\n## A Jaula está aberta",\n        "fechamento explícito de polarização, Fuga Identitária e influência",\n    )\n\n    text = replace_once(\n        text,\n        "## O ritual final\\n\\n### 1. Observe os Frutos",'''

    text = replace_or_confirm(text, marker, inserted, "transformação final no gerador 07")
    write(path, text)


def validate_sources() -> None:
    pre = read("revisao-b-global/03_ONDA_1_PRE_LIVRO_REV_B.md")
    part2 = read("revisao-b-global/05_ONDA_2_PARTE_II_REV_B.md")
    part3 = read("revisao-b-global/07_ONDA_3_PARTE_III_REV_B.md")
    part7 = read("revisao-b-global/29_ONDA_7_PARTE_VII_REV_B.md")
    gen7 = read("scripts/gerar_revisao_b_marco_07.py")

    assert "A estrutura da Árvore é:" in pre
    assert "> **Solo → Raízes → Tronco → Galhos → Frutos.**" in pre
    assert "Não é uma camada da Árvore" in pre
    assert "## O Filtro da Influência" not in part2
    assert "## O Filtro da Sensatez aplicado à influência" in part2
    assert "Estes focos não formam outra lista oficial" in part2
    assert "# CHECKPOINT DA PARTE III" in part3
    assert "## Checkpoint da Parte III" not in part3
    assert "O Mirante não é uma nova camada da Árvore" in part7
    assert "fechamento explícito de polarização, Fuga Identitária e influência" in gen7


def main() -> None:
    patch_prebook()
    patch_part_ii()
    patch_part_iii()
    patch_part_vii_and_generator()
    patch_generator_vii()
    validate_sources()
    print("Correções metodológicas localizadas aplicadas e fontes reprodutíveis atualizadas.")


if __name__ == "__main__":
    main()
