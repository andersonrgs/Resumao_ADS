#!/usr/bin/env python3
"""Gera as páginas HTML de resumos completos de Comunicação e Linguagem e Direito Digital."""

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

        /* Header de navegação superior */
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

        /* Container principal */
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

        /* Conteúdo Markdown estilizado */
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

        /* Tabelas */
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

        /* Alertas e Blockquotes */
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

        /* Mermaid Diagrams */
        .mermaid {{
            background: #0f172a;
            padding: 1.5rem;
            border-radius: 8px;
            border: 1px solid var(--border);
            margin: 1.75rem 0;
            text-align: center;
            overflow-x: auto;
        }}

        /* Código */
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

def generate_comunicacao():
    md_path = BASE / "prova_05062026 -Direito + comunicação" / "Comunicação e linguagem" / "Ebook+Materiais" / "resumo_e_mapa_mental_u1_a_u4.md"
    raw_md = md_path.read_text(encoding="utf-8")
    
    # Process mermaid blocks
    processed_md = re.sub(r'```mermaid\n(.*?)\n```', r'<div class="mermaid">\n\1\n</div>', raw_md, flags=re.DOTALL)
    
    # Process alerts
    processed_md = re.sub(r'>\s*\[!IMPORTANT\]\s*\n(.*?)(?=\n\n|\n[#>-]|$)', r'<div class="alert-box alert-important"><span>⚠️</span><div>\1</div></div>', processed_md, flags=re.DOTALL)
    processed_md = re.sub(r'>\s*\[!TIP\]\s*\n(.*?)(?=\n\n|\n[#>-]|$)', r'<div class="alert-box alert-tip"><span>💡</span><div>\1</div></div>', processed_md, flags=re.DOTALL)
    processed_md = re.sub(r'>\s*\[!NOTE\]\s*\n(.*?)(?=\n\n|\n[#>-]|$)', r'<div class="alert-box alert-note"><span>ℹ️</span><div>\1</div></div>', processed_md, flags=re.DOTALL)
    
    body_html = markdown.markdown(processed_md, extensions=['tables', 'fenced_code'])
    
    html = STYLE_HEADER.format(
        title="Comunicação e Linguagem — Resumo e Mapas Mentais",
        subtitle="Síntese completa das Unidades 1 a 4, 6 Funções da Linguagem de Jakobson, Estratégias PCN, 7 Fatores de Textualidade e Gêneros Acadêmicos.",
        data_prova="05/11/2026",
        sala_prova="Sala 308 - Prédio 1 LABIN",
        horario_prova="20h00 às 20h15",
        simulado_link="simulado_comunicacao_e_linguagem_U1-U4.html",
        body=body_html
    )
    
    out_file = BASE / "resumo_comunicacao_e_linguagem.html"
    out_file.write_text(html, encoding="utf-8")
    print(f"Gerado: {out_file} ({len(html)} bytes)")

def generate_direito():
    md_content = """# 📚 Resumo Executivo e Tópicos de Prova — Direito Digital (Unidades 1 a 4)

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
2. **Elemento Objetivo (Prestação):** Conduta devida de **Dar** (coisa certa ou incerta), **Fazer** ou **Não Fazer** (abstenção). *(Atenção: "pagar" é espécie de obrigação de dar).*
3. **Elemento Imaterial / Vínculo Jurídico:** O enlace legal que compele o devedor a adimplir a prestação sob pena de responder com seu patrimônio (responsabilidade civil).

### 3.2 Princípio da Socialidade (art. 421 do CC)
* Vinculado à **Função Social dos Contratos e das Obrigações**.
* As partes não devem apenas respeitar a boa-fé subjetiva entre si, mas devem pactuar e executar o negócio **de modo a não prejudicar a coletividade e o interesse social**.

### 3.3 Casos Notáveis dos Questionários
* **Dívidas de Jogo (Jogos de Azar):** São obrigações puramente naturais. Não geram responsabilidade civil e não podem ser cobradas judicialmente em juízo.
* **Fornecimento de Água e Energia:** É uma **obrigação pessoal** vinculada ao indivíduo/usuário que consumiu o serviço, e **NÃO** uma obrigação *propter rem* (que acompanha a coisa/imóvel).

---

## 📌 UNIDADE 4 — Marco Civil da Internet (Lei 12.965/14) e LGPD (Lei 13.709/18)

### 4.1 Marco Civil da Internet (Lei nº 12.965/2014)
* **Princípios Fundamentais (art. 3º):** Garantia da liberdade de expressão, comunicação e manifestação de pensamento; proteção da privacidade e dos dados pessoais; preservação da neutralidade da rede.
* **Provedor de Conexão vs. Provedor de Aplicações:**
  - *Conexão:* Empresas de telecomunicações que dão acesso à rede (NET, Vivo, Claro). Devem guardar registros de conexão por 1 ano. **É vedado guardar registros de acesso a aplicações.**
  - *Aplicações:* Conjunto de funcionalidades acessadas via web (Facebook, Google, Mercado Livre, portais). Devem guardar registros de acesso a aplicações por 6 meses.
* **Responsabilidade Civil por Danos de Conteúdo de Terceiros (Regra Geral x Exceção):**
  - **Regra Geral (art. 19):** Para assegurar a liberdade de expressão e evitar a censura privada prévia, o provedor de aplicações **só responde civilmente se, após ordem judicial específica**, não tomar as providências para indisponibilizar o conteúdo no prazo assinalado.
  - **Exceção de Intimidade Sexual (art. 21):** Em casos de divulgação não autorizada de imagens, vídeos ou materiais contendo nudez ou atos sexuais de caráter privado (pornografia de vingança), o provedor responderá subsidiariamente se não remover o material **após simples notificação extrajudicial realizada pela própria vítima ou seu representante legal**.

### 4.2 LGPD nas Relações de Trabalho (Lei nº 13.709/2018)
* **Aplicação Integral no Ambiente Laboral:** Embora a LGPD não esteja expressamente dentro do texto consolidado da CLT, aplica-se plenamente a todas as fases da relação de emprego (art. 1º e 5º da LGPD):
  - **Fase Pré-contratual:** Candidatos a vagas de emprego, currículos e processos seletivos.
  - **Fase Contratual:** Empregados ativos (dados de saúde, biométricos, sindicais).
  - **Fase Pós-contratual:** Ex-funcionários desligados (guarda de prontuários, rescisões).
* **Classificação dos Atores:**
  - **Empregador = Controlador** (determina como e por que os dados são tratados).
  - **Trabalhadores/Candidatos = Titulares dos dados**.
* **Princípios Obrigatórios:** Licitude, lealdade, transparência, segurança, necessidade e finalidade legítima.
"""

    processed_md = re.sub(r'```mermaid\n(.*?)\n```', r'<div class="mermaid">\n\1\n</div>', md_content, flags=re.DOTALL)
    processed_md = re.sub(r'>\s*\[!IMPORTANT\]\s*\n(.*?)(?=\n\n|\n[#>-]|$)', r'<div class="alert-box alert-important"><span>⚠️</span><div>\1</div></div>', processed_md, flags=re.DOTALL)
    processed_md = re.sub(r'>\s*\[!TIP\]\s*\n(.*?)(?=\n\n|\n[#>-]|$)', r'<div class="alert-box alert-tip"><span>💡</span><div>\1</div></div>', processed_md, flags=re.DOTALL)
    
    body_html = markdown.markdown(processed_md, extensions=['tables', 'fenced_code'])
    
    html = STYLE_HEADER.format(
        title="Direito Digital — Resumo Executivo e Tópicos de Prova",
        subtitle="Síntese das Unidades 1 a 4, Teoria dos Sujeitos, Registro de Software no INPI (Hash & RPC), Obrigações, Marco Civil da Internet (art. 19 e 21) e LGPD.",
        data_prova="05/11/2026",
        sala_prova="Sala 308 - Prédio 1 LABIN",
        horario_prova="20h00 às 20h15",
        simulado_link="simulado_direito_digital_U1-U4.html",
        body=body_html
    )
    
    out_file = BASE / "resumo_direito_digital.html"
    out_file.write_text(html, encoding="utf-8")
    print(f"Gerado: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_comunicacao()
    generate_direito()
