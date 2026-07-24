#!/usr/bin/env python3
"""Gera a Parte VI em Revisão B, o manuscrito contínuo e o Marco 05.

A Parte VI é derivada da fonte histórica da Revisão A por transformações
explícitas e validadas. A fonte histórica não é alterada. O Marco 05 reúne
Pré-livro e Partes I-VI em Revisão B; Partes VII-VIII continuam herdadas da
Revisão A até a próxima passagem.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PART_VI_A = ROOT / "revisao-integral/06_PARTE_VI_REV_A.md"
PART_VI_B = ROOT / "revisao-b-global/26_ONDA_6_PARTE_VI_REV_B.md"

B_SOURCES = [
    Path("revisao-b-global/03_ONDA_1_PRE_LIVRO_REV_B.md"),
    Path("revisao-b-global/04_ONDA_1_PARTE_I_REV_B.md"),
    Path("revisao-b-global/05_ONDA_2_PARTE_II_REV_B.md"),
    Path("revisao-b-global/07_ONDA_3_PARTE_III_REV_B.md"),
    Path("revisao-b-global/20_ONDA_4_PARTE_IV_REV_B.md"),
    Path("revisao-b-global/23_ONDA_5_PARTE_V_REV_B.md"),
    Path("revisao-b-global/26_ONDA_6_PARTE_VI_REV_B.md"),
]

A_FALLBACK_SOURCES = [
    Path("revisao-integral/07_PARTE_VII_REV_A.md"),
    Path("revisao-integral/08_PARTE_VIII_REV_A.md"),
]

CONTINUOUS = ROOT / "manuscrito-revisao-b/REPOSICIONESE_REV_B_CONTINUO.md"
MILESTONE = ROOT / "marcos-revisao-b/MARCO_05_PRE_LIVRO_PARTES_I_II_III_IV_V_VI.md"

CHAPTER_RE = re.compile(r"^# CAP[IÍ]TULO\s+(\d+)\b", re.MULTILINE | re.IGNORECASE)
EPILOGUE_RE = re.compile(r"^# EP[IÍ]LOGO\b", re.MULTILINE | re.IGNORECASE)


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"Substituição {label!r}: esperado 1 trecho; encontrado {count}.")
    return text.replace(old, new, 1)


def build_part_vi() -> str:
    text = PART_VI_A.read_text(encoding="utf-8").replace("\r\n", "\n").strip()

    text = replace_once(
        text,
        "> Nem toda árvore fragilizada perdeu a vida. Às vezes, algo está consumindo por dentro aquilo que ainda tenta crescer.\n\n---",
        "> Nem toda árvore fragilizada perdeu a vida. Às vezes, algo está consumindo por dentro aquilo que ainda tenta crescer.\n\nNesta Parte, o nome recai sobre o **mecanismo**, nunca sobre a pessoa. Praga não é identidade, sentença moral ou diagnóstico. É uma forma pedagógica de observar aquilo que drena, distorce, captura uma necessidade legítima ou impede revisão apesar dos frutos.\n\nA investigação seguirá quatro movimentos já conhecidos:\n\n> **Observe o fruto. Nomeie o mecanismo. Proteja o que é legítimo. Recupere espaço de decisão.**\n\nA Jaula aparecerá como intervenção narrativa, não como método concorrente. Ela confronta uma permanência já percebida; não substitui a Árvore, o Filtro, a proteção material ou a ajuda especializada.\n\n---",
        "abertura da Parte VI",
    )

    text = replace_once(
        text,
        "No Método da Árvore do Discernimento, **Praga é um mecanismo interno ou externo que, de forma persistente, drena vida, distorce realidade, resiste à revisão ou alimenta frutos incompatíveis com os valores declarados**.",
        "No Método da Árvore do Discernimento, **Praga é um mecanismo interno ou externo que, de forma persistente, drena vida, distorce realidade, captura uma necessidade legítima, resiste à revisão ou alimenta frutos incompatíveis com os valores declarados**.\n\nO nome descreve o funcionamento observado. Não autoriza dizer que alguém *é* uma Praga.",
        "definição de Praga",
    )

    text = replace_once(
        text,
        "A emoção não vira Praga porque incomoda.\n\nO mecanismo se torna Praga quando passa a governar repetidamente, exige distorção ou impede revisão apesar dos frutos.",
        "A emoção não vira Praga porque incomoda.\n\nTambém existe, por trás de muitos mecanismos, uma necessidade legítima: segurança, pertencimento, descanso, reconhecimento, proteção, sentido ou cuidado. O trabalho não é destruir a necessidade. É impedir que a forma usada para atendê-la continue produzindo dano.\n\nO mecanismo se torna Praga quando passa a governar repetidamente, exige distorção ou impede revisão apesar dos frutos.",
        "necessidade legítima",
    )

    text = replace_once(
        text,
        "Esses critérios não formam diagnóstico clínico.\n\nOrganizam investigação pedagógica.\n\n## A Praga pode usar uma coisa boa",
        "Esses critérios não formam diagnóstico clínico.\n\nOrganizam investigação pedagógica.\n\n## Antes de nomear\n\nNão use a palavra Praga como atalho para condenar alguém, vencer uma discussão ou evitar contexto. Antes de nomear, pergunte:\n\n- qual comportamento ou mecanismo estou descrevendo?\n- que repetição e que frutos consigo observar?\n- que necessidade legítima pode ter sido capturada?\n- o que ainda não sei?\n- existe explicação médica, psicológica, jurídica, social ou material que exige competência profissional?\n\nSe você não consegue mostrar o funcionamento, a repetição e o fruto, ainda não possui base para usar o nome.\n\n## A Praga pode usar uma coisa boa",
        "proteção antes de nomear",
    )

    text = replace_once(
        text,
        "9. Oferece alívio imediato e custo prolongado?\n10. Que parte da Árvore está sendo afetada?",
        "9. Oferece alívio imediato e custo prolongado?\n10. Que parte da Árvore está sendo afetada?\n11. Que necessidade legítima tenta atender?\n12. Que prática saudável poderia atender essa necessidade sem repetir o mesmo fruto?",
        "perguntas de reconhecimento",
    )

    text = replace_once(
        text,
        "Negligência finge que esperar não produz fruto.\n\nPergunte:",
        "Negligência finge que esperar não produz fruto.\n\nA pergunta não é se você realizou tudo. É se existe direção verificável. Uma pessoa pode avançar devagar e estar cuidando da realidade; outra pode falar muito sobre mudança e continuar renovando o mesmo adiamento.\n\nPergunte:",
        "direção verificável",
    )

    text = replace_once(
        text,
        "## A Jaula do depois\n\n> **A JAULA ESTÁ ABERTA.**",
        "## O cuidado que já funciona\n\nNem toda rotina é sinal de acomodação. Algumas práticas mantêm a vida possível:\n\n- consulta marcada e acompanhada;\n- conta revisada regularmente;\n- conversa que acontece antes do acúmulo;\n- descanso protegido;\n- responsabilidade distribuída;\n- pedido de ajuda feito antes do colapso;\n- limite revisto diante dos frutos.\n\nReconheça a manutenção que funciona. O método não serve apenas para despertar você do que foi adiado. Serve para tornar consciente o cuidado que já impede a deterioração.\n\n## A Jaula do depois\n\n> **A JAULA ESTÁ ABERTA.**",
        "cuidado que funciona",
    )

    text = replace_once(
        text,
        "É o Sofá Quente da Mentira.\n\nEle não precisa parecer preguiça.",
        "É o Sofá Quente da Mentira.\n\nO problema não é o conforto. Conforto legítimo restaura corpo, vínculo e capacidade de decidir. A imagem do Sofá descreve apenas o conforto usado para impedir contato com uma contradição já reconhecida.\n\nEle não precisa parecer preguiça.",
        "conforto legítimo",
    )

    text = replace_once(
        text,
        "## A Jaula do conforto conhecido\n\n> **A JAULA ESTÁ ABERTA.**",
        "## O conforto que devolve vida\n\nAntes de abandonar uma rotina, relação, crença ou ambiente apenas porque é conhecido, observe os frutos. O conhecido também pode conter segurança real, vínculo confiável, tradição examinada, descanso e pertencimento saudável.\n\nPergunte:\n\n- este conforto restaura ou entorpece?\n- amplia minha capacidade de agir ou substitui a ação?\n- permite verdade e revisão?\n- protege algo legítimo ou apenas preserva aparência?\n- que bom fruto preciso manter enquanto enfrento a contradição?\n\n## A Jaula do conforto conhecido\n\n> **A JAULA ESTÁ ABERTA.**",
        "conforto restaurador",
    )

    old_autopiedade = """Na linguagem pedagógica deste método, chamo a Autopiedade de **praga-mãe**.

Uso essa expressão porque ela consegue alimentar diversas outras Pragas ao transformar:

- dor em governo;
- explicação em moradia;
- responsabilidade em tarefa permanente dos outros;
- cuidado em imunidade;
- pertencimento em confirmação contínua da ferida.

Essa expressão não é diagnóstico clínico.

Também não significa que toda dor não resolvida seja Autopiedade.

Autopiedade não é:

- sentir dor;
- chorar;
- precisar de tempo;
- reconhecer trauma;
- falar sobre injustiça;
- receber cuidado;
- pedir ajuda;
- denunciar violência;
- não conseguir agir imediatamente;
- respeitar limites reais.

Uma pessoa pode estar profundamente ferida e não estar vivendo em Autopiedade.

Outra pode falar pouco sobre dor e organizar toda a vida ao redor dela.

A diferença não está no volume do sofrimento.

Está na função que a dor passou a exercer."""

    new_autopiedade = """Na linguagem pedagógica deste método, chamo a Autopiedade de **praga-mãe** porque ela pode alimentar mecanismos diferentes ao transformar:

- dor em governo;
- explicação em moradia;
- responsabilidade possível em tarefa permanente dos outros;
- cuidado em imunidade à revisão;
- pertencimento em confirmação contínua da ferida.

Uso a expressão com cautela. Ela não é diagnóstico clínico, identidade nem insulto. Não autoriza olhar para alguém ferido e concluir: “Você está na Autopiedade.” O conceito existe primeiro para auto-observação responsável e precisa ser aplicado com contexto, evidência, cuidado e limites de competência.

Autopiedade não é sentir dor, chorar, precisar de tempo, reconhecer trauma, falar sobre injustiça, receber cuidado, pedir ajuda, denunciar violência, não conseguir agir imediatamente ou respeitar limites reais.

Uma pessoa pode estar profundamente ferida e não estar vivendo em Autopiedade. Outra pode falar pouco sobre dor e organizar decisões, vínculos e responsabilidade possível ao redor da ferida.

A diferença não está no volume do sofrimento.

Está na função que a dor passou a exercer — e essa função não pode ser presumida de fora com uma frase rápida."""

    text = replace_once(text, old_autopiedade, new_autopiedade, "uso pedagógico de Autopiedade")

    text = replace_once(
        text,
        "## A Jaula da dor\n\n> **A JAULA ESTÁ ABERTA.**",
        "## Como não usar este capítulo\n\nNão use Autopiedade para:\n\n- silenciar relato de violência;\n- apressar luto;\n- negar sintomas ou limitações;\n- exigir ação sem recurso e segurança;\n- humilhar quem pede ajuda;\n- transformar responsabilidade possível em culpa total;\n- substituir avaliação profissional.\n\nAutocompaixão sem direção pode virar estagnação. Confronto sem cuidado pode virar nova violência. O método exige verdade suficiente para recuperar movimento e cuidado suficiente para não repetir o dano.\n\n## A Jaula da dor\n\n> **A JAULA ESTÁ ABERTA.**",
        "proteção de uso de Autopiedade",
    )

    text = replace_once(
        text,
        "A teoria completa pertence a *Fuga Identitária: O Apagamento do Eu*.\n\n## A Jaula da plateia",
        "A teoria completa pertence a *Fuga Identitária: O Apagamento do Eu*.\n\n## Influência saudável e acesso consciente\n\nNem toda influência disputa governo. Uma influência saudável pode:\n\n- ampliar fatos;\n- admitir limite e erro;\n- ensinar competência;\n- incentivar segunda opinião;\n- devolver responsabilidade;\n- respeitar saída e discordância;\n- produzir vínculo com mais realidade.\n\nA pergunta não é se alguém influenciou você. É que acesso recebeu, com que competência, sob quais limites e com que fruto.\n\n> **Posso escutar sem me entregar. Posso aprender sem desaparecer.**\n\n## A Jaula da plateia",
        "influência saudável",
    )

    text = replace_once(
        text,
        "A Jaula aparece ao longo do livro porque algumas prisões continuam funcionando mesmo quando parte da estrutura externa mudou.",
        "A Jaula aparece ao longo do livro como **intervenção narrativa** porque algumas prisões continuam funcionando mesmo quando parte da estrutura externa mudou. Ela não diagnostica, não explica toda a Árvore e não ordena uma saída. Apenas torna visível a pergunta que já não pode ser evitada.",
        "função da Jaula",
    )

    text = replace_once(
        text,
        "- diferencio Autocompaixão de Autopiedade?\n- entendo `praga-mãe` como linguagem pedagógica, não diagnóstico?",
        "- diferencio Autocompaixão de Autopiedade?\n- entendo `praga-mãe` como linguagem pedagógica, não diagnóstico, identidade ou insulto?\n- consigo falar de Autopiedade sem silenciar dor, violência, luto ou limitação real?",
        "checkpoint de Autopiedade",
    )

    text = replace_once(
        text,
        "- identifiquei comparação, validação, ressentimento, pensamento binário, influência indevida ou anestesia?\n- aplico o Filtro ao meu grupo e à informação conveniente?",
        "- identifiquei comparação, validação, ressentimento, pensamento binário, influência indevida ou anestesia?\n- reconheço influência saudável que amplia responsabilidade e merece continuidade?\n- aplico o Filtro ao meu grupo e à informação conveniente?",
        "checkpoint de influência",
    )

    text = replace_once(
        text,
        "Na próxima Parte, a pergunta muda.\n\nJá observamos aquilo que drena e distorce.",
        "Na próxima Parte, a pergunta muda.\n\nJá observamos aquilo que drena e distorce sem transformar pessoas, emoções ou dores em Pragas. Também reconhecemos necessidades e influências saudáveis que precisam ser protegidas.",
        "ponte para a Parte VII",
    )

    chapters = [int(value) for value in CHAPTER_RE.findall(text)]
    if chapters != list(range(21, 27)):
        raise ValueError(f"Parte VI inválida. Esperado capítulos 21-26; encontrado {chapters}.")

    PART_VI_B.parent.mkdir(parents=True, exist_ok=True)
    PART_VI_B.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")
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
> Gerado em {generated}. A Revisão A e os Marcos 01–04 permanecem preservados.

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
    build_part_vi()

    continuous_sources = [(path, "REVISÃO B") for path in B_SOURCES] + [
        (path, "HERDADO TEMPORARIAMENTE DA REVISÃO A")
        for path in A_FALLBACK_SOURCES
    ]
    continuous_body = assemble(continuous_sources)
    validate(continuous_body, list(range(1, 39)), require_epilogue=True)

    milestone_body = assemble([(path, "REVISÃO B") for path in B_SOURCES])
    validate(milestone_body, list(range(1, 27)), require_epilogue=False)

    CONTINUOUS.parent.mkdir(parents=True, exist_ok=True)
    MILESTONE.parent.mkdir(parents=True, exist_ok=True)

    CONTINUOUS.write_text(
        metadata(
            "Manuscrito contínuo vivo — Revisão B — Marco 05",
            "MANUSCRITO DE TRABALHO — REVISÃO B. Pré-livro e Partes I–VI revisados; Partes VII–VIII ainda herdadas da Revisão A.",
        )
        + continuous_body,
        encoding="utf-8",
        newline="\n",
    )

    MILESTONE.write_text(
        metadata(
            "Marco 05 — Pré-livro e Partes I–VI — Revisão B",
            "MARCO 05 DA REVISÃO B — Pré-livro e Partes I, II, III, IV, V e VI revisados.",
        )
        + milestone_body,
        encoding="utf-8",
        newline="\n",
    )

    print(f"Gerado: {PART_VI_B.relative_to(ROOT)}")
    print(f"Gerado: {CONTINUOUS.relative_to(ROOT)}")
    print(f"Gerado: {MILESTONE.relative_to(ROOT)}")
    print("Validação: Parte VI capítulos 21–26; contínuo 1–38 + Epílogo; Marco 05 capítulos 1–26.")


if __name__ == "__main__":
    main()
