from __future__ import annotations

import math
import re
from pathlib import Path

MANUSCRITO = Path("manuscrito-revisao-b/REPOSICIONESE_REV_B_CONTINUO.md")
RELATORIO = Path("revisao-b-global/16_MEDICAO_EDITORIAL_10_PORCENTO_KINDLE.md")


def palavras(texto: str) -> list[str]:
    return re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:[-’'][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)*", texto)


def texto_contavel(linha: str) -> str:
    linha = re.sub(r"<!--.*?-->", "", linha)
    linha = re.sub(r"^---\s*$", "", linha)
    linha = re.sub(r"^[#>\-*+\d.()\s]+", "", linha)
    linha = re.sub(r"[`*_\\]", "", linha)
    return linha


def heading(linha: str) -> str | None:
    match = re.match(r"^(#{1,3})\s+(.+?)\s*$", linha)
    if not match:
        return None
    return match.group(2)


texto = MANUSCRITO.read_text(encoding="utf-8")
linhas = texto.splitlines()

# Remove metadados YAML e comentários de fonte da contagem editorial.
em_yaml = False
linhas_contaveis: list[tuple[int, str]] = []
for numero, linha in enumerate(linhas, start=1):
    if numero == 1 and linha.strip() == "---":
        em_yaml = True
        continue
    if em_yaml:
        if linha.strip() == "---":
            em_yaml = False
        continue
    if linha.lstrip().startswith("<!--"):
        continue
    linhas_contaveis.append((numero, linha))

total = sum(len(palavras(texto_contavel(linha))) for _, linha in linhas_contaveis)
alvo = math.ceil(total * 0.10)

acumulado = 0
linha_limite = 0
texto_limite = ""
for numero, linha in linhas_contaveis:
    acumulado += len(palavras(texto_contavel(linha)))
    if acumulado >= alvo:
        linha_limite = numero
        texto_limite = linha.strip()
        break

cabecalho_anterior = ""
cabecalho_seguinte = ""
for numero, linha in enumerate(linhas, start=1):
    titulo = heading(linha)
    if not titulo:
        continue
    if numero <= linha_limite:
        cabecalho_anterior = titulo
    elif not cabecalho_seguinte:
        cabecalho_seguinte = titulo
        break

marcos = [
    "VOCÊ JÁ ESTÁ POSICIONADA",
    "OBSERVE OS FRUTOS",
    "O QUE ESTE LIVRO VAI TREINAR EM VOCÊ",
    "SUA PRIMEIRA SUBIDA",
    "COMO USAR ESTE LIVRO",
    "PARTE I — OBSERVE OS FRUTOS",
    "CAPÍTULO 1 — A VITRINE DA VIDA",
    "CAPÍTULO 2 — A MORTE EM VIDA",
    "PARTE II — SEMENTE, SOLO E CONFIGURAÇÃO",
    "CAPÍTULO 3 — A SEMENTE E O SOLO",
    "CAPÍTULO 4 — O CELULAR CONFIGURADO",
    "CAPÍTULO 5 — O SOLO DIGITAL",
    "CAPÍTULO 6 — CRENÇAS, VALORES E MODO OPERANTE",
]

posicoes: dict[str, tuple[int, int]] = {}
acum_por_linha = 0
for numero, linha in linhas_contaveis:
    for marco in marcos:
        if marco in linha and marco not in posicoes:
            posicoes[marco] = (numero, acum_por_linha)
    acum_por_linha += len(palavras(texto_contavel(linha)))

linhas_matriz = []
for marco in marcos:
    if marco not in posicoes:
        linhas_matriz.append(f"| {marco} | não localizado | — |")
        continue
    numero, antes = posicoes[marco]
    percentual = (antes / total * 100) if total else 0
    status = "dentro" if antes <= alvo else "depois"
    linhas_matriz.append(f"| {marco} | {status} | {percentual:.2f}% |")

inicio_contexto = max(1, linha_limite - 6)
fim_contexto = min(len(linhas), linha_limite + 6)
contexto = "\n".join(f"{i}: {linhas[i-1]}" for i in range(inicio_contexto, fim_contexto + 1))

relatorio = f"""# MEDIÇÃO EDITORIAL DOS 10% KINDLE
## Reposicione-se™ — Bloco 1

**Status:** medição automática concluída  
**Manuscrito:** `manuscrito-revisao-b/REPOSICIONESE_REV_B_CONTINUO.md`  
**Método:** contagem editorial de palavras do Markdown, excluindo YAML e comentários técnicos  
**Limite:** esta medição estima a posição dos 10%; a conversão final do arquivo Kindle pode deslocar ligeiramente a fronteira.

---

# 1. RESULTADO

- Total editorial estimado: **{total:,} palavras**;
- alvo de 10%: **{alvo:,} palavras**;
- linha aproximada da fronteira: **{linha_limite}**;
- seção em que a fronteira cai: **{cabecalho_anterior}**;
- próxima seção identificada: **{cabecalho_seguinte or 'fim do manuscrito'}**;
- texto na linha de fronteira: `{texto_limite}`.

---

# 2. O QUE O LEITOR ALCANÇA

| Marco editorial | Posição | Percentual aproximado de entrada |
|---|---:|---:|
{chr(10).join(linhas_matriz)}

---

# 3. LEITURA EDITORIAL

A degustação deve ser avaliada pelo que o leitor recebe antes da fronteira estimada:

1. tese inaugural;
2. promessa de transformação;
3. definição acessível de metacognição;
4. primeira prática;
5. modo de usar;
6. experiência concreta na Parte I;
7. progressão disponível da Parte II até a seção indicada acima.

A decisão de fazer novos cortes, deslocamentos ou acréscimos deverá considerar a conversão final em EPUB/KPF e uma inspeção do arquivo efetivamente enviado ao KDP.

---

# 4. CONTEXTO DA FRONTEIRA

```text
{contexto}
```

---

# 5. REGRA DE USO

Este relatório não autoriza mudanças automáticas. Ele serve para responder:

- a promessa aparece antes do corte?
- o leitor experimenta o método antes do corte?
- existe curiosidade real para continuar?
- a fronteira termina numa passagem que impulsiona ou interrompe a leitura?

Qualquer ajuste textual posterior deverá ser aprovado e rastreado.
"""

RELATORIO.write_text(relatorio, encoding="utf-8")
print(f"Medição concluída: {total} palavras; 10% = {alvo}; linha {linha_limite}; seção {cabecalho_anterior}.")
