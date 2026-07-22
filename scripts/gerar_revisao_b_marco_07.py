#!/usr/bin/env python3
"""Gera a Parte VIII e o Epílogo em Revisão B e fecha o Marco 07.

A Parte VIII é derivada da fonte histórica da Revisão A por transformações
explícitas e validadas. A fonte histórica não é alterada. O Marco 07 reúne o
manuscrito completo em Revisão B, capítulos 1–38 e Epílogo.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PART_VIII_A = ROOT / "revisao-integral/08_PARTE_VIII_REV_A.md"
PART_VIII_B = ROOT / "revisao-b-global/32_ONDA_8_PARTE_VIII_EPILOGO_REV_B.md"

B_SOURCES = [
    Path("revisao-b-global/03_ONDA_1_PRE_LIVRO_REV_B.md"),
    Path("revisao-b-global/04_ONDA_1_PARTE_I_REV_B.md"),
    Path("revisao-b-global/05_ONDA_2_PARTE_II_REV_B.md"),
    Path("revisao-b-global/07_ONDA_3_PARTE_III_REV_B.md"),
    Path("revisao-b-global/20_ONDA_4_PARTE_IV_REV_B.md"),
    Path("revisao-b-global/23_ONDA_5_PARTE_V_REV_B.md"),
    Path("revisao-b-global/26_ONDA_6_PARTE_VI_REV_B.md"),
    Path("revisao-b-global/29_ONDA_7_PARTE_VII_REV_B.md"),
    Path("revisao-b-global/32_ONDA_8_PARTE_VIII_EPILOGO_REV_B.md"),
]

CONTINUOUS = ROOT / "manuscrito-revisao-b/REPOSICIONESE_REV_B_CONTINUO.md"
MILESTONE = ROOT / "marcos-revisao-b/MARCO_07_MANUSCRITO_COMPLETO_REV_B.md"

CHAPTER_RE = re.compile(r"^# CAP[IÍ]TULO\s+(\d+)\b", re.MULTILINE | re.IGNORECASE)
EPILOGUE_RE = re.compile(r"^# EP[IÍ]LOGO\b", re.MULTILINE | re.IGNORECASE)

SEVEN_FRUITS = [
    "Verdade",
    "Responsabilidade",
    "Discernimento",
    "Coerência",
    "Coragem",
    "Sabedoria",
    "Legado",
]

FINAL_PHRASE = "Sua Árvore.\n\nSeus frutos.\n\nSua responsabilidade.\n\nSua possibilidade de cultivo."


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"Substituição {label!r}: esperado 1 trecho; encontrado {count}.")
    return text.replace(old, new, 1)


def build_part_viii() -> str:
    text = PART_VIII_A.read_text(encoding="utf-8").replace("\r\n", "\n").strip()

    text = replace_once(
        text,
        "> A Poda abre espaço. A Nova Semente decide o que será cultivado nesse espaço.\n\n---",
        "> A Poda abre espaço. A Nova Semente decide o que será cultivado nesse espaço.\n\nEsta Parte não acrescenta outro método. Ela completa o cultivo: escolher uma prática, criar condições, repetir com consciência, observar frutos, ajustar sem condenação e voltar à vida.\n\nO movimento será:\n\n> **Plante o que pode ser praticado. Repita o que produz vida. Revise o que não funciona. Desça e continue cultivando.**\n\nO livro não termina com uma promessa de transformação instantânea. Termina devolvendo a você um modo de observar, decidir, praticar e retornar.\n\n---",
        "abertura da Parte VIII",
    )

    text = replace_once(
        text,
        "Nova Semente é uma prática, interpretação, decisão, limite, ambiente ou hábito escolhido conscientemente e repetido até começar a produzir outro modo de viver.",
        "Nova Semente é uma prática, interpretação, decisão, limite, ambiente ou hábito escolhido conscientemente e repetido até começar a produzir outro modo de viver. Não é pensamento positivo, frase inspiradora nem promessa feita no auge da emoção. É algo que pode entrar na agenda, na linguagem, no acesso, no corpo, no dinheiro, no vínculo ou na forma de responder.",
        "definição prática da Nova Semente",
    )

    text = replace_once(
        text,
        "“Nas próximas quatro semanas, antes de aceitar compromissos, pedirei tempo para verificar agenda, energia e custo” é uma prática observável.\n\n## Desejo não é cultivo",
        "“Nas próximas quatro semanas, antes de aceitar compromissos, pedirei tempo para verificar agenda, energia e custo” é uma prática observável.\n\n## A menor Semente viável\n\nUma Semente praticável responde a cinco perguntas:\n\n1. **O quê:** qual comportamento será visível?\n2. **Quando:** que situação lembrará você de praticá-lo?\n3. **Onde:** em que Galho ou ambiente começará?\n4. **Com que apoio:** que recurso amplia sua capacidade sem decidir por você?\n5. **Quando revisar:** que prazo e que fruto mostrarão se precisa continuar, ajustar ou trocar a estratégia?\n\nComece pequeno o suficiente para entrar na vida e sério o suficiente para alterar direção. Pequeno não significa simbólico. Significa repetível.\n\n## Desejo não é cultivo",
        "menor Semente viável",
    )

    text = replace_once(
        text,
        "Ambiente não substitui escolha.\n\nEscolha não elimina ambiente.\n\nA Nova Semente precisa dos dois.",
        "Ambiente não substitui escolha.\n\nEscolha não elimina ambiente.\n\nA Nova Semente precisa dos dois. Também pode usar recursos que já existem em outro Galho: a disciplina que funciona no trabalho, a honestidade presente numa amizade, a capacidade de pedir ajuda numa área ou a prudência que você já pratica com outras pessoas. Cultivar não é começar do zero quando a própria Árvore já oferece material saudável.",
        "transferência de recursos saudáveis",
    )

    text = replace_once(
        text,
        "Responsabilidade não exige perfeição.\n\nExige retorno.\n\n## Apoio sem terceirização",
        "Responsabilidade não exige perfeição.\n\nExige retorno.\n\nRetornar significa observar sem transformar recaída em identidade, reparar o que for seu, reconhecer a condição que aumentou vulnerabilidade e recolocar a prática na vida com o ajuste necessário.\n\nTambém significa repetir conscientemente o que funcionou. O método não foi criado apenas para investigar erro. Um bom fruto precisa revelar que prática, ambiente, vínculo e recurso merecem continuidade.\n\n## Apoio sem terceirização",
        "retorno e repetição do que funciona",
    )

    text = replace_once(
        text,
        "> **LEI 14 — SEJA SENSATA.**\n>\n> Sensatez não se apega à forma por vaidade. Preserva o propósito e revisa o caminho quando a realidade exige.\n\n---",
        "> **LEI 14 — SEJA SENSATA.**\n>\n> Sensatez não se apega à forma por vaidade. Preserva o propósito e revisa o caminho quando a realidade exige.\n\n## O cultivo continua\n\nDepois deste livro, o movimento permanece simples:\n\n> **Observe os frutos → reconheça o que funcionou e o que falhou → investigue estrutura e influência → passe pelo Filtro → escolha uma resposta → aja → observe novos frutos.**\n\nIsso não recebe outro nome porque não é outro método. É a Árvore em uso.\n\nMetacognição não é uma técnica reservada à crise. É a disciplina de perceber como você está pensando antes de acreditar, repetir, reagir ou decidir — e de saber quando parar de analisar para agir.\n\n---",
        "continuidade do cultivo",
    )

    text = replace_once(
        text,
        "Este capítulo não apresenta os Sete Frutos canônicos.\n\nApresenta sinais cotidianos de que o método começa a ser incorporado.",
        "Este capítulo não apresenta os Sete Frutos canônicos.\n\nApresenta sinais cotidianos de que o método começa a ser incorporado. Eles não formam certificado de maturidade nem escala de valor. Servem como evidências provisórias, observadas em padrão e contexto — nunca como sentença produzida por um episódio isolado.",
        "sinais cotidianos sem desempenho",
    )

    text = replace_once(
        text,
        "Os sete frutos abaixo não são recompensas garantidas.\n\nNão são as únicas consequências possíveis.\n\nNão significam perfeição.\n\nSão uma síntese pedagógica de qualidades que tendem a crescer quando discernimento e posicionamento são cultivados.",
        "Os sete frutos abaixo não são recompensas garantidas.\n\nNão são as únicas consequências possíveis.\n\nNão significam perfeição.\n\nSão uma síntese pedagógica de qualidades que tendem a crescer quando discernimento e posicionamento são cultivados. Permanecem subordinados à Árvore: nenhum deles explica sozinho a pessoa, o contexto ou o valor de uma vida. O padrão ao longo do tempo importa mais do que um resultado isolado.",
        "Sete Frutos subordinados à Árvore",
    )

    old_ch38_opening = """Você já estava posicionada quando abriu este livro.

Talvez sua posição fosse silêncio.

Adaptação.

Reação.

Controle.

Medo.

Conveniência.

Coragem.

Responsabilidade.

Confusão.

Talvez variasse conforme o Galho.

O objetivo nunca foi transformar você numa personagem firme o tempo inteiro.

Foi ensinar a enxergar.

Observar frutos.

Subir na Árvore.

Deixar na Árvore aquilo que ainda não foi examinado.

Voltar às Raízes sem morar no passado.

Compreender o Solo sem tratá-lo como destino.

Reconhecer Pragas sem transformar pessoas em Pragas.

Passar pelo Filtro.

Podar com sensatez.

Plantar uma prática.

Descer para a vida."""

    new_ch38_opening = """Você já estava posicionada quando abriu este livro.

Talvez sua posição fosse silêncio, adaptação, reação, controle, medo, coragem, responsabilidade ou confusão. Talvez variasse conforme o Galho.

O objetivo nunca foi transformar você numa personagem firme o tempo inteiro. Foi ensinar a enxergar e voltar à vida com mais participação: observar frutos, perceber como está pensando, investigar sem morar no passado, filtrar sem entregar a consciência, podar sem punir, plantar uma prática e descer.

O resultado mais honesto não é:

> “Agora eu sei tudo sobre quem sou.”

É:

> **Agora sei como continuar examinando quem estou me tornando.**"""

    text = replace_once(text, old_ch38_opening, new_ch38_opening, "concentração do Capítulo 38")

    text = replace_once(
        text,
        "Responsabilidade pergunta:\n\n> O que é meu agora?\n\n## A Jaula está aberta",
        "Responsabilidade pergunta:\n\n> O que é meu agora?\n\n## Cinco convicções para continuar\n\n1. **Pelos frutos a Árvore é investigada.** Fruto é evidência em contexto e ao longo do tempo, não sentença sobre identidade.\n2. **O que funciona também deve ser observado.** Reconheça a prática, o vínculo, o ambiente e o recurso que produziram vida — e repita com consciência.\n3. **Pensar por si não é pensar sozinho.** Aprenda, consulte, pertença e confie proporcionalmente sem terceirizar a conclusão.\n4. **Responsabilidade real não é culpa total.** Responda pelo que é seu dentro da esfera, dos recursos e das possibilidades existentes.\n5. **A consciência precisa continuar observável.** Qualquer pessoa, grupo, fé, causa, autoridade, algoritmo ou autora pode voltar a ocupar espaço demais quando deixa de ser examinada.\n\nVocê não precisa viver desconfiando de tudo. Precisa continuar capaz de perguntar por que acredita, quem participa da conclusão, o que ainda precisa verificar e que fruto essa forma de pensar tende a produzir.\n\n## A Jaula está aberta",
        "cinco convicções finais",
    )

    text = replace_once(
        text,
        "Você não precisa viver desconfiando de tudo. Precisa continuar capaz de perguntar por que acredita, quem participa da conclusão, o que ainda precisa verificar e que fruto essa forma de pensar tende a produzir.\n\n## A Jaula está aberta",
        "Você não precisa viver desconfiando de tudo. Precisa continuar capaz de perguntar por que acredita, quem participa da conclusão, o que ainda precisa verificar e que fruto essa forma de pensar tende a produzir.\n\n> **Nenhum grupo pensará automaticamente por mim, nem mesmo o grupo que representa meus valores.**\n\nQuando a polarização tentar entregar uma sentença antes do exame, quando a Fuga Identitária oferecer um rótulo para substituir a pessoa inteira, ou quando influenciadores e algoritmos repetirem uma voz até ela parecer sua, volte às perguntas: *Estou aprendendo ou entregando o trabalho da minha consciência? Consigo pertencer sem desaparecer? Esta identificação amplia minha consciência ou está substituindo quem sou?*\n\n## A Jaula está aberta",
        "fechamento explícito de polarização, Fuga Identitária e influência",
    )

    text = replace_once(
        text,
        "## O ritual final\n\n### 1. Observe os Frutos",
        "## O ritual final\n\nEstes dez movimentos não formam um método novo. Reúnem, numa travessia breve, aquilo que você já praticou ao longo da Árvore.\n\n### 1. Observe os Frutos",
        "ritual como síntese",
    )

    text = replace_once(
        text,
        "## Agora desça\n\nVocê não precisa saber tudo.",
        "## Agora desça\n\nMetacognição será uma disciplina permanente de liberdade, mas não uma moradia. Você continuará observando o pensamento para devolver qualidade à ação — não para adiar indefinidamente o custo de escolher.\n\nVocê não precisa saber tudo.",
        "metacognição e descida",
    )

    old_epilogue = """# EPÍLOGO — O CAJUEIRO AINDA ESTÁ LÁ

O Cajueiro de Pirangi não se tornou menor depois que você enxergou sua estrutura.

Continuou vasto.

Complexo.

Cheio de caminhos, apoios, sombras e expansões.

Compreender não retirou a beleza.

Aumentou o olhar.

Talvez sua vida também continue complexa depois desta leitura.

Algumas perguntas permanecerão.

Alguns frutos precisarão de tempo.

Algumas Raízes ainda serão encontradas.

Alguns Galhos exigirão cuidado que este livro não consegue oferecer sozinho.

Mas agora você possui um ponto de observação.

Quando a emoção ocupar todo o horizonte, suba.

Quando o grupo oferecer certeza rápida, suba.

Quando a culpa tentar condenar, suba.

Quando a dor pedir cuidado, suba sem abandoná-la no chão.

Quando a análise virar moradia, desça.

Quando a clareza chegar, desça.

Quando a responsabilidade estiver na sua esfera, desça.

A Árvore não existe para afastar você da vida.

Existe para devolver você a ela com mais consciência.

O mundo continuará tentando ensinar reação.

Você agora possui uma linguagem para escolher presença.

E toda vez que um novo fruto aparecer, a investigação poderá começar outra vez.

Sua Árvore.

Seus frutos.

Sua responsabilidade.

Sua possibilidade de cultivo."""

    new_epilogue = """# EPÍLOGO — O CAJUEIRO AINDA ESTÁ LÁ

O Cajueiro de Pirangi continua vasto.

De longe, parece um emaranhado. De perto, revela apoios, caminhos, sombras, raízes que encontram o chão e Galhos que continuam avançando.

Compreender sua estrutura não o tornou menor.

Aumentou o olhar.

Sua vida talvez continue complexa depois desta leitura. Alguns frutos precisarão de tempo. Algumas Raízes ainda serão encontradas. Certos Galhos exigirão cuidado, proteção ou competência que um livro não pode oferecer sozinho.

Mas agora você possui um ponto de observação.

Quando a reação ocupar todo o horizonte, suba.

Quando a clareza suficiente chegar, desça.

A Árvore não existe para afastar você da vida.

Existe para devolver você a ela com mais consciência.

O Cajueiro ainda está lá.

E você também — não fora da própria história, mas presente o suficiente para continuar cultivando.

Sua Árvore.

Seus frutos.

Sua responsabilidade.

Sua possibilidade de cultivo."""

    text = replace_once(text, old_epilogue, new_epilogue, "Epílogo literário concentrado")

    chapters = [int(value) for value in CHAPTER_RE.findall(text)]
    if chapters != list(range(33, 39)):
        raise ValueError(f"Parte VIII inválida. Esperado capítulos 33-38; encontrado {chapters}.")
    if not EPILOGUE_RE.search(text):
        raise ValueError("Epílogo ausente na Parte VIII.")

    for fruit in SEVEN_FRUITS:
        if f"## {SEVEN_FRUITS.index(fruit) + 1}. {fruit}" not in text:
            raise ValueError(f"Fruto canônico ausente: {fruit}")

    if FINAL_PHRASE not in text:
        raise ValueError("Frase final canônica ausente ou alterada.")

    PART_VIII_B.parent.mkdir(parents=True, exist_ok=True)
    PART_VIII_B.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")
    return text.strip() + "\n"


def read(path: Path) -> str:
    full = ROOT / path
    if not full.is_file():
        raise FileNotFoundError(f"Fonte ausente: {path}")
    text = full.read_text(encoding="utf-8").replace("\r\n", "\n").strip()
    if not text:
        raise ValueError(f"Fonte vazia: {path}")
    return text


def validate(text: str) -> None:
    found = [int(value) for value in CHAPTER_RE.findall(text)]
    if found != list(range(1, 39)):
        raise ValueError(f"Sequência inválida. Esperado 1-38; encontrado {found}")
    if len(found) != len(set(found)):
        raise ValueError("Há capítulos duplicados.")
    if not EPILOGUE_RE.search(text):
        raise ValueError("Epílogo ausente.")
    if text.count("# EPÍLOGO") != 1:
        raise ValueError("Quantidade inválida de Epílogos.")


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
> Gerado em {generated}. A Revisão A e os Marcos 01–06 permanecem preservados.

\\newpage
'''


def assemble(sources: list[Path]) -> str:
    pieces: list[str] = []
    for index, path in enumerate(sources):
        if index:
            pieces.append("\n")
        pieces.append(f"<!-- FONTE: {path.as_posix()} | STATUS: REVISÃO B -->")
        pieces.append(read(path))
        pieces.append(f"<!-- FIM DA FONTE: {path.as_posix()} -->")
    return "\n\n".join(pieces).strip() + "\n"


def main() -> None:
    build_part_viii()

    body = assemble(B_SOURCES)
    validate(body)

    CONTINUOUS.parent.mkdir(parents=True, exist_ok=True)
    MILESTONE.parent.mkdir(parents=True, exist_ok=True)

    CONTINUOUS.write_text(
        metadata(
            "Manuscrito contínuo completo — Revisão B — Marco 07",
            "MANUSCRITO DE TRABALHO — REVISÃO B COMPLETA. Pré-livro, Partes I–VIII e Epílogo revisados.",
        )
        + body,
        encoding="utf-8",
        newline="\n",
    )

    MILESTONE.write_text(
        metadata(
            "Marco 07 — Manuscrito completo — Revisão B",
            "MARCO 07 DA REVISÃO B — Manuscrito completo, capítulos 1–38 e Epílogo revisados.",
        )
        + body,
        encoding="utf-8",
        newline="\n",
    )

    print(f"Gerado: {PART_VIII_B.relative_to(ROOT)}")
    print(f"Gerado: {CONTINUOUS.relative_to(ROOT)}")
    print(f"Gerado: {MILESTONE.relative_to(ROOT)}")
    print("Validação: Parte VIII 33–38 + Epílogo; manuscrito e Marco 07 com capítulos 1–38 + Epílogo.")


if __name__ == "__main__":
    main()
