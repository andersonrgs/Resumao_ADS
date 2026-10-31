# Questionário Unidades 1 e 2 — Requisitos de Software (Transcrição e Gabarito Comentado)

- **Disciplina:** Requisitos de Software (ADS — Unilasalle 2026/2)
- **Avaliação:** Questionário Unidades 1 e 2 (G1)
- **Nota Obtida nas Capturas:** **2,0 / 2,0 pontos (100% de aproveitamento)**
- **Referência Oficial:** E-book *Requisitos de Software* (SAGAH / Editora LaSalle, 366 páginas)

---

## Resumo do Gabarito (U1 e U2)

| Questão | Peso | Tema Central | Alternativa Correta | Status nas Capturas | Referência no E-book |
| :---: | :---: | :--- | :---: | :---: | :--- |
| **1** | 0,4 | Características de um Requisito Bem Especificado (ISO/IEC/IEEE 29148:2018) | **C** | Correta (0,4/0,4) | Unidade 1, Parte 2, p. 38–40 (PDF p. 40–42) |
| **2** | 0,4 | Priorização de Requisitos — Legislação com Data de Entrada em Vigor | **B** | Correta (0,4/0,4) | Unidade 1, Parte 2, p. 36–38 (PDF p. 38–40) |
| **3** | 0,4 | Formato Padronizado e Componentes do Cartão (*Card*) de História de Usuário | **B** | Correta (0,4/0,4) | Unidade 2, Parte 4, p. 162–163 (PDF p. 164–165) |
| **4** | 0,2 | Características das Histórias de Usuário vs. Abordagens Tradicionais | **D** | Correta (0,2/0,2) | Unidade 1, Parte 4, p. 93 (PDF p. 95) e Unidade 2, Parte 4, p. 169 (PDF p. 171) |
| **5** | 0,4 | Priorização de Requisitos quando a Equipe tem Pouca Experiência com a Tecnologia | **A** | Correta (0,4/0,4) | Unidade 1, Parte 2, p. 36–38 (PDF p. 38–40) |
| **6** | 0,2 | Limitações de Casos de Uso e Histórias de Usuário (Sistemas Intensivos em Processamento) | **B** | Correta (0,2/0,2) | Unidade 2, Parte 1, p. 99 (PDF p. 101) e Parte 4, p. 170 (PDF p. 172) |

---

## Transcrição Completa e Justificativas

### Questão 1 (0,4 / 0,4 ponto) — Múltipla Escolha

**Enunciado:**
A especificação clara e detalhada dos requisitos é fundamental para o sucesso de um projeto de software. Um requisito mal compreendido ou mal documentado pode levar a problemas como estimativas inadequadas de esforço, retrabalho e dificuldades na realização de testes. A norma ISO/IEC/IEEE 29148 (2018) define as características de um requisito bem especificado, que inclui ser mensurável, verificável e atender a uma necessidade específica de um stakeholder.

*(Fonte: E-book, Unidade 1 [citado como Unidade 2 no AVA], Página(s) do e-book: 38, 39, 40)*

De acordo com a Norma ISO/IEC/IEEE 29148 (2018), qual das seguintes características é essencial para um requisito ser considerado bem especificado? Com base nas informações apresentadas, assinale a alternativa correta.

- [ ] **A.** O requisito deve ser escrito em termos de como a solução será implementada.
- [ ] **B.** O requisito deve ser impreciso para permitir flexibilidade durante o desenvolvimento.
- [x] **C. O requisito deve ser mensurável, com condições claras e verificáveis** *(Resposta Correta)*
- [ ] **D.** O requisito deve ser especificado apenas com base no entendimento dos desenvolvedores.
- [ ] **E.** O requisito não precisa ser verificável, pois ele será ajustado posteriormente.

> **Justificativa Oficial (E-book, Unidade 1, Parte 2 — "Requisitos de Software", p. 39–40 do livro / p. 41–42 do PDF):**
> De acordo com a Norma Internacional ISO/IEC/IEEE 29148 (2018), um requisito bem especificado contém um ou mais destes itens:
> 1. Deve ser atendido ou tido por um sistema para resolver um problema, atingir um objetivo ou tratar de uma preocupação de um *stakeholder*;
> 2. **É qualificado por condições mensuráveis**;
> 3. É limitado por restrições;
> 4. Define o desempenho do sistema quando usado por um *stakeholder* específico ou é a capacidade correspondente de um sistema (e não a capacidade de um usuário);
> 5. **Pode ser verificado** (isto é, a realização de um requisito no sistema pode ser demonstrada).
>
> *Por que as demais estão incorretas?*
> - **A:** Os requisitos devem definir **o quê** deve ser feito, e não **como** deve ser implementado (p. 41 do livro / p. 43 do PDF).
> - **B e E:** Um bom requisito deve ser **não ambíguo** e **verificável** (Quadro 3, p. 43 do livro / p. 45 do PDF).
> - **D:** O requisito deve ser **correto** sob a ótica do usuário/cliente ou seus representantes, e escrito sob a ótica de quem lê.

---

### Questão 2 (0,4 / 0,4 ponto) — Múltipla Escolha

**Enunciado:**
A priorização de requisitos em projetos de software é um processo essencial para garantir que os itens mais importantes sejam atendidos primeiro. Fatores como o valor que o requisito agrega ao negócio, dependências entre requisitos, e até mesmo requisitos legais e regulatórios influenciam essa decisão. Além disso, a equipe de desenvolvimento deve considerar a experiência com o domínio e a tecnologia, bem como o impacto de cada requisito no cronograma e custo do projeto.

*(Fonte: E-book, Unidade 1 [citado como Unidade 2 no AVA], Página(s) do e-book: 36, 37 e 38)*

Qual dos seguintes fatores deve ser priorizado quando um requisito é influenciado por uma legislação com data específica de entrada em vigor? Com base nas informações apresentadas, assinale a alternativa correta:

- [ ] **A.** A experiência da equipe com a tecnologia envolvida no projeto.
- [x] **B. A data de entrada em vigor da determinação legal ou regulatória.** *(Resposta Correta)*
- [ ] **C.** A dependência do requisito em relação a outros requisitos.
- [ ] **D.** O valor agregado ao negócio pelo requisito.
- [ ] **E.** A necessidade de substituir processos manuais que são sujeitos a falhas.

> **Justificativa Oficial (E-book, Unidade 1, Parte 2 — "Requisitos de Software", p. 38 do livro / p. 40 do PDF):**
> No tópico **"2 Priorização de requisitos"**, o livro destaca expressamente:
> *"Demandas de implementações para atender a determinações de ordem legal ou regulatória: é comum que demandas de ordem legal ou que sejam demandadas por órgãos regulamentadores tenham datas específicas para entrar em vigor. Requisitos que implementam essas necessidades precisam ser priorizados em versões compatíveis com as datas demandadas."*

---

### Questão 3 (0,4 / 0,4 ponto) — Múltipla Escolha

**Enunciado:**
Em ambientes ágeis, as Histórias de Usuário se tornaram a forma mais comum de expressar requisitos funcionais, servindo como itens do *backlog* do produto. Ao contrário das especificações tradicionais, elas são curtas, focadas no valor de negócio e escritas em um formato padronizado que busca capturar a perspectiva de quem se beneficiará da funcionalidade.

Identifique o formato padronizado e os três componentes essenciais que caracterizam a expressão de uma História de Usuário (também chamada de "voz do usuário" ou *card*).

- [ ] **A.** "[Ação] será executada por [Papel] se a [Pré-condição] for satisfeita", contendo Verbo, Objeto e Condição.
- [x] **B. "Como [Papel], eu quero [Ação], para [Resultado/Valor]", contendo Papel (Quem), Ação (O Quê) e Resultado/Valor (Porquê).** *(Resposta Correta)*
- [ ] **C.** "O *backlog* terá [Item] por [Prioridade] visando [Resultado]", contendo Prioridade, Item e Descrição.
- [ ] **D.** "O analista de requisitos deve [Ação] a fim de que [Resultado]", contendo Analista, Ação e Objetivo.
- [ ] **E.** "O Sistema deve [Ação] para [Papel], desde que [Resultado]", contendo Componente, Estrutura e Valor.

> **Justificativa Oficial (E-book, Unidade 2, Parte 4 — "Especificação de Requisitos Funcionais Utilizando Histórias de Usuário", p. 162 do livro / p. 164 do PDF):**
> Na seção **"Cartão (Card)"** (Figura 3):
> *"Com o passar do tempo e o uso nas organizações, as histórias de usuário passaram a ter um formato mais padronizado, com afirmações escritas em primeira pessoa, contendo o papel (quem), a ação (o que) e o resultado da ação ou o valor de negócio da história (porque): **Como `<tipo do usuário>` (QUEM), eu quero `<ação específica>` (O QUÊ) de modo que / para `<resultado esperado/valor agregado>` (PORQUE)**."*
> O **papel (QUEM)** representa quem se beneficiará da funcionalidade; a **atividade (O QUÊ)** descreve a funcionalidade (requisito funcional); e o **resultado (PORQUE)** traduz o valor de negócio.

---

### Questão 4 (0,2 / 0,2 ponto) — Múltipla Escolha

**Enunciado:**
A adoção da abordagem de Histórias de Usuário marca uma mudança em relação à documentação tradicional de requisitos. Diferentemente das especificações massivas e detalhadas no início do projeto, as Histórias de Usuário são vistas como expressões de intenção, que promovem uma comunicação contínua e focada em entregas rápidas e incrementais.

Analise as características das Histórias de Usuário em relação às abordagens tradicionais de requisitos e assinale a alternativa correta.

- [ ] **A.** O foco principal das Histórias de Usuário é a descrição da interface, não sendo adequadas para capturar o valor de negócio ou a perspectiva do usuário.
- [ ] **B.** Elas são especificações detalhadas e não negociáveis, escritas em documentos grandes e pesados que requerem manutenção rigorosa.
- [ ] **C.** Elas são escritas em formato técnico, sendo compreensíveis apenas para desenvolvedores e arquitetos de *software*, e não para os *stakeholders* de negócio.
- [x] **D. Elas representam pequenos incrementos de funcionalidade de valor, que são elaboradas à medida que são necessárias (*just-in-time*), evitando especificações prematuras.** *(Resposta Correta)*
- [ ] **E.** Elas são elaboradas em profundidade no início do projeto (*big design up front*), evitando a necessidade de contato constante com o cliente ao longo do desenvolvimento.

> **Justificativa Oficial (E-book, Unidade 1, Parte 4, p. 93 do livro / p. 95 do PDF; e Unidade 2, Parte 4, p. 169 do livro / p. 171 do PDF):**
> De acordo com Leffingwell (2011), as Histórias de Usuário diferem das abordagens tradicionais porque:
> - Não são especificações detalhadas, mas sim **expressões de intenção negociáveis**;
> - São curtas, fáceis de ler e compreensíveis por *stakeholders*, desenvolvedores e usuários;
> - **Representam pequenos incrementos de funcionalidade de valor**, que podem ser implementadas em poucos dias ou semanas;
> - **Não são detalhadas no início do projeto, mas são elaboradas à medida que são necessárias (*just-in-time*), evitando especificações prematuras**, atrasos no desenvolvimento, longo inventário de requisitos e uma declaração da solução muito restritiva;
> - Requerem pouca ou nenhuma manutenção e podem ser descartadas após a implementação.

---

### Questão 5 (0,4 / 0,4 ponto) — Múltipla Escolha

**Enunciado:**
Em projetos de desenvolvimento de software, a priorização dos requisitos é uma etapa crucial para o sucesso. O tamanho e a complexidade do projeto podem aumentar o risco de fracasso, por isso, é importante dividir o trabalho em partes menores e mais gerenciáveis. A priorização dos requisitos pode ser baseada em diversos fatores, como o valor agregado ao negócio, a dependência de outros requisitos, a experiência da equipe, entre outros. A metodologia ágil adota ciclos curtos de desenvolvimento, chamados de sprints, para permitir que os requisitos sejam detalhados e entregues de forma gradual.

*(Fonte: E-book, Unidade 1 [citado como Unidade 2 no AVA], Página(s) do e-book: 36, 37 e 38)*

De acordo com o texto, qual dos seguintes fatores é mais relevante na priorização de requisitos quando a equipe tem pouca experiência com a tecnologia envolvida no projeto? Com base no exposto, avalie as afirmativas a seguir.

**I.** A facilidade de aprendizado da tecnologia e o menor risco para o projeto.
**II.** A proximidade com o cliente ou usuários para melhor entendimento do domínio.
**III.** A facilidade de aprendizado da tecnologia e o maior risco para o projeto.

É correto o que se afirma em:

- [x] **A. I, apenas.** *(Resposta Correta)*
- [ ] **B.** III, apenas.
- [ ] **C.** I, II e III.
- [ ] **D.** II e III, apenas.
- [ ] **E.** I e II, apenas.

> **Justificativa Oficial (E-book, Unidade 1, Parte 2 — "Requisitos de Software", p. 37 do livro / p. 39 do PDF):**
> Na página 37 do livro, os fatores "Experiência com a tecnologia" e "Experiência no domínio de aplicação" são separados de forma bem distinta:
> - **Experiência com a tecnologia por parte da equipe do projeto (Afirmativa I):** *"a falta de experiência da equipe de desenvolvimento com a tecnologia pode levar à priorização de requisitos que não sejam exatamente os que geram mais valor ao cliente, mas sim **aqueles que possibilitam o aprendizado mais rápido e com menor risco para o projeto como um todo**."* (Logo, **I é verdadeira** e **III é falsa**).
> - **Experiência no domínio de aplicação por parte da equipe (Afirmativa II):** *"a falta de experiência da equipe com o **domínio de aplicação** requer cuidados redobrados na priorização [...] Nesses casos, a proximidade com o usuário, cliente ou seus representantes é fundamental."* Como a pergunta indaga especificamente sobre quando a equipe tem pouca experiência com a **tecnologia** (e não com o domínio de negócio), apenas a afirmativa **I** responde ao comando da questão.

---

### Questão 6 (0,2 / 0,2 ponto) — Múltipla Escolha

**Enunciado:**
Embora Casos de Uso e Histórias de Usuário sejam excelentes para elicitar requisitos em sistemas com forte interação do usuário por meio de interfaces, eles não são a ferramenta mais adequada para todos os tipos de projeto. A escolha da técnica de especificação deve ser sempre guiada pela natureza da complexidade do *software* a ser construído.

Identifique o tipo de sistema para o qual as abordagens centradas na interação (Histórias de Usuário e Casos de Uso) são consideradas menos eficazes.

- [ ] **A.** Aplicações móveis e *web* com múltiplas interfaces de usuário e *stakeholders* distintos.
- [x] **B. Sistemas intensivos em processamento, como rotinas *batch*, algoritmos de inteligência artificial ou processamento de *big data*.** *(Resposta Correta)*
- [ ] **C.** Projetos em que a rastreabilidade dos requisitos desde a concepção até o teste é uma prioridade.
- [ ] **D.** Sistemas de informação (*back-office*) com grande volume de formulários e regras de negócio complexas.
- [ ] **E.** Sistemas cujo controle está na mão do usuário, com muitas interações por meio de interfaces com o usuário.

> **Justificativa Oficial (E-book, Unidade 2, Parte 4 — "Especificação de Requisitos Funcionais Utilizando Histórias de Usuário", p. 170 do livro / p. 172 do PDF):**
> Na seção **"Aplicações, limitações e complementações"**:
> *"Tanto casos de uso quanto histórias do usuário são excelentes para elicitar requisitos de sistemas cujo controle está na mão do usuário, ou seja, sistemas com muitas interações por meio de interfaces com o usuário. No entanto, para os sistemas cuja complexidade não resida na interação propriamente dita, essas duas ferramentas podem não se aplicar tão bem. **Esse é o caso de sistemas intensivos em processamento, como rotinas batch, processamento de grandes volumes de dados (aplicações de business intelligence, big data), algoritmos de inteligência artificial etc.** Esse também é o caso de sistemas embarcados ou de tempo real (WIEGERS; BEATTY, 2013). Para esses casos, outras abordagens podem ser mais adequadas, como diagramas de máquinas de estado, diagrama de atividades, diagrama de sequência, diagrama de componentes, pseudocódigo etc."*
