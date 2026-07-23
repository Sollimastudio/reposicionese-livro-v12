#!/usr/bin/env python3
"""Aplica voz, ritmo e repetição — Lote 04: Partes VII–VIII e Epílogo.

Passagem estritamente estilística. Preserva as 12 perguntas, os 14 Tipos,
as 14 Leis, os Sete Frutos, o ritual final, o Epílogo e marcações pendentes.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P7 = ROOT / "revisao-b-global/29_ONDA_7_PARTE_VII_REV_B.md"
P8 = ROOT / "revisao-b-global/32_ONDA_8_PARTE_VIII_EPILOGO_REV_B.md"


def guarded(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise ValueError(f"{label}: esperado 1 trecho antigo ou versão nova; encontrado {count}")


def apply(path: Path, replacements):
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    for label, old, new in replacements:
        text = guarded(text, old, new, label)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def main():
    apply(P7, [
        ("abertura escuta", """Ouvir uma verdade pode doer.

Ouvir uma mentira também.

Ser confrontada pode gerar vergonha, raiva, medo ou alívio.

Ser humilhada pode produzir emoções semelhantes.

Por isso, desconforto não distingue sozinho correção de violência.""", """Ouvir uma verdade pode doer — e ouvir uma mentira também. Confronto e humilhação podem produzir vergonha, raiva, medo ou alívio.

Por isso, desconforto não distingue sozinho correção de violência."""),
        ("reações à fala", """Quando uma fala toca identidade, a reação tenta decidir imediatamente.

Atacar.

Explicar.

Desaparecer.

Concordar por medo.

Rejeitar tudo.""", """Quando uma fala toca identidade, a reação tenta decidir imediatamente: atacar, explicar, desaparecer, concordar por medo ou rejeitar tudo."""),
        ("desconfortos necessários", """Há conversas necessárias que doem.

Receber um não.

Ouvir que uma promessa não foi cumprida.

Reconhecer impacto.

Receber avaliação profissional.

Ser confrontada por contradição.

Descobrir que boa intenção não impediu dano.""", """Há conversas necessárias que doem: receber um não, ouvir que uma promessa não foi cumprida, reconhecer impacto, receber avaliação profissional, ser confrontada por contradição ou descobrir que boa intenção não impediu dano."""),
        ("ouvido submetido", """Outra pessoa aceita tudo.

Se alguém fala com autoridade, acredita.

Se uma liderança corrige, assume culpa.

Se o parceiro acusa, pede perdão antes de investigar.

Se o grupo desaprova, muda de posição.""", """Outra pessoa aceita tudo: se alguém fala com autoridade, acredita; se uma liderança corrige, assume culpa; se o parceiro acusa, pede perdão antes de investigar; se o grupo desaprova, muda de posição."""),
        ("polarização e escuta", """Na polarização, ouvir parece conceder vitória.

Perguntar parece fraqueza.

Reconhecer um ponto do outro parece traição.

Mas escutar não é aderir.""", """Na polarização, ouvir parece conceder vitória, perguntar parece fraqueza e reconhecer um ponto do outro parece traição. Mas escutar não é aderir."""),
        ("mudança dos modos", """A mesma pessoa pode operar de forma saudável no trabalho, morna na família e tóxica numa discussão política.

Pode amadurecer.

Pode regredir sob pressão.

Pode reconhecer um modo e praticar outro.""", """A mesma pessoa pode operar de forma saudável no trabalho, morna na família e tóxica numa discussão política. Pode amadurecer, regredir sob pressão, reconhecer um modo e praticar outro."""),
        ("sensatez adequada", """Posicionamento saudável não é metade entre agressão e desaparecimento.

É resposta adequada ao contexto.

Às vezes, firme.

Delicada.

Pública.

Privada.

Imediata.

Preparada.

Sensatez não é temperatura média.

É adequação responsável.""", """Posicionamento saudável não é metade entre agressão e desaparecimento. É resposta adequada ao contexto: às vezes firme, delicada, pública, privada, imediata ou preparada.

Sensatez não é temperatura média. É adequação responsável."""),
        ("introdução dos Tipos", """Os 14 Tipos não dizem quem você é.

Mostram como pode estar operando num contexto.

Uma pessoa pode apresentar mais de um tipo.

Pode mudar conforme o Galho, o poder, o medo e a pressão.

Os nomes são imagens pedagógicas.""", """Os 14 Tipos não dizem quem você é; mostram como pode estar operando num contexto. Uma pessoa pode apresentar mais de um tipo e mudar conforme o Galho, o poder, o medo e a pressão.

Os nomes são imagens pedagógicas."""),
        ("dor depois da Poda", """Chorar uma relação que precisava terminar.

Sentir culpa depois do limite.

Estranhar a paz.

Perder pertencimento.

Descobrir que liberdade possui solidão inicial.

Dor depois da Poda não prova erro.

Alívio também não prova acerto definitivo.""", """Você pode chorar uma relação que precisava terminar, sentir culpa depois do limite, estranhar a paz, perder pertencimento ou descobrir que a liberdade possui solidão inicial.

Dor depois da Poda não prova erro. Alívio também não prova acerto definitivo."""),
        ("Poda gradual", """Algumas mudanças precisam ser graduais.

Reduzir exposição.

Reorganizar dinheiro.

Construir rede.

Treinar resposta.

Alterar agenda.

Delegar.

Buscar qualificação.

Planejar saída.""", """Algumas mudanças precisam ser graduais: reduzir exposição, reorganizar dinheiro, construir rede, treinar resposta, alterar agenda, delegar, buscar qualificação ou planejar saída."""),
        ("Poda imediata", """Outras situações exigem interrupção rápida.

Risco físico.

Fraude.

Violação grave.

Ameaça.

Exposição perigosa.

Conduta que exige denúncia ou proteção.""", """Outras situações exigem interrupção rápida: risco físico, fraude, violação grave, ameaça, exposição perigosa ou conduta que exige denúncia ou proteção."""),
        ("fruto provável", """Você pode decidir com cuidado e encontrar resultado inesperado.

Outra pessoa possui liberdade.

O ambiente muda.

Informações faltam.

Acidentes acontecem.

Responsabilidade não é previsão perfeita.""", """Você pode decidir com cuidado e encontrar resultado inesperado: outra pessoa possui liberdade, o ambiente muda, informações faltam e acidentes acontecem.

Responsabilidade não é previsão perfeita."""),
        ("custo da posição", """Toda posição real fecha possibilidades.

Dizer sim limita outras escolhas.

Dizer não pode frustrar.

Assumir erro altera imagem.

Mudar de grupo reduz pertencimento.

Manter convicção pode custar aprovação.

Revisar convicção pode custar orgulho.""", """Toda posição real fecha possibilidades: dizer sim limita outras escolhas; dizer não pode frustrar; assumir erro altera imagem; mudar de grupo reduz pertencimento; manter convicção pode custar aprovação; revisar convicção pode custar orgulho."""),
        ("transição para plantio", """A próxima Parte não será sobre cortar mais.

Será sobre plantar.

Uma Árvore não muda apenas pela retirada do que adoece.

Precisa de nova prática, ambiente, repetição e acompanhamento.""", """A próxima Parte não será sobre cortar mais, mas sobre plantar. Uma Árvore não muda apenas pela retirada do que adoece; precisa de nova prática, ambiente, repetição e acompanhamento."""),
    ])

    apply(P8, [
        ("Poda e Semente", """A Poda interrompe.

A Nova Semente inicia cultivo.""", """A Poda interrompe; a Nova Semente inicia cultivo."""),
        ("consciência e incorporação", """Compreender produz possibilidade.

Não garante incorporação.

Você pode viver uma leitura transformadora e voltar ao modo anterior quando a pressão chega.

Isso não prova que nada mudou.

Mostra que o novo ainda precisa de cultivo.""", """Compreender produz possibilidade, não incorporação automática. Você pode viver uma leitura transformadora e voltar ao modo anterior quando a pressão chega.

Isso não prova que nada mudou; mostra que o novo ainda precisa de cultivo."""),
        ("apoio sem terceirização", """Apoio pode vir de:

- amizade madura;
- família segura;
- comunidade responsável;
- terapia;
- aconselhamento pastoral;
- supervisão profissional;
- grupo de apoio;
- mentoria;
- orientação jurídica, médica ou financeira.""", """Apoio pode vir de amizade madura, família segura, comunidade responsável, terapia, aconselhamento pastoral, supervisão profissional, grupo de apoio, mentoria ou orientação jurídica, médica e financeira."""),
        ("Semente sem resultado", """Uma prática pode não produzir o fruto esperado.

Talvez esteja mal definida.

Talvez o ambiente precise mudar.

Talvez o problema exija apoio especializado.

Talvez o fruto precise de mais tempo.

Talvez a hipótese estivesse errada.

Talvez a prática cobre um recurso que você ainda não possui.""", """Uma prática pode não produzir o fruto esperado porque está mal definida, o ambiente precisa mudar, o problema exige apoio especializado, o fruto precisa de mais tempo, a hipótese estava errada ou a prática cobra um recurso que você ainda não possui."""),
        ("limites do posicionamento", """Posicionamento não elimina dor.

Não impede toda rejeição.

Não garante sucesso financeiro.

Não protege contra todas as violências.

Não torna relações simples.

Não oferece controle sobre o comportamento alheio.

O que pode produzir é outra participação diante da realidade.""", """Posicionamento não elimina dor, impede toda rejeição, garante sucesso financeiro, protege contra todas as violências, torna relações simples ou oferece controle sobre o comportamento alheio.

O que pode produzir é outra participação diante da realidade."""),
        ("retorno ao eixo", """Você percebe.

Nomeia.

Repara.

Pede ajuda.

Revê a prática.

Retoma.""", """Você percebe, nomeia, repara, pede ajuda, revê a prática e retoma."""),
        ("não controlar tudo", """A outra pessoa pode discordar.

Pode não compreender.

Pode ir embora.

Pode precisar de tempo.

Pode não mudar.""", """A outra pessoa pode discordar, não compreender, ir embora, precisar de tempo ou não mudar."""),
        ("mapa dos Galhos final", """Retome o mapa feito no início.

Relacionamentos.

Família.

Trabalho.

Dinheiro.

Fé.

Corpo.

Limites.

Identidade.

Paz.

Propósito.

Política e pertencimento.

Vida digital.""", """Retome o mapa feito no início: relacionamentos, família, trabalho, dinheiro, fé, corpo, limites, identidade, paz, propósito, política e pertencimento, vida digital."""),
        ("proteção final", """Essa frase não significa que tudo foi causado por você.

Não significa que o mundo é justo.

Não significa que abuso é responsabilidade da vítima.

Não significa que contexto não importa.

Não significa que vontade supera qualquer limite material.""", """Essa frase não significa que tudo foi causado por você, que o mundo é justo, que abuso é responsabilidade da vítima, que contexto não importa ou que vontade supera qualquer limite material."""),
        ("porta interna", """Talvez a porta seja interna.

Uma conversa.

Uma permissão que precisa ser retirada.

Um pedido de ajuda.

Parar de se punir.""", """Talvez a porta seja interna: uma conversa, uma permissão que precisa ser retirada, um pedido de ajuda ou o fim da autopunição."""),
    ])
    print("Lote 04 aplicado com sucesso.")


if __name__ == "__main__":
    main()
