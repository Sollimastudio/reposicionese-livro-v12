#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def replace_guarded(text, old, new, label):
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise ValueError(f"{label}: esperado trecho antigo ou versão nova; encontrado {count}")

def update(path, replacements):
    text = path.read_text(encoding='utf-8').replace('\r\n','\n')
    for label, old, new in replacements:
        text = replace_guarded(text, old, new, label)
    path.write_text(text.rstrip()+'\n', encoding='utf-8', newline='\n')

def main():
    update(ROOT/'LER_AGORA_REPOSICIONESE_REV_B.md', [
        ('estado', 'voz e ritmo concluídos nos Lotes 01–03; especialistas e produção pendentes', 'voz e ritmo concluídos nos Lotes 01–04; leitura contínua, especialistas e produção pendentes'),
        ('lotes pendentes', '- passagem global de voz, ritmo e repetição no Lote 4;', '- leitura contínua global após a conclusão dos quatro lotes;'),
        ('proxima etapa', 'A passagem global de voz, ritmo e repetição avançou em lotes controlados. Os **Lotes 01–03 — Pré-livro e Partes I–VI** estão concluídos. A próxima unidade autorizável é o **Lote 04 — Partes VII–VIII e Epílogo**. A pista visual permanece separada porque os binários ainda não foram versionados no repositório.', 'A passagem global de voz, ritmo e repetição foi concluída nos **Lotes 01–04 — Pré-livro, Partes I–VIII e Epílogo**. A próxima etapa é a **leitura contínua global**, seguida das decisões autorais e auditorias especializadas. A pista visual permanece separada porque os binários ainda não foram versionados no repositório.'),
    ])
    update(ROOT/'direcao-editorial/12_REGISTRO_MESTRE_DE_CONTEXTO.md', [
        ('versao', '**Versão:** 3.3 — Voz e ritmo, Lotes 01–03', '**Versão:** 3.4 — Voz e ritmo, Lotes 01–04'),
        ('estado', 'voz e ritmo concluídos nos Lotes 01–03', 'voz e ritmo concluídos nos Lotes 01–04'),
        ('fase', '- voz, ritmo e repetição concluídos no Pré-livro e Partes I–VI;\n- próximo lote textual: Partes VII–VIII e Epílogo;', '- voz, ritmo e repetição concluídos no Pré-livro, Partes I–VIII e Epílogo;\n- próxima etapa textual: leitura contínua global;'),
    ])
    update(ROOT/'direcao-editorial/13_MATRIZ_DE_NAO_PERDA.md', [
        ('versao', '**Versão:** 2.3 — Pós-coerência e voz, Lotes 01–03', '**Versão:** 2.4 — Pós-coerência e voz, Lotes 01–04'),
        ('estado', 'voz e ritmo concluídos no Pré-livro e Partes I–VI', 'voz e ritmo concluídos no Pré-livro, Partes I–VIII e Epílogo'),
    ])
    print('Estado sincronizado após Lote 04.')

if __name__ == '__main__':
    main()
