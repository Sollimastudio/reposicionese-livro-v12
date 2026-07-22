#!/usr/bin/env python3
"""Gera a Parte VII em Revisão B, o manuscrito contínuo e o Marco 06.

A Parte VII é derivada da fonte histórica da Revisão A por transformações
explícitas e validadas. A fonte histórica não é alterada. O Marco 06 reúne
Pré-livro e Partes I–VII em Revisão B; a Parte VIII continua herdada da
Revisão A até a próxima passagem.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PART_VII_A = ROOT / "revisao-integral/07_PARTE_VII_REV_A.md"
PART_VII_B = ROOT / "revisao-b-global/29_ONDA_7_PARTE_VII_REV_B.md"

B_SOURCES = [
    Path("revisao-b-global/03_ONDA_1_PRE_LIVRO_REV_B.md"),
    Path("revisao-b-global/04_ONDA_1_PARTE_I_REV_B.md"),
    Path("revisao-b-global/05_ONDA_2_PARTE_II_REV_B.md"),
    Path("revisao-b-global/07_ONDA_3_PARTE_III_REV_B.md"),
    Path("revisao-b-global/20_ONDA_4_PARTE_IV_REV_B.md"),
    Path("revisao-b-global/23_ONDA_5_PARTE_V_REV_B.md"),
    Path("revisao-b-global/26_ONDA_6_PARTE_VI_REV_B.md"),
    Path("revisao-b-global/29_ONDA_7_PARTE_VII_REV_B.md"),
]

A_FALLBACK_SOURCES = [Path("revisao-integral/08_PARTE_VIII_REV_A.md")]

CONTINUOUS = ROOT / "manuscrito-revisao-b/REPOSICIONESE_REV_B_CONTINUO.md"
MILESTONE = ROOT / "marcos-revisao-b/MARCO_06_PRE_LIVRO_PARTES_I_II_III_IV_V_VI_VII.md"

CHAPTER_RE = re.compile(r"^# CAP[IÍ]TULO\s+(\d+)\b", re.MULTILINE | re.IGNORECASE)
EPILOGUE_RE = re.compile(r"^# EP[IÍ]LOGO\b", re.MULTILINE | re.IGNORECASE)

OFFICIAL_FILTER = """1. Isso é verdadeiro?
2. Tem lógica?
3. Tem evidência?
4. É justo?
5. É nobre?
6. Constrói vínculos ou alimenta divisão?
7. Resistiria ao tempo?
8. Que fruto produz a curto, médio e longo prazo?
9. É fato, narrativa ou manipulação?
10. Estou reagindo ou discernindo?
11. Qual parte da Árvore está falando?
12. O que uma pessoa posicionada faria com essa informação?"""

TYPE_NAMES = [
    "O Soberano",
    "O Vulcão",
    "A Névoa",
    "O Fantasma",
    "O Espelho Partido",
    "O Ator",
    "O Herdeiro",
    "O Náufrago",
    "O Eco",
    "A Vitrine",
    "O Muro",
    "O Espelho",
    "O Templo",
    "O Camaleão",
]

LAWS = [
    "Pense Antes de Reagir",
    "Questione a Narrativa",
    "Desligue o Piloto Automático",
    "Cultive o Silêncio Mental",
    "Resista à Manada",
    "Filtre Suas Influências",
    "Pratique o Julgamento Próprio",
    "Não Ignore o Óbvio",
    "Pense a Longo Prazo",
    "Observe os Frutos",
    "Assuma Sua Responsabilidade",
    "Cumpra Seu Dever",
    "Abrace o Desconforto",
    "Seja Sensata",
]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"Substituição {label!r}: esperado 1 trecho; encontrado {count}.")
    return text.replace(old, new, 1)


def build_part_vii() -> str:
    text = PART_VII_A.read_text(encoding="utf-8").replace("\r\n", "\n").strip()

    text = replace_once(
        text,
        "> Discernimento sem decisão vira contemplação. Decisão sem discernimento vira reação. Posicionamento exige os dois.\n\n---",
        "> Discernimento sem decisão vira contemplação. Decisão sem discernimento vira reação. Posicionamento exige os dois.\n\nEsta Parte não acrescenta outro método. Ela transforma a leitura da Árvore em decisão: examinar com o Filtro, reconhecer modos de posicionamento, escolher a Poda adequada e descer com uma ação.\n\nO movimento será:\n\n> **Filtre com proporção. Nomeie sem rotular. Pode sem punir. Preserve o que produz vida. Plante antes de deixar o espaço vazio.**\n\nDiscernimento não é duvidar de tudo para sempre. É verificar o necessário, decidir com honestidade dentro da incerteza e revisar quando novas evidências ou novos frutos aparecerem.\n\n---",
        "abertura da Parte VII",
    )

    text = replace_once(
        text,
        "O objetivo é que o Filtro deixe de ser uma lista decorada e se torne uma forma de pensar.",
        "O objetivo é que o Filtro deixe de ser uma lista decorada e se torne uma forma de pensar.\n\n## Filtro proporcional\n\nNem toda situação exige o mesmo grau de investigação.\n\n- **Baixo custo e fácil reversão:** use as perguntas necessárias para não agir no automático.\n- **Custo médio:** verifique fato, interpretação, valor, influência e consequência.\n- **Alto custo, difícil reversão ou risco para outras pessoas:** use as doze perguntas, procure competência adequada e considere tempo, segurança, dever e impacto.\n- **Perigo imediato:** proteção pode vir antes da análise completa. O Filtro não exige permanência em risco para produzir uma resposta intelectualmente perfeita.\n\nProporção impede dois erros: decidir sem exame e usar exame infinito para não decidir.\n\n## Regra de parada do Filtro\n\nO Filtro não promete certeza absoluta. Ele procura base suficiente para o próximo movimento responsável.\n\nVocê pode parar de examinar e decidir quando:\n\n1. os fatos relevantes disponíveis foram separados das interpretações;\n2. as fontes usadas possuem competência compatível com a afirmação;\n3. riscos, deveres, poder e pessoas afetadas foram considerados;\n4. a decisão combina com os valores que você afirma sustentar;\n5. existe uma ação possível e um critério para revisar depois.\n\nQuando informação importante ainda falta, a decisão pode ser provisória. Quando nenhuma evidência nova aparece e o pensamento apenas repete medo, a investigação pode ter virado adiamento.\n\n> **Confiar provisoriamente não é terceirizar a consciência. Decidir sob incerteza não é agir sem critério.**",
        "proporção e regra de parada do Filtro",
    )

    text = replace_once(
        text,
        "- a afirmação pode ser testada?\n\nNão transforme ausência de prova completa em prova de ausência.",
        "- a afirmação pode ser testada?\n\nUma fonte competente pode receber confiança provisória sem receber governo ilimitado. Verifique competência, escopo, histórico, possíveis conflitos, transparência sobre incerteza e possibilidade de confirmação independente. Especialistas ajudam você a decidir melhor; não substituem automaticamente sua responsabilidade de compreender o suficiente para consentir, escolher ou pedir outra avaliação.\n\nNão transforme ausência de prova completa em prova de ausência.",
        "confiança provisória em fontes",
    )

    text = replace_once(
        text,
        "Ouvir verdade exige Filtro, não submissão.\n\n## Como receber uma crítica",
        "Ouvir verdade exige Filtro, não submissão.\n\n## O ouvido discernente\n\nEntre o ouvido defensivo e o ouvido submetido existe um terceiro modo: permanecer presente sem entregar a conclusão.\n\nO ouvido discernente consegue:\n\n- escutar até o fim quando há segurança;\n- pedir exemplos e evidências;\n- separar conteúdo, forma e intenção provável;\n- reconhecer uma parte verdadeira sem aceitar a acusação inteira;\n- discordar sem apagar o que precisa reparar;\n- consultar outra fonte quando falta competência;\n- suspender resposta quando a emoção ainda governa;\n- encerrar a conversa quando existe abuso ou risco.\n\nMetacognição aparece aqui como pergunta prática: **o que estou fazendo com o que ouvi antes de concluir quem sou ou o que devo fazer?**\n\n## Como receber uma crítica",
        "ouvido discernente",
    )

    text = replace_once(
        text,
        "Essas palavras descrevem modos de posicionamento.\n\nA mesma pessoa pode operar de forma saudável no trabalho, morna na família e tóxica numa discussão política.",
        "Essas palavras descrevem modos de posicionamento. Não autorizam dizer que uma pessoa *é* saudável, tóxica ou morna como identidade total. Descreva o comportamento, o contexto, o poder, a repetição e o fruto.\n\nA mesma pessoa pode operar de forma saudável no trabalho, morna na família e tóxica numa discussão política.",
        "modos, não identidades",
    )

    text = replace_once(
        text,
        "Os nomes são imagens pedagógicas.\n\nNão são categorias clínicas.\n\n## 1. O Soberano",
        "Os nomes são imagens pedagógicas.\n\nNão são categorias clínicas. Também não são testes de personalidade, sentença espiritual ou licença para catalogar quem convive com você.\n\nAntes de reconhecer um Tipo, nomeie:\n\n1. o Galho em que aparece;\n2. a situação e a pressão presentes;\n3. o comportamento observável;\n4. o fruto repetido;\n5. o recurso legítimo que precisa ser recuperado;\n6. o próximo movimento praticável.\n\nUm episódio isolado não define um Tipo. O Tipo é um espelho temporário do Modo Operante.\n\n## 1. O Soberano",
        "regras de uso dos Tipos",
    )

    praga_count = text.count("**Praga provável:**")
    if praga_count != 14:
        raise ValueError(f"Esperadas 14 ocorrências de 'Praga provável'; encontradas {praga_count}.")
    text = text.replace("**Praga provável:**", "**Mecanismo que pode aparecer:**")

    text = replace_once(
        text,
        "Não use os Tipos para analisar todos ao redor e escapar de si.\n\n> **SUBA NA ÁRVORE.**",
        "Não use os Tipos para analisar todos ao redor e escapar de si. Não diga “ele é o Vulcão” ou “ela é a Vitrine”. Diga, quando necessário: “nesta situação, observo tal comportamento, tal mecanismo e tal fruto”.\n\nUse os Tipos primeiro para reconhecer o que aparece em você sob pressão. Depois procure onde o Soberano já existe: o Galho em que você consegue escutar, sustentar limite, admitir erro, preservar dignidade e agir com responsabilidade. Esse recurso pode ser transferido.\n\nNenhum Tipo precisa ser destruído como se fosse uma pessoa interna. O trabalho é preservar a necessidade legítima e mudar a forma de atendê-la. A energia do Vulcão pode virar coragem com pausa. A prudência da Névoa pode ganhar prazo. A adaptação do Camaleão pode voltar a servir à flexibilidade sem trair o eixo.\n\n> **SUBA NA ÁRVORE.**",
        "uso responsável e recurso dos Tipos",
    )

    text = replace_once(
        text,
        "Nem toda Poda é rompimento.\n\nPode ser redução, reorganização, pausa, mudança de frequência, limite, delegação, revisão de contrato, saída gradual ou interrupção completa.\n\n## O percurso da Poda",
        "Nem toda Poda é rompimento.\n\nPode ser redução, reorganização, pausa, mudança de frequência, limite, delegação, revisão de contrato, saída gradual ou interrupção completa.\n\n## Antes de podar, reconheça o que produz vida\n\nA investigação não começa com a pergunta “o que posso cortar?”. Começa com:\n\n- que bom fruto existe aqui?\n- que valor, vínculo, competência, tradição, rotina ou dever precisa ser preservado?\n- o problema está no mecanismo, no acesso, na prática, no acordo ou no vínculo inteiro?\n- existe reparação possível e segura?\n- que responsabilidade continua mesmo se a forma mudar?\n- qual Nova Semente impedirá que o espaço volte a ser ocupado pelo mesmo padrão?\n\nUma relação pode precisar de limite sem precisar de destruição. Uma tradição pode precisar de exame sem precisar de desprezo. Uma rotina pode precisar de ajuste, não abandono. Um ambiente perigoso pode exigir saída, proteção ou denúncia. O fruto, o poder, o dever e a segurança determinam a forma.\n\n## O percurso da Poda",
        "preservação antes da Poda",
    )

    text = replace_once(
        text,
        "### 8. Prepare a Nova Semente\n\nO que ocupará o espaço aberto?\n\n## Poda não é vingança",
        "### 8. Prepare a Nova Semente\n\nO que ocupará o espaço aberto?\n\n## O objeto exato da Poda\n\nAntes de agir, escreva uma frase precisa:\n\n> **Não estou podando uma pessoa. Estou interrompendo, reduzindo ou reorganizando __________ porque os frutos observados são __________. Vou preservar __________ e plantar __________.**\n\nA Poda pode ter objetos diferentes:\n\n- **mecanismo:** interromper reação, mentira, silêncio automático ou confirmação seletiva;\n- **acesso:** reduzir frequência, assunto, canal, dinheiro, autoridade ou proximidade;\n- **prática ou compromisso:** encerrar hábito, contrato, rotina, consumo ou tarefa;\n- **expectativa:** deixar de sustentar uma promessa que os frutos não confirmam;\n- **vínculo:** reorganizar, distanciar ou encerrar quando contexto, padrão, incompatibilidade ou risco tornam isso necessário.\n\nDizer o objeto exato reduz cortes impulsivos e impede que a linguagem da Poda transforme pessoas em coisas descartáveis.\n\n## Poda não é vingança",
        "objeto exato da Poda",
    )

    text = replace_once(
        text,
        "Poda gradual não é covardia quando possui direção e critérios.\n\nOutras situações exigem interrupção rápida.",
        "Poda gradual não é covardia quando possui direção e critérios. Quando há segurança, comece pela intervenção menos destrutiva capaz de proteger o que precisa ser protegido e estabeleça critérios de revisão. Isso não obriga tentativas infinitas nem reconciliação. Apenas evita usar intensidade como prova de coragem.\n\nDecisões de difícil reversão pedem mais Filtro, dever cumprido e apoio competente. Risco iminente pode exigir interrupção antes dessa sequência completa.\n\nOutras situações exigem interrupção rápida.",
        "proporção da Poda",
    )

    text = replace_once(
        text,
        "Responsabilidade não é previsão perfeita.\n\nÉ decisão honesta com dados, valores e recursos disponíveis.\n\n## O custo da posição",
        "Responsabilidade não é previsão perfeita.\n\nÉ decisão honesta com dados, valores e recursos disponíveis.\n\n## Decidir e revisar\n\nUma decisão responsável pode ser firme sem fingir onisciência. Registre:\n\n- o que sabe agora;\n- o que ainda não sabe;\n- que risco aceita;\n- que sinal exigirá revisão;\n- quando voltará a observar os frutos;\n- quem possui competência para ajudar.\n\nMudar de decisão diante de evidência nova não é incoerência automática. Pode ser coerência com a verdade. Permanecer apenas para não parecer indecisa também pode ser uma Jaula.\n\nConfiança, acordos e posições podem ser provisórios sem serem frágeis: possuem base atual, limite claro e abertura para revisão responsável.\n\n## O custo da posição",
        "decisão sob incerteza",
    )

    text = replace_once(
        text,
        "Chega um momento em que investigar mais não aumenta clareza.\n\nAumenta adiamento.",
        "Chega um momento em que investigar mais não aumenta clareza.\n\nAumenta adiamento. A regra de parada chegou quando existe base suficiente para o próximo movimento, o risco foi considerado e nenhuma informação nova relevante está entrando. O desconforto restante pode ser o custo da posição, não falta de análise.\n\nO Mirante não é uma nova camada da Árvore nem um lugar em que você precisa permanecer. É o nome do ponto de observação criado quando você sobe, percebe como está pensando e recupera panorama suficiente para escolher. Metacognição também reconhece quando pensar deixou de servir à decisão e começou a protegê-la do custo.",
        "regra de parada para descer",
    )

    text = replace_once(
        text,
        "As Leis não substituem a Árvore.\n\nFuncionam como critérios recorrentes:",
        "As Leis não substituem a Árvore, o Filtro, a competência profissional, a lei civil ou a leitura de segurança. Nenhuma Lei isolada autoriza agir contra fatos, deveres ou proteção.\n\nFuncionam como critérios recorrentes:",
        "subordinação das Leis",
    )

    text = replace_once(
        text,
        "- uso as doze perguntas oficiais sem criar outro Filtro?\n- aplico o Filtro à autora e ao meu lado?",
        "- uso as doze perguntas oficiais sem criar outro Filtro?\n- aplico o Filtro proporcionalmente ao custo e à reversibilidade?\n- reconheço quando existe base suficiente para decidir sem certeza absoluta?\n- consigo confiar provisoriamente em fontes competentes sem terceirizar minha consciência?\n- defini que nova evidência ou fruto exigirá revisão?\n- aplico o Filtro à autora e ao meu lado?",
        "checkpoint do Filtro",
    )

    text = replace_once(
        text,
        "- uso os 14 Tipos como espelhos?\n- identifiquei um Tipo que aparece sob pressão?\n- diferencio Poda de vingança, impulso e abandono de dever?",
        "- uso os 14 Tipos como espelhos e não como nomes para terceiros?\n- identifiquei um Tipo que aparece sob pressão e um recurso saudável que pode ser transferido?\n- diferencio Poda de vingança, impulso e abandono de dever?\n- nomeei o objeto exato da Poda: mecanismo, acesso, prática, expectativa ou vínculo?\n- reconheci o que não deve ser podado porque produz vida ou corresponde a dever legítimo?\n- preparei a Nova Semente antes de deixar o espaço vazio?",
        "checkpoint de Tipos e Poda",
    )

    chapters = [int(value) for value in CHAPTER_RE.findall(text)]
    if chapters != list(range(27, 33)):
        raise ValueError(f"Parte VII inválida. Esperado capítulos 27-32; encontrado {chapters}.")

    if OFFICIAL_FILTER not in text:
        raise ValueError("As doze perguntas oficiais do Filtro foram alteradas ou removidas.")

    headings = re.findall(r"^##\s+(?:\d+\.\s+)?(.+)$", text, flags=re.MULTILINE)
    for name in TYPE_NAMES:
        if name not in headings:
            raise ValueError(f"Tipo canônico ausente: {name}")

    for law in LAWS:
        if law not in text:
            raise ValueError(f"Lei canônica ausente: {law}")

    if text.count("**Mecanismo que pode aparecer:**") != 14:
        raise ValueError("Os 14 Tipos não possuem a nova formulação de mecanismo.")

    PART_VII_B.parent.mkdir(parents=True, exist_ok=True)
    PART_VII_B.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")
    return text.strip() + "\n"


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
> Gerado em {generated}. A Revisão A e os Marcos 01–05 permanecem preservados.

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
    build_part_vii()

    continuous_sources = [(path, "REVISÃO B") for path in B_SOURCES] + [
        (path, "HERDADO TEMPORARIAMENTE DA REVISÃO A")
        for path in A_FALLBACK_SOURCES
    ]
    continuous_body = assemble(continuous_sources)
    validate(continuous_body, list(range(1, 39)), require_epilogue=True)

    milestone_body = assemble([(path, "REVISÃO B") for path in B_SOURCES])
    validate(milestone_body, list(range(1, 33)), require_epilogue=False)

    CONTINUOUS.parent.mkdir(parents=True, exist_ok=True)
    MILESTONE.parent.mkdir(parents=True, exist_ok=True)

    CONTINUOUS.write_text(
        metadata(
            "Manuscrito contínuo vivo — Revisão B — Marco 06",
            "MANUSCRITO DE TRABALHO — REVISÃO B. Pré-livro e Partes I–VII revisados; Parte VIII ainda herdada da Revisão A.",
        )
        + continuous_body,
        encoding="utf-8",
        newline="\n",
    )

    MILESTONE.write_text(
        metadata(
            "Marco 06 — Pré-livro e Partes I–VII — Revisão B",
            "MARCO 06 DA REVISÃO B — Pré-livro e Partes I, II, III, IV, V, VI e VII revisados.",
        )
        + milestone_body,
        encoding="utf-8",
        newline="\n",
    )

    print(f"Gerado: {PART_VII_B.relative_to(ROOT)}")
    print(f"Gerado: {CONTINUOUS.relative_to(ROOT)}")
    print(f"Gerado: {MILESTONE.relative_to(ROOT)}")
    print("Validação: Parte VII capítulos 27–32; Marco 06 capítulos 1–32; contínuo 1–38 + Epílogo.")


if __name__ == "__main__":
    main()
