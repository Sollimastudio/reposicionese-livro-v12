#!/usr/bin/env python3
"""Aplica voz, ritmo e repetição — Lote 03: Partes V–VI.

A passagem é estritamente estilística: preserva capítulos, método, comandos,
marcadores autorais e especializados, salvaguardas de segurança, histórias,
Leis, Jaulas, práticas e checkpoints.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART5 = ROOT / "revisao-b-global/23_ONDA_5_PARTE_V_REV_B.md"
PART6 = ROOT / "revisao-b-global/26_ONDA_6_PARTE_VI_REV_B.md"


def replace_guarded(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise ValueError(
        f"{label}: esperado um trecho antigo ou a versão nova já aplicada; encontrado {count}."
    )


def apply(path: Path, replacements: list[tuple[str, str, str]]) -> None:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    for label, old, new in replacements:
        text = replace_guarded(text, old, new, label)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    apply(
        PART5,
        [
            (
                "abertura Parte V",
                """A Árvore não termina no interior da pessoa.

Ela aparece na relação, na família, no trabalho, no dinheiro, na fé, na política, no corpo, no descanso, na sexualidade, na amizade e no cuidado.

Essas áreas são os Galhos.

Nenhum Galho receberá aqui um método separado. Não abriremos seis livros dentro deste livro.""",
                """A Árvore não termina no interior da pessoa. Ela aparece na relação, na família, no trabalho, no dinheiro, na fé, na política, no corpo, no descanso, na sexualidade, na amizade e no cuidado. Essas áreas são os Galhos.

Nenhum deles receberá um método separado. Não abriremos seis livros dentro deste livro.""",
            ),
            (
                "retomada Capítulo 15",
                """Você já observou frutos.

Distinguiu Semente de Solo.

Reconheceu configurações, Raízes, Correntes e Mapas.

Perguntou o que o Tronco consegue sustentar quando existe custo.

Agora a investigação entra na vida concreta.""",
                """Você já observou frutos, distinguiu Semente de Solo, reconheceu configurações, Raízes, Correntes e Mapas e perguntou o que o Tronco consegue sustentar quando existe custo.

Agora a investigação entra na vida concreta.""",
            ),
            (
                "exemplos de Galhos diferentes",
                """Você pode ter dificuldade num relacionamento e possuir amizades saudáveis.

Pode cometer um erro profissional sem ser incompetente em tudo.

Pode perder o domínio numa conversa e reconhecer que desenvolveu autocontrole em muitos outros contextos.

Pode sustentar limites no trabalho e desaparecer diante da família.

Pode ter clareza financeira e confusão afetiva.

Pode ter voz política e não conseguir dizer não a uma pessoa específica.

Pode cuidar dos filhos com responsabilidade e negligenciar o próprio corpo.

Pode possuir fé profunda e precisar revisar a maneira como lida com autoridade religiosa.""",
                """Você pode ter dificuldade num relacionamento e possuir amizades saudáveis; cometer um erro profissional sem ser incompetente em tudo; perder o domínio numa conversa e, ainda assim, reconhecer o autocontrole desenvolvido em outros contextos.

Pode sustentar limites no trabalho e desaparecer diante da família, ter clareza financeira e confusão afetiva, voz política e dificuldade para dizer não a uma pessoa específica. Pode cuidar dos filhos com responsabilidade e negligenciar o próprio corpo, possuir fé profunda e ainda precisar revisar a maneira como lida com autoridade religiosa.""",
            ),
            (
                "Galho e identidade inteira",
                """Trabalho.

Casamento.

Maternidade.

Igreja.

Imagem.

Causa política.

Uma área pode ser profundamente importante.""",
                """Trabalho, casamento, maternidade, igreja, imagem ou causa política: uma área pode ser profundamente importante.""",
            ),
            (
                "fusão relacional",
                """Você deixa de falar.

Afasta vínculos importantes.

Pede autorização para decisões que pertencem à sua esfera.

Muda valores, roupas, projetos ou opiniões apenas para evitar punição.

Mede cada palavra pelo humor da outra pessoa.

Duvida continuamente da própria percepção.""",
                """Você deixa de falar, afasta vínculos importantes e pede autorização para decisões que pertencem à sua esfera. Muda valores, roupas, projetos ou opiniões para evitar punição, mede cada palavra pelo humor da outra pessoa e passa a duvidar continuamente da própria percepção.""",
            ),
            (
                "intensidade relacional",
                """Mensagens contínuas.

Planos acelerados.

Promessas precoces.

Sensação de reconhecimento total.

A intensidade pode participar de uma relação saudável.""",
                """Mensagens contínuas, planos acelerados, promessas precoces, sensação de reconhecimento total: a intensidade pode participar de uma relação saudável.""",
            ),
            (
                "verdade na relação",
                """A verdade não garante o resultado desejado.

Pode aproximar.

Pode revelar incompatibilidade.

Pode mostrar matéria para reconstrução.

Pode mostrar que a relação só permanecia por ambiguidade.""",
                """A verdade não garante o resultado desejado. Pode aproximar, revelar incompatibilidade, mostrar matéria para reconstrução ou expor que a relação só permanecia por ambiguidade.""",
            ),
            (
                "papéis familiares atuais",
                """A responsável.

O pacificador.

A forte.

O provedor.

A religiosa.

A problemática.

O invisível.

A filha que cuida de todos.

O filho que compensa os demais.

A pessoa pode sair de casa e continuar executando o papel décadas depois.""",
                """A responsável, o pacificador, a forte, o provedor, a religiosa, a problemática, o invisível, a filha que cuida de todos, o filho que compensa os demais: a pessoa pode sair de casa e continuar executando o papel décadas depois.""",
            ),
            (
                "abertura trabalho",
                """Uma pessoa pode liderar equipes e não conseguir cobrar pelo próprio trabalho.

Pode sustentar limites em casa e desaparecer diante de uma chefia.

Pode ganhar bem e usar produtividade para nunca se encontrar.

Pode chamar exploração de oportunidade porque teme parecer ingrata.

Pode rejeitar toda disciplina como opressão e chamar desorganização de liberdade.""",
                """Uma pessoa pode liderar equipes e não conseguir cobrar pelo próprio trabalho; sustentar limites em casa e desaparecer diante de uma chefia; ganhar bem e usar produtividade para nunca se encontrar.

Pode chamar exploração de oportunidade porque teme parecer ingrata ou rejeitar toda disciplina como opressão e chamar desorganização de liberdade.""",
            ),
            (
                "trabalho invisível",
                """Cuidado doméstico.

Cuidado de crianças e idosos.

Organização de rotina.

Apoio comunitário.

Serviço religioso.

Essas atividades possuem valor e custo, mesmo quando não recebem salário.""",
                """Cuidado doméstico, cuidado de crianças e idosos, organização de rotina, apoio comunitário e serviço religioso possuem valor e custo, mesmo quando não recebem salário.""",
            ),
            (
                "abertura pertencimento",
                """Fé, comunidade e política são Galhos diferentes.

Compartilham, porém, uma força poderosa.

Oferecem linguagem, valores, direção, identidade coletiva e pertencimento.

Também podem despertar medo de exclusão, lealdade cega, simplificação e terceirização da consciência.

O problema não é pertencer.

O problema começa quando permanecer exige desaparecimento.""",
                """Fé, comunidade e política são Galhos diferentes, mas compartilham uma força poderosa: oferecem linguagem, valores, direção, identidade coletiva e pertencimento. Também podem despertar medo de exclusão, lealdade cega, simplificação e terceirização da consciência.

O problema não é pertencer. Começa quando permanecer exige desaparecimento.""",
            ),
            (
                "corpo e interpretações únicas",
                """Não espiritualize todo sintoma.

Não psicologize toda doença.

Não ignore o corpo para proteger um discurso de força.

Procure avaliação adequada quando necessário.""",
                """Não espiritualize todo sintoma, não psicologize toda doença nem ignore o corpo para proteger um discurso de força. Procure avaliação adequada quando necessário.""",
            ),
            (
                "amizade e mudança de fase",
                """Nem toda amizade precisa permanecer com a mesma intensidade.

Fases mudam.

Distâncias acontecem.

Mas desaparecer sem linguagem, usar pessoas apenas em crise ou exigir disponibilidade unilateral também produz frutos.""",
                """Nem toda amizade precisa permanecer com a mesma intensidade. Fases mudam, distâncias acontecem; ainda assim, desaparecer sem linguagem, usar pessoas apenas em crise ou exigir disponibilidade unilateral também produz frutos.""",
            ),
        ],
    )

    apply(
        PART6,
        [
            (
                "retomada Capítulo 21",
                """Você observou frutos.

Localizou Galhos.

Investigou Semente, Solo, Raízes, Mapas e Tronco.

Agora precisamos perguntar:""",
                """Você observou frutos, localizou Galhos e investigou Semente, Solo, Raízes, Mapas e Tronco.

Agora precisamos perguntar:""",
            ),
            (
                "emoções não são Praga",
                """Raiva pode sinalizar injustiça.

Medo pode alertar perigo.

Culpa pode revelar responsabilidade.

Tristeza pode acompanhar luto.

Desejo de pertencimento pode conduzir a comunidade saudável.

A emoção não vira Praga porque incomoda.""",
                """Raiva pode sinalizar injustiça; medo, alertar perigo; culpa, revelar responsabilidade; tristeza, acompanhar luto; desejo de pertencimento, conduzir a comunidade saudável.

A emoção não vira Praga porque incomoda.""",
            ),
            (
                "mecanismos externos e internos",
                """Alguns mecanismos chegam de fora.

Manipulação.

Pressão de grupo.

Propaganda.

Algoritmo.

Controle coercitivo.

Abuso de autoridade.

Cultura de humilhação.

Outros são mantidos internamente.

Comparação repetida.

Ressentimento cultivado.

Busca compulsiva por confirmação.

Narrativa de incapacidade.

Autopunição.

Medo de crescer.""",
                """Alguns mecanismos chegam de fora: manipulação, pressão de grupo, propaganda, algoritmo, controle coercitivo, abuso de autoridade e cultura de humilhação.

Outros são mantidos internamente: comparação repetida, ressentimento cultivado, busca compulsiva por confirmação, narrativa de incapacidade, autopunição e medo de crescer.""",
            ),
            (
                "definição de negligência",
                """Negligência não é descansar.

Não é falhar uma vez.

Não é não conseguir fazer tudo.

Existem limites reais de tempo, saúde, dinheiro, energia e conhecimento.

Há fases de sobrevivência.

Há pessoas sobrecarregadas, não adormecidas.

Há decisões que precisam de informação, proteção e tempo.""",
                """Negligência não é descansar, falhar uma vez ou não conseguir fazer tudo. Existem limites reais de tempo, saúde, dinheiro, energia e conhecimento; há fases de sobrevivência, pessoas sobrecarregadas — não adormecidas — e decisões que precisam de informação, proteção e tempo.""",
            ),
            (
                "atos adiados",
                """A conversa não acontece.

O exame não é marcado.

A conta não é aberta.

O pedido de ajuda não é feito.

O limite nunca sai do rascunho.

O problema no trabalho é comentado com todos, menos com quem pode participar da solução.

A relação se deteriora enquanto ausência de conflito recebe o nome de paz.""",
                """A conversa não acontece, o exame não é marcado, a conta não é aberta, o pedido de ajuda não é feito e o limite nunca sai do rascunho. O problema no trabalho é comentado com todos, menos com quem pode participar da solução; a relação se deteriora enquanto ausência de conflito recebe o nome de paz.""",
            ),
            (
                "sinais do óbvio",
                """O dinheiro não fecha há meses.

A equipe não compreende prioridades.

O corpo pede avaliação.

A relação não possui acordo básico.

A dívida cresce.

O ressentimento mudou a forma de falar.

O ambiente pune perguntas.

A pessoa prometeu reparar, mas os frutos permanecem iguais.""",
                """O dinheiro não fecha há meses; a equipe não compreende prioridades; o corpo pede avaliação; a relação não possui acordo básico. A dívida cresce, o ressentimento mudou a forma de falar, o ambiente pune perguntas e a pessoa prometeu reparar — mas os frutos permanecem iguais.""",
            ),
            (
                "negligência consigo",
                """Algumas pessoas cuidam de tudo, menos da estrutura que torna o cuidado possível.

Dormem apenas quando o corpo desliga.

Pedem ajuda somente depois do colapso.

Comem quando sobra tempo.

Não acompanham saúde.

Vivem em disponibilidade permanente.

Chamam exaustão de compromisso.""",
                """Algumas pessoas cuidam de tudo, menos da estrutura que torna o cuidado possível: dormem apenas quando o corpo desliga, pedem ajuda depois do colapso, comem quando sobra tempo, não acompanham a saúde, vivem em disponibilidade permanente e chamam exaustão de compromisso.""",
            ),
            (
                "negligência relacional",
                """Relações podem enfraquecer pela soma de pequenas ausências.

A conversa sempre adiada.

O pedido nunca feito.

O reparo substituído por presente.

A tarefa invisível nunca reconhecida.

O limite atravessado porque ninguém quis lidar com a reação.""",
                """Relações podem enfraquecer pela soma de pequenas ausências: a conversa sempre adiada, o pedido nunca feito, o reparo substituído por presente, a tarefa invisível nunca reconhecida, o limite atravessado porque ninguém quis lidar com a reação.""",
            ),
            (
                "conforto que restaura",
                """Existe conforto que restaura.

Descanso.

Casa segura.

Rotina possível.

Silêncio.

Presença confiável.

Existe também um conforto que protege uma contradição já percebida.""",
                """Existe conforto que restaura: descanso, casa segura, rotina possível, silêncio, presença confiável.

Existe também um conforto que protege uma contradição já percebida.""",
            ),
            (
                "formas do Sofá",
                """Ele não precisa parecer preguiça.

Pode ser excesso de trabalho.

Consumo de conteúdo.

Uma relação que não exige verdade.

Uma crença que poupa decisão.

A certeza oferecida por um grupo.

A explicação que permite continuar sem tocar no fruto.""",
                """Ele não precisa parecer preguiça. Pode assumir a forma de excesso de trabalho, consumo de conteúdo, relação que não exige verdade, crença que poupa decisão, certeza oferecida por um grupo ou explicação que permite continuar sem tocar no fruto.""",
            ),
            (
                "validação e plateia",
                """Ser reconhecida é humano.

Feedback ajuda.

Uma comunidade pode confirmar capacidades que você não via.

A Praga aparece quando valor, decisão ou identidade não conseguem permanecer sem retorno constante.

A pessoa posta para saber se sente.

Decide pelo engajamento.

Muda opinião pela reação.

Transforma sofrimento em conteúdo antes de processá-lo.

Confunde visibilidade com existência.""",
                """Ser reconhecida é humano, feedback ajuda e uma comunidade pode confirmar capacidades que você não via.

A Praga aparece quando valor, decisão ou identidade não conseguem permanecer sem retorno constante: a pessoa posta para saber se sente, decide pelo engajamento, muda opinião pela reação, transforma sofrimento em conteúdo antes de processá-lo e confunde visibilidade com existência.""",
            ),
            (
                "ressentimento alimentado",
                """A pessoa repete a cena.

Reescreve conversas.

Procura confirmação.

Recusa informação que complique a posição de vítima e culpado.""",
                """A pessoa repete a cena, reescreve conversas, procura confirmação e recusa informação que complique a posição de vítima e culpado.""",
            ),
            (
                "Jaulas externas reais",
                """Há Jaulas externas reais.

Ameaça.

Violência.

Dependência financeira.

Controle de documentos.

Vigilância.

Risco para filhos.

Doença.

Coerção institucional.

Ausência de moradia.

Dependência de cuidado.

A porta pode estar aberta numa dimensão e bloqueada em outra.""",
                """Há Jaulas externas reais: ameaça, violência, dependência financeira, controle de documentos, vigilância, risco para filhos, doença, coerção institucional, ausência de moradia e dependência de cuidado.

A porta pode estar aberta numa dimensão e bloqueada em outra.""",
            ),
        ],
    )

    print("Voz, ritmo e repetição aplicados às Partes V–VI — Lote 03.")


if __name__ == "__main__":
    main()
