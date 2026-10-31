#!/usr/bin/env python3
"""Gera os simulados HTML com layout fiel ao Blackboard Ultra (AVA Unilasalle),
incluindo:
- Círculo roxo com número da questão
- Tag "MÚLTIPLA ESCOLHA"
- Badge verde "CORRETO" / vermelho "INCORRETO" pós-envio
- Pílula preta com pontuação "0,4 / 0,4"
- Alternativas em cinza claro com realce verde (#e3fcef) e tag "Resposta correta" à direita
- Prefixos "Correta:" dinâmicos na alternativa certa
- Barra superior do Blackboard Ultra com breadcrumb e "Nota final"
- Embaralhamento dinâmico a cada F5
- Reações animadas (GIFs e emojis)
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
        "codigo": "2026/2 - ENS1E0402E0012 - COMUNICAÇÃO E LINGUAGEM",
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
        "codigo": "2026/2 - ENS1E0402E0021 - DIREITO DIGITAL",
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
        "codigo": "2026/2 - ENS1E0402E0031 - REQUISITOS DE SOFTWARE",
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
        "codigo": "2026/2 - ENS1E0402E0041 - GERENCIAMENTO DE PROJETOS",
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
        ln_clean = ln.strip()
        if ln_clean in ("PORQUE", "**PORQUE**"):
            if buf:
                out.append("<br>".join(buf))
                buf = []
            out.append('<div class="porque-separator">PORQUE</div>')
            continue
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
        
        alt_indices = [i for i, l in enumerate(linhas) if re.match(r"^\s*-\s*\[( |x)\]", l)]
        assert len(alt_indices) >= 5, f"Alternativas insuficientes em {md_path}: {linhas[0]}"
        
        primeira_alt = alt_indices[0]
        ultima_alt = alt_indices[-1]
        
        enun_linhas = []
        fonte_info = ""
        for l in linhas[1:primeira_alt]:
            s = l.strip()
            if s.startswith("**Enunciado:**"):
                continue
            if s in ("**Alternativas:**", "Alternativas:"):
                continue
            if "Fonte:" in l or "Página" in l or "página" in l:
                fonte_info = l.strip().strip("*").strip("()").strip()
                continue
            enun_linhas.append(l)
        enunciado = paragrafos(enun_linhas)
        
        alts = []
        correta = None
        for j in range(primeira_alt, ultima_alt + 1):
            line = linhas[j]
            m = re.match(r"^\s*-\s*\[( |x)\]\s*(.*)", line)
            if not m:
                continue
            marcado = m.group(1) == "x"
            resto = m.group(2).strip()
            resto = re.sub(r"\s*\*\([^)]*\)\*\s*$", "", resto)
            resto = resto.strip("*").strip()
            resto = re.sub(r"^[A-E]\.\s*", "", resto)
            resto = resto.strip("*").strip()
            alts.append(resto)
            if marcado:
                correta = len(alts) - 1
        
        assert correta is not None and len(alts) == 5, f"Questão sem gabarito ou alternativa inválida em {md_path}: {linhas[0]}"
        
        expl_linhas = [l for l in linhas[ultima_alt + 1:] if l.strip().startswith(">")]
        explicacao = paragrafos(expl_linhas) if expl_linhas else ""
        
        questoes.append({
            "unidade": un,
            "enunciado": enunciado,
            "fonte": fonte_info,
            "alts": alts,
            "correta": correta,
            "explicacao": explicacao
        })
    return questoes

BLACKBOARD_CSS = """
        :root {
            --bb-bg: #eceff1;
            --bb-card-bg: #ffffff;
            --bb-border: #cfd8dc;
            --bb-purple: #8e24aa;
            --bb-purple-light: #f3e5f5;
            --bb-green: #00875a;
            --bb-green-bg: #e3fcef;
            --bb-green-border: #abf5d1;
            --bb-red: #de350b;
            --bb-red-bg: #ffebe6;
            --bb-red-border: #ffbdad;
            --bb-gray-dark: #212529;
            --bb-gray-med: #495057;
            --bb-gray-light: #f4f5f7;
            --bb-text: #172b4d;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bb-bg);
            color: var(--bb-text);
            line-height: 1.55;
            padding-bottom: 5rem;
            -webkit-font-smoothing: antialiased;
        }

        /* Top Navbar Blackboard Ultra */
        .bb-top-bar {
            background-color: #191919;
            color: #ffffff;
            padding: 0.65rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.85rem;
            border-bottom: 2px solid #2d2d2d;
        }

        .bb-top-left {
            display: flex;
            align-items: center;
            gap: 1.25rem;
        }

        .bb-back-link {
            color: #90caf9;
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            transition: color 0.2s;
        }

        .bb-back-link:hover {
            color: #ffffff;
            text-decoration: underline;
        }

        .bb-course-code {
            color: #b0bec5;
            font-weight: 500;
            letter-spacing: 0.3px;
        }

        .bb-user-profile {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #cfd8dc;
            font-weight: 500;
        }

        .bb-avatar-circle {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background-color: #37474f;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            color: #eceff1;
        }

        /* Banner de Nota Final (Estilo Print 5) */
        .bb-score-banner {
            background-color: #ffffff;
            border-bottom: 1px solid var(--bb-border);
            padding: 1rem 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
            margin-bottom: 1.5rem;
        }

        .bb-score-left {
            display: flex;
            align-items: center;
            gap: 0.85rem;
        }

        .bb-score-label {
            font-weight: 700;
            font-size: 1.05rem;
            color: var(--bb-gray-dark);
        }

        .bb-score-pill {
            background-color: var(--bb-gray-dark);
            color: #ffffff;
            font-weight: 700;
            font-size: 0.95rem;
            padding: 0.25rem 0.85rem;
            border-radius: 999px;
            letter-spacing: 0.5px;
        }

        .bb-score-right {
            text-align: right;
            font-size: 0.8rem;
            color: #607d8b;
        }

        .bb-score-right strong {
            color: var(--bb-gray-dark);
        }

        /* Main Container */
        .bb-container {
            max-width: 980px;
            margin: 0 auto;
            padding: 0 1.25rem;
        }

        .bb-alert-bar {
            background-color: #fff9db;
            border: 1px solid #ffe066;
            border-radius: 4px;
            padding: 0.85rem 1.25rem;
            margin-bottom: 1.5rem;
            font-size: 0.875rem;
            color: #664d03;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        /* Card da Questão Blackboard Ultra */
        .question-container {
            background-color: var(--bb-card-bg);
            border: 1px solid var(--bb-border);
            border-radius: 4px;
            padding: 1.5rem 1.75rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
            position: relative;
        }

        .q-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.15rem;
            padding-bottom: 0.75rem;
            border-bottom: 1px solid #f0f2f5;
        }

        .q-header-left {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            flex-wrap: wrap;
        }

        /* Círculo Roxo/Magenta do Número */
        .q-circle-number {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            border: 2px solid var(--bb-purple);
            color: var(--bb-purple);
            font-weight: 800;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            background: #ffffff;
        }

        .q-type-label {
            font-weight: 800;
            font-size: 0.8rem;
            color: #212529;
            letter-spacing: 0.6px;
            text-transform: uppercase;
        }

        /* Pílula de Status (Correto / Incorreto / Não respondido) */
        .status-pill-ava {
            font-size: 0.65rem;
            font-weight: 800;
            padding: 0.2rem 0.6rem;
            border-radius: 999px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: none;
        }

        .status-pill-ava.correto {
            display: inline-block;
            background-color: var(--bb-green);
            color: #ffffff;
        }

        .status-pill-ava.incorreto {
            display: inline-block;
            background-color: var(--bb-red);
            color: #ffffff;
        }

        .status-pill-ava.vazio {
            display: inline-block;
            background-color: #f59e0b;
            color: #ffffff;
        }

        /* Badge de Unidade */
        .unit-pill {
            font-size: 0.68rem;
            font-weight: 700;
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            letter-spacing: 0.4px;
        }

        .unit-1 { background-color: #e3f2fd; color: #1565c0; border: 1px solid #bbdefb; }
        .unit-2 { background-color: #e8f5e9; color: #2e7d32; border: 1px solid #c8e6c9; }
        .unit-3 { background-color: #fff3e0; color: #e65100; border: 1px solid #ffe0b2; }
        .unit-4 { background-color: #f3e5f5; color: #6a1b9a; border: 1px solid #e1bee7; }

        .q-header-right {
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        /* Pílula Preta com Pontuação */
        .q-score-badge {
            background-color: var(--bb-gray-dark);
            color: #ffffff;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.25rem 0.65rem;
            border-radius: 999px;
            letter-spacing: 0.4px;
        }

        .q-chevron {
            color: #78909c;
            font-size: 0.85rem;
            user-select: none;
        }

        /* Enunciado */
        .question-text {
            font-size: 0.95rem;
            line-height: 1.6;
            color: #212529;
            margin-bottom: 1.25rem;
            white-space: pre-line;
            word-break: break-word;
        }

        .fonte-tag {
            text-align: right;
            font-size: 0.8rem;
            color: #546e7a;
            font-weight: 600;
            margin-bottom: 1rem;
            font-style: italic;
        }

        .porque-separator {
            text-align: center;
            font-weight: 800;
            font-size: 0.95rem;
            color: #212529;
            letter-spacing: 2px;
            margin: 1.25rem 0;
            display: block;
        }

        /* Opções de Alternativas */
        .options {
            display: flex;
            flex-direction: column;
            gap: 0.45rem;
            margin-top: 1rem;
        }

        .option-row {
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            padding: 0.85rem 1rem;
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.15s ease;
            position: relative;
        }

        .option-row:hover {
            background-color: #f1f3f5;
            border-color: #dee2e6;
        }

        .option-left {
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            flex: 1;
        }

        .option-row input[type="radio"] {
            margin-top: 0.2rem;
            transform: scale(1.15);
            accent-color: #00875a;
            cursor: pointer;
            flex-shrink: 0;
        }

        .option-content {
            font-size: 0.925rem;
            color: #212529;
            line-height: 1.45;
            word-break: break-word;
        }

        .letter-prefix {
            font-weight: 700;
            color: #212529;
            margin-right: 0.35rem;
        }

        .correta-highlight {
            display: none;
            font-weight: 800;
            color: #006644;
            margin-right: 0.35rem;
        }

        .option-tag {
            font-size: 0.75rem;
            font-weight: 700;
            white-space: nowrap;
            margin-left: 0.75rem;
            display: none;
        }

        /* Estilos Pós-Correção (Fiel ao AVA Blackboard Ultra) */
        .option-row.is-correct-answer {
            background-color: var(--bb-green-bg) !important;
            border: 1px solid var(--bb-green-border) !important;
            color: #006644 !important;
        }

        .option-row.is-correct-answer .correta-highlight {
            display: inline;
        }

        .option-row.is-correct-answer .option-tag {
            display: inline;
            color: #006644;
        }

        .option-row.is-wrong-answer {
            background-color: var(--bb-red-bg) !important;
            border: 1px solid var(--bb-red-border) !important;
            color: #bf2600 !important;
        }

        .option-row.is-wrong-answer .option-tag {
            display: inline;
            color: #bf2600;
        }

        /* Comentários / Justificativa Oficial */
        .explicacao {
            display: none;
            margin-top: 1.25rem;
            padding: 1rem 1.25rem;
            background-color: var(--bb-gray-light);
            border-left: 4px solid var(--bb-green);
            border-radius: 0 4px 4px 0;
            font-size: 0.88rem;
            color: #172b4d;
            line-height: 1.6;
        }

        .explicacao b.expl-title {
            color: #00875a;
            display: block;
            margin-bottom: 0.4rem;
            font-size: 0.925rem;
        }

        /* Reação animada (GIF / Emoji) */
        .reacao {
            display: none;
            float: right;
            width: 140px;
            margin: 0 0 10px 15px;
            text-align: center;
        }

        .reacao img {
            width: 140px;
            max-height: 140px;
            object-fit: contain;
            border-radius: 6px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);
        }

        .reacao .emoji {
            font-size: 4em;
            line-height: 1;
            display: inline-block;
        }

        .reacao.acertou .emoji { animation: pula 0.8s ease-in-out infinite; }
        .reacao.errou .emoji { animation: balanca 0.6s ease-in-out 4; }

        @keyframes pula { 0%,100% { transform: translateY(0) scale(1); } 50% { transform: translateY(-12px) scale(1.15); } }
        @keyframes balanca { 0%,100% { transform: rotate(0); } 25% { transform: rotate(-10deg); } 75% { transform: rotate(10deg); } }

        /* Botão de Envio Blackboard Ultra */
        .btn-submit {
            display: block;
            width: 100%;
            padding: 16px;
            font-size: 1.1rem;
            font-weight: 700;
            color: #ffffff;
            background-color: var(--bb-green);
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.2s;
            margin-top: 2rem;
            box-shadow: 0 2px 4px rgba(0,135,90,0.25);
        }

        .btn-submit:hover {
            background-color: #006644;
        }

        /* Caixa de Resultado */
        .result-box {
            text-align: center;
            font-size: 1.35rem;
            font-weight: 700;
            margin-top: 2rem;
            padding: 1.75rem;
            border-radius: 4px;
            display: none;
            box-sizing: border-box;
        }

        .pass {
            background-color: #e3fcef;
            color: #006644;
            border: 1px solid #abf5d1;
        }

        .fail {
            background-color: #fff9db;
            color: #856404;
            border: 1px solid #ffe066;
        }

        .by-unit {
            font-size: 0.65em;
            font-weight: 500;
            color: #495057;
            margin-top: 0.85rem;
        }

        .btn-retry {
            display: inline-block;
            margin-top: 1.25rem;
            padding: 0.65rem 1.25rem;
            font-size: 0.85rem;
            font-weight: 700;
            color: #ffffff;
            background-color: var(--bb-gray-dark);
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
        }

        .btn-retry:hover {
            background-color: #343a40;
        }

        @media (max-width: 600px) {
            .bb-top-bar { padding: 0.65rem 1rem; flex-direction: column; gap: 0.5rem; align-items: flex-start; }
            .bb-score-banner { padding: 0.85rem 1rem; flex-direction: column; gap: 0.5rem; align-items: flex-start; }
            .reacao { float: none; margin: 10px auto; }
            .question-container { padding: 1.15rem; }
        }
"""

BLACKBOARD_JS = """
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

        // Embaralhamento inicial (F5)
        (function() {
            const form = document.getElementById('quizForm');
            const submitBtn = document.querySelector('.btn-submit');

            // 1. Embaralha as perguntas mantendo seus atributos e etiquetas
            const questions = Array.from(document.querySelectorAll('.question-container'));
            for (let i = questions.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [questions[i], questions[j]] = [questions[j], questions[i]];
            }

            // 2. Renumera o círculo roxo e reatribui radio names
            questions.forEach((q, index) => {
                const newNum = index + 1;
                const newId = 'q' + newNum;
                q.id = newId;

                const circleNum = q.querySelector('.q-circle-number');
                if (circleNum) circleNum.innerText = newNum;

                q.querySelectorAll('input[type="radio"]').forEach(r => {
                    r.name = newId;
                    r.checked = false;
                });

                form.insertBefore(q, submitBtn);

                // 3. Embaralha as alternativas de cada pergunta
                const optionsDiv = q.querySelector('.options');
                if (optionsDiv) {
                    const labels = Array.from(optionsDiv.querySelectorAll('.option-row'));
                    const letters = ['A', 'B', 'C', 'D', 'E'];
                    for (let i = labels.length - 1; i > 0; i--) {
                        const j = Math.floor(Math.random() * (i + 1));
                        [labels[i], labels[j]] = [labels[j], labels[i]];
                    }
                    optionsDiv.innerHTML = '';
                    labels.forEach((label, idx) => {
                        const prefix = label.querySelector('.letter-prefix');
                        if (prefix) prefix.innerText = letters[idx] + '. ';
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

            // Limpa estilos anteriores
            document.querySelectorAll('.option-row').forEach(l => {
                l.classList.remove('is-correct-answer', 'is-wrong-answer');
            });
            document.querySelectorAll('.status-pill-ava').forEach(sp => {
                sp.className = 'status-pill-ava';
                sp.style.display = 'none';
            });

            for (let i = 1; i <= TOTAL; i++) {
                const q = document.getElementById('q' + i);
                const unidade = q.getAttribute('data-unit');
                porUnidade[unidade] = porUnidade[unidade] || { ok: 0, total: 0 };
                porUnidade[unidade].total++;

                const statusPill = q.querySelector('.status-pill-ava');
                const scoreBadge = q.querySelector('.q-score-badge');
                const options = document.getElementsByName('q' + i);

                let respondeu = false;
                let acertou = false;

                for (const option of options) {
                    const label = option.closest('.option-row');
                    const isCorrect = label.getAttribute('data-correct') === 'true';

                    if (option.checked) {
                        respondeu = true;
                        if (isCorrect) {
                            acertou = true;
                            label.classList.add('is-correct-answer');
                        } else {
                            label.classList.add('is-wrong-answer');
                            const tag = label.querySelector('.option-tag');
                            if (tag) {
                                tag.innerText = 'Sua resposta (Incorreta)';
                                tag.style.display = 'inline';
                            }
                        }
                    }

                    if (isCorrect) {
                        label.classList.add('is-correct-answer');
                        const tag = label.querySelector('.option-tag');
                        if (tag) {
                            tag.innerText = 'Resposta correta';
                            tag.style.display = 'inline';
                        }
                    }
                }

                if (acertou) {
                    acertos++;
                    porUnidade[unidade].ok++;
                    if (statusPill) {
                        statusPill.innerText = 'CORRETO';
                        statusPill.className = 'status-pill-ava correto';
                    }
                    if (scoreBadge) scoreBadge.innerText = '0,4 / 0,4';
                } else if (respondeu) {
                    if (statusPill) {
                        statusPill.innerText = 'INCORRETO';
                        statusPill.className = 'status-pill-ava incorreto';
                    }
                    if (scoreBadge) scoreBadge.innerText = '0,0 / 0,4';
                } else {
                    if (statusPill) {
                        statusPill.innerText = 'NÃO RESPONDIDO';
                        statusPill.className = 'status-pill-ava vazio';
                    }
                    if (scoreBadge) scoreBadge.innerText = '0,0 / 0,4';
                }

                mostrarReacao(q, acertou);

                // Exibe justificativa
                const ex = q.querySelector('.explicacao');
                if (ex) ex.style.display = 'block';
            }

            // Atualiza nota no Banner Superior (estilo Print 5)
            const notaEscala10 = ((acertos / TOTAL) * 10).toFixed(1).replace('.', ',');
            const headerPill = document.getElementById('header-score-pill');
            if (headerPill) headerPill.innerText = notaEscala10 + ' / 10,0';

            const headerSub = document.getElementById('header-score-sub');
            if (headerSub) {
                const now = new Date();
                const horaStr = now.toLocaleDateString('pt-BR') + ' ' + now.toLocaleTimeString('pt-BR', {hour: '2-digit', minute:'2-digit'});
                headerSub.innerHTML = '<strong>ENVIADO:</strong> ' + horaStr + ' (BRT)';
            }

            // Exibe caixa de resultado final
            const resultBox = document.getElementById('resultado');
            resultBox.style.display = 'block';
            const aproveitamento = ((acertos / TOTAL) * 100).toFixed(0);
            const detalhe = Object.keys(porUnidade).sort().map(u => `Unidade ${u}: ${porUnidade[u].ok}/${porUnidade[u].total}`).join(' &nbsp;|&nbsp; ');

            resultBox.innerHTML = `
                <div>Você acertou <strong>${acertos}</strong> de <strong>${TOTAL}</strong> questões! (Nota: <strong>${notaEscala10}</strong>)</div>
                <div style="font-size: 0.85em; font-weight: normal; margin-top: 4px;">Aproveitamento Total: ${aproveitamento}%</div>
                <div class="by-unit">${detalhe}</div>
                <button type="button" class="btn-retry" onclick="window.location.reload()">🔄 Refazer Simulado (Embaralhar Novamente)</button>
            `;
            resultBox.className = 'result-box ' + (acertos >= MIN_APROVACAO ? 'pass' : 'fail');
            resultBox.scrollIntoView({ behavior: 'smooth' });
        }
"""

def gerar_simulado_blackboard(disc):
    questoes = []
    for arq_path, unidades in disc["arquivos"]:
        questoes += parse_markdown_questions(arq_path, unidades)

    total = len(questoes)
    minimo = -(-total * 60 // 100)  # 60% aprovação arredondada para cima
    corpo = []
    
    for n, q in enumerate(questoes, 1):
        alts_html = []
        for k, a in enumerate(q["alts"]):
            is_correta = k == q["correta"]
            alts_html.append(
                f'                <label class="option-row" data-correct="{"true" if is_correta else "false"}">\n'
                f'                    <div class="option-left">\n'
                f'                        <input type="radio" name="q{n}" value="">\n'
                f'                        <div class="option-content">\n'
                f'                            <span class="letter-prefix"></span>\n'
                f'                            <span class="correta-highlight">Correta:</span>\n'
                f'                            <span class="option-text">{inline(a)}</span>\n'
                f'                        </div>\n'
                f'                    </div>\n'
                f'                    <span class="option-tag"></span>\n'
                f'                </label>'
            )
        
        fonte_div = f'            <div class="fonte-tag">Fonte: {q["fonte"]}</div>\n' if q["fonte"] else ""
        expl_div = (f'            <div class="explicacao">\n'
                    f'                <b class="expl-title">💬 Fundamentação Oficial no E-book:</b>\n'
                    f'                <div>{q["explicacao"]}</div>\n'
                    f'            </div>\n' if q["explicacao"] else "")

        corpo.append(
            f'        <div class="question-container" id="q{n}" data-unit="{q["unidade"]}">\n'
            f'            <div class="q-header">\n'
            f'                <div class="q-header-left">\n'
            f'                    <div class="q-circle-number">{n}</div>\n'
            f'                    <span class="q-type-label">MÚLTIPLA ESCOLHA</span>\n'
            f'                    <span class="status-pill-ava"></span>\n'
            f'                    <span class="unit-pill unit-{q["unidade"]}">UNIDADE {q["unidade"]}</span>\n'
            f'                </div>\n'
            f'                <div class="q-header-right">\n'
            f'                    <span class="q-score-badge">0,4 / 0,4</span>\n'
            f'                    <span class="q-chevron">▲</span>\n'
            f'                </div>\n'
            f'            </div>\n'
            f'            <div class="question-text">{q["enunciado"]}</div>\n'
            f'{fonte_div}'
            f'            <div class="options">\n' + "\n".join(alts_html) + '\n            </div>\n'
            f'{expl_div}'
            f'        </div>\n'
        )

    js = BLACKBOARD_JS.replace("__TOTAL__", str(total)).replace("__MIN__", str(minimo)).replace("__GIFS__", json.dumps(gifs_embutidos())).replace("__ACERTOU__", json.dumps(GIFS_ACERTOU)).replace("__ERROU__", json.dumps(GIFS_ERROU))
    
    doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Avaliação: {disc["nome"]} — Blackboard Ultra (Simulado ADS)</title>
    <style>{BLACKBOARD_CSS}    </style>
</head>
<body>

    <!-- Barra Superior Blackboard Ultra -->
    <header class="bb-top-bar">
        <div class="bb-top-left">
            <a href="index.html" class="bb-back-link">← Voltar ao Portal ADS 2026.2</a>
            <span class="bb-course-code">{disc["codigo"]}</span>
        </div>
        <div class="bb-user-profile">
            <div class="bb-avatar-circle">👤</div>
            <span>Anderson (ADS 7º Semestre)</span>
        </div>
    </header>

    <!-- Banner de Nota Final (Fiel ao Blackboard Ultra) -->
    <div class="bb-score-banner">
        <div class="bb-score-left">
            <span class="bb-score-label">Nota final</span>
            <span class="bb-score-pill" id="header-score-pill">-- / 10,0</span>
        </div>
        <div class="bb-score-right" id="header-score-sub">
            <span>Questionário Oficial U1-U4 • <strong>12 Questões</strong></span>
        </div>
    </div>

    <main class="bb-container">
        <!-- Aviso de Embaralhamento -->
        <div class="bb-alert-bar">
            <span>🔄 <strong>Modo Simulado Ativo:</strong> A cada carregamento (<strong>F5</strong>), as questões e alternativas mudam de posição como no exame real.</span>
            <span style="font-size: 0.8em; color: #856404; font-weight: 700;">Simulado G2 Presencial</span>
        </div>

        <form id="quizForm">

{"".join(corpo)}
            <button type="button" class="btn-submit" onclick="calcularNota()">Finalizar e Enviar Questionário ({total} Questões)</button>

            <div id="resultado" class="result-box"></div>
        </form>
    </main>

    <script>{js}    </script>
</body>
</html>
"""
    # Salva na raiz
    saida_raiz = BASE / disc["saida_raiz"]
    saida_raiz.write_text(doc, encoding="utf-8")
    print(f"✓ Gerado (Estilo Blackboard Ultra): {saida_raiz.name}")

    # Salva cópia na pasta respectiva
    saida_copia = BASE / disc["copia_pasta"]
    saida_copia.write_text(doc, encoding="utf-8")
    print(f"✓ Cópia atualizada em: {saida_copia}")

if __name__ == "__main__":
    print("Atualizando todos os simulados para o layout Blackboard Ultra da faculdade...")
    for d in DISCIPLINAS:
        gerar_simulado_blackboard(d)
    print("\nTodos os simulados foram atualizados com sucesso no layout do Blackboard Ultra!")
