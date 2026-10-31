# 🎓 Resumão ADS — Provas Finais (7º Semestre)

Portal de estudos, simulados interativos e acervo de materiais para as provas finais do 7º / último semestre do curso de **Análise e Desenvolvimento de Sistemas (ADS)**.

---

## 📅 Cronograma Oficial das Provas Presenciais

| Disciplina | Data | Sala / Prédio | Horário | Status |
| :--- | :---: | :---: | :---: | :---: |
| **Direito Digital** | **05/11/2026** | **308 - Prédio 1 LABIN** | **20h00 às 20h15** | 🟢 Simulado, E-books & Gabaritos Prontos |
| **Comunicação e Linguagem** | **05/11/2026** | **308 - Prédio 1 LABIN** | **20h00 às 20h15** | 🟢 Simulado, Vídeos & Resumo Prontos |
| **Gerenciamento de Projetos** | **12/11/2026** | **607 - Prédio 15** | **18h45 às 19h00** | ⏳ Em Preparação (Bloco 2) |
| **Requisitos de Software** | **12/11/2026** | **607 - Prédio 15** | **18h45 às 19h00** | ⏳ E-books e Questionários catalogados |

---

## 🌐 Como Acessar o Portal

Basta abrir o arquivo **[`index.html`](index.html)** em qualquer navegador web.

O portal inclui:
- ⏱️ **Cronômetro Regressivo** em tempo real para os dois blocos de provas.
- 🎯 **Simulados Interativos** (U1 a U4) com embaralhamento dinâmico de questões e alternativas, nota por unidade e reações animadas.
- 📖 **Páginas de Resumos Executivos** com mapas mentais renderizados via Mermaid.js:
  - [`resumo_comunicacao_e_linguagem.html`](resumo_comunicacao_e_linguagem.html)
  - [`resumo_direito_digital.html`](resumo_direito_digital.html)
- 📚 **Catálogo de E-books oficiais** (SAGAH e apostilas oficiais em PDF).
- 🎬 **Videoaulas oficiais do YouTube** com transcrições integrais.
- ✅ **Checklist de Estudos** com salvamento automático no navegador (`localStorage`).

---

## 📁 Estrutura do Repositório

```text
├── index.html                                        # Portal central de estudos
├── simulado_direito_digital_U1-U4.html               # Simulado oficial U1 a U4 de Direito Digital
├── simulado_comunicacao_e_linguagem_U1-U4.html       # Simulado oficial U1 a U4 de Comunicação
├── resumo_direito_digital.html                       # Resumo completo e mapas mentais (Direito)
├── resumo_comunicacao_e_linguagem.html               # Resumo completo e mapas mentais (Comunicação)
├── gerar_paginas_resumos.py                          # Script de geração dos resumos HTML
├── gifs/                                             # Reações animadas dos simulados
├── prova_05062026 -Direito + comunicação/            # Materiais e PDFs do Bloco 1
│   ├── Comunicação e linguagem/                      # E-books, videoaulas e questionários
│   ├── Direito digital/                              # E-books Sagah, artigos e questionários
│   └── Modelos Provas Emuladas Anteriores/           # Simulados base de semestres anteriores
└── Provas_12112026 - Requisitos + Gerenciamento/     # Materiais do Bloco 2
    ├── Requisitos de software/                       # E-books Unidades 1-4 e questionários
    └── Gerenciamento de Projetos/                    # Estrutura para os materiais de projetos
```
