# Registro de Consolidação — Reposicione-se™
## Manuscrito Canônico Consolidado — Revisão A

**Autora:** Sol Lima  
**Branch:** `direcao-editorial-executiva-2026-07-20`  
**Estado:** consolidação técnica da Revisão A; não é edição final

---

# 1. OBJETIVO

Gerar um manuscrito contínuo e auditável a partir dos nove módulos da Revisão Integral A, sem apagar nem substituir as fontes modulares.

O arquivo consolidado servirá para:

- leitura contínua;
- revisão autoral;
- auditoria de transições;
- confronto com versões anteriores;
- marcação de pendências;
- preparação textual posterior.

Não servirá ainda como:

- arquivo final de publicação;
- DOCX diagramado;
- Kindle;
- prova gráfica;
- texto certificado.

---

# 2. FONTES, NA ORDEM CANÔNICA

1. `revisao-integral/00_PRE_LIVRO_REV_A.md`;
2. `revisao-integral/01_PARTE_I_REV_A.md`;
3. `revisao-integral/02_PARTE_II_REV_A.md`;
4. `revisao-integral/03_PARTE_III_REV_A.md`;
5. `revisao-integral/04_PARTE_IV_REV_A.md`;
6. `revisao-integral/05_PARTE_V_REV_A.md`;
7. `revisao-integral/06_PARTE_VI_REV_A.md`;
8. `revisao-integral/07_PARTE_VII_REV_A.md`;
9. `revisao-integral/08_PARTE_VIII_REV_A.md`.

---

# 3. ARQUIVO DE SAÍDA

`manuscrito-canonico-rev-a/REPOSICIONESE_REV_A_CONSOLIDADO.md`

O arquivo deverá conter:

- aviso de estado editorial;
- identificação da autora e do método;
- conteúdo integral das nove fontes;
- marcadores invisíveis de origem entre módulos;
- Pré-livro;
- Capítulos 1–38;
- Epílogo.

---

# 4. VALIDAÇÕES AUTOMÁTICAS

O gerador deverá interromper a consolidação se:

- alguma fonte estiver ausente;
- a codificação não for UTF-8;
- a sequência de capítulos não for exatamente 1–38;
- houver número duplicado;
- faltar o Epílogo;
- o arquivo de saída ficar vazio.

Também deverá registrar no cabeçalho:

- data e hora UTC da geração;
- commit de origem quando disponível;
- lista de arquivos-fonte;
- quantidade de capítulos encontrada.

---

# 5. REGRAS DE PRESERVAÇÃO

A consolidação não poderá:

- reescrever frases;
- resolver marcações `[VALIDAÇÃO AUTORAL PENDENTE]`;
- remover marcações de revisão especializada;
- alterar títulos;
- renumerar silenciosamente;
- apagar os módulos;
- transformar Revisão A em versão final.

Qualquer edição posterior deverá ocorrer:

- primeiro com decisão registrada;
- depois no manuscrito canônico ou numa nova revisão;
- com rastreabilidade para a fonte afetada.

---

# 6. MARCADORES DE ORIGEM

Entre os módulos, o gerador inserirá comentários HTML no formato:

`<!-- FONTE: revisao-integral/XX_ARQUIVO.md -->`

Esses comentários não aparecem na leitura normal do Markdown, mas permitem localizar a origem de cada trecho.

---

# 7. USO EDITORIAL

Depois de gerado, o consolidado passará por cinco leituras independentes:

1. continuidade e ritmo;
2. repetição global;
3. voz e posicionamento autoral;
4. ética, segurança e não generalização;
5. pendências factuais e especializadas.

Somente depois dessas leituras será criada uma Revisão B ou uma versão para aprovação autoral.

---

# 8. GOVERNANÇA

Em caso de conflito:

- conceitos: Registro Mestre de Contexto;
- estágio operacional: Status Executivo;
- destino de conteúdo: Matriz de Não Perda;
- decisão por lote: Auditorias e Relatórios Comparativos;
- texto da Revisão A: arquivos modulares listados neste registro.

---

# 9. PRÓXIMA ENTREGA APÓS A GERAÇÃO

Criar um pacote de leitura autoral contendo:

- consolidado;
- sumário;
- ficha de decisões autorais;
- lista de marcações pendentes;
- relatório de riscos;
- instruções para comentários sem alterar a fonte.
