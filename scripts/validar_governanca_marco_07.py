#!/usr/bin/env python3
"""Valida a governança canônica da Revisão B após o Marco 07."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE_RECONCILIACAO = "fb2b3e6f0d7c1c7ad57f512cd56d48c63586bddb"


def read(path: str) -> str:
    full = ROOT / path
    if not full.is_file():
        raise AssertionError(f"Arquivo obrigatório ausente: {path}")
    text = full.read_text(encoding="utf-8")
    if not text.strip():
        raise AssertionError(f"Arquivo obrigatório vazio: {path}")
    return text


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"Ausente em {label}: {needle!r}")


def require_ci(text: str, needle: str, label: str) -> None:
    if needle.casefold() not in text.casefold():
        raise AssertionError(f"Ausente em {label}: {needle!r}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise AssertionError(f"Regressão em {label}: {needle!r}")


def changed_files() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{BASE_RECONCILIACAO}..HEAD"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> None:
    ler = read("LER_AGORA_REPOSICIONESE_REV_B.md")
    readme = read("direcao-editorial/README.md")
    constituicao = read("direcao-editorial/00_CONSTITUICAO_EDITORIAL_REPOSICIONESE.md")
    arquitetura = read("direcao-editorial/01_ARQUITETURA_DEFINITIVA_DA_OBRA.md")
    mapa = read("direcao-editorial/02_MAPA_DA_ARVORE_E_COMANDOS.md")
    filtro = read("direcao-editorial/06_FILTRO_DA_SENSATEZ.md")
    registro = read("direcao-editorial/12_REGISTRO_MESTRE_DE_CONTEXTO.md")
    matriz = read("direcao-editorial/13_MATRIZ_DE_NAO_PERDA.md")
    protocolo = read("direcao-editorial/15_PROTOCOLO_FASE_GLOBAL_POS_MARCO_07.md")
    retomada = read("revisao-b-global/36_PONTO_DE_RETOMADA_POS_AUDITORIA_GLOBAL.md")
    manuscrito = read("manuscrito-revisao-b/REPOSICIONESE_REV_B_CONTINUO.md")
    marco = read("marcos-revisao-b/MARCO_07_MANUSCRITO_COMPLETO_REV_B.md")

    # Estado atual
    require(ler, "Partes I–VIII — Revisão B", "LER_AGORA")
    require(ler, "Marco 07 vigente", "LER_AGORA")
    require(readme, "governança reconciliada com o Marco 07", "README")
    require(registro, "Versão:** 3.0", "Registro Mestre")
    require(retomada, "PÓS-RECONCILIAÇÃO DE GOVERNANÇA", "Ponto de retomada")

    for label, text in {
        "LER_AGORA": ler,
        "README": readme,
        "Constituição": constituicao,
        "Arquitetura": arquitetura,
        "Mapa": mapa,
        "Registro": registro,
        "Retomada": retomada,
    }.items():
        forbid(text, "Partes IV–VIII — herdadas temporariamente da Revisão A", label)
        forbid(text, "Parte IV como próximo", label)

    # Estrutura reconciliada
    for label, text in {
        "Constituição": constituicao,
        "Arquitetura": arquitetura,
        "Mapa": mapa,
        "Registro": registro,
    }.items():
        require(text, "Semente", label)
        require(text, "Solo → Raízes → Tronco → Galhos → Frutos", label)
        require_ci(text, "entrada do cultivo", label)

    # Comandos canônicos
    commands = [
        "Observe os Frutos",
        "Suba na Árvore",
        "Deixe na Árvore",
        "Volte às Raízes",
        "Passe pelo Filtro da Sensatez",
        "Desça da Árvore",
    ]
    for label, text in {
        "Constituição": constituicao,
        "Mapa": mapa,
        "Registro": registro,
        "Protocolo": protocolo,
    }.items():
        for command in commands:
            require(text, command, label)

    require(mapa, "RITUAL COMPLETO DE DEZ MOVIMENTOS", "Mapa")
    require(mapa, "ROTA CURTA DE NAVEGAÇÃO", "Mapa")
    require(registro, "A rota curta é forma memorizável", "Registro")

    # Filtro oficial único
    require(filtro, "única ferramenta oficial de avaliação", "Filtro")
    require(filtro, "AS DOZE PERGUNTAS OFICIAIS", "Filtro")
    require(filtro, "não designa outro Filtro", "Filtro")
    questions = re.findall(r"^\d+\. \*\*.+?\*\*$", filtro, flags=re.M)
    if len(questions) != 12:
        raise AssertionError(f"Filtro oficial: esperado 12 perguntas; encontrado {len(questions)}")

    # Matriz e protocolo
    require(matriz, "CORREÇÃO LOCALIZADA", "Matriz")
    require(matriz, "RETIRADO/SUSPENSO", "Matriz")
    forbid(matriz, "| EM REESCRITA |", "Matriz")
    require(protocolo, "Marco 07 vigente", "Protocolo")
    require(protocolo, "A obra completa não recebe nota final 10/10", "Protocolo")

    # Integridade estrutural do manuscrito e do Marco 07
    chapter_re = re.compile(r"^# CAP[IÍ]TULO\s+(\d+)\b", flags=re.M | re.I)
    for label, text in {"manuscrito": manuscrito, "Marco 07": marco}.items():
        chapters = [int(value) for value in chapter_re.findall(text)]
        if chapters != list(range(1, 39)):
            raise AssertionError(f"{label}: capítulos inválidos: {chapters}")
        epilogues = len(re.findall(r"^# EP[IÍ]LOGO\b", text, flags=re.M | re.I))
        if epilogues != 1:
            raise AssertionError(f"{label}: esperado 1 Epílogo; encontrado {epilogues}")

    # A rodada de governança não pode alterar o manuscrito ou fontes B.
    protected_prefixes = (
        "manuscrito-revisao-b/",
        "marcos-revisao-b/",
    )
    protected_exact = {
        "revisao-b-global/03_ONDA_1_PRE_LIVRO_REV_B.md",
        "revisao-b-global/04_ONDA_1_PARTE_I_REV_B.md",
        "revisao-b-global/05_ONDA_2_PARTE_II_REV_B.md",
        "revisao-b-global/07_ONDA_3_PARTE_III_REV_B.md",
        "revisao-b-global/20_ONDA_4_PARTE_IV_REV_B.md",
        "revisao-b-global/23_ONDA_5_PARTE_V_REV_B.md",
        "revisao-b-global/26_ONDA_6_PARTE_VI_REV_B.md",
        "revisao-b-global/29_ONDA_7_PARTE_VII_REV_B.md",
        "revisao-b-global/32_ONDA_8_PARTE_VIII_EPILOGO_REV_B.md",
    }
    violations = [
        path
        for path in changed_files()
        if path.startswith(protected_prefixes) or path in protected_exact
    ]
    if violations:
        raise AssertionError(f"Rodada de governança alterou arquivos protegidos: {violations}")

    print("Validação concluída: governança reconciliada, comandos únicos, Marco 07 íntegro e manuscrito não alterado.")


if __name__ == "__main__":
    main()
