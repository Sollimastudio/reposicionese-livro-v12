# VALIDAÇÃO FINAL — VOZ, RITMO E REPETIÇÃO — LOTE 04

**Escopo:** Parte VII, Parte VIII e Epílogo  
**Status:** aprovado como passagem textual, estrutural e de integração  
**Commit final:** `28e2f053f2599b8de20ebd1dd17e01912849ca69`

---

# 1. PROVAS

- aplicação: `scripts/aplicar_voz_ritmo_repeticao_lote_04.py`;
- correção de regressão: `scripts/corrigir_regressao_parte_viii_pos_lote_04.py`;
- sincronização: `scripts/sincronizar_estado_pos_voz_lote_04.py`;
- pipeline vigente: `.github/workflows/gerar-revisao-b-marco-07.yml`;
- execução final aprovada: workflow `30032146530`;
- medição Kindle: **37.026 palavras**.

# 2. INTEGRIDADE CONFIRMADA

- Parte VII: capítulos 27–32;
- Parte VIII: capítulos 33–38;
- manuscrito e Marco 07: capítulos 1–38;
- um Epílogo;
- doze perguntas oficiais;
- quatorze Tipos, com `O Camaleão` como Tipo 14;
- quatorze Leis;
- Sete Frutos;
- frase contemporânea final;
- ritual de dez movimentos;
- comando final de descida;
- frase final do Epílogo;
- validação autoral dos Tipos;
- Revisão A e Marcos 01–06.

# 3. TRAVA CONTRA REGRESSÃO

A validação agora falha se a Parte VIII voltar a conter as formas fragmentadas:

- `Você observou frutos.` seguido de `Subiu na Árvore.`;
- `O desejo importa.` seguido de `Mostra direção.`;
- exemplos de mudança pequena em linhas isoladas.

O gerador vigente não reconstrói mais a Parte VIII a partir da Revisão A. Monta o manuscrito e o Marco 07 diretamente das fontes vivas da Revisão B.

# 4. KINDLE

- total editorial estimado: **37.026 palavras**;
- alvo de 10%: **3.703 palavras**;
- Capítulo 2 — *A Morte em Vida*: aproximadamente **8,69%**;
- fronteira: `O primeiro sinal de retorno`;
- Bloco 1 preservado.

# 5. VISUAL E PRODUÇÃO

A execução final que gravou a correção validou o texto e publicou pacote textual de workflow.

Houve uma execução anterior que gerou DOCX, PDF e páginas renderizadas, mas ela falhou antes do versionamento por causa de uma asserção incorreta. Esses arquivos não substituem uma nova prova gráfica integral do estado final corrigido.

Portanto, permanecem pendentes:

- geração e inspeção gráfica do texto final atual;
- EPUB/KPF;
- prova impressa;
- integração visual real.

# 6. VEREDITO

> **Lote 04 aprovado. A passagem global de voz, ritmo e repetição está concluída no Pré-livro, Partes I–VIII e Epílogo, sem regressão da Parte VIII.**
