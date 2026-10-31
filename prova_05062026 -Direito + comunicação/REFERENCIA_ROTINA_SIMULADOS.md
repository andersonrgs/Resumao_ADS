# Referência: Rotina de Estudo e Simulados HTML (Provas G2 — 05/11/2026)

> Documento vivo. Atualize a seção **Backlog / Ideias de melhoria** sempre que surgir algo novo a implementar.
> Última atualização: 2026-10-30

## 1. Contexto
- Provas finais G2 em **05/11/2026**: **Comunicação e Linguagem** e **Direito Digital** (conteúdo das Unidades 1 a 4 de cada).
- Rotina usada em semestres anteriores: resumo de estudo, mapa mental, áudio/vídeo (NotebookLM/Gemini) e simulados HTML com base nos questionários corrigidos.
- Decisão desta rodada: **um simulado único por disciplina (U1–U4 juntas)**, com **etiqueta de unidade** em cada questão.

## 2. Estrutura de pastas (`prova_05062026/`)
```
prova_05062026/
├── Comunicação e linguagem/
│   ├── Ebook+Materiais/   (PDFs U1-U4, resumo_e_mapa_mental_u1_a_u4.md, transcricao_videoaulas_u1_a_u4.md, pastas *_youtube)
│   └── Questionarios/     (PNGs + questionario_u1_u2_transcricao.md + questionario_u3_u4_transcricao.md)
├── Direito digital/
│   ├── Ebook + Materiais/ (PDFs Sagah Un1-Un4 + materiais extras)
│   └── Questionarios/     (PNGs + os 2 .md de transcrição)
├── Modelos Provas Emuladas Anteriores/   (V16 Experiência Empreendedora = modelo base; v5 de outras disciplinas)
├── gerar_simulados.py
├── simulado_comunicacao_e_linguagem_U1-U4.html
├── simulado_direito_digital_U1-U4.html
└── REFERENCIA_ROTINA_SIMULADOS.md  (este arquivo)
```

## 3. Como funciona o gerador (`gerar_simulados.py`)
1. Lê os `.md` de transcrição de cada disciplina (`Questionarios/`).
2. Cada questão é um bloco `## Questão|Pergunta N`, com `**Enunciado:**`, `**Alternativas:**` e um bloco `>` de explicação.
3. Alternativas no formato `- [ ] A. ...`; a correta é `- [x] **B. ...** *(Correta)*`. Sufixos `*(...)*` são removidos.
4. A unidade de cada questão vem das listas em `DISCIPLINAS` (ordem = ordem das questões no `.md`).
5. Gera o HTML com o CSS e o JS baseados no modelo V16:
   - embaralha questões e alternativas a cada carregamento (F5), renumerando e reletrando;
   - badge colorido `UNIDADE N` que acompanha a questão (`data-unit`);
   - correção com feedback, explicação do gabarito e nota **por unidade**;
   - aprovação em 60% (arredondado para cima).
6. Regerar: `python3 gerar_simulados.py`.

### Mapeamento de unidades atual
| Disciplina | Arquivo | Unidades (Q1..Q6) | Origem |
|---|---|---|---|
| Comunicação | U1+U2 | 1, 2, 2, 1, 2, 1 | **Inferido pelo tema** (conferir) |
| Comunicação | U3+U4 | 4, 3, 4, 3, 3, 4 | E-book citado na transcrição |
| Direito Digital | U1+U2 | 2, 1, 1, 2, 2, 1 | E-book citado na transcrição |
| Direito Digital | U3+U4 | 3, 4, 4, 3, 3, 4 | E-book citado na transcrição |

## 4. Como replicar para uma nova disciplina
1. Criar `Disciplina/Questionarios/` com `questionario_u1_u2_transcricao.md` e `questionario_u3_u4_transcricao.md`, no formato da seção 3.
2. Incluir nas transcrições a **unidade/página do e-book** de cada questão. Assim o mapeamento deixa de ser inferido.
3. Adicionar uma entrada em `DISCIPLINAS` no script (nome, pasta, saída, arquivos + lista de unidades).
4. Rodar o script e abrir o HTML no navegador para testar.

## 5. Pendências conhecidas
- Só **12 questões por disciplina** (3 por unidade). Cobertura limitada para uma prova G2 de conteúdo completo.
- Unidade das questões de Comunicação U1+U2 é inferida; a Q5 (coerência) é a mais duvidosa (U2 ou U3).
- Questões 2 e 6 de Comunicação dependem de figuras, que estão apenas descritas em texto.
- Direito Digital ainda sem resumo/mapa mental (Comunicação já tem `resumo_e_mapa_mental_u1_a_u4.md`, a revisar).
- JavaScript dos HTML não foi testado em navegador (sem Node na máquina); só a estrutura foi conferida.

## 5b. Reações animadas (GIFs) — implementado em 2026-10-30
- Ao finalizar, cada questão mostra à direita um GIF aleatório: `Acertou_N.gif` (acerto) ou `Errou_N.gif` (erro ou em branco).
- Pasta esperada: `gifs/` ao lado dos HTML. Nomes: `Acertou_1..4.gif` e `Errou_1..4.gif`.
- Para mudar as quantidades, edite `QTD_GIFS` e `PASTA_GIFS` no JS dentro do `gerar_simulados.py` e regenere.
- Se o GIF não existir, aparece um emoji animado no lugar (pula no acerto, balança no erro).

## 6. Backlog / Ideias de melhoria (registrar aqui novas ideias)
- [ ] **Ampliar o banco de questões** (provas antigas, listas de exercícios, questões autorais por unidade a partir dos PDFs) para 8–10 por unidade.
- [ ] **Filtro por unidade** no simulado (botões "só U1", "só U3"...) para revisão direcionada.
- [ ] **Modo "revisar erros"**: refazer só as questões erradas na tentativa anterior (via `localStorage`).
- [ ] **Histórico de tentativas** salvo no navegador, com nota total e por unidade, para acompanhar a evolução até 05/11.
- [ ] **Cronômetro** opcional para simular o tempo da prova.
- [ ] **Embutir as figuras** das questões 2 e 6 de Comunicação (recortar dos PNGs sem revelar o gabarito).
- [ ] **Gerar o resumo e o mapa mental de Direito Digital** (Mermaid/MD) e revisar o de Comunicação.
- [ ] **Flashcards HTML** (conceitos e pegadinhas) a partir dos resumos.
- [ ] **Marcar pegadinhas** (por exemplo, as Q4 e Q5 de Direito U1+U2) com selo "⚠ pegadinha".
- [ ] **Checagem automática** no script (contar questões, validar a alternativa correta) e teste do JS com Node ou Playwright.
- [ ] **Script único de build** que gere todos os materiais (simulados, resumos, flashcards) de uma vez.
- [ ] Reaproveitar o gerador nas **próximas disciplinas/semestres**, extraindo as listas de unidades para um `config.json`.

## 7. Histórico
| Data | Alteração |
|---|---|
| 2026-10-30 | Reações animadas (GIF/emoji) por questão após a correção. |
| 2026-10-30 | Criado `gerar_simulados.py` e os simulados únicos U1–U4 de Comunicação e Direito Digital (12 questões cada, com badge de unidade, nota por unidade e explicação). |
