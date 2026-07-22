# Catálogo Editorial — Banco Visual Reposicione-se™

**Versão:** 2.0 — auditoria de prontidão antes do Lote 02  
**Estado:** 73 ativos únicos catalogados por hash; arquivos binários ainda não versionados no repositório

## 1. Estado real do acervo

O Lote 01 contém **73 imagens únicas** e **47 duplicatas exatas identificadas por SHA-256**.

Nesta branch existem:

- `README.md`;
- `MANIFESTO_LOTE_01.csv`;
- este catálogo editorial;
- dimensões, tamanhos e hashes dos 73 originais.

Ainda **não existem arquivos `.jpg`, `.jpeg` ou `.png` dentro do repositório**. Portanto:

- o banco foi registrado, mas não foi integralmente enviado;
- o manuscrito não deve apontar para caminhos binários inexistentes;
- nenhuma peça pode ser considerada integrada ou diagramada apenas porque aparece no manifesto;
- a transferência dos bytes continua pendente.

## 2. Famílias visuais

1. **Identidade e capa** — capa preta e dourada, árvore, título, lombada e quarta capa.
2. **Pré-livro** — ruído externo, Cajueiro de Pirangi, mapa-base, comandos, dicionário visual e limites éticos.
3. **Árvore canônica** — Solo, Raízes, Tronco, Galhos, Frutos, Pragas, Poda e Nova Semente.
4. **Filtro da Sensatez** — guia visual, influência, lógica e diagnóstico de acesso indevido.
5. **Jaula** — A Jaula Está Aberta, sofá quente da mentira, sono da negligência e escada da travessia.
6. **Autoria e repetição** — autoria emocional, sistema operacional interno, automático e padrões de repetição.
7. **Pragas e intervenção** — autopiedade, autocompaixão, pragas, poda, liquidação emocional e nova semente.
8. **Tipos e leis** — estados de posicionamento, 14 Tipos e 14 Leis.
9. **Checkpoints e Workbook** — testes, diagnósticos e instrumentos extensos.

## 3. Primeira triagem conceitual

### 3.1 Aprovadas como candidatas para integração inicial

Estas peças estão coerentes com o manuscrito vigente e podem avançar para prova de leitura depois do upload binário:

| Código | Título visual | Destino provável | Status | Observação |
|---|---|---|---|---|
| `IMG-003` | O Que Este Método Não Autoriza | Pré-livro — blindagem ética | `CANDIDATA CANÔNICA` | linguagem coerente com agressão, controle, manipulação, dureza e diagnóstico como acusação |
| `IMG-018` | Frutos — evidências do que foi cultivado | Parte I — fruto como evidência | `CANDIDATA CANÔNICA` | preserva a frase “O fruto não é sentença; é evidência” |
| `IMG-036` | Cajueiro de Pirangi | Pré-livro e Epílogo | `CANDIDATA CANÔNICA` | imagem literária e estrutural; não cria protocolo concorrente |

### 3.2 Candidatas condicionais para Partes III–IV

| Código | Título visual | Destino provável | Status | Condição |
|---|---|---|---|---|
| `IMG-001` | Raízes — crenças, dores e lealdades | Parte III | `CANDIDATA COM REVISÃO` | revisar a frase “Transformar as raízes é transformar o fruto” para não sugerir causalidade automática |
| `IMG-046` | Raízes — crenças, dores e lealdades | Parte III / Workbook | `CANDIDATA COM REVISÃO` | ajustar generalizações sobre medo, dor, narrativa e limite; validar psicologicamente |
| `IMG-044` | Autoria Emocional | Parte IV / Workbook | `CANDIDATA COM ESPECIALISTA` | depende da revisão psicológica da autoria emocional e da distinção entre resposta, controle e consequência |

### 3.3 Bloqueadas até correção metodológica visual

Estas peças não devem entrar no manuscrito vigente sem tratamento:

| Código ou família | Motivo do bloqueio |
|---|---|
| `IMG-024`, `IMG-039`, `IMG-072` e outros mapas-base | misturam representação estrutural, processo, Praga, Poda e Nova Semente; alguns tratam Semente como camada ou usam frases não canônicas |
| `IMG-058` e mapas de comandos com oito movimentos | conflito com os seis comandos oficiais e com a distinção entre rota curta e ritual completo |
| `IMG-006` — Alinhamento Interno | reduz o Filtro a “como você interpreta o que vive”, o que não corresponde ao Filtro oficial |
| `IMG-007`, `IMG-070`, `IMG-073` e peças de Filtro | apresentam comandos, quantidades ou sequências que podem competir com as doze perguntas oficiais |
| peças de Autopiedade, influência, diagnóstico e autoria | aguardam revisões psicológica, clínica, jurídica, teológica ou factual proporcionais ao risco |

## 4. Regra de integração

1. Originais ficam em `banco-imagens/originais/lote-01/` e nunca são sobrescritos.
2. Versões tratadas entram em `banco-imagens/derivados/`.
3. Toda imagem integrada precisa registrar:
   - código;
   - função;
   - posição;
   - escala;
   - legenda;
   - texto alternativo;
   - autoria e licença;
   - status de aprovação;
   - relação com o conceito canônico.
4. Nenhuma imagem entra apenas para decorar ou interromper páginas.
5. Uma imagem com texto divergente não é “quase correta”: permanece bloqueada até correção.
6. Ilustração não deve ocorrer dentro do mesmo commit de voz e ritmo; a integração visual precisa ser rastreável em pista própria.

## 5. Primeira integração recomendada

Depois do upload binário, produzir uma prova ilustrada controlada com apenas três peças:

1. `IMG-003` após a blindagem ética do Pré-livro;
2. `IMG-036` junto ao Cajueiro de Pirangi, com possível retorno no Epílogo;
3. `IMG-018` depois da definição de fruto como evidência na Parte I.

A Parte III pode receber uma imagem de Raízes somente depois da revisão da frase visual e da validação psicológica correspondente.

## 6. Próxima ação técnica

- transferir os 73 originais ou, no mínimo, o primeiro conjunto canônico para o repositório;
- validar cada arquivo pelo SHA-256 do manifesto;
- não inserir links quebrados no manuscrito;
- gerar prova DOCX/PDF ilustrada em pista separada;
- comparar legibilidade em Kindle, PDF e impressão antes da canonização visual.
