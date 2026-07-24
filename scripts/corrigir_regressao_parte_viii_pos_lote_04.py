#!/usr/bin/env python3
"""Restaura a cadência canônica da Parte VIII após o Lote 04.

Este script existe porque o gerador histórico da Parte VIII reconstruía a fonte B
a partir da Revisão A. As substituições abaixo preservam conteúdo e restauram a
concentração já aprovada na Revisão B.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "revisao-b-global/32_ONDA_8_PARTE_VIII_EPILOGO_REV_B.md"


def guarded(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise ValueError(f"{label}: esperado trecho antigo ou versão nova; encontrado {count}")


def main() -> None:
    text = PATH.read_text(encoding="utf-8").replace("\r\n", "\n")
    replacements = [
        (
            "recapitulação Capítulo 33",
            """Você observou frutos.

Subiu na Árvore.

Localizou Galhos.

Examinou Tronco, Raízes, Mapas e Solo.

Reconheceu Pragas.

Passou pelo Filtro.

Definiu uma Poda.""",
            """Você observou frutos, subiu na Árvore, localizou Galhos, examinou Tronco, Raízes, Mapas e Solo, reconheceu Pragas, passou pelo Filtro e definiu uma Poda.""",
        ),
        (
            "espaço após a Poda",
            """Retirar um hábito não cria automaticamente um hábito saudável.

Encerrar uma relação não ensina sozinho a construir outro modo de vínculo.

Sair de um grupo não produz identidade.

Reconhecer uma crença não instala uma resposta nova.

Dizer não uma vez não constrói limite sustentado.""",
            """Retirar um hábito não cria automaticamente outro saudável; encerrar uma relação não ensina sozinho a construir um novo modo de vínculo; sair de um grupo não produz identidade. Reconhecer uma crença não instala uma resposta nova, e dizer não uma vez não constrói limite sustentado.""",
        ),
        (
            "desejo e cultivo",
            """Você pode desejar paz e repetir guerra.

Desejar limite e continuar explicando o não até ele virar sim.

Desejar liberdade e manter todas as permissões antigas.

Desejar identidade e passar o dia pedindo à plateia que confirme quem é.

Desejar maturidade e evitar todo desconforto.

O desejo importa.

Mostra direção.

Mas cultivo é feito de práticas.""",
            """Você pode desejar paz e repetir guerra; desejar limite e explicar o não até ele virar sim; desejar liberdade e manter todas as permissões antigas; desejar identidade e pedir à plateia que confirme quem é; desejar maturidade e evitar todo desconforto.

O desejo importa porque mostra direção. Mas cultivo é feito de práticas.""",
        ),
        (
            "mudanças menos cinematográficas",
            """Uma conversa marcada.

Uma resposta adiada por vinte minutos.

Uma fonte verificada.

Um pedido feito sem desculpa.

Uma consulta.

Um limite repetido com a mesma linguagem.

Uma hora protegida.

Uma transferência automática.

Uma noite sem entrar na discussão.""",
            """Uma conversa marcada, uma resposta adiada por vinte minutos, uma fonte verificada, um pedido feito sem desculpa, uma consulta, um limite repetido com a mesma linguagem, uma hora protegida, uma transferência automática, uma noite sem entrar na discussão.""",
        ),
        (
            "o novo pode parecer estranho",
            """O limite pode parecer egoísmo.

O descanso pode parecer irresponsabilidade.

A paz pode parecer vazio.

Uma relação estável pode parecer sem emoção.

Questionar pode parecer deslealdade.

Receber ajuda pode parecer fracasso.

Cobrar pelo trabalho pode parecer arrogância.

Admitir dúvida pode parecer fraqueza.""",
            """O limite pode parecer egoísmo; o descanso, irresponsabilidade; a paz, vazio; uma relação estável, falta de emoção. Questionar pode parecer deslealdade, receber ajuda pode parecer fracasso, cobrar pelo trabalho pode parecer arrogância e admitir dúvida pode parecer fraqueza.""",
        ),
        (
            "registro dos frutos",
            """Mudanças internas podem ser difíceis de perceber no cotidiano.

Registre evidências.

Não apenas grandes resultados.""",
            """Mudanças internas podem ser difíceis de perceber no cotidiano. Registre evidências — não apenas grandes resultados.""",
        ),
        (
            "recaída não é identidade",
            """Você pode repetir um padrão depois de meses.

Voltar a dizer sim por medo.

Compartilhar algo sem verificar.

Explodir.

Desaparecer.

Procurar aprovação.""",
            """Você pode repetir um padrão depois de meses: voltar a dizer sim por medo, compartilhar algo sem verificar, explodir, desaparecer ou procurar aprovação.""",
        ),
        (
            "ajuda e consciência",
            """Escolha apoio que amplie autoria.

Cuidado que exige dependência permanente, impede contraditório ou decide tudo por você precisa ser examinado.

A ajuda participa do cultivo.

Não ocupa o lugar da consciência.""",
            """Escolha apoio que amplie autoria. Cuidado que exige dependência permanente, impede contraditório ou decide tudo por você precisa ser examinado.

A ajuda participa do cultivo; não ocupa o lugar da consciência.""",
        ),
        (
            "relações mais visíveis",
            """Isso não significa que toda pessoa que resiste ao seu posicionamento esteja errada.

Talvez seu modo de comunicar precise de revisão.

Talvez exista incompatibilidade.

Talvez o outro precise de tempo.

Talvez você esteja usando firmeza como arma.""",
            """Isso não significa que toda pessoa que resiste ao seu posicionamento esteja errada. Talvez seu modo de comunicar precise de revisão, exista incompatibilidade, o outro precise de tempo ou você esteja usando firmeza como arma.""",
        ),
        (
            "explicação adequada",
            """Explicação é importante.

Contexto ajuda.

Prestação de contas pode ser dever.""",
            """Explicação é importante, contexto ajuda e prestação de contas pode ser dever.""",
        ),
    ]
    for label, old, new in replacements:
        text = guarded(text, old, new, label)
    PATH.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    print("Cadência da Parte VIII restaurada e protegida.")


if __name__ == "__main__":
    main()
