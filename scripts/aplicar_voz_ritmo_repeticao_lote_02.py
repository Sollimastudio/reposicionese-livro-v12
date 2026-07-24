#!/usr/bin/env python3
"""Aplica voz, ritmo e repetição — Lote 02: Partes III–IV.

A passagem é estritamente estilística: não move conteúdo entre Partes, não
altera arquitetura, método, comandos, Leis, Jaulas, checkpoints ou marcações de
validação especializada.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART3 = ROOT / "revisao-b-global/07_ONDA_3_PARTE_III_REV_B.md"
PART4 = ROOT / "revisao-b-global/20_ONDA_4_PARTE_IV_REV_B.md"


def replace_guarded(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise ValueError(f"{label}: esperado um trecho antigo ou a versão nova já aplicada; encontrado {count}.")


def apply(path: Path, replacements: list[tuple[str, str, str]]) -> None:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    for label, old, new in replacements:
        text = replace_guarded(text, old, new, label)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    apply(
        PART3,
        [
            (
                "abertura Parte III",
                """Você já observou frutos.

Separou fato de interpretação.

Percebeu que mensagens encontram ambientes diferentes e que algumas configurações tentam decidir antes de você.

Agora a investigação desce.

Não para encontrar um culpado original.

Não para fabricar uma explicação capaz de justificar tudo.

Desce para descobrir o que ainda recebe alimento — e o que merece continuar vivo.""",
                """Você já observou frutos, separou fato de interpretação e percebeu que mensagens encontram ambientes diferentes — algumas configurações tentam decidir antes de você.

Agora a investigação desce. Não para encontrar um culpado original nem fabricar uma explicação capaz de justificar tudo, mas para descobrir o que ainda recebe alimento — e o que merece continuar vivo.""",
            ),
            (
                "definição de Raiz",
                """No Método da Árvore do Discernimento, Raiz é aquilo de onde um padrão continua retirando seiva.

Pode ser uma crença ainda aceita.

Uma memória que continua definindo perigo.

Uma culpa.

Uma recompensa.

Uma relação que confirma a mesma interpretação.

Uma visão sobre Deus.

Uma vantagem difícil de admitir.

Uma conclusão antiga que o presente já contrariou, mas que você ainda protege porque não sabe quem será sem ela.""",
                """No Método da Árvore do Discernimento, Raiz é aquilo de onde um padrão continua retirando seiva: uma crença ainda aceita, uma memória que continua definindo perigo, culpa, recompensa, uma relação que confirma a mesma interpretação, uma visão sobre Deus, uma vantagem difícil de admitir ou uma conclusão antiga que o presente já contrariou — mas que você ainda protege porque não sabe quem será sem ela.""",
            ),
            (
                "responsabilidade sem réu",
                """Há danos reais.

Omissões reais.

Abusos reais.

Pessoas respondem pelo que fizeram.""",
                """Há danos, omissões e abusos reais. Pessoas respondem pelo que fizeram.""",
            ),
            (
                "verdades simultâneas",
                """Alguém pode ter amado você e falhado gravemente.

Pode ter tido boa intenção e produzido dano.

Pode ter protegido em uma área e abandonado em outra.

Humanizar não é absolver.

Responsabilizar não exige transformar uma pessoa inteira no pior ato que praticou.""",
                """Alguém pode ter amado você e falhado gravemente, ter tido boa intenção e produzido dano, protegido em uma área e abandonado em outra.

Humanizar não é absolver. Responsabilizar não exige transformar uma pessoa inteira no pior ato que praticou.""",
            ),
            (
                "função protetiva antiga",
                """Uma resposta antiga pode ter sido sensata num ambiente anterior.

O silêncio pode ter reduzido risco.

A adaptação pode ter protegido uma criança.

A vigilância pode ter ajudado a antecipar perigo.

A performance pode ter garantido algum acolhimento.""",
                """Uma resposta antiga pode ter sido sensata num ambiente anterior: o silêncio reduziu risco, a adaptação protegeu uma criança, a vigilância ajudou a antecipar perigo ou a performance garantiu algum acolhimento.""",
            ),
            (
                "obrigações legítimas",
                """Nem toda obrigação é prisão.

Cuidar de um filho.

Cumprir um compromisso assumido.

Responder por uma dívida real.

Sustentar um dever profissional.

Reparar um dano causado.

Tudo isso pode exigir sacrifício sem ser Corrente.""",
                """Nem toda obrigação é prisão. Cuidar de um filho, cumprir um compromisso assumido, responder por uma dívida real, sustentar um dever profissional ou reparar um dano causado pode exigir sacrifício sem ser Corrente.""",
            ),
            (
                "culpa de diferenciar",
                """Quando uma pessoa muda, o sistema precisa se reorganizar.

A que resolvia tudo começa a dizer não.

A que concordava começa a perguntar.

A que protegia segredo começa a nomear.

A que repetia opinião começa a examinar.""",
                """Quando uma pessoa muda, o sistema precisa se reorganizar: a que resolvia tudo começa a dizer não; a que concordava, a perguntar; a que protegia segredo, a nomear; a que repetia opinião, a examinar.""",
            ),
            (
                "mapa do conflito",
                """Você pode concordar depressa.

Explicar demais.

Atacar antes de ouvir.

Desaparecer.

Pedir desculpa por existir.""",
                """Você pode concordar depressa, explicar demais, atacar antes de ouvir, desaparecer ou pedir desculpa por existir.""",
            ),
            (
                "papéis herdados",
                """Algumas pessoas receberam papéis antes de receber perguntas.

A responsável.

O forte.

A boazinha.

O rebelde.

A pacificadora.

O provedor.

A invisível.

O orgulho da casa.

A decepção.""",
                """Algumas pessoas receberam papéis antes de receber perguntas: a responsável, o forte, a boazinha, o rebelde, a pacificadora, o provedor, a invisível, o orgulho da casa, a decepção.""",
            ),
            (
                "famílias sem sentença universal",
                """Por isso, frases universais sobre família quase sempre perdem a realidade.

Nem toda família é segura.

Nem toda família é destrutiva.

Nem toda permanência é lealdade.

Nem toda distância é maturidade.

O método não oferece sentença pronta.

Oferece critérios.""",
                """Por isso, frases universais sobre família quase sempre perdem a realidade. Há famílias seguras e destrutivas; permanência não é sempre lealdade, assim como distância não é sempre maturidade.

O método não oferece sentença pronta. Oferece critérios.""",
            ),
            (
                "autoridade e consciência",
                """Julgamento próprio significa continuar presente enquanto aprende.

Perguntar.

Comparar.

Verificar.

Reconhecer competência e limite.

Admitir que não sabe.

Buscar segunda opinião.

Observar frutos.""",
                """Julgamento próprio significa continuar presente enquanto aprende: perguntar, comparar, verificar, reconhecer competência e limite, admitir que não sabe, buscar segunda opinião e observar frutos.""",
            ),
            (
                "prisão externa",
                """Há situações em que reconhecer a Corrente não basta.

Existe ameaça.

Dependência financeira.

Vigilância.

Controle de documentos.

Risco físico.

Isolamento.

Coerção religiosa.

Pressão familiar organizada.""",
                """Há situações em que reconhecer a Corrente não basta. Existe ameaça, dependência financeira, vigilância, controle de documentos, risco físico, isolamento, coerção religiosa ou pressão familiar organizada.""",
            ),
        ],
    )

    apply(
        PART4,
        [
            (
                "abertura Parte IV",
                """Você já observou frutos, distinguiu Semente de Solo, reconheceu configurações e voltou às Raízes.

Sabe que origem explica onde algo começou, enquanto Raiz mostra de onde ainda retira força. Também sabe que uma Corrente restringe e que um Mapa herdado pode orientar sem ser verdade final.

Agora a pergunta muda.

Não basta compreender de onde veio.

É preciso descobrir:""",
                """Você já observou frutos, distinguiu Semente de Solo, reconheceu configurações e voltou às Raízes. Sabe que a origem explica onde algo começou, enquanto a Raiz mostra de onde ainda retira força; que uma Corrente restringe; e que um Mapa herdado pode orientar sem ser verdade final.

Agora a pergunta muda. Compreender de onde veio já não basta. É preciso descobrir:""",
            ),
            (
                "Tronco sem força bruta",
                """O Tronco não é força bruta. Não é rigidez, dureza nem independência absoluta.

É a estrutura que transforma consciência em coerência possível.""",
                """O Tronco não é força bruta, rigidez, dureza ou independência absoluta. É a estrutura que transforma consciência em coerência possível.""",
            ),
            (
                "conhecimento e prática",
                """Você pode compreender sua história e continuar repetindo o mesmo fruto.

Pode nomear uma Raiz e obedecer a ela.

Pode explicar metacognição e responder ao primeiro impulso.

Pode defender limites em público e negociar todos dentro de casa.

Pode falar de liberdade e ser governada por aprovação.

Pode ensinar responsabilidade e usar a dor para não cumprir o que já está na própria esfera.

Pode reconhecer o erro do grupo e continuar protegendo a tribo quando o custo chega.""",
                """Você pode compreender sua história e continuar repetindo o mesmo fruto; nomear uma Raiz e obedecer a ela; explicar metacognição e responder ao primeiro impulso; defender limites em público e negociar todos dentro de casa.

Pode falar de liberdade e ser governada por aprovação, ensinar responsabilidade e usar a dor para não cumprir o que já está na própria esfera, reconhecer o erro do grupo e ainda proteger a tribo quando o custo chega.""",
            ),
            (
                "declarações identitárias",
                """Frases identitárias podem oferecer linguagem:

“Eu sou forte.”

“Eu sou cristã.”

“Eu sou conservadora.”

“Eu sou livre.”

“Eu sou independente.”

“Eu sou assim.”""",
                """Frases identitárias podem oferecer linguagem: “Eu sou forte”, “sou cristã”, “sou conservadora”, “sou livre”, “sou independente”, “sou assim”.""",
            ),
            (
                "autoria emocional abertura",
                """Pessoas afetam você.

Palavras ferem.

Perdas atravessam.

Ambientes organizam ou desorganizam.

O corpo reage.

Violência produz consequências.

Controle não se torna responsabilidade de quem foi controlado.""",
                """Pessoas afetam você. Palavras ferem, perdas atravessam, ambientes organizam ou desorganizam, o corpo reage e a violência produz consequências.

Controle não se torna responsabilidade de quem foi controlado.""",
            ),
            (
                "soberania definição",
                """Não é frieza.

Não é isolamento.

Não é independência absoluta.

Não é domínio sobre os outros.

Não é a fantasia de que ninguém consegue afetar você.""",
                """Não é frieza, isolamento, independência absoluta, domínio sobre os outros nem a fantasia de que ninguém consegue afetar você.""",
            ),
            (
                "fontes terceirizadas",
                """“Meu pai mandou.”

“Minha igreja disse.”

“Meu partido orientou.”

“Minha terapeuta afirmou.”

“Todo mundo compartilhou.”

“O influenciador explicou.”

“O algoritmo mostrou.”

“Este livro disse.”""",
                """“Meu pai mandou.” “Minha igreja disse.” “Meu partido orientou.” “Minha terapeuta afirmou.” “Todo mundo compartilhou.” “O influenciador explicou.” “O algoritmo mostrou.” “Este livro disse.”""",
            ),
            (
                "limite como pessoa",
                """Ele diz:

“Aqui existe uma pessoa.”

“Esta pessoa possui corpo, valores, tempo, responsabilidades, necessidades e escolhas.”

“Pode amar sem desaparecer.”

“Pode ajudar sem assumir tudo.”

“Pode ouvir sem aceitar humilhação.”

“Pode pertencer sem entregar acesso irrestrito.”""",
                """Ele diz: “Aqui existe uma pessoa. Ela possui corpo, valores, tempo, responsabilidades, necessidades e escolhas. Pode amar sem desaparecer, ajudar sem assumir tudo, ouvir sem aceitar humilhação e pertencer sem entregar acesso irrestrito.”""",
            ),
            (
                "proteção não é muro",
                """Mas nem toda distância é muro.

Algumas relações representam risco real. Alguns contextos exigem bloqueio, afastamento, medida jurídica ou ausência de contato.

Chamar proteção de “muro emocional” pode ser crueldade disfarçada de linguagem terapêutica.

Nem toda pessoa merece proximidade.

Nem toda relação pode ser preservada.

Nem toda conversa é segura.""",
                """Mas nem toda distância é muro. Algumas relações representam risco real e alguns contextos exigem bloqueio, afastamento, medida jurídica ou ausência de contato.

Chamar proteção de “muro emocional” pode ser crueldade disfarçada de linguagem terapêutica. Nem toda pessoa merece proximidade, nem toda relação pode ser preservada e nem toda conversa é segura.""",
            ),
            (
                "poder e limites",
                """Limites não acontecem no vazio.

Existe diferença entre dizer não a um amigo e a alguém que controla sua renda.

Entre recusar pedido e enfrentar pessoa violenta.

Entre discordar de colega e de liderança capaz de retaliar.

Entre estabelecer linha numa relação respeitosa e tentar fazê-lo num contexto de coerção.""",
                """Limites não acontecem no vazio. Existe diferença entre dizer não a um amigo e a alguém que controla sua renda; entre recusar um pedido e enfrentar uma pessoa violenta; entre discordar de um colega e de uma liderança capaz de retaliar; entre estabelecer uma linha numa relação respeitosa e tentar fazê-lo num contexto de coerção.""",
            ),
            (
                "contratos invisíveis origem",
                """Alguns contratos são herdados.

Outros, supostos.

Outros, impostos por quem possui mais poder.""",
                """Alguns contratos são herdados; outros, supostos; outros ainda, impostos por quem possui mais poder.""",
            ),
            (
                "clareza e realidade",
                """Uma conversa clara pode aproximar.

Também pode revelar que duas pessoas desejam coisas diferentes.

Você pode comunicar uma necessidade e descobrir que o outro não consegue ou não quer atendê-la.

Pode ouvir o que ele precisa e perceber que não consegue oferecer.

Isso não significa que a conversa falhou.

Significa que a realidade apareceu.""",
                """Uma conversa clara pode aproximar — ou revelar que duas pessoas desejam coisas diferentes. Você pode comunicar uma necessidade e descobrir que o outro não consegue ou não quer atendê-la; pode ouvir o que ele precisa e perceber que não consegue oferecer.

A conversa não falhou. A realidade apareceu.""",
            ),
            (
                "Tronco nos Galhos",
                """O Tronco não aparece no discurso sobre quem você é.

Aparece nos Galhos.

Na relação.

Na família.

No trabalho.

Na fé.

No dinheiro.

Na política.

Nos lugares em que a vida cobra uma resposta concreta.""",
                """O Tronco não aparece no discurso sobre quem você é. Aparece nos Galhos: na relação, na família, no trabalho, na fé, no dinheiro, na política — nos lugares em que a vida cobra uma resposta concreta.""",
            ),
        ],
    )

    p3 = PART3.read_text(encoding="utf-8")
    p4 = PART4.read_text(encoding="utf-8")

    chapter_re = re.compile(r"^# CAP[IÍ]TULO\s+(\d+)\b", flags=re.M | re.I)
    if [int(x) for x in chapter_re.findall(p3)] != [7, 8, 9, 10]:
        raise AssertionError("Parte III perdeu a sequência dos capítulos 7–10.")
    if [int(x) for x in chapter_re.findall(p4)] != [11, 12, 13, 14]:
        raise AssertionError("Parte IV perdeu a sequência dos capítulos 11–14.")

    protected = [
        "[REVISÃO TEOLÓGICA — validar contexto bíblico e formulação.]",
        "[REVISÃO PSICOLÓGICA — validar a formulação final de autoria emocional e suas proteções antes da edição definitiva.]",
        "Sua origem participa da história. Seu posicionamento decide o que continuará atravessando você.",
        "Posicionamento é consciência sustentada em conduta.",
        "Segurança vem antes do desempenho de firmeza.",
        "Se você terminar repetindo Sol Lima, mas incapaz de examinar uma ideia, esta obra falhou.",
    ]
    combined = p3 + "\n" + p4
    for phrase in protected:
        if phrase not in combined:
            raise AssertionError(f"Trecho protegido ausente: {phrase}")

    print("Lote 02 aplicado: Partes III–IV refinadas; capítulos, salvaguardas e marcações especializadas preservados.")


if __name__ == "__main__":
    main()
