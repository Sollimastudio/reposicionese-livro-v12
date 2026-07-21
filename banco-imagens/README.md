# Banco Oficial de Imagens — Reposicione-se™

## Estado do acervo

O banco visual foi aberto oficialmente nesta branch para receber, preservar, catalogar e integrar as imagens do livro.

### Lote 01 recebido na conversa

- **73 arquivos únicos identificados**;
- **47 duplicatas exatas removidas por hash SHA-256**;
- formatos originais predominantes: JPEG;
- mockups gerados pelo assistente não foram classificados como originais da autora;
- cada ativo recebeu código provisório `IMG-001` a `IMG-073` no manifesto técnico.

## Estrutura

```text
banco-imagens/
├── README.md
├── MANIFESTO_LOTE_01.csv
├── CATALOGO_EDITORIAL.md
├── originais/
│   └── lote-01/
├── derivados/
├── capas-e-aberturas/
├── mapas-canônicos/
├── ferramentas/
├── checkpoints/
└── arquivo-morto-e-duplicatas/
```

## Regra de preservação

1. Arquivos em `originais/` nunca são sobrescritos.
2. Ajustes de corte, contraste, ortografia, resolução ou diagramação entram em `derivados/`.
3. Cada imagem precisa registrar código, título, função, destino no livro, legenda, texto alternativo, autoria/licença e status de aprovação.
4. Nenhuma imagem entra no manuscrito apenas por decoração.
5. Variantes concorrentes permanecem preservadas até a escolha canônica.
6. A integração no livro começa pelo Pré-livro da Revisão B e avança por marcos, sem alterar a Revisão A.

## Limitação técnica deste commit

O conector GitHub disponível nesta sessão grava arquivos textuais, mas não transfere diretamente os bytes binários dos JPEGs recebidos no chat. Por isso, este commit consolida imediatamente a estrutura, os 73 registros, dimensões, tamanhos e hashes dos originais. Os bytes continuam preservados no pacote local de ingestão e devem ser enviados ao diretório `originais/lote-01/` por upload binário ou automação compatível antes da diagramação final.

O manifesto impede perda, troca ou confusão de versões: qualquer arquivo futuro pode ser validado pelo hash SHA-256 correspondente.

## Próxima ação editorial

- catalogar semanticamente os 73 ativos;
- escolher imagens canônicas do Pré-livro;
- integrar Cajueiro, mapa-base da Árvore, comandos e blindagem ética;
- gerar o primeiro Pré-livro ilustrado em DOCX e PDF.
