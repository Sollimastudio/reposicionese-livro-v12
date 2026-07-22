#!/usr/bin/env python3
"""Aplica voz, ritmo e repetição — Lote 04: Partes VII–VIII e Epílogo.

Passagem estritamente estilística. Preserva as 12 perguntas, os 14 Tipos,
as Leis, os Sete Frutos, o ritual final, o Epílogo e marcações pendentes.
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
        ("abertura cap27",
         """Você já encontrou frutos.\n\nLocalizou Galhos.\n\nExaminou Tronco, Raízes, Mapas e Solo.\n\nReconheceu Pragas e Jaulas.\n\nAgora precisa decidir o que fará com aquilo que percebeu.""",
         """Você já encontrou frutos, localizou Galhos, examinou Tronco, Raízes, Mapas e Solo e reconheceu Pragas e Jaulas.\n\nAgora precisa decidir o que fará com aquilo que percebeu."""),
        ("verdade exemplos",
         """Uma interpretação pode combinar com sua dor e ainda estar incompleta.\n\nUma notícia pode confirmar sua posição política e continuar falsa.\n\nUma acusação pode circular milhares de vezes sem evidência.\n\nUma pessoa pode dizer algo verdadeiro para humilhar.\n\nOutra pode falar com carinho e oferecer uma mentira.""",
         """Uma interpretação pode combinar com sua dor e ainda estar incompleta; uma notícia pode confirmar sua posição política e continuar falsa; uma acusação pode circular milhares de vezes sem evidência.\n\nUma pessoa pode dizer algo verdadeiro para humilhar, enquanto outra fala com carinho e oferece uma mentira."""),
        ("logica exemplos",
         """“Se você me ama, fará o que peço.”\n\n“Se discorda, está contra mim.”\n\n“Como esta pessoa errou uma vez, tudo o que diz é falso.”\n\n“Como sofri, minha reação está correta.”""",
         """“Se você me ama, fará o que peço.” “Se discorda, está contra mim.” “Como esta pessoa errou uma vez, tudo o que diz é falso.” “Como sofri, minha reação está correta.”"""),
        ("nobreza exemplos",
         """Uma ação pode ser legal e pequena.\n\nPode ser eficiente e cruel.\n\nPode vencer a discussão e diminuir todos os envolvidos.""",
         """Uma ação pode ser legal e pequena, eficiente e cruel, ou vencer a discussão diminuindo todos os envolvidos."""),
        ("fruto horizontes",
         """O fruto não é o único critério.\n\nResultados podem demorar.\n\nUma decisão correta pode gerar desconforto inicial.\n\nUma escolha destrutiva pode oferecer prazer rápido.""",
         """O fruto não é o único critério, e resultados podem demorar. Uma decisão correta pode gerar desconforto inicial; uma escolha destrutiva, prazer rápido."""),
        ("pessoa posicionada",
         """Às vezes, a pessoa posicionada fala.\n\nÀs vezes, escuta.\n\nAdmite que não sabe.\n\nProcura ajuda.\n\nEstabelece limite.\n\nMuda de opinião.\n\nPermanece.\n\nEncerra.""",
         """Às vezes, a pessoa posicionada fala; em outras, escuta, admite que não sabe, procura ajuda, estabelece limite, muda de opinião, permanece ou encerra."""),
    ])

    apply(P8, [
        ("abertura cap33",
         """Você observou frutos.\n\nSubiu na Árvore.\n\nLocalizou Galhos.\n\nExaminou Tronco, Raízes, Mapas e Solo.\n\nReconheceu Pragas.\n\nPassou pelo Filtro.\n\nDefiniu uma Poda.\n\nAgora surge uma pergunta que muita gente esquece:""",
         """Você observou frutos, subiu na Árvore, localizou Galhos, examinou Tronco, Raízes, Mapas e Solo, reconheceu Pragas, passou pelo Filtro e definiu uma Poda.\n\nAgora surge uma pergunta que muita gente esquece:"""),
        ("poda e semente",
         """Retirar um hábito não cria automaticamente um hábito saudável.\n\nEncerrar uma relação não ensina sozinho a construir outro modo de vínculo.\n\nSair de um grupo não produz identidade.\n\nReconhecer uma crença não instala uma resposta nova.\n\nDizer não uma vez não constrói limite sustentado.""",
         """Retirar um hábito não cria automaticamente outro saudável; encerrar uma relação não ensina sozinho a construir um novo modo de vínculo; sair de um grupo não produz identidade. Reconhecer uma crença não instala uma resposta nova, e dizer não uma vez não constrói limite sustentado."""),
        ("desejo cultivo",
         """Você pode desejar paz e repetir guerra.\n\nDesejar limite e continuar explicando o não até ele virar sim.\n\nDesejar liberdade e manter todas as permissões antigas.\n\nDesejar identidade e passar o dia pedindo à plateia que confirme quem é.\n\nDesejar maturidade e evitar todo desconforto.\n\nO desejo importa.\n\nMostra direção.\n\nMas cultivo é feito de práticas.""",
         """Você pode desejar paz e repetir guerra; desejar limite e explicar o não até ele virar sim; desejar liberdade e manter todas as permissões antigas; desejar identidade e pedir à plateia que confirme quem é; desejar maturidade e evitar todo desconforto.\n\nO desejo importa porque mostra direção. Mas cultivo é feito de práticas."""),
        ("pequenas mudancas",
         """Uma conversa marcada.\n\nUma resposta adiada por vinte minutos.\n\nUma fonte verificada.\n\nUm pedido feito sem desculpa.\n\nUma consulta.\n\nUm limite repetido com a mesma linguagem.\n\nUma hora protegida.\n\nUma transferência automática.\n\nUma noite sem entrar na discussão.""",
         """Uma conversa marcada, uma resposta adiada por vinte minutos, uma fonte verificada, um pedido feito sem desculpa, uma consulta, um limite repetido com a mesma linguagem, uma hora protegida, uma transferência automática, uma noite sem entrar na discussão."""),
        ("novo estranho",
         """O limite pode parecer egoísmo.\n\nO descanso pode parecer irresponsabilidade.\n\nA paz pode parecer vazio.\n\nUma relação estável pode parecer sem emoção.\n\nQuestionar pode parecer deslealdade.\n\nReceber ajuda pode parecer fracasso.\n\nCobrar pelo trabalho pode parecer arrogância.\n\nAdmitir dúvida pode parecer fraqueza.""",
         """O limite pode parecer egoísmo; o descanso, irresponsabilidade; a paz, vazio; uma relação estável, falta de emoção. Questionar pode parecer deslealdade, receber ajuda pode parecer fracasso, cobrar pelo trabalho pode parecer arrogância e admitir dúvida pode parecer fraqueza."""),
        ("recaida exemplos",
         """Você pode repetir um padrão depois de meses.\n\nVoltar a dizer sim por medo.\n\nCompartilhar algo sem verificar.\n\nExplodir.\n\nDesaparecer.\n\nProcurar aprovação.""",
         """Você pode repetir um padrão depois de meses: voltar a dizer sim por medo, compartilhar algo sem verificar, explodir, desaparecer ou procurar aprovação."""),
    ])
    print("Lote 04 aplicado com sucesso.")


if __name__ == "__main__":
    main()
