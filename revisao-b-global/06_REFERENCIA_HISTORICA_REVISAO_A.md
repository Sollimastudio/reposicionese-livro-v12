# Referência Histórica Preservada — Revisão A

**Projeto:** Reposicione-se™  
**Autora:** Sol Lima  
**Branch de origem:** `direcao-editorial-executiva-2026-07-20`  
**Commit-base da Revisão B:** `3c0338bdb13d6c2c66216a3bd18b3f3603a5faa2`

---

# REGRA DE PRESERVAÇÃO

A Revisão A é o marco histórico e comparativo da Revisão B.

Não poderá ser sobrescrita, renomeada, apagada ou corrigida dentro desta branch.

Os seguintes caminhos ficam congelados:

- `revisao-integral/`;
- `manuscrito-canonico-rev-a/`;
- `manuscrito-v13/`;
- `revisao-autoral/`;
- `LER_AGORA_REPOSICIONESE_REV_A.md`;
- `VISUALIZAR_REVISAO_INTEGRAL_A.md`.

Toda mudança da Revisão B deve ocorrer em:

- `revisao-b-global/`;
- `manuscrito-revisao-b/`;
- `marcos-revisao-b/`;
- scripts e workflows específicos da Revisão B.

---

# FUNÇÃO DA REVISÃO A

A Revisão A permanece disponível para:

- comparação de cortes;
- recuperação de trechos;
- auditoria de não perda;
- confronto de decisões conceituais;
- leitura da evolução editorial;
- retorno seguro se uma intervenção da Revisão B enfraquecer a obra.

Ela não é descartada quando uma nova versão fica melhor.

É preservada como evidência do caminho editorial.

---

# VALIDAÇÃO AUTOMÁTICA

O workflow da Revisão B executará um `git diff` contra o commit-base nos caminhos congelados.

Se qualquer arquivo da Revisão A for alterado, a geração do manuscrito B e dos pacotes de leitura deverá falhar.

---

# REGRA DE SUBSTITUIÇÃO NO MANUSCRITO VIVO

O manuscrito contínuo da Revisão B trabalha por substituição progressiva:

- bloco já revisado: fonte B;
- bloco ainda não revisado: fonte A;
- nenhuma mistura silenciosa dentro de um mesmo bloco;
- cada fonte recebe marcador invisível de origem;
- ao concluir uma nova Parte, o gerador substitui a fonte A pela fonte B correspondente.

Assim, o leitor sempre pode abrir um livro inteiro, enquanto a equipe mantém rastreabilidade e segurança.