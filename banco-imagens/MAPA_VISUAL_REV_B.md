# Mapa Visual — Revisão B

## Objetivo

Distribuir as ilustrações do banco oficial no manuscrito da Revisão B sem reabrir a arquitetura textual, sem usar imagens como decoração e sem comprometer Kindle, EPUB ou impressão.

## Estado técnico

- Banco registrado: 73 ativos únicos (`IMG-001` a `IMG-073`).
- Duplicatas exatas já removidas no inventário: 47.
- Bytes binários dos JPEGs ainda não confirmados no repositório.
- Até a presença dos arquivos em `banco-imagens/originais/lote-01/`, as inserções permanecem como marcadores editoriais seguros.

## Regras de integração

1. O manuscrito textual oficial permanece preservado.
2. A versão ilustrável vive em arquivo separado.
3. Nenhuma imagem entra apenas por decoração.
4. Cada ativo precisa de título, função, destino, legenda, texto alternativo, autoria/licença e aprovação.
5. Imagens canônicas do livro principal devem ser distintas das reservadas a Workbook e Atlas.
6. Kindle recebe versões simplificadas e legíveis em escala reduzida.
7. Diagramas com texto interno precisam de revisão ortográfica antes de publicação.
8. Não usar códigos `IMG-###` como seleção definitiva sem inspeção visual dos arquivos.

## Distribuição editorial proposta

| ID visual | Local no manuscrito | Peça/função | Classe | Prioridade | Estado |
|---|---|---|---|---|---|
| VIS-001 | Capa/folha de rosto | Capa oficial preta e dourada | CANÔNICA | Essencial | A selecionar |
| VIS-002 | Antes de “Você já está posicionada” | Ruído externo / entrada narrativa | CANÔNICA | Alta | A selecionar |
| VIS-003 | “O Cajueiro de Pirangi” | Cajueiro e visão do conjunto | CANÔNICA | Essencial | A selecionar |
| VIS-004 | “O mapa da Árvore” | Árvore canônica completa | CANÔNICA | Essencial | A selecionar |
| VIS-005 | “Os comandos da Árvore” | Fluxo dos seis comandos | CANÔNICA | Essencial | A selecionar |
| VIS-006 | “O Filtro da Sensatez” | Doze perguntas do Filtro | CANÔNICA | Essencial | A selecionar |
| VIS-007 | Pré-livro / blindagem ética | O que este método não autoriza | CANÔNICA | Essencial | A selecionar |
| VIS-008 | Cap. 1 — Vitrine | Vitrine: discurso, comportamento e fruto | CANÔNICA | Média | A selecionar |
| VIS-009 | Cap. 4 — Celular configurado | Configuração, permissões e modo operante | CANÔNICA | Alta | A selecionar |
| VIS-010 | Partes II–III | Solo, Raiz, Corrente e Mapa — diferenças | CANÔNICA | Essencial | A selecionar |
| VIS-011 | Parte IV | Pedido × limite × acordo × exigência | CANÔNICA | Essencial | A selecionar |
| VIS-012 | Parte V | Galhos e transferência de recursos | CANÔNICA | Alta | A selecionar |
| VIS-013 | Parte VI | Critérios de reconhecimento de Praga | CANÔNICA | Alta | A selecionar |
| VIS-014 | “A Jaula está aberta” | Jaula como intervenção, não método paralelo | CANÔNICA | Média | A selecionar |
| VIS-015 | Cap. 22 | Sono da negligência / preparação × adiamento | CANÔNICA | Média | A selecionar |
| VIS-016 | Cap. 23 | Sofá quente da mentira | CANÔNICA | Média | A selecionar |
| VIS-017 | Cap. 30 | 14 Tipos de Posicionamento — quadro síntese | CANÔNICA | Essencial | Pendente validação autoral |
| VIS-018 | Cap. 31 | Percurso da Poda | CANÔNICA | Essencial | A selecionar |
| VIS-019 | Após Poda | Nova Semente e ocupação do espaço | CANÔNICA | Alta | A selecionar |
| VIS-020 | Encerramento | Sete Frutos / retorno à vida | CANÔNICA | Alta | A selecionar |
| VIS-021 | Epílogo | Retorno ao Cajueiro | CANÔNICA | Alta | A selecionar |

## Peças reservadas ao Workbook

- testes e pontuações dos 14 Tipos;
- folhas de auditoria de permissões;
- práticas extensas de acordos;
- diagnóstico de influência indevida;
- checkpoints preenchíveis;
- exercícios “Observe e Replante”.

## Peças reservadas ao Atlas

- variantes concorrentes da Árvore;
- diagramas detalhados de cada elemento;
- séries visuais de Pragas, Tipos e Leis;
- versões expandidas dos mapas de Galhos;
- peças narrativas que não couberem no livro principal.

## Critério de seleção dos 73 ativos

Cada `IMG-###` deverá receber:

- título visual;
- descrição objetiva do conteúdo;
- família editorial;
- orientação (retrato/paisagem);
- texto interno existente;
- legibilidade em Kindle;
- necessidade de derivação;
- destino: CANÔNICA, WORKBOOK, ATLAS, DERIVADA ou ARQUIVO;
- posição proposta;
- legenda;
- texto alternativo;
- autoria/licença;
- decisão autoral.

## Bloqueio atual

A associação exata entre `IMG-001` e `IMG-073` e os IDs `VIS-001` a `VIS-021` depende da inspeção dos JPEGs. O manifesto contém metadados e hashes, mas não descreve semanticamente cada imagem.

## Próxima ação automática possível

Quando os JPEGs forem enviados para `banco-imagens/originais/lote-01/`:

1. validar nomes e hashes contra `MANIFESTO_LOTE_01.csv`;
2. gerar folha de contato;
3. catalogar semanticamente os 73 ativos;
4. preencher o catálogo canônico;
5. substituir os marcadores da versão ilustrável por links reais;
6. gerar derivações para Kindle e impressão;
7. produzir prova visual e relatório de QA.
