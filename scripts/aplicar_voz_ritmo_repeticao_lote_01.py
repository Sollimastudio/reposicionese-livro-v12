#!/usr/bin/env python3
"""Aplica a passagem localizada de voz, ritmo e repetição no Lote 01.

Escopo protegido: Pré-livro e Partes I–II. O script não move conteúdo entre
Partes, não altera headings, histórias, conceitos canônicos, perguntas oficiais
ou marcações de validação. As mudanças fundem fragmentação mecânica e negações
próximas, preservando conteúdo e função.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "pre": ROOT / "revisao-b-global/03_ONDA_1_PRE_LIVRO_REV_B.md",
    "part1": ROOT / "revisao-b-global/04_ONDA_1_PARTE_I_REV_B.md",
    "part2": ROOT / "revisao-b-global/05_ONDA_2_PARTE_II_REV_B.md",
}


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\wÀ-ÖØ-öø-ÿ]+(?:[-’'][\wÀ-ÖØ-öø-ÿ]+)*\b", text))


def headings(text: str) -> list[str]:
    return re.findall(r"^#{1,6}\s+.+$", text, flags=re.MULTILINE)


def replace_guarded(text: str, old: str, new: str, label: str) -> tuple[str, bool]:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1), True
    if count == 0 and new in text:
        return text, False
    raise ValueError(f"{label}: esperado um trecho antigo ou a versão nova já aplicada; encontrado {count} trecho(s) antigo(s).")


REPLACEMENTS: dict[str, list[tuple[str, str, str]]] = {
    "pre": [
        (
            "promessa de aprendizagem em fluxo",
            "Ao final, você deverá observar sem transformar fruto em identidade; distinguir fato, interpretação e influência; reconhecer o automático; aprender sem terceirizar a consciência; fortalecer o que funciona; assumir sua responsabilidade real; filtrar, interromper, plantar outra prática e agir.",
            "Você aprenderá a observar sem transformar fruto em identidade, distinguir fato, interpretação e influência e reconhecer o automático. Aprenderá sem terceirizar a consciência, fortalecendo o que funciona e assumindo sua responsabilidade real. Então poderá filtrar, interromper, plantar outra prática e agir.",
        ),
        (
            "Árvore sem redução nem dependência",
            "A Árvore organiza a investigação sem causa única, diagnóstico de pessoas ou poder da autora sobre seu pensamento.\n\nExiste para devolver visão, autoria e decisão.",
            "A Árvore organiza a investigação sem reduzir tudo a uma causa, diagnosticar pessoas ou entregar à autora poder sobre seu pensamento.\n\nEla existe para devolver visão, autoria e decisão.",
        ),
        (
            "proteções éticas com respiração",
            "Este livro não autoriza diagnosticar pessoas, acusar com a Jaula, chamar todo sofrimento de Autopiedade, culpabilizar vítimas, punir com limites, humilhar com a verdade, impedir investigação pela fé, rejeitar aprendizagem ou ruminar em nome da metacognição.",
            "Este livro não autoriza diagnosticar pessoas, acusar com a Jaula nem chamar todo sofrimento de Autopiedade. Também não autoriza culpabilizar vítimas, punir com limites, humilhar com a verdade ou impedir investigação pela fé.\n\nAprender continua necessário. Metacognição continua ligada à vida — não à ruminação.",
        ),
    ],
    "part1": [
        (
            "abertura da Parte I sem negação seriada",
            "A investigação começa pelo que pode ser observado.\n\nNão pelo rótulo.\n\nNão pela justificativa.\n\nNão pela promessa de mudança.\n\nPelo fruto.",
            "A investigação começa pelo que pode ser observado — antes do rótulo, da justificativa e da promessa de mudança.\n\nComeça pelo fruto.",
        ),
        (
            "rotina do apagamento em frase contínua",
            "Há uma forma de desaparecimento que não interrompe a rotina.\n\nA pessoa acorda.\n\nTrabalha.\n\nCuida.\n\nCumpre.\n\nSorri quando esperam.\n\nResponde mensagens.\n\nMantém a casa, a família, a função ou a imagem.",
            "Há uma forma de desaparecimento que não interrompe a rotina.\n\nA pessoa acorda, trabalha, cuida, cumpre, sorri quando esperam, responde mensagens e mantém a casa, a família, a função ou a imagem.",
        ),
        (
            "definição autoral sem ritmo defensivo",
            "A expressão é autoral e pedagógica.\n\nEla nomeia apagamento, desconexão e ausência de participação consciente na própria vida.\n\nNão substitui avaliação psicológica ou psiquiátrica.\n\nTambém não transforma sofrimento em culpa.",
            "A expressão é autoral e pedagógica: nomeia apagamento, desconexão e ausência de participação consciente na própria vida, sem substituir avaliação psicológica ou psiquiátrica nem transformar sofrimento em culpa.",
        ),
        (
            "Jaula sem dupla negação",
            "Não significa que toda saída seja simples.\n\nNão significa que toda porta esteja livre.\n\nSignifica que uma prisão percebida já não pode continuar sendo chamada apenas de destino.",
            "A frase não promete saída simples nem afirma que toda porta esteja livre.\n\nSignifica que uma prisão percebida já não pode continuar sendo chamada apenas de destino.",
        ),
    ],
    "part2": [
        (
            "abertura da Parte II afirmativa",
            "A investigação começa sem tribunal.\n\nSemente não é destino.\n\nSolo não é sentença.\n\nConfiguração não é identidade.\n\nInfluência não é automaticamente manipulação.\n\nAquilo que veio de fora não é necessariamente falso.\n\nAquilo que nasceu dentro de você não é automaticamente verdadeiro.\n\nMas o que não é examinado pode continuar governando como se fosse natureza.",
            "A investigação começa sem tribunal.\n\nSemente abre possibilidade, não destino. Solo oferece condições, não sentença. Configuração orienta, mas não define identidade.\n\nInfluência pode ensinar, corrigir, confundir ou manipular. O que veio de fora pode ser verdadeiro; o que nasceu dentro de você também pode precisar de exame.\n\nAquilo que não é examinado pode continuar governando como se fosse natureza.",
        ),
        (
            "Sementes em cadência, não inventário vertical",
            "Uma frase.\n\nUma perda.\n\nUm elogio.\n\nUma ameaça.\n\nUma interpretação bíblica.\n\nUma regra familiar.\n\nUma notícia.\n\nUm modelo de amor.\n\nUma oportunidade.\n\nUma decisão.\n\nUma imagem repetida.\n\nUma crença oferecida por um grupo.\n\nUma experiência de cuidado.\n\nUm exemplo de coragem.",
            "Uma frase, uma perda, um elogio ou uma ameaça.\n\nUma interpretação bíblica, uma regra familiar, uma notícia ou um modelo de amor.\n\nUma oportunidade, uma decisão, uma imagem repetida, uma crença oferecida por um grupo, uma experiência de cuidado ou um exemplo de coragem.",
        ),
        (
            "Solo com participação integrada",
            "Família participa.\n\nCultura participa.\n\nFé, escola, território, linguagem, dinheiro, perdas, elogios, punições e silêncios participam.\n\nTelas, músicas, grupos e algoritmos também.\n\nEstado físico participa.\n\nCansaço, fome, medo, solidão e sensação de segurança podem alterar a maneira como uma mensagem é recebida.",
            "Família e cultura participam. Fé, escola, território, linguagem, dinheiro, perdas, elogios, punições e silêncios também. Telas, músicas, grupos e algoritmos entram nesse ambiente.\n\nO estado físico participa: cansaço, fome, medo, solidão e sensação de segurança podem alterar a maneira como uma mensagem é recebida.",
        ),
        (
            "ambientes saudáveis em frase imagética",
            "Talvez você já tenha encontrado um ambiente assim.\n\nUma amizade.\n\nUma sala de aula.\n\nUma igreja.\n\nUma equipe.\n\nUma terapia.\n\nUma conversa familiar.\n\nUm livro.",
            "Talvez você já tenha encontrado um ambiente assim numa amizade, sala de aula, igreja, equipe, terapia, conversa familiar ou livro.",
        ),
        (
            "terrenos da parábola em uma imagem",
            "Na Parábola do Semeador, a mesma Semente encontra terrenos diferentes.\n\nCaminho endurecido.\n\nPedras.\n\nEspinhos.\n\nBoa terra.",
            "Na Parábola do Semeador, a mesma Semente encontra terrenos diferentes: caminho endurecido, pedras, espinhos e boa terra.",
        ),
        (
            "configuração do celular sem lista mecânica",
            "Depois começa a configuração.\n\nIdioma.\n\nRede.\n\nContatos.\n\nAplicativos.\n\nSenhas.\n\nNotificações.\n\nPermissões.",
            "Depois começa a configuração: idioma, rede, contatos, aplicativos, senhas, notificações e permissões.",
        ),
        (
            "permissões do aplicativo em fluxo",
            "Todo aplicativo pede acesso.\n\nLocalização.\n\nCâmera.\n\nMicrofone.\n\nContatos.\n\nArquivos.\n\nInfluências também pedem permissões.",
            "Todo aplicativo pede acesso: localização, câmera, microfone, contatos, arquivos.\n\nInfluências também pedem permissões.",
        ),
        (
            "decisões sem enumeração fragmentada",
            "Você pode escolher por convicção.\n\nPor medo.\n\nPressa.\n\nLealdade.\n\nCarência.\n\nPressão de grupo.\n\nOu por uma evidência que realmente precisava ser considerada.",
            "Você pode escolher por convicção, medo, pressa, lealdade, carência ou pressão de grupo.\n\nTambém pode escolher porque uma evidência realmente precisava ser considerada.",
        ),
    ],
}


PROTECTED = {
    "pre": [
        "Você já está posicionada.",
        "A posição que você ocupa está produzindo os frutos que deseja continuar colhendo?",
        "O mundo ensinou você a reagir. Ninguém ensinou você a existir.",
        "Pensar por si é aprender com muitas vozes sem entregar a nenhuma delas o governo da sua consciência.",
    ],
    "part1": [
        "[VALIDAÇÃO AUTORAL PENDENTE]",
        "A JAULA ESTÁ ABERTA.",
        "Morte em Vida não é diagnóstico clínico",
        "O que imaginei que aconteceria se eu aparecesse como realmente desejava aparecer?",
    ],
    "part2": [
        "Não existe um segundo Filtro.",
        "O problema não é alguém participar do seu pensamento. É você não perceber quando alguém tomou o lugar dele.",
        "Fato não é interpretação. Interpretação não é Semente aceita.",
        "VOLTE ÀS RAÍZES.",
    ],
}


def main() -> None:
    total_before = 0
    total_after = 0
    applied: list[str] = []

    for key, path in FILES.items():
        original = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        original_headings = headings(original)
        before = word_count(original)
        text = original

        for label, old, new in REPLACEMENTS[key]:
            text, changed = replace_guarded(text, old, new, label)
            if changed:
                applied.append(f"{key}: {label}")

        if headings(text) != original_headings:
            raise ValueError(f"{path.name}: a hierarquia ou o nome de headings foi alterado.")

        for phrase in PROTECTED[key]:
            if phrase not in text:
                raise ValueError(f"{path.name}: frase protegida ausente: {phrase}")

        if key == "part1":
            if text.count("[VALIDAÇÃO AUTORAL PENDENTE]") != original.count("[VALIDAÇÃO AUTORAL PENDENTE]"):
                raise ValueError("A quantidade de marcações de validação autoral mudou na Parte I.")

        after = word_count(text)
        total_before += before
        total_after += after
        path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")

    delta = total_after - total_before
    if abs(delta) > 80:
        raise ValueError(f"Variação lexical excessiva para uma passagem de voz: {delta:+d} palavras.")

    part1 = FILES["part1"].read_text(encoding="utf-8")
    part2 = FILES["part2"].read_text(encoding="utf-8")
    chapters = [int(x) for x in re.findall(r"^# CAP[IÍ]TULO\s+(\d+)\b", part1 + "\n" + part2, flags=re.M | re.I)]
    if chapters != [1, 2, 3, 4, 5, 6]:
        raise ValueError(f"Capítulos do Lote 01 alterados: {chapters}")

    print(f"Passagem concluída. Variação lexical do lote: {delta:+d} palavras.")
    if applied:
        print("Transformações aplicadas:")
        for item in applied:
            print(f"- {item}")
    else:
        print("Todas as transformações já estavam aplicadas.")


if __name__ == "__main__":
    main()
