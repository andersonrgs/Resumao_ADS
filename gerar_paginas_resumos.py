#!/usr/bin/env python3
"""Gera as páginas HTML de resumos completos e mapas mentais para as 4 disciplinas finais de ADS."""

import markdown
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent

STYLE_HEADER = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Resumo ADS 2026.2</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <style>
        :root {{
            --bg: #0b0f19;
            --surface: #111827;
            --surface-elevated: #1f2937;
            --border: #374151;
            --border-subtle: #1f2937;
            --text: #f3f4f6;
            --text-muted: #9ca3af;
            --text-dim: #6b7280;
            --primary: #3b82f6;
            --primary-hover: #2563eb;
            --primary-light: rgba(59, 130, 246, 0.15);
            --accent: #8b5cf6;
            --accent-light: rgba(139, 92, 246, 0.15);
            --success: #10b981;
            --success-light: rgba(16, 185, 129, 0.15);
            --warning: #f59e0b;
            --warning-light: rgba(245, 158, 11, 0.15);
            --danger: #ef4444;
            --radius: 12px;
            --shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.7;
            padding-bottom: 5rem;
            -webkit-font-smoothing: antialiased;
        }}

        .top-nav {{
            position: sticky;
            top: 0;
            z-index: 50;
            backdrop-filter: blur(12px);
            background-color: rgba(11, 15, 25, 0.85);
            border-bottom: 1px solid var(--border);
            padding: 0.85rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}

        .nav-brand {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            text-decoration: none;
            color: var(--text);
            font-weight: 700;
            font-size: 1rem;
        }}

        .nav-brand .badge {{
            background: var(--primary-light);
            color: #60a5fa;
            border: 1px solid rgba(96, 165, 250, 0.3);
            font-size: 0.75rem;
            padding: 0.2rem 0.5rem;
            border-radius: 999px;
            font-weight: 600;
        }}

        .nav-actions {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}

        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            font-size: 0.875rem;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            transition: all 0.2s ease;
            border: 1px solid transparent;
        }}

        .btn-primary {{
            background: linear-gradient(135deg, #2563eb, #1d4ed8);
            color: #fff;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }}

        .btn-primary:hover {{
            background: linear-gradient(135deg, #1d4ed8, #1e40af);
            transform: translateY(-1px);
        }}

        .btn-secondary {{
            background: var(--surface-elevated);
            color: var(--text);
            border-color: var(--border);
        }}

        .btn-secondary:hover {{
            background: #374151;
            color: #fff;
        }}

        .container {{
            max-width: 960px;
            margin: 2rem auto;
            padding: 0 1.5rem;
        }}

        .page-header {{
            background: linear-gradient(180deg, rgba(31, 41, 55, 0.6) 0%, rgba(17, 24, 39, 0.8) 100%);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 2.25rem 2rem;
            margin-bottom: 2.5rem;
            box-shadow: var(--shadow);
            position: relative;
            overflow: hidden;
        }}

        .page-header::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, #3b82f6, #8b5cf6, #10b981);
        }}

        .meta-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-bottom: 1rem;
        }}

        .meta-pill {{
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .meta-pill.highlight {{
            background: rgba(245, 158, 11, 0.15);
            border-color: rgba(245, 158, 11, 0.35);
            color: #fbbf24;
        }}

        .page-header h1 {{
            font-size: 2.1rem;
            font-weight: 800;
            letter-spacing: -0.025em;
            color: #f9fafb;
            margin-bottom: 0.75rem;
            line-height: 1.25;
        }}

        .page-header p {{
            color: var(--text-muted);
            font-size: 1.05rem;
            max-width: 750px;
        }}

        .content {{
            background: var(--surface);
            border: 1px solid var(--border-subtle);
            border-radius: var(--radius);
            padding: 2.5rem;
            box-shadow: var(--shadow);
        }}

        .content h2 {{
            font-size: 1.5rem;
            font-weight: 700;
            color: #60a5fa;
            margin-top: 2.5rem;
            margin-bottom: 1.25rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .content h2:first-child {{
            margin-top: 0;
        }}

        .content h3 {{
            font-size: 1.2rem;
            font-weight: 600;
            color: #e5e7eb;
            margin-top: 1.75rem;
            margin-bottom: 0.75rem;
        }}

        .content p {{
            margin-bottom: 1.15rem;
            color: #d1d5db;
        }}

        .content ul, .content ol {{
            margin-bottom: 1.25rem;
            padding-left: 1.5rem;
            color: #d1d5db;
        }}

        .content li {{
            margin-bottom: 0.4rem;
        }}

        .content strong {{
            color: #f3f4f6;
            font-weight: 600;
        }}

        .content table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0 2rem;
            font-size: 0.925rem;
            background: #0f172a;
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid var(--border);
        }}

        .content th {{
            background: #1e293b;
            color: #93c5fd;
            font-weight: 700;
            text-align: left;
            padding: 0.85rem 1rem;
            border-bottom: 2px solid var(--border);
        }}

        .content td {{
            padding: 0.85rem 1rem;
            border-bottom: 1px solid #1e293b;
            color: #cbd5e1;
            vertical-align: top;
        }}

        .content tr:nth-child(even) {{
            background: rgba(30, 41, 59, 0.4);
        }}

        .content tr:hover {{
            background: rgba(59, 130, 246, 0.08);
        }}

        .content blockquote {{
            background: rgba(31, 41, 55, 0.5);
            border-left: 4px solid var(--primary);
            padding: 1rem 1.25rem;
            border-radius: 0 8px 8px 0;
            margin: 1.5rem 0;
            color: #e5e7eb;
        }}

        .alert-box {{
            padding: 1rem 1.25rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            display: flex;
            gap: 0.75rem;
            align-items: flex-start;
        }}

        .alert-important {{
            background: rgba(239, 68, 68, 0.12);
            border: 1px solid rgba(239, 68, 68, 0.35);
            color: #fca5a5;
        }}

        .alert-tip {{
            background: rgba(16, 185, 129, 0.12);
            border: 1px solid rgba(16, 185, 129, 0.35);
            color: #6ee7b7;
        }}

        .alert-note {{
            background: rgba(59, 130, 246, 0.12);
            border: 1px solid rgba(59, 130, 246, 0.35);
            color: #93c5fd;
        }}

        .mermaid {{
            background: #0f172a;
            padding: 1.5rem;
            border-radius: 8px;
            border: 1px solid var(--border);
            margin: 1.75rem 0;
            text-align: center;
            overflow-x: auto;
        }}

        code {{
            font-family: 'JetBrains Mono', monospace;
            background: rgba(255, 255, 255, 0.1);
            color: #f472b6;
            padding: 0.15rem 0.4rem;
            border-radius: 4px;
            font-size: 0.85em;
        }}

        pre code {{
            background: transparent;
            padding: 0;
            color: inherit;
        }}

        .content hr {{
            border: none;
            border-top: 1px solid var(--border);
            margin: 2.5rem 0;
        }}

        @media (max-width: 768px) {{
            .content {{
                padding: 1.5rem;
            }}
            .page-header {{
                padding: 1.5rem 1.25rem;
            }}
            .page-header h1 {{
                font-size: 1.6rem;
            }}
        }}
    </style>
</head>
<body>
    <header class="top-nav">
        <a href="index.html" class="nav-brand">
            <span>← ADS 2026.2</span>
            <span class="badge">Portal de Estudos</span>
        </a>
        <div class="nav-actions">
            <a href="{simulado_link}" class="btn btn-primary">🎯 Fazer Simulado</a>
            <a href="index.html" class="btn btn-secondary">🏠 Início</a>
        </div>
    </header>

    <main class="container">
        <header class="page-header">
            <div class="meta-pills">
                <span class="meta-pill highlight">📅 Prova: {data_prova}</span>
                <span class="meta-pill">📍 {sala_prova}</span>
                <span class="meta-pill">⏰ {horario_prova}</span>
                <span class="meta-pill">💡 Unidades 1 a 4</span>
            </div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </header>

        <article class="content">
            {body}
        </article>
    </main>

    <script>
        mermaid.initialize({{
            startOnLoad: true,
            theme: 'dark',
            themeVariables: {{
                fontFamily: 'Plus Jakarta Sans',
                primaryColor: '#1e3a8a',
                primaryBorderColor: '#3b82f6',
                primaryTextColor: '#f3f4f6',
                lineColor: '#60a5fa'
            }}
        }});
    </script>
</body>
</html>
"""

def render_markdown_page(md_text, title, subtitle, data_prova, sala_prova, horario_prova, simulado_link, out_filename):
    processed_md = re.sub(r'```mermaid\n(.*?)\n```', r'<div class="mermaid">\n\1\n</div>', md_text, flags=re.DOTALL)
    processed_md = re.sub(r'>\s*\[!IMPORTANT\]\s*\n(.*?)(?=\n\n|\n[#>-]|$)', r'<div class="alert-box alert-important"><span>⚠️</span><div>\1</div></div>', processed_md, flags=re.DOTALL)
    processed_md = re.sub(r'>\s*\[!TIP\]\s*\n(.*?)(?=\n\n|\n[#>-]|$)', r'<div class="alert-box alert-tip"><span>💡</span><div>\1</div></div>', processed_md, flags=re.DOTALL)
    processed_md = re.sub(r'>\s*\[!NOTE\]\s*\n(.*?)(?=\n\n|\n[#>-]|$)', r'<div class="alert-box alert-note"><span>ℹ️</span><div>\1</div></div>', processed_md, flags=re.DOTALL)
    
    body_html = markdown.markdown(processed_md, extensions=['tables', 'fenced_code'])
    
    html_out = STYLE_HEADER.format(
        title=title,
        subtitle=subtitle,
        data_prova=data_prova,
        sala_prova=sala_prova,
        horario_prova=horario_prova,
        simulado_link=simulado_link,
        body=body_html
    )
    
    out_file = BASE / out_filename
    out_file.write_text(html_out, encoding="utf-8")
    print(f"Gerado: {out_file.name} ({len(html_out)} bytes)")

def generate_comunicacao():
    md_path = BASE / "prova_05062026 -Direito + comunicação" / "Comunicação e linguagem" / "Ebook+Materiais" / "resumo_e_mapa_mental_u1_a_u4.md"
    raw_md = md_path.read_text(encoding="utf-8")
    render_markdown_page(
        md_text=raw_md,
        title="Comunicação e Linguagem — Resumo e Mapas Mentais",
        subtitle="Síntese completa das Unidades 1 a 4, 6 Funções da Linguagem de Jakobson, Estratégias PCN, 7 Fatores de Textualidade e Gêneros Acadêmicos.",
        data_prova="05/11/2026",
        sala_prova="Sala 308 - Prédio 1 LABIN",
        horario_prova="20h00 às 20h15",
        simulado_link="simulado_comunicacao_e_linguagem_U1-U4.html",
        out_filename="resumo_comunicacao_e_linguagem.html"
    )

def generate_direito():
    md = """# 📚 Resumo Executivo e Tópicos de Prova — Direito Digital (Unidades 1 a 4)

**Disciplina:** Direito Digital (Unilasalle / Sagah)  
**Data da Prova Presencial (Bloco 1):** 05/11/2026 (20h00 às 20h15 — Sala 308, Prédio 1 LABIN)  
**Validação:** Baseado integralmente no livro oficial da disciplina e nas 12 questões dos questionários oficiais.

---

## 🧠 Mapa Mental Geral da Disciplina (4 Unidades)

```mermaid
flowchart LR
    DD["⚖️ DIREITO DIGITAL"]
    
    DD --> U1["📌 UNIDADE 1: Teoria Geral & Sujeitos"]
    DD --> U2["📌 UNIDADE 2: Propriedade Intelectual & Software"]
    DD --> U3["📌 UNIDADE 3: Obrigações & Responsabilidade"]
    DD --> U4["📌 UNIDADE 4: Marco Civil & LGPD"]

    U1 --> U1A["Direito Público x Privado"]
    U1 --> U1B["Capacidade de Gozo x de Fato (art. 1º CC)"]
    U1 --> U1C["Nascituro protegido (art. 2º CC)"]
    U1 --> U1D["PJ: Início no Registro art. 45 CC"]
    U1 --> U1E["Autarquias e Fundações Públicas (Dir. Público)"]

    U2 --> U2A["Software: Bens Intangíveis (Custos Fixos Altos / Marginais Baixos)"]
    U2 --> U2B["Copyright (Expressão Literal) x Patente (Funcionalidade)"]
    U2 --> U2C["RPC no INPI protegido por Hash Criptográfico"]
    U2 --> U2D["Autorização prévia/expressa para uso da obra"]

    U3 --> U3A["Elementos: Sujeitos, Objeto e Vínculo Jurídico"]
    U3 --> U3B["Prestação de Dar, Fazer e Não Fazer"]
    U3 --> U3C["Princípio da Socialidade (Função Social art. 421 CC)"]
    U3 --> U3D["Água = Obrigação Pessoal (NÃO propter rem)"]
    U3 --> U3E["Jogos de azar = Obrigação Natural (Sem cobrança civil)"]

    U4 --> U4A["Marco Civil: Liberdade de Expressão + Privacidade + Neutralidade"]
    U4 --> U4B["Responsabilidade Subjetiva Provedor Aplicação: art. 19 (Ordem Judicial)"]
    U4 --> U4C["Exceção Intimidade Sexual: art. 21 (Notificação Extrajudicial)"]
    U4 --> U4D["LGPD nas Relações Trabalhistas (Candidatos, Ativos e Desligados)"]
    U4 --> U4E["Princípios: Licitude, Lealdade, Transparência e Finalidade"]
```

---

## 📌 UNIDADE 1 — Teoria Geral do Direito e Sujeitos de Direito Privado

> [!IMPORTANT]
> **Pegadinha Clássica de Prova (Questões 2 e 3 do Questionário):**
> 1. O Código Civil (art. 1º) **combina capacidade com personalidade** ("toda pessoa é capaz de direitos e deveres na ordem civil").
> 2. **Nem toda pessoa tem capacidade de fato (exercício):** Um bebê recém-nascido tem capacidade de direito (gozo), mas é absolutamente incapaz de exercer pessoalmente os atos da vida civil.
> 3. **A personalidade jurídica das empresas NÃO começa com a assinatura do contrato social**, mas sim com o **REGISTRO/INSCRIÇÃO** do ato constitutivo no órgão competente (Junta Comercial / Cartório de Registro Civil de PJ, conforme art. 45 do CC).
> 4. **O nascituro é protegido pela lei** desde a concepção (art. 2º do CC).

### 1.1 Classificação das Pessoas Jurídicas no Código Civil
* **Pessoas Jurídicas de Direito Público Interno (art. 41 do CC):**
  - União, Estados, DF, Municípios.
  - **Autarquias** (ex.: INSS, Banco Central).
  - **Fundações públicas/estatais**.
* **Pessoas Jurídicas de Direito Privado (art. 44 do CC):**
  - **Associações** (sem fins econômicos).
  - **Sociedades** (empresariais e simples).
  - **Fundações privadas**.
  - **Organizações religiosas**.
  - **Partidos políticos**.

---

## 📌 UNIDADE 2 — Propriedade Intelectual e Proteção de Software

### 2.1 Natureza Econômica e Jurídica do Software
* **Características:** O software é **intangível**, possui **altos custos fixos de produção** e **baixos custos marginais de reprodução** (Shapiro & Varian). Seu preço é fixado pelo valor que o usuário está disposto a pagar, e não pelo custo da cópia física.
* **Copyright vs. Patentes:**
  - **Copyright (Direito do Autor - Lei 9.609/98 e 9.610/98):** Protege a **expressão literal** do código (código-fonte e objeto) contra pirataria e cópia direta. Não depende de registro para ter proteção, mas o registro confere segurança probatória.
  - **Patente:** Protege a **funcionalidade técnica/ideias** e invenções implementadas por computador. Evita a cópia por concorrentes de métodos técnicos inovadores.

### 2.2 Registro de Programa de Computador (RPC) no INPI
* O registro no **INPI (Instituto Nacional da Propriedade Industrial)** utiliza uma **função hash criptográfica**.
* O algoritmo **hash** gera uma impressão digital única do código do software, garantindo a **autenticidade e integridade** do arquivo guardado pelo titular sem necessidade de envio do código-fonte em texto aberto.
* O direito autoral no Brasil define que qualquer utilização da obra depende de **autorização prévia e expressa do titular**.

---

## 📌 UNIDADE 3 — Direito das Obrigações e Responsabilidade Civil

### 3.1 Estrutura da Relação Obrigacional
Toda obrigação jurídica é composta por 3 elementos fundamentais:
1. **Elemento Subjetivo:** Sujeito Ativo (credor) e Sujeito Passivo (devedor).
2. **Elemento Objetivo (Prestação):** Conduta devida de **Dar** (coisa certa ou incerta), **Fazer** ou **Não Fazer** (abstenção).
3. **Elemento Imaterial / Vínculo Jurídico:** O enlace legal que compele o devedor a adimplir a prestação sob pena de responder com seu patrimônio (responsabilidade civil).

### 3.2 Princípio da Socialidade (art. 421 do CC)
* Vinculado à **Função Social dos Contratos e das Obrigações**.
* As partes não devem apenas respeitar a boa-fé subjetiva entre si, mas devem pactuar e executar o negócio **de modo a não prejudicar a coletividade e o interesse social**.

---

## 📌 UNIDADE 4 — Marco Civil da Internet (Lei 12.965/14) e LGPD (Lei 13.709/18)

### 4.1 Marco Civil da Internet (Lei nº 12.965/2014)
* **Responsabilidade Civil por Danos de Conteúdo de Terceiros (Regra Geral x Exceção):**
  - **Regra Geral (art. 19):** Para assegurar a liberdade de expressão e evitar a censura privada prévia, o provedor de aplicações **só responde civilmente se, após ordem judicial específica**, não tomar as providências para indisponibilizar o conteúdo no prazo assinalado.
  - **Exceção de Intimidade Sexual (art. 21):** Em casos de divulgação não autorizada de imagens, vídeos ou materiais contendo nudez ou atos sexuais de caráter privado (pornografia de vingança), o provedor responderá subsidiariamente se não remover o material **após simples notificação extrajudicial realizada pela própria vítima ou seu representante legal**.

### 4.2 LGPD nas Relações de Trabalho (Lei nº 13.709/2018)
* Aplica-se integralmente a todas as fases da relação de emprego (art. 1º e 5º da LGPD):
  - **Fase Pré-contratual:** Candidatos a vagas de emprego, currículos e processos seletivos.
  - **Fase Contratual:** Empregados ativos (dados de saúde, biométricos, sindicais).
  - **Fase Pós-contratual:** Ex-funcionários desligados (guarda de prontuários, rescisões).
"""
    render_markdown_page(
        md_text=md,
        title="Direito Digital — Resumo Executivo e Tópicos de Prova",
        subtitle="Síntese das Unidades 1 a 4, Teoria dos Sujeitos, Registro de Software no INPI (Hash & RPC), Obrigações, Marco Civil da Internet (art. 19 e 21) e LGPD.",
        data_prova="05/11/2026",
        sala_prova="Sala 308 - Prédio 1 LABIN",
        horario_prova="20h00 às 20h15",
        simulado_link="simulado_direito_digital_U1-U4.html",
        out_filename="resumo_direito_digital.html"
    )

def generate_requisitos():
    md = """# 📚 Resumo Executivo e Tópicos de Prova — Requisitos de Software (Unidades 1 a 4)

**Disciplina:** Requisitos de Software (Unilasalle EAD)  
**Data da Prova Presencial (Bloco 2):** 12/11/2026 (18h45 às 19h00 — Sala 607, Prédio 15)  
**Validação:** Baseado integralmente nos 4 e-books oficiais da disciplina e nas 12 questões dos questionários oficiais comentados.

---

## 🧠 Mapa Mental Geral da Disciplina (4 Unidades)

```mermaid
flowchart LR
    RS["⚙️ REQUISITOS DE SOFTWARE"]
    
    RS --> U1["📌 UNIDADE 1: Fundamentos & Especificação"]
    RS --> U2["📌 UNIDADE 2: Elicitação & Modelagem"]
    RS --> U3["📌 UNIDADE 3: Verificação & Validação"]
    RS --> U4["📌 UNIDADE 4: Gerenciamento & Rastreabilidade"]

    U1 --> U1A["ISO/IEC/IEEE 29148: Características de Bom Requisito"]
    U1 --> U1B["Mensurável, Verificável e sem Ambiguidade"]
    U1 --> U1C["O Que vs. Como (Não especificar solução técnica)"]
    U1 --> U1D["Requisitos Funcionais vs. Não-Funcionais (FURPS+)"]

    U2 --> U2A["Técnicas de Elicitação: Entrevistas, Questionários, JAD, Etnografia"]
    U2 --> U2B["Casos de Uso UML: Atores, Cenários e Relações Include/Extend"]
    U2 --> U2C["User Stories Ágeis (Como um... Quero... Para que...)"]
    U2 --> U2D["Critérios INVEST e Critérios de Aceitação"]

    U3 --> U3A["ISO/IEC/IEEE 12207: Diferença Verificação x Validação"]
    U3 --> U3B["Verificação: 'Construindo o produto corretamente?' (Conformidade)"]
    U3 --> U3C["Validação: 'Construindo o produto correto?' (Necessidade do Cliente)"]
    U3 --> U3D["Testes desenvolvidos concomitantemente aos requisitos"]
    U3 --> U3E["Gerenciamento de Resultados e Aceite Formal"]

    U4 --> U4A["Baseline de Requisitos (Acordo formal entre devs e stakeholders)"]
    U4 --> U4B["Desenvolvimento de Requisitos vs. Gerenciamento de Requisitos"]
    U4 --> U4C["6 Causas de Mudança (Mercado, Gestão, Usuários, Leis, Processos, Lições)"]
    U4 --> U4D["Matriz de Rastreabilidade Bidirecional e Comitê de Mudanças (CCB)"]
```

---

## 📌 UNIDADE 1 — Fundamentos da Engenharia de Requisitos

> [!IMPORTANT]
> **Norma ISO/IEC/IEEE 29148 (2018) — Requisito Bem Especificado (Questões 1, 2 e 5 do Questionário):**
> 1. Um requisito de software deve definir **O QUÊ** o sistema deve fazer, e **NUNCA COMO** a solução técnica será implementada (linguagem, banco de dados ou detalhes de arquitetura pertencem ao design).
> 2. Deve ser **mensurável** (com condições quantificáveis claras) e **verificável** (deve existir um método prático de teste ou demonstração para provar que foi atendido).
> 3. Deve ser **não ambíguo** (ter apenas uma interpretação possível tanto pela equipe técnica quanto pelos usuários).
> 4. Deve atender a uma necessidade real de um **stakeholder** específico.

### 1.1 Classificação dos Requisitos (Modelo FURPS+)
* **Requisitos Funcionais (F):** Ações, comportamentos, cálculos, regras de negócio e serviços que o sistema deve executar diretamente.
* **Requisitos Não-Funcionais (URPS):**
  - **Usability (Usabilidade):** Facilidade de aprendizado, ergonomia, estética da interface.
  - **Reliability (Confiabilidade):** MTBF (tempo médio entre falhas), disponibilidade (99,9%), segurança contra falhas.
  - **Performance (Desempenho):** Tempo de resposta de transações, vazão, uso de memória/CPU.
  - **Supportability (Suportabilidade):** Facilidade de manutenção, portabilidade, testabilidade e extensibilidade.

---

## 📌 UNIDADE 2 — Elicitação e Modelagem de Requisitos

### 2.1 Técnicas de Elicitação
* **Entrevistas (Abertas ou Estruturadas):** Diálogo direto com os stakeholders; excelente para aprofundar problemas complexos.
* **Questionários:** Ideais quando os usuários estão dispersos geograficamente ou quando se busca dados estatísticos com amostras grandes.
* **JAD (Joint Application Design):** Workshops colaborativos e estruturados reunindo usuários, analistas e desenvolvedores.
* **Observação Direta / Etnografia:** O analista observa o usuário em seu ambiente real de trabalho para descobrir requisitos tácitos e reais.
* **Prototipação:** Criação de telas e simulações de fluxo para obter validação precoce do usuário.

### 2.2 Modelagem de Requisitos
* **Casos de Uso (UML):** Representam as interações entre **Atores** (usuários ou sistemas externos) e o sistema.
  - *Include:* Inclusão obrigatória de um subcomportamento (ex.: Validar Login no caso de uso Realizar Transferência).
  - *Extend:* Extensão condicional / opcional de um comportamento em ponto específico.
* **User Stories (Histórias de Usuário):** Sintéticas e centradas no valor de negócio:
  - Formato: *"Como [tipo de usuário], eu quero [funcionalidade] para que [benefício/valor]."*
  - **Critérios INVEST:** **I**ndependente, **N**egociável, **V**aliosa, **E**stimável, **S**mall (pequena) e **T**estável.

---

## 📌 UNIDADE 3 — Verificação e Validação de Requisitos

> [!IMPORTANT]
> **Pegadinha Clássica de Prova (Questão 6 do Questionário):**
> * **Verificação (ISO/IEC/IEEE 12207):** Confirmação, por meio de evidência objetiva, de que os requisitos especificados foram atendidos. Pergunta-chave: *"Estamos construindo o produto corretamente?"* (Foco na conformidade com o documento/normas).
> * **Validação (ISO/IEC/IEEE 12207):** Confirmação de que os requisitos para um uso ou aplicação pretendida específica foram atendidos. Pergunta-chave: *"Estamos construindo o produto correto?"* (Foco na real necessidade e satisfação do cliente).

### 3.1 Testes Concomitantes aos Requisitos (Questão 5)
* O grande benefício de desenvolver casos de teste **concomitantemente à especificação de requisitos** (ou logo após) é que os testes funcionam como uma ferramenta de **revisão e validação precoce**, permitindo identificar ambiguidades, incompletudes e contradições antes de qualquer linha de código ser escrita.

### 3.2 Gerenciamento dos Resultados da Validação (Questão 1)
* Ao concluir a validação, se o produto estiver conforme, formaliza-se o **aceite**.
* Se houver divergências ou defeitos, os resultados devem ser documentados e gerenciados para garantir o retrabalho corretivo e a reavaliação.

---

## 📌 UNIDADE 4 — Gerenciamento e Rastreabilidade de Requisitos

### 4.1 Baseline de Requisitos (Questão 2)
* Uma **Baseline** é uma versão estável e formalmente acordada de um conjunto de requisitos.
* A partir do momento em que a baseline é estabelecida, nenhuma alteração pode ser realizada de forma informal ou direta; qualquer mudança passa obrigatoriamente pelo fluxo formal de **Controle de Mudanças (CCB - Change Control Board)**.

### 4.2 Desenvolvimento vs. Gerenciamento de Requisitos (Questão 3)
A Engenharia de Requisitos é dividida em dois grandes grupos:
1. **Desenvolvimento de Requisitos:** Elicitação, Análise, Especificação e Validação (fase de criação e descoberta).
2. **Gerenciamento de Requisitos:** Controle de versão, controle de mudanças, rastreabilidade e monitoramento do status dos requisitos (fase de manutenção e governança durante todo o ciclo de vida).

### 4.3 Causas de Solicitações de Mudança (Questão 4)
As 6 causas fundamentais de mudanças de requisitos:
1. Mudanças no ambiente operacional de mercado.
2. **Decisões estratégicas ou operacionais da gerência da organização.**
3. Requisitos esquecidos ou novos desejos dos usuários finais.
4. Novas leis, regulamentações ou atos governamentais.
5. Melhoria de processos organizacionais.
6. Lições aprendidas e anomalias de projetos anteriores.
"""
    render_markdown_page(
        md_text=md,
        title="Requisitos de Software — Resumo Executivo e Tópicos de Prova",
        subtitle="Síntese das Unidades 1 a 4, ISO/IEC/IEEE 29148 e 12207, FURPS+, Elicitação, User Stories INVEST, Verificação vs. Validação e Baseline.",
        data_prova="12/11/2026",
        sala_prova="Sala 607 - Prédio 15",
        horario_prova="18h45 às 19h00",
        simulado_link="simulado_requisitos_de_software_U1-U4.html",
        out_filename="resumo_requisitos_de_software.html"
    )

def generate_gerenciamento():
    md = """# 📚 Resumo Executivo e Tópicos de Prova — Gerenciamento de Projetos (Unidades 1 a 4)

**Disciplina:** Gerenciamento de Projetos (Unilasalle EAD)  
**Data da Prova Presencial (Bloco 2):** 12/11/2026 (18h45 às 19h00 — Sala 607, Prédio 15)  
**Validação:** Baseado integralmente nos 4 e-books tutores da disciplina, no PMBOK e nas 12 questões dos questionários oficiais comentados.

---

## 🧠 Mapa Mental Geral da Disciplina (4 Unidades)

```mermaid
flowchart LR
    GP["📊 GERENCIAMENTO DE PROJETOS"]
    
    GP --> U1["📌 UNIDADE 1: Conceitos & Ciclo de Vida"]
    GP --> U2["📌 UNIDADE 2: Áreas do PMBOK"]
    GP --> U3["📌 UNIDADE 3: Estruturas & Governança"]
    GP --> U4["📌 UNIDADE 4: Competências & Ética PMI"]

    U1 --> U1A["Projeto: Temporário, Único e Progressivo"]
    U1 --> U1B["Projetos vs. Operações Rotineiras Contínuas"]
    U1 --> U1C["Principais Causas de Fracasso (Escopo, Comunicação, Prazos)"]
    U1 --> U1D["Ciclos de Vida: Preditivo, Adaptativo/Ágil e Híbrido"]

    U2 --> U2A["Escopo: EAP / WBS e Dicionário da EAP"]
    U2 --> U2B["Cronograma: Caminho Crítico (CPM) e Folgas"]
    U2 --> U2C["Custos: Orçamento e Valor Agregado (EVM: VP, VA, CR)"]
    U2 --> U2D["Riscos: Matriz de Probabilidade x Impacto e Respostas"]

    U3 --> U3A["Estruturas: Funcional x Projetizada x Matricial"]
    U3 --> U3B["Matricial Forte: GP com Autoridade Alta e Dedicação Integral"]
    U3 --> U3C["Modelos de PMO / EGP: Suporte, Controle e Diretivo"]
    U3 --> U3D["Estudos de Mercado e Viabilidade Técnico-Econômica"]

    U4 --> U4A["Modelo PMCDF: Dimensões de Conhecimento, Pessoal e Desempenho"]
    U4 --> U4B["Competências: Técnicas, Comportamentais e Contextuais"]
    U4 --> U4C["Código de Ética do PMI: Responsabilidade, Respeito, Justiça e Honestidade"]
    U4 --> U4D["Práticas Ágeis: Scrum (Papéis, Cerimônias e Artefatos)"]
```

---

## 📌 UNIDADE 1 — Fundamentos do Gerenciamento de Projetos

### 1.1 Definição de Projeto vs. Operações (Questão 3 do Questionário U1)
* **Projeto (PMI / PMBOK):** Um empreendimento **temporário** (tem início, meio e fim definidos) conduzido para criar um produto, serviço ou resultado **único / exclusivo**.
* **Operações Contínuas:** Atividades repetitivas, rotineiras e permanentes voltadas a sustentar o negócio da empresa no dia a dia (ex.: suporte ao cliente, folha de pagamento, manufatura em série).
* **Elaboração Progressiva (Questão 6):** Significa desenvolver em etapas e continuar por incrementos à medida que mais detalhes e informações se tornam disponíveis ao longo do projeto.

### 1.2 Causas Comuns de Fracasso em Projetos (Questão 5)
* Objetivos e escopo mal definidos ou frequentemente alterados sem controle.
* Estimativas de prazos e custos irrealistas.
* Comunicação ineficiente entre a equipe e as partes interessadas (*stakeholders*).
* Falta de engajamento do patrocinador (*sponsor*) e liderança ineficaz.

---

## 📌 UNIDADE 2 — Áreas de Conhecimento do PMBOK

### 2.1 Gerenciamento do Escopo e EAP (Questão 1)
* **Estrutura Analítica do Projeto (EAP / WBS):** Decomposição hierárquica orientada a entregas do trabalho total a ser executado pela equipe do projeto.
* A EAP organiza e define o escopo total do projeto; o menor nível da EAP é chamado de **Pacote de Trabalho (Work Package)**.

### 2.2 Gerenciamento de Custos e Análise de Valor Agregado (EVM) (Questão 2)
* **VP (Valor Planejado):** Orçamento autorizado atribuído ao trabalho planejado.
* **VA (Valor Agregado):** Medida do trabalho executado expressa em termos do orçamento autorizado para esse trabalho.
* **CR (Custo Real):** Custo total efetivamente incorrido na execução do trabalho.
* **Índices de Desempenho:**
  - *IDP (Índice de Desempenho de Prazos) = VA / VP* (IDP > 1: adiantado; IDP < 1: atrasado).
  - *IDC (Índice de Desempenho de Custos) = VA / CR* (IDC > 1: abaixo do orçamento/economia; IDC < 1: acima do orçamento).

### 2.3 Gerenciamento de Riscos (Questão 4)
* O risco em projetos é um evento ou condição incerta que, se ocorrer, terá um efeito positivo (oportunidade) ou negativo (ameaça) em pelo menos um objetivo do projeto (prazo, custo, escopo ou qualidade).
* Estratégias de resposta para riscos negativos: **Prevenir/Evitar, Mitigar, Transferir ou Aceitar**.

---

## 📌 UNIDADE 3 — Estruturas Organizacionais e Escritório de Projetos (PMO)

> [!IMPORTANT]
> **Pegadinhas Clássicas sobre Estruturas Organizacionais (Questões 1 e 2 do Questionário U3):**
> * **Estrutura Funcional Clássica:** Hierarquia tradicional dividida por departamentos (TI, RH, Vendas). O gerente funcional tem toda a autoridade; o projeto tem prioridade baixa e o gestor atua apenas como coordenador de meio período.
> * **Estrutura Projetizada:** A organização é orientada a projetos. O gerente de projeto possui **autoridade total**, controla os recursos e a equipe trabalha em tempo integral dedicada ao projeto.
> * **Estrutura Matricial (Fraca, Balanceada e Forte):**
>   - *Matricial Fraca:* Semelhante à funcional (papel do gestor é facilitador/expedidor).
>   - *Matricial Balanceada:* Compartilhamento de poder entre gerente funcional e gerente de projetos.
>   - *Matricial Forte:* **O gerente de projetos tem alta autoridade**, equipe dedicada e controle significativo sobre o orçamento, mantendo as especialidades funcionais.

### 3.1 Modelos de Escritório de Gerenciamento de Projetos (EGP / PMO) (Questão 5)
1. **PMO de Suporte:** Fornece políticas, metodologias, modelos e lições aprendidas (grau de controle **baixo**).
2. **PMO de Controle:** Exige conformidade com frameworks, governança e ferramentas (grau de controle **médio**).
3. **PMO Diretivo:** Assume a gestão direta dos projetos e designa os gerentes de projeto (grau de controle **alto**).

### 3.2 Ciclos de Vida do Projeto (Questão 6)
* **Preditivo (Cascata / Tradicional):** Escopo, prazo e custo são definidos o mais cedo possível no início do projeto.
* **Iterativo e Incremental:** O escopo inicial é decomposto em entregas progressivas que agregam funcionalidade.
* **Adaptativo / Ágil:** Ciclos curtos (sprints), alta colaboração com o cliente e escopo aberto a mudanças contínuas.
* **Híbrido:** Combina abordagem preditiva para partes estáveis com ágil para partes de alta incerteza.

---

## 📌 UNIDADE 4 — Competências do Gestor e Código de Ética

### 4.1 Modelo PMCDF e Competências (PMI)
O gestor de projetos deve equilibrar três dimensões fundamentais:
* **Conhecimento (Técnico):** Domínio das técnicas, ferramentas e práticas consagradas de gerenciamento.
* **Desempenho (Prático):** Capacidade de aplicar o conhecimento para gerar resultados e gerenciar restrições.
* **Pessoal (Comportamental):** Liderança, inteligência emocional, negociação, ética, postura assertiva e comunicação.

### 4.2 Código de Ética e Conduta Profissional do PMI
Os quatro pilares éticos universais:
1. **Responsabilidade:** Assumir a propriedade das decisões tomadas e de suas consequências.
2. **Respeito:** Demonstrar consideração e apreço pelos recursos humanos, culturais e ambientais.
3. **Imparcialidade (Justiça):** Tomar decisões de forma equânime, transparente e livre de conflitos de interesse.
4. **Honestidade:** Agir com veracidade e transparência nas comunicações e relatórios do projeto.
"""
    render_markdown_page(
        md_text=md,
        title="Gerenciamento de Projetos — Resumo Executivo e Tópicos de Prova",
        subtitle="Síntese das Unidades 1 a 4, PMBOK, EAP/WBS, Análise de Valor Agregado (EVM), Estruturas Matriciais, PMO e Código de Ética do PMI.",
        data_prova="12/11/2026",
        sala_prova="Sala 607 - Prédio 15",
        horario_prova="18h45 às 19h00",
        simulado_link="simulado_gerenciamento_de_projetos_U1-U4.html",
        out_filename="resumo_gerenciamento_de_projetos.html"
    )

if __name__ == "__main__":
    generate_comunicacao()
    generate_direito()
    generate_requisitos()
    generate_gerenciamento()
