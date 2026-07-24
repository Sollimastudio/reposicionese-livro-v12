#!/usr/bin/env python3
"""Audita o estado atual da Revisão B sem alterar o manuscrito.

Gera um relatório objetivo sobre estrutura, pendências explícitas, densidade
editorial, coerência canônica, referências visuais e arquivos de produção.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "revisao-b-global/49_AUDITORIA_TECNICA_AUTOMATICA_ESTADO_ATUAL.md"

SOURCES = [
    ("Pré-livro", Path("revisao-b-global/03_ONDA_1_PRE_LIVRO_REV_B.md"), None),
    ("Parte I", Path("revisao-b-global/04_ONDA_1_PARTE_I_REV_B.md"), range(1, 3)),
    ("Parte II", Path("revisao-b-global/05_ONDA_2_PARTE_II_REV_B.md"), range(3, 7)),
    ("Parte III", Path("revisao-b-global/07_ONDA_3_PARTE_III_REV_B.md"), range(7, 11)),
    ("Parte IV", Path("revisao-b-global/20_ONDA_4_PARTE_IV_REV_B.md"), range(11, 15)),
    ("Parte V", Path("revisao-b-global/23_ONDA_5_PARTE_V_REV_B.md"), range(15, 21)),
    ("Parte VI", Path("revisao-b-global/26_ONDA_6_PARTE_VI_REV_B.md"), range(21, 27)),
    ("Parte VII", Path("revisao-b-global/29_ONDA_7_PARTE_VII_REV_B.md"), range(27, 33)),
    ("Parte VIII + Epílogo", Path("revisao-b-global/32_ONDA_8_PARTE_VIII_EPILOGO_REV_B.md"), range(33, 39)),
]

CHAPTER_RE = re.compile(r"^# CAP[IÍ]TULO\s+(\d+)\b", re.M | re.I)
EPILOGUE_RE = re.compile(r"^# EP[IÍ]LOGO\b", re.M | re.I)
MARKER_RE = re.compile(r"\[(?:REVISÃO|VALIDAÇÃO)[^\]]+\]", re.I)
WORD_RE = re.compile(r"\b[\wÀ-ÖØ-öø-ÿ]+(?:[-’'][\wÀ-ÖØ-öø-ÿ]+)*\b", re.UNICODE)
IMAGE_LINK_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")

CANONICAL_COMMANDS = [
    "OBSERVE OS FRUTOS",
    "SUBA NA ÁRVORE",
    "DEIXE NA ÁRVORE",
    "VOLTE ÀS RAÍZES",
    "PASSE PELO FILTRO DA SENSATEZ",
    "DESÇA DA ÁRVORE",
]

LEGACY_TERMS = [
    "OLHE OS FRUTOS",
    "VOLTE PARA A RAIZ",
]

SPECIALIST_BUCKETS = {
    "autoral": ("VALIDAÇÃO AUTORAL",),
    "psicológica/clínica": ("REVISÃO PSICOLÓGICA", "REVISÃO CLÍNICA"),
    "teológica": ("REVISÃO TEOLÓGICA",),
    "jurídica": ("REVISÃO JURÍDICA",),
    "factual/terminológica": ("REVISÃO FACTUAL", "REVISÃO TERMINOLÓGICA"),
}


def read(path: Path) -> str:
    full = ROOT / path
    if not full.is_file():
        raise FileNotFoundError(path)
    return full.read_text(encoding="utf-8").replace("\r\n", "\n")


def editorial_words(text: str) -> int:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return len(WORD_RE.findall(text))


def marker_lines(text: str, path: Path) -> list[tuple[int, str, str]]:
    out = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for match in MARKER_RE.finditer(line):
            out.append((lineno, match.group(0), path.as_posix()))
    return out


def percentage(part: int, whole: int) -> float:
    return 0.0 if not whole else (part / whole) * 100


def fmt_int(value: int) -> str:
    return f"{value:,}".replace(",", ".")


def fmt_pct(value: float) -> str:
    return f"{value:.1f}".replace(".", ",")


def main() -> None:
    rows = []
    all_text = []
    markers = []
    all_chapters = []
    epilogues = 0
    total_words = 0
    total_bullets = 0
    total_numbered = 0
    total_neg_is = 0
    total_neg_means = 0
    total_questions = 0

    for name, path, expected in SOURCES:
        text = read(path)
        words = editorial_words(text)
        chapters = [int(x) for x in CHAPTER_RE.findall(text)]
        eps = len(EPILOGUE_RE.findall(text))
        bullets = len(re.findall(r"^\s*-\s+", text, re.M))
        numbered = len(re.findall(r"^\s*\d+\.\s+", text, re.M))
        neg_is = len(re.findall(r"\bnão é\b", text, re.I))
        neg_means = len(re.findall(r"\bnão significa\b", text, re.I))
        questions = text.count("?")
        expected_list = list(expected) if expected is not None else []
        structural_ok = chapters == expected_list if expected is not None else not chapters

        rows.append({
            "name": name,
            "path": path.as_posix(),
            "words": words,
            "chapters": chapters,
            "epilogues": eps,
            "bullets": bullets,
            "numbered": numbered,
            "neg_is": neg_is,
            "neg_means": neg_means,
            "questions": questions,
            "ok": structural_ok,
        })
        all_text.append(text)
        markers.extend(marker_lines(text, path))
        all_chapters.extend(chapters)
        epilogues += eps
        total_words += words
        total_bullets += bullets
        total_numbered += numbered
        total_neg_is += neg_is
        total_neg_means += neg_means
        total_questions += questions

    combined = "\n".join(all_text)
    manuscript_path = Path("manuscrito-revisao-b/REPOSICIONESE_REV_B_CONTINUO.md")
    manuscript = read(manuscript_path)
    manuscript_chapters = [int(x) for x in CHAPTER_RE.findall(manuscript)]
    manuscript_epilogues = len(EPILOGUE_RE.findall(manuscript))
    manuscript_words = editorial_words(manuscript)

    image_files = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}
    )
    image_links = IMAGE_LINK_RE.findall(manuscript)
    broken_image_links = []
    for target in image_links:
        if "://" in target or target.startswith("data:"):
            continue
        candidate = (ROOT / manuscript_path.parent / target).resolve()
        if not candidate.is_file():
            broken_image_links.append(target)

    pdfs = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*.pdf") if path.is_file())
    docx = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*.docx") if path.is_file())
    epubs = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*.epub") if path.is_file())
    kpf = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*.kpf") if path.is_file())

    command_counts = {cmd: len(re.findall(re.escape(cmd), combined, re.I)) for cmd in CANONICAL_COMMANDS}
    legacy_counts = {term: len(re.findall(re.escape(term), combined, re.I)) for term in LEGACY_TERMS}

    marker_bucket_counts = Counter()
    for _, marker, _ in markers:
        upper = marker.upper()
        matched = False
        for bucket, terms in SPECIALIST_BUCKETS.items():
            if any(term in upper for term in terms):
                marker_bucket_counts[bucket] += 1
                matched = True
                break
        if not matched:
            marker_bucket_counts["outra validação"] += 1

    part_words = {row["name"]: row["words"] for row in rows}
    remaining_voice_words = sum(part_words[name] for name in ["Parte VII", "Parte VIII + Epílogo"])

    checks = {
        "fontes estruturais": all(row["ok"] for row in rows),
        "capítulos 1–38 nas fontes": all_chapters == list(range(1, 39)),
        "um Epílogo nas fontes": epilogues == 1,
        "capítulos 1–38 no manuscrito": manuscript_chapters == list(range(1, 39)),
        "um Epílogo no manuscrito": manuscript_epilogues == 1,
        "Filtro único declarado": "Não existe um segundo Filtro." in combined,
        "frase de fechamento contemporâneo": "Nenhum grupo pensará automaticamente por mim" in combined,
        "Praga nunca pessoa": (
            "O nome descreve o funcionamento observado. Não autoriza dizer que alguém *é* uma Praga." in combined
            and "nunca sobre a pessoa" in combined
        ),
        "Jaula não culpabiliza": "Você fica porque quer" in combined,
        "Revisão A declarada preservada": "Revisão A" in manuscript[:1500],
        "sem comandos antigos nas fontes vivas": all(value == 0 for value in legacy_counts.values()),
    }

    lines = [
        "# AUDITORIA TÉCNICA AUTOMÁTICA — ESTADO ATUAL DA REVISÃO B",
        "",
        "**Escopo:** fontes vivas da Revisão B, manuscrito contínuo, pendências explícitas, imagens e artefatos de produção  ",
        "**Regra:** relatório gerado sem alterar o manuscrito.",
        "",
        "---",
        "",
        "# 1. ESTRUTURA E VOLUME",
        "",
        f"- palavras nas nove fontes vivas: **{fmt_int(total_words)}**;",
        f"- palavras no manuscrito contínuo: **{fmt_int(manuscript_words)}**;",
        f"- capítulos nas fontes: **{len(all_chapters)}**;",
        f"- capítulos no manuscrito: **{len(manuscript_chapters)}**;",
        f"- Epílogos nas fontes: **{epilogues}**;",
        f"- Epílogos no manuscrito: **{manuscript_epilogues}**.",
        "",
        "| Unidade | Palavras | Capítulos | Listas | `não é` | `não significa` | Perguntas | Estrutura |",
        "|---|---:|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        chapters_label = "—" if not row["chapters"] else f"{row['chapters'][0]}–{row['chapters'][-1]}"
        lists = row["bullets"] + row["numbered"]
        lines.append(
            f"| {row['name']} | {fmt_int(row['words'])} | {chapters_label} | {lists} | {row['neg_is']} | {row['neg_means']} | {row['questions']} | {'OK' if row['ok'] else 'FALHA'} |"
        )

    lines += [
        "",
        f"A Parte VII, a Parte VIII e o Epílogo concentram **{fmt_int(remaining_voice_words)} palavras**, equivalentes a **{fmt_pct(percentage(remaining_voice_words, total_words))}%** das fontes vivas. Essas unidades ainda não receberam a passagem completa de voz e ritmo do Lote 04.",
        "",
        "---",
        "",
        "# 2. CHECAGENS CANÔNICAS",
        "",
    ]
    for label, ok in checks.items():
        lines.append(f"- {'✅' if ok else '❌'} {label}.")

    lines += ["", "## Comandos oficiais — ocorrências nas fontes vivas", ""]
    for command, count in command_counts.items():
        lines.append(f"- `{command}`: {count}.")
    lines += ["", "## Formas antigas", ""]
    for term, count in legacy_counts.items():
        lines.append(f"- `{term}`: {count}.")

    lines += [
        "",
        "---",
        "",
        "# 3. PENDÊNCIAS EXPLÍCITAS NO MANUSCRITO",
        "",
        f"Foram encontrados **{len(markers)} marcadores editoriais explícitos** nas fontes vivas.",
        "",
    ]
    if markers:
        lines.append("| Linha | Arquivo | Marcador |")
        lines.append("|---:|---|---|")
        for lineno, marker, path in markers:
            lines.append(f"| {lineno} | `{path}` | {marker.replace('|', '\\|')} |")
    else:
        lines.append("Nenhum marcador explícito foi encontrado.")

    lines += ["", "## Distribuição", ""]
    for bucket, count in sorted(marker_bucket_counts.items()):
        lines.append(f"- {bucket}: **{count}**.")

    lines += [
        "",
        "---",
        "",
        "# 4. DENSIDADE EDITORIAL",
        "",
        f"- linhas com marcadores de lista: **{total_bullets + total_numbered}**;",
        f"- ocorrências de `não é`: **{total_neg_is}**;",
        f"- ocorrências de `não significa`: **{total_neg_means}**;",
        f"- sinais de pergunta: **{total_questions}**.",
        "",
        "Esses números não representam erro automático. Servem para localizar risco de fadiga, especialmente nas unidades ainda não submetidas ao Lote 04.",
        "",
        "---",
        "",
        "# 5. IMAGENS E REFERÊNCIAS VISUAIS",
        "",
        f"- arquivos binários de imagem encontrados na branch: **{len(image_files)}**;",
        f"- referências Markdown a imagens no manuscrito canônico: **{len(image_links)}**;",
        f"- referências locais quebradas: **{len(broken_image_links)}**.",
        "",
    ]
    if image_files:
        lines.append("## Binários encontrados")
        lines.append("")
        lines.extend(f"- `{path}`" for path in image_files)
    if broken_image_links:
        lines.append("")
        lines.append("## Referências quebradas")
        lines.append("")
        lines.extend(f"- `{path}`" for path in broken_image_links)

    lines += [
        "",
        "---",
        "",
        "# 6. ARTEFATOS DE PRODUÇÃO VERSIONADOS",
        "",
        f"- PDF: **{len(pdfs)}**;",
        f"- DOCX: **{len(docx)}**;",
        f"- EPUB: **{len(epubs)}**;",
        f"- KPF: **{len(kpf)}**.",
        "",
        "A ausência no repositório não prova que nunca foram gerados como artefatos temporários de workflow. Prova apenas que não existe atualmente um arquivo versionado e auditável desses formatos na branch.",
        "",
        "---",
        "",
        "# 7. VEREDITO TÉCNICO",
        "",
    ]

    critical_failures = [label for label, ok in checks.items() if not ok]
    if critical_failures:
        lines.append("**FALHA TÉCNICA:** existem checagens canônicas ou estruturais não aprovadas.")
        lines.append("")
        lines.extend(f"- {label}" for label in critical_failures)
    else:
        lines.append("**APROVADO ESTRUTURALMENTE:** capítulos, Epílogo, comandos vigentes e travas metodológicas essenciais estão íntegros.")

    lines += [
        "",
        "O manuscrito ainda não está pronto para publicação porque permanecem:",
        "",
        "1. Lote 04 de voz, ritmo e repetição;",
        "2. marcadores autorais e especializados;",
        "3. leitura contínua final após todos os lotes;",
        "4. imagens binárias e prova visual canônica;",
        "5. EPUB/KPF e prova impressa auditáveis;",
        "6. fechamento dos PRs e decisão formal de merge/publicação.",
        "",
    ]

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"Relatório gerado: {REPORT.relative_to(ROOT)}")
    print(f"Palavras: {total_words}; marcadores: {len(markers)}; imagens: {len(image_files)}")


if __name__ == "__main__":
    main()
