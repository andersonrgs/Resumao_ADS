#!/usr/bin/env python3
"""Gera os simulados HTML unicos (U1-U4) para as 4 disciplinas finais de ADS:
1. Comunicação e Linguagem
2. Direito Digital
3. Requisitos de Software
4. Gerenciamento de Projetos

Layout, lógica e embaralhamento baseados no modelo V16 com reações animadas.
"""
import base64
import html
import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent

# Configuração de GIFs
EMBUTIR_GIFS = False
GIFS_ACERTOU = ["Acertou_7.gif"]
GIFS_ERROU = ["Errou_7.gif"]

def gifs_embutidos():
    mapa = {}
    if EMBUTIR_GIFS:
        for f in sorted((BASE / "gifs" / n for n in GIFS_ACERTOU + GIFS_ERROU)):
            if f.exists():
                mapa[f.name] = "data:image/gif;base64," + base64.b64encode(f.read_bytes()).decode()
    return mapa

DISCIPLINAS = [
    {
        "id": "comunicacao",
        "nome": "Comunicação e Linguagem",
        "saida_raiz": "simulado_comunicacao_e_linguagem_U1-U4.html",
        "copia_pasta": "prova_05062026 -Direito + comunicação/simulado_comunicacao_e_linguagem_U1-U4.html",
        "arquivos": [
            (BASE / "prova_05062026 -Direito + comunicação" / "Comunicação e linguagem" / "Questionarios" / "questionario_u1_u2_transcricao.md", [1, 2, 2, 1, 2, 1]),
            (BASE / "prova_05062026 -Direito + comunicação" / "Comunicação e linguagem" / "Questionarios" / "questionario_u3_u4_transcricao.md", [4, 3, 4, 3, 3, 4]),
        ],
    },
    {
        "id": "direito",
        "nome": "Direito Digital",
        "saida_raiz": "simulado_direito_digital_U1-U4.html",
        "copia_pasta": "prova_05062026 -Direito + comunicação/simulado_direito_digital_U1-U4.html",
        "arquivos": [
            (BASE / "prova_05062026 -Direito + comunicação" / "Direito digital" / "Questionarios" / "questionario_u1_u2_transcricao.md", [2, 1, 1, 2, 2, 1]),
            (BASE / "prova_05062026 -Direito + comunicação" / "Direito digital" / "Questionarios" / "questionario_u3_u4_transcricao.md", [3, 4, 4, 3, 3, 4]),
        ],
    },
    {
        "id": "requisitos",
        "nome": "Requisitos de Software",
        "saida_raiz": "simulado_requisitos_de_software_U1-U4.html",
        "copia_pasta": "Provas_12112026 - Requisitos + Gerenciamento/simulado_requisitos_de_software_U1-U4.html",
        "arquivos": [
            (BASE / "Provas_12112026 - Requisitos + Gerenciamento" / "Requisitos de software" / "Questionarios" / "questionario_u1_u2_transcricao.md", [1, 1, 2, 1, 1, 2]),
            (BASE / "Provas_12112026 - Requisitos + Gerenciamento" / "Requisitos de software" / "Questionarios" / "questionario_u3_u4_transcricao.md", [3, 4, 4, 4, 3, 3]),
        ],
    },
    {
        "id": "gerenciamento",
        "nome": "Gerenciamento de Projetos",
        "saida_raiz": "simulado_gerenciamento_de_projetos_U1-U4.html",
        "copia_pasta": "Provas_12112026 - Requisitos + Gerenciamento/simulado_gerenciamento_de_projetos_U1-U4.html",
        "arquivos": [
            (BASE / "Provas_12112026 - Requisitos + Gerenciamento" / "Gerenciamento de Projetos" / "Questinarios" / "questionario_u1_u2_transcricao.md", [2, 2, 1, 2, 1, 1]),
            (BASE / "Provas_12112026 - Requisitos + Gerenciamento" / "Gerenciamento de Projetos" / "Questinarios" / "questionario_u3_u4_transcricao.md", [3, 3, 4, 3, 4, 3]),
        ],
    },
]

def inline(txt):
    t = html.escape(txt, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return t

def paragrafos(linhas):
    out, buf = [], []
    for ln in linhas:
        ln = re.sub(r"^\s*>\s?", "", ln).rstrip()
        if ln.strip() in ("", ">"):
            if buf:
                out.append("<br>".join(buf))
                buf = []
        else:
            buf.append(inline(ln.strip()))
    if buf:
        out.append("<br>".join(buf))
    return "<br><br>".join(out)

def parse_markdown_questions(md_path, unidades):
    txt = md_path.read_text(encoding="utf-8")
    blocos = re.split(r"\n(?=#{2,3} (?:Quest[aã]o|Pergunta) \d+)", txt)[1:]
    assert len(blocos) == len(unidades), f"Erro no arquivo {md_path}: esperava {len(unidades)} questões, encontrou {len(blocos)}"
    
    questoes = []
    for bloco, un in zip(blocos, unidades):
        linhas = bloco.splitlines()
        
        # Localiza índices de alternativas
        alt_indices = [i for i, l in enumerate(linhas) if re.match(r"^\s*-\s*\[( |x)\]", l)]
        assert len(alt_indices) >= 5, f"Alternativas insuficientes em {md_path}: {linhas[0]}"
        
        primeira_alt = alt_indices[0]
        ultima_alt = alt_indices[-1]
        
        # Enunciado: do cabeçalho até a primeira alternativa
        enun_linhas = []
        for l in linhas[1:primeira_alt]:
            if l.strip().startswith("**Enunciado:**"):
                continue
            enun_linhas.append(l)
        enunciado = paragrafos(enun_linhas)
        
        # Alternativas
        alts = []
        correta = None
        for j in range(primeira_alt, ultima_alt + 1):
            line = linhas[j]
            m = re.match(r"^\s*-\s*\[( |x)\]\s*(.*)", line)
            if not m:
                continue
            marcado = m.group(1) == "x"
            resto = m.group(2).strip()
            # Remove sufixos como *(Resposta Correta)* ou *(Correta)*
            resto = re.sub(r"\s*\*\([^)]*\)\*\s*$", "", resto)
            resto = resto.strip("*").strip()
            resto = re.sub(r"^[A-E]\.\s*", "", resto)
            resto = resto.strip("*").strip()
            alts.append(resto)
            if marcado:
                correta = len(alts) - 1
        
        assert correta is not None and len(alts) == 5, f"Questão sem gabarito ou alternativa inválida em {md_path}: {linhas[0]}"
        
        # Explicação / Justificativa
        expl_linhas = [l for l in linhas[ultima_alt + 1:] if l.strip().startswith(">")]
        explicacao = paragrafos(expl_linhas) if expl_linhas else ""
        
        questoes.append({
            "unidade": un,
            "enunciado": enunciado,
            "alts": alts,
            "correta": correta,
            "explicacao": explicacao
        })
    return questoes

CSS = """
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; line-height: 1.6; }
        .top-nav { display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; padding-bottom: 12px; border-bottom: 1px solid #ddd; }
        .top-nav a { text-decoration: none; color: #2980b9; font-weight: bold; font-size: 0.95em; }
        .top-nav a:hover { text-decoration: underline; }
        h1 { text-align: center; color: #2c3e50; margin-bottom: 5px; font-size: 2em; }
        p.subtitle { text-align: center; color: #7f8c8d; margin-bottom: 20px; font-weight: bold; }
        .question-container { background-color: #fff; border-radius: 8px; padding: 25px; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); box-sizing: border-box; position: relative; }
        .unit-badge { display: inline-block; font-size: 0.8em; font-weight: bold; color: #fff; padding: 3px 12px; border-radius: 12px; margin-bottom: 10px; letter-spacing: 0.5px; }
        .unit-1 { background-color: #2980b9; } .unit-2 { background-color: #27ae60; }
        .unit-3 { background-color: #e67e22; } .unit-4 { background-color: #8e44ad; }
        .question-text { font-size: 1.1em; font-weight: bold; margin-bottom: 15px; color: #2c3e50; white-space: pre-line; word-break: break-word; }
        .options { margin-top: 15px; clear: none; }
        .options label { display: flex; align-items: flex-start; padding: 12px; margin-bottom: 10px; background-color: #f8f9fa; border: 1px solid #ddd; border-radius: 5px; cursor: pointer; transition: all 0.3s ease; box-sizing: border-box; }
        .options label:hover { background-color: #e9ecef; border-color: #b1bccc; }
        .options input[type="radio"] { margin-top: 4px; margin-right: 12px; transform: scale(1.2); flex-shrink: 0; }
        .options label span { word-break: break-word; }
        .letter-prefix { font-weight: bold; margin-right: 5px; color: #2c3e50; flex-shrink: 0; }
        .btn-submit { display: block; width: 100%; padding: 18px; font-size: 1.2em; font-weight: bold; color: #fff; background-color: #27ae60; border: none; border-radius: 8px; cursor: pointer; transition: background-color 0.3s; margin-top: 30px; box-shadow: 0 4px 6px rgba(39,174,96,0.2); }
        .btn-submit:hover { background-color: #219653; }
        .result-box { text-align: center; font-size: 1.5em; font-weight: bold; margin-top: 30px; padding: 30px; border-radius: 8px; display: none; box-sizing: border-box; }
        .pass { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .fail { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }
        .by-unit { font-size: 0.6em; font-weight: normal; color: #444; margin-top: 12px; }
        .correct-answer { background-color: #e6ffec !important; border-color: #4ac26b !important; font-weight: bold; color: #1e7e34; }
        .wrong-answer { background-color: #ffeef0 !important; border-color: #fdaeb7 !important; color: #cb2431; }
        .feedback { display: none; margin-top: 10px; font-size: 0.9em; font-weight: bold; padding: 10px; border-radius: 5px; box-sizing: border-box; }
        .feedback.correct { display: block; color: #155724; background-color: #d4edda; border: 1px solid #c3e6cb; }
        .feedback.incorrect { display: block; color: #721c24; background-color: #f8d7da; border: 1px solid #f5c6cb; }
        .explicacao { display: none; margin-top: 10px; font-size: 0.9em; padding: 10px 14px; border-left: 4px solid #b1bccc; background: #f8f9fa; color: #444; }
        .reacao { display: none; float: right; width: 150px; margin: 0 0 10px 15px; text-align: center; }
        .reacao img { width: 150px; max-height: 150px; object-fit: contain; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.2); }
        .reacao .emoji { font-size: 4.5em; line-height: 1.1; display: inline-block; }
        .reacao.acertou .emoji { animation: pula 0.8s ease-in-out infinite; }
        .reacao.errou .emoji { animation: balanca 0.6s ease-in-out 4; }
        @keyframes pula { 0%,100% { transform: translateY(0) scale(1); } 50% { transform: translateY(-14px) scale(1.15); } }
        @keyframes balanca { 0%,100% { transform: rotate(0); } 25% { transform: rotate(-12deg); } 75% { transform: rotate(12deg); } }
        .shuffle-note { text-align: center; font-size: 0.9em; color: #e36209; background: #fff8c5; padding: 10px; border-radius: 5px; margin-bottom: 20px;}
        @media (max-width: 600px) { .reacao { float: none; margin: 10px auto; } }
        @media (max-width: 768px) {
            .question-container { padding: 15px; }
            .btn-submit { padding: 15px; font-size: 1.1em; }
        }
"""

JS = """
        const TOTAL = __TOTAL__;
        const MIN_APROVACAO = __MIN__;
        const PASTA_GIFS = 'gifs/';
        const GIFS_EMBUTIDOS = __GIFS__;
        const LISTA_GIFS = { acertou: __ACERTOU__, errou: __ERROU__ };

        function mostrarReacao(q, acertou) {
            const tipo = acertou ? 'acertou' : 'errou';
            let box = q.querySelector('.reacao');
            if (!box) {
                box = document.createElement('div');
                q.insertBefore(box, q.querySelector('.question-text'));
            }
            const lista = LISTA_GIFS[tipo];
            const nome = lista[Math.floor(Math.random() * lista.length)];
            const emojis = acertou ? ['🎉','🥳','😄','👏'] : ['😢','😞','🤦','😵'];
            box.className = 'reacao ' + tipo;
            box.style.display = 'block';
            box.innerHTML = '';
            const img = document.createElement('img');
            img.alt = acertou ? 'Acertou!' : 'Errou';
            img.onerror = () => {
                box.innerHTML = '<span class="emoji">' + emojis[Math.floor(Math.random() * emojis.length)] + '</span>';
            };
            img.src = GIFS_EMBUTIDOS[nome] || (PASTA_GIFS + nome);
            box.appendChild(img);
        }

        // Embaralhamento inicial ao carregar (F5)
        (function() {
            const form = document.getElementById('quizForm');
            const submitBtn = document.querySelector('.btn-submit');

            // 1. Embaralha as questoes (etiqueta de unidade acompanha cada questao)
            const questions = Array.from(document.querySelectorAll('.question-container'));
            for (let i = questions.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [questions[i], questions[j]] = [questions[j], questions[i]];
            }

            // 2. Renumera e reinsere no DOM
            questions.forEach((q, index) => {
                const newNum = index + 1;
                const newId = 'q' + newNum;
                q.id = newId;
                q.querySelectorAll('input[type="radio"]').forEach(r => { r.name = newId; r.checked = false; });
                const qText = q.querySelector('.question-text');
                if (qText) qText.innerHTML = qText.innerHTML.replace(/^\\s*\\d+\\.\\s*/, newNum + '. ');
                form.insertBefore(q, submitBtn);

                // 3. Embaralha as alternativas e reatribui as letras A, B, C, D, E
                const optionsDiv = q.querySelector('.options');
                if (optionsDiv) {
                    const labels = Array.from(optionsDiv.querySelectorAll('label'));
                    const letters = ['A', 'B', 'C', 'D', 'E'];
                    for (let i = labels.length - 1; i > 0; i--) {
                        const j = Math.floor(Math.random() * (i + 1));
                        [labels[i], labels[j]] = [labels[j], labels[i]];
                    }
                    optionsDiv.innerHTML = '';
                    labels.forEach((label, idx) => {
                        const prefix = label.querySelector('.letter-prefix');
                        if (prefix) prefix.innerText = letters[idx] + ') ';
                        const input = label.querySelector('input');
                        if (input) input.value = letters[idx];
                        optionsDiv.appendChild(label);
                    });
                }
            });
        })();

        function calcularNota() {
            let acertos = 0;
            const porUnidade = {};

            document.querySelectorAll('.options label').forEach(l => l.classList.remove('correct-answer', 'wrong-answer'));
            document.querySelectorAll('.feedback').forEach(fb => { fb.classList.remove('correct', 'incorrect'); fb.style.display = 'none'; fb.innerHTML = ''; });

            for (let i = 1; i <= TOTAL; i++) {
                const q = document.getElementById('q' + i);
                const unidade = q.getAttribute('data-unit');
                porUnidade[unidade] = porUnidade[unidade] || { ok: 0, total: 0 };
                porUnidade[unidade].total++;

                const options = document.getElementsByName('q' + i);
                const feedbackDiv = q.querySelector('.feedback');
                let respondeu = false, acertou = false;

                for (const option of options) {
                    const label = option.closest('label');
                    const isCorrect = label.getAttribute('data-correct') === 'true';
                    if (option.checked) {
                        respondeu = true;
                        if (isCorrect) {
                            acertou = true;
                            label.classList.add('correct-answer');
                            feedbackDiv.innerHTML = '✔ Resposta Correta!';
                            feedbackDiv.classList.add('correct');
                        } else {
                            label.classList.add('wrong-answer');
                            const cl = label.parentElement.querySelector('label[data-correct="true"]');
                            const letra = cl ? cl.querySelector('input').value : '?';
                            feedbackDiv.innerHTML = `✖ Resposta Incorreta. A alternativa correta é a ${letra}.`;
                            feedbackDiv.classList.add('incorrect');
                        }
                    }
                    if (isCorrect) label.classList.add('correct-answer');
                }
                if (acertou) { acertos++; porUnidade[unidade].ok++; }
                mostrarReacao(q, acertou);
                if (!respondeu) {
                    feedbackDiv.innerHTML = '⚠ Questão não respondida.';
                    feedbackDiv.classList.add('incorrect');
                }
                feedbackDiv.style.display = 'block';
                const ex = q.querySelector('.explicacao');
                if (ex) ex.style.display = 'block';
            }

            const resultBox = document.getElementById('resultado');
            resultBox.style.display = 'block';
            const aproveitamento = ((acertos / TOTAL) * 100).toFixed(0);
            const detalhe = Object.keys(porUnidade).sort().map(u => `Unidade ${u}: ${porUnidade[u].ok}/${porUnidade[u].total}`).join(' &nbsp;|&nbsp; ');
            resultBox.innerHTML = `Você acertou ${acertos} de ${TOTAL} questões!<br><span style="font-size: 0.8em; color: #7f8c8d; font-weight: normal;">Aproveitamento: ${aproveitamento}%</span><div class="by-unit">${detalhe}</div>`;
            resultBox.className = 'result-box ' + (acertos >= MIN_APROVACAO ? 'pass' : 'fail');
            resultBox.scrollIntoView({ behavior: 'smooth' });
        }
"""

def gerar_simulado(disc):
    questoes = []
    for arq_path, unidades in disc["arquivos"]:
        questoes += parse_markdown_questions(arq_path, unidades)

    total = len(questoes)
    minimo = -(-total * 60 // 100)  # 60% aprovação arredondada para cima
    corpo = []
    
    for n, q in enumerate(questoes, 1):
        alts = "\n".join(
            f'                <label{" data-correct=\"true\"" if k == q["correta"] else ""}>'
            f'<input type="radio" name="q{n}"><span class="letter-prefix"></span>'
            f'<span>{inline(a)}</span></label>'
            for k, a in enumerate(q["alts"])
        )
        expl = (f'            <div class="explicacao"><b>Justificativa / Gabarito Comentado:</b><br>{q["explicacao"]}</div>\n'
                if q["explicacao"] else "")
        corpo.append(
            f'        <div class="question-container" id="q{n}" data-unit="{q["unidade"]}">\n'
            f'            <span class="unit-badge unit-{q["unidade"]}">UNIDADE {q["unidade"]}</span>\n'
            f'            <div class="question-text">{n}. {q["enunciado"]}</div>\n'
            f'            <div class="options">\n{alts}\n            </div>\n'
            f'            <div class="feedback"></div>\n{expl}'
            f'        </div>\n'
        )

    js = JS.replace("__TOTAL__", str(total)).replace("__MIN__", str(minimo)).replace("__GIFS__", json.dumps(gifs_embutidos())).replace("__ACERTOU__", json.dumps(GIFS_ACERTOU)).replace("__ERROU__", json.dumps(GIFS_ERROU))
    doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulado Completo ({total} Questões) — {disc["nome"]}</title>
    <style>{CSS}    </style>
</head>
<body>

    <div class="top-nav">
        <a href="index.html">← Voltar ao Portal ADS 2026.2</a>
        <span style="font-size:0.85em; color:#7f8c8d;">ADS • 7º Semestre</span>
    </div>

    <h1>Simulado: {disc["nome"]}</h1>
    <p class="subtitle">Unidades 1 a 4 — Mix Completo ({total} Questões de Prova)</p>
    <div class="shuffle-note">🔄 <b>Embaralhamento Ativo:</b> Pressione <b>F5</b> para embaralhar novamente tanto as perguntas quanto as alternativas (A, B, C, D, E). A etiqueta colorida indica a unidade de cada questão.</div>

    <form id="quizForm">

{"".join(corpo)}
        <button type="button" class="btn-submit" onclick="calcularNota()">Finalizar Simulado Completo ({total} Questões)</button>

        <div id="resultado" class="result-box"></div>
    </form>

    <script>{js}    </script>
</body>
</html>
"""
    # Salva na raiz
    saida_raiz = BASE / disc["saida_raiz"]
    saida_raiz.write_text(doc, encoding="utf-8")
    print(f"✓ Gerado na raiz: {saida_raiz.name} ({total} questões)")

    # Salva cópia na pasta respectiva
    saida_copia = BASE / disc["copia_pasta"]
    saida_copia.write_text(doc, encoding="utf-8")
    print(f"✓ Cópia gerada em: {saida_copia}")

if __name__ == "__main__":
    print("Iniciando geração de simulados para as 4 disciplinas...")
    for d in DISCIPLINAS:
        gerar_simulado(d)
    print("\nTodos os simulados foram gerados com sucesso!")
