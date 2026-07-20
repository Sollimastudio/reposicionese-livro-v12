# Protocolo de Continuidade sem Fadiga — Reposicione-se™

## Finalidade

Este protocolo organiza o trabalho em lotes controlados para impedir:

- perda de contexto;
- decisões contraditórias;
- cansaço por excesso de informação;
- reescritas repetidas;
- cortes acidentais;
- mistura entre fonte, rascunho e texto canônico;
- afirmações de execução que não correspondem ao que foi salvo.

A regra central é simples:

> O projeto não dependerá da memória da conversa. Dependerá de arquivos de governança, rastreabilidade e estado.

---

# 1. ARQUIVOS QUE DEVEM SER LIDOS ANTES DE CADA RODADA

## Leitura obrigatória curta

1. `direcao-editorial/README.md`
2. `direcao-editorial/12_REGISTRO_MESTRE_DE_CONTEXTO.md`
3. `direcao-editorial/13_MATRIZ_DE_NAO_PERDA.md`
4. último arquivo `_RASTREABILIDADE_LOTE_*.md`
5. parte imediatamente anterior do `manuscrito-v13/`

## Leitura obrigatória por tema

- Árvore/comandos: `02_MAPA_DA_ARVORE_E_COMANDOS.md`
- Jaula: `03_MAPA_DA_JAULA.md`
- imagens: `04_MAPA_DAS_IMAGENS_PRELIMINAR.md`
- leis/tipos: `05_DISTRIBUICAO_DOS_PRINCIPIOS_E_TIPOS.md`
- Filtro: `06_FILTRO_DA_SENSATEZ.md`
- fios: `07_FIOS_CONDUTORES.md`
- riscos: `09_AUDITORIA_DE_COERENCIA_E_RISCOS.md`
- destino dos capítulos: `10_MATRIZ_CAPITULO_A_CAPITULO.md`
- fatos a verificar: `11_INVENTARIO_DE_AFIRMACOES_FACTUAIS.md`

Não é necessário reler todos os documentos integralmente em toda rodada. A leitura é orientada pelo tema, mas o Registro Mestre e a Matriz de Não Perda são sempre obrigatórios.

---

# 2. TAMANHO DE CADA LOTE

Cada lote deverá conter, no máximo:

- uma Parte curta; ou
- dois a quatro capítulos relacionados; ou
- um sistema editorial específico; ou
- um conjunto visual homogêneo.

Não editar simultaneamente:

- texto;
- visual;
- Workbook;
- referências;
- diagramação;
- marketing.

Misturar frentes aumenta a chance de perder decisões.

---

# 3. FLUXO DE UMA RODADA TEXTUAL

## Etapa A — Recuperar

1. localizar todos os trechos da fonte antiga relacionados ao lote;
2. localizar decisões autorais recentes;
3. verificar conceitos na Matriz de Não Perda;
4. verificar riscos no inventário factual;
5. identificar imagens e testes ligados ao tema.

## Etapa B — Classificar

Cada bloco da fonte recebe uma decisão:

- manter;
- mover;
- fundir;
- cortar;
- reescrever;
- transferir para Workbook;
- transferir para apêndice;
- transferir para livro futuro;
- manter como pendência factual.

## Etapa C — Reescrever

A nova versão deverá:

- preservar a voz da autora;
- obedecer à Árvore;
- avançar o posicionamento;
- reduzir repetição sem apagar função;
- incluir comandos apenas quando pedagogicamente necessários;
- aplicar proteção ética;
- separar fato de metáfora;
- deixar marcações de fonte quando necessário.

## Etapa D — Rastrear

Criar um arquivo de rastreabilidade para cada lote, contendo:

- fontes consultadas;
- conceitos preservados;
- trechos movidos;
- trechos cortados;
- razões dos cortes;
- riscos encontrados;
- fatos a verificar;
- elementos enviados ao Workbook;
- decisões ainda abertas;
- próximo lote.

## Etapa E — Verificar

Aplicar o teste de coerência do Registro Mestre e conferir a Matriz de Não Perda.

## Etapa F — Salvar

Somente declarar uma etapa executada depois que:

- o arquivo foi criado ou atualizado no GitHub;
- o commit foi confirmado;
- o README ou estado foi atualizado;
- o PR recebeu registro da rodada, quando relevante.

---

# 4. SEPARAÇÃO ENTRE TIPOS DE ARQUIVO

## Fontes antigas

Permanecem em `manuscrito/` e demais diretórios históricos.

Não são editadas destrutivamente.

## Manuscrito novo

Fica em `manuscrito-v13/`.

Cada Parte possui arquivo próprio.

## Rastreabilidade

Arquivos iniciados por `_RASTREABILIDADE_` ficam junto do manuscrito V13.

## Governança

Fica em `direcao-editorial/`.

## Método

Definições de consulta ficam em `metodo/`.

## Workbook

Quando iniciado, deverá ter diretório próprio: `workbook/`.

## Banco visual

Quando os originais forem recuperados, deverá ter:

- inventário;
- nomes padronizados;
- originais;
- P&B;
- premium;
- Kindle;
- descartes documentados.

---

# 5. CONTROLE DE REPETIÇÃO

Uma repetição pode ter quatro funções diferentes:

1. ensino inicial;
2. lembrança;
3. aplicação em outro contexto;
4. fechamento.

Antes de cortar, identificar a função.

## Cortar quando

- repete definição sem acrescentar aplicação;
- repete história sem nova leitura;
- repete chamada sem progressão;
- repete indignação no lugar de argumento;
- repete o mesmo exemplo em capítulos próximos.

## Manter quando

- o leitor precisa recuperar um comando;
- o conceito reaparece em outro galho;
- a frase é elemento de identidade da obra;
- a repetição marca ritual de passagem;
- o retorno aos frutos demonstra verificabilidade.

---

# 6. CONTROLE DE CONCEITOS CONCORRENTES

Antes de criar novo nome, perguntar:

- já existe conceito equivalente?
- isso pertence à Árvore?
- isso é comando, lei, tipo, ferramenta, metáfora ou fio?
- o leitor precisará decorar mais uma linguagem?
- o ganho justifica o custo cognitivo?

## Limite de sistemas

O leitor deverá reconhecer claramente:

- um método central: Árvore;
- uma ferramenta central: Filtro;
- uma metáfora de confronto: Jaula;
- um conjunto de critérios: 14 Leis;
- uma tipologia de espelho: 14 Tipos;
- comandos operacionais.

Qualquer sistema adicional precisa ser subordinado ou retirado.

---

# 7. CONTROLE DE FATOS

Todo trecho técnico recebe uma marca interna de trabalho:

- `[FONTE]` — precisa de referência;
- `[METÁFORA]` — não apresentar como descrição científica;
- `[AUTORAL]` — experiência ou posição da autora;
- `[CASO]` — verificar anonimização e autorização;
- `[BÍBLIA]` — confirmar tradução e contexto;
- `[JURÍDICO]` — revisão especializada;
- `[SENSIBILIDADE]` — risco de dano, generalização ou culpabilização.

Essas marcas podem ser removidas apenas na preparação final, depois da validação.

---

# 8. CONTROLE DE VOZ AUTORAL

A edição deverá preservar:

- primeira pessoa quando a experiência é da autora;
- perguntas diretas;
- frases curtas de confronto;
- imagens concretas;
- coragem de declarar posição;
- humor pontual;
- ritmo oral;
- linguagem acessível.

Deverá corrigir:

- absolutos não sustentados;
- humilhação involuntária;
- causalidade simplista;
- repetição exaustiva;
- jargão científico usado como autoridade;
- ataque a categorias;
- exposição desnecessária de terceiros.

Editar a voz não significa esterilizá-la.

Proteger a voz não significa preservar todo excesso.

---

# 9. ESTADO DE CADA PARTE

Cada Parte será marcada como:

- **Fonte localizada**;
- **Primeira versão editorial**;
- **Rastreabilidade concluída**;
- **Revisão conceitual concluída**;
- **Revisão factual concluída**;
- **Revisão autoral pendente/concluída**;
- **Pronta para consolidação**.

Nenhuma Parte será chamada de final enquanto houver pendência factual, autoral ou jurídica relevante.

---

# 10. PROTOCOLO DE PAUSA E RETOMADA

Ao interromper uma rodada, registrar:

- último arquivo lido;
- último trecho analisado;
- arquivo criado ou atualizado;
- decisões feitas;
- pendências;
- próximo passo exato.

Ao retomar:

1. ler o último registro de estado;
2. não confiar apenas na conversa;
3. conferir o `head` da branch;
4. verificar se houve alterações externas;
5. continuar a partir do próximo passo registrado.

---

# 11. PROIBIÇÃO DE EXECUÇÃO FICTÍCIA

Não declarar:

- “salvei” sem commit confirmado;
- “revisei tudo” sem delimitar arquivos e escopo;
- “concluído” quando existe apenas plano;
- “manuscrito final” quando há apenas Markdown parcial;
- “imagens organizadas” sem inventário técnico;
- “DOCX atualizado” sem arquivo binário realmente alterado;
- “GitHub sincronizado” sem verificar branch e PR.

A comunicação ao usuário deverá separar claramente:

- o que foi analisado;
- o que foi escrito;
- o que foi salvo;
- o que permanece pendente.

---

# 12. CHECKLIST DE ENCERRAMENTO DE RODADA

- [ ] Registro Mestre consultado.
- [ ] Matriz de Não Perda consultada.
- [ ] Fontes antigas localizadas.
- [ ] Decisões classificadas.
- [ ] Texto novo salvo.
- [ ] Rastreabilidade salva.
- [ ] Riscos factuais registrados.
- [ ] README/estado atualizado.
- [ ] PR atualizado.
- [ ] Próximo passo exato registrado.
- [ ] Nenhum merge automático realizado.
- [ ] Nenhum arquivo antigo destruído.

---

# 13. RESULTADO DESTE PROTOCOLO

O volume de informação deixa de ser uma ameaça quando cada elemento tem:

- nome;
- lugar;
- status;
- fonte;
- destino;
- risco;
- próximo passo.

A continuidade não será garantida por trabalhar sem parar.

Será garantida por conseguir parar e retomar sem perder o fio.
