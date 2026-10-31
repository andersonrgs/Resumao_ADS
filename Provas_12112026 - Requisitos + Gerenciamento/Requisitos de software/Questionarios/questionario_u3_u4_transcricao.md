# Questionário Unidades 3 e 4 — Requisitos de Software (Transcrição e Validação Pré-Envio)

- **Disciplina:** Requisitos de Software (ADS — Unilasalle 2026/2)
- **Avaliação:** Questionário Unidades 3 e 4 (G1)
- **Pontuação Total Projetada:** **2,0 / 2,0 pontos (100% — todas as 6 alternativas selecionadas estão corretas!)**
- **Referência Oficial:** E-book *Requisitos de Software* (SAGAH / Editora LaSalle, 366 páginas)

---

## Quadro de Conferência Rápida (Pré-Envio no AVA)

| Questão | Peso | Alternativa Selecionada no Print | Gabarito Validado no E-book | Status da Seleção | Página de Prova no E-book |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Pergunta 1** | 0,2 | **D** | **D** | **100% CORRETA** | Unidade 3, Parte 4, p. 261 (PDF p. 263) |
| **Pergunta 2** | 0,4 | **E** | **E** | **100% CORRETA** | Unidade 4, Parte 2, p. 309 (PDF p. 311) |
| **Pergunta 3** | 0,4 | **D** | **D** | **100% CORRETA** | Unidade 4, Parte 3 e 4, p. 313 e 337 (PDF p. 315 e 339) |
| **Pergunta 4** | 0,4 | **B** | **B** | **100% CORRETA** | Unidade 4, Parte 2, p. 303 (PDF p. 305) |
| **Pergunta 5** | 0,2 | **A** | **A** | **100% CORRETA** | Unidade 3, Parte 3, p. 244 (PDF p. 246) |
| **Pergunta 6** | 0,4 | **A** | **A** | **100% CORRETA** | Unidade 3, Parte 3 e 4, p. 227 e 254 (PDF p. 229 e 256) |

---

## Transcrição Completa e Fundamentação no E-book

### Pergunta 1 (0,2 Ponto) — Múltipla Escolha

**Enunciado:**
O processo de Validação de Requisitos pode ser compreendido como um conjunto de três atividades principais: 1) Preparar para a validação (planejamento), 2) Realizar a validação (execução) e 3) Gerenciar os resultados da validação. A etapa de planejamento é fundamental para definir a estratégia, incluindo os produtos de trabalho a serem validados, as restrições, os métodos e técnicas, bem como os critérios de aceitação.

Assinale a alternativa que descreve uma ação tipicamente realizada durante a etapa de Gerenciamento dos resultados da validação, após a conclusão da execução.

- [ ] **A.** Definir quais métodos e técnicas serão empregados na validação, bem como os respectivos critérios de aceitação.
- [ ] **B.** Definir que produtos de trabalho (artefatos) serão validados (documentos ou o próprio código).
- [ ] **C.** Identificar as restrições que podem existir para que a validação seja executada, como recursos e prazos.
- [x] **D. Analisar as anomalias encontradas, identificar e priorizar as ações necessárias, podendo requerer uma nova rodada do processo de validação.** *(Selecionado — CORRETA)*
- [ ] **E.** Formalizar o aceite do produto pelo cliente, mesmo que anomalias de baixa gravidade tenham sido encontradas.

> **Validação no E-book (Unidade 3, Parte 4 — "Validação de Requisitos de Software", p. 261 do livro / p. 263 do PDF):**
> *"Quando a validação estiver concluída, é preciso **gerenciar os resultados**. Se o produto estiver de acordo com o esperado, basta formalizar o aceite e dar por encerrado o processo de validação, seguindo com o projeto/versão para as demais atividades. **Caso anomalias tenham sido encontradas, elas deverão ser analisadas e as ações necessárias deverão ser identificadas, priorizadas e executadas. Nova rodada do processo de validação pode ser requerida, nesses casos.**"*
>
> *Por que as demais estão incorretas?*
> - **A, B e C** descrevem tarefas da primeira atividade (**Preparar a validação**, listadas na p. 261 do livro / p. 263 do PDF).
> - **E** é falsa porque o aceite só é formalizado imediatamente se o produto estiver de acordo com o esperado; quando há anomalias (erros nos requisitos), o erro deve obrigatoriamente ser corrigido antes que prossiga para a implementação (p. 268 do livro / p. 270 do PDF).

---

### Pergunta 2 (0,4 Ponto) — Múltipla Escolha

**Enunciado:**
O controle de versão é um dos pilares do gerenciamento de requisitos e envolve atividades como definir um esquema de identificação e rastrear versões individuais e do conjunto de requisitos. Dentro desse contexto, é fundamental estabelecer um ponto de referência estável e acordado para o desenvolvimento do projeto, a partir do qual outros artefatos serão gerados.

Assinale a alternativa que define corretamente o conceito de *baseline* de requisitos.

- [ ] **A.** É o conjunto de requisitos que possui o maior risco de instabilidade ou que apresenta a maior prioridade de negócio no início do projeto.
- [ ] **B.** É o artefato final e mais detalhado que contém todas as especificações de caso de uso e requisitos não funcionais, pronto para a entrega ao cliente.
- [ ] **C.** É a lista completa e exaustiva de todas as pendências (TBD) que precisam ser resolvidas antes que a fase de testes de aceitação possa ser iniciada.
- [ ] **D.** Representa uma versão volátil dos requisitos, usada apenas durante as atividades de elicitação e análise inicial pela equipe de desenvolvimento.
- [x] **E. É uma versão estável dos requisitos, acordada entre a equipe de desenvolvimento e os *stakeholders*, que serve como base para gerar todos os demais artefatos do projeto.** *(Selecionado — CORRETA)*

> **Validação no E-book (Unidade 4, Parte 2 — "Gerenciamento de Requisitos", p. 309 do livro / p. 311 do PDF):**
> Na subseção **"Baseline de requisitos"**:
> *"Quando um conjunto de requisitos é acordado entre a equipe de desenvolvimento e os stakeholders, então, ele passa a constituir o que denominamos **baseline de requisitos**. **Uma baseline pode ser compreendida como uma versão estável dos requisitos, que será usada como base para gerar os demais artefatos do projeto, incluindo o código.** Quando um conjunto de requisitos é acordado, ele será a base para gerar as especificações detalhadas, as interfaces, os casos de teste e o próprio código."*

---

### Pergunta 3 (0,4 Ponto) — Múltipla Escolha

**Enunciado:**
A Engenharia de Requisitos é a disciplina que estrutura as atividades necessárias para a correta concepção e acompanhamento dos requisitos de software. Ela é dividida em dois grandes grupos de atividades, que possuem focos distintos, mas que devem ser executados de forma integrada.

Compare os dois grandes grupos de atividades da Engenharia de Requisitos e identifique a alternativa que associa corretamente as atividades ao grupo de *Desenvolvimento dos Requisitos*.

- [ ] **A.** O grupo de *Desenvolvimento dos Requisitos* lida com o acompanhamento do *status* e o controle de mudanças, deixando a validação e a especificação para o outro grupo.
- [ ] **B.** O grupo de *Desenvolvimento dos Requisitos* compartilha as atividades de elicitação e validação, mas lida com a especificação e o outro grupo com a rastreabilidade.
- [ ] **C.** As atividades de análise e especificação são exclusivas do *Gerenciamento dos Requisitos*, pois envolvem artefatos formais.
- [x] **D. O grupo de *Desenvolvimento dos Requisitos* engloba a compreensão do contexto, a elicitação, a análise, a especificação e a validação.** *(Selecionado — CORRETA)*
- [ ] **E.** O grupo de *Desenvolvimento dos Requisitos* foca na rastreabilidade e no controle de versão, enquanto o outro grupo concentra-se na elicitação e na análise.

> **Validação no E-book (Unidade 4, Parte 3, p. 313 do livro / p. 315 do PDF; e Parte 4, p. 337 do livro / p. 339 do PDF):**
> *"A engenharia de requisitos está organizada em dois grandes grupos de atividades: o desenvolvimento dos requisitos e o gerenciamento dos requisitos. **No desenvolvimento dos requisitos estão concentradas as atividades relacionadas à compreensão do contexto do projeto, elicitação, análise, especificação e validação dos requisitos.** Já no gerenciamento dos requisitos estão concentradas as atividades relacionadas com a rastreabilidade, o acompanhamento do status, o controle de versão e o controle de mudanças nos requisitos."*

---

### Pergunta 4 (0,4 Ponto) — Múltipla Escolha

**Enunciado:**
Mesmo com a adoção das melhores práticas de Engenharia de Requisitos e um processo de Gerenciamento de Requisitos bem estabelecido, as solicitações de mudança são uma realidade inevitável no ciclo de vida do software. Essas alterações podem ter diversas origens, muitas delas externas ao processo de desenvolvimento, mas internas à estrutura organizacional.

Identifique qual das seguintes situações é uma causa para a mudança de requisitos que se origina de uma reestruturação ou nova direção interna da organização.

- [ ] **A.** A análise de dados de projetos anteriores ou encerrados revela anomalias que estavam ocultas e precisam ser corrigidas ou adaptadas no sistema atual.
- [x] **B. A gerência da organização implementa uma mudança em sua operação, levando a alterações nas funcionalidades essenciais ou nas regras de negócio.** *(Selecionado — CORRETA)*
- [ ] **C.** O ambiente tecnológico no qual o sistema está inserido sofre uma grande inovação, exigindo uma resposta da organização em nível técnico.
- [ ] **D.** Alguns usuários finais relembram requisitos que foram esquecidos ou se conscientizam de novas necessidades após o congelamento inicial do escopo.
- [ ] **E.** Uma nova regulamentação ou lei governamental que força a adaptação do sistema a um novo conjunto de normas legais.

> **Validação no E-book (Unidade 4, Parte 2 — "Gerenciamento de Requisitos", p. 302–303 do livro / p. 304–305 do PDF):**
> Na seção **"2 Impacto das solicitações de mudança"**, o texto cita as seis causas abrangentes de mudança segundo Chemuturi (2013):
> 1. O ambiente no qual a organização opera sofreu uma mudança à qual a organização precisa responder;
> 2. **"a gerência da organização pode realizar uma mudança na sua operação e isso pode levar a mudanças nas funcionalidades essenciais dos requisitos;"** *(correspondente exatamente à alternativa B e à origem de reestruturação ou nova direção interna da organização)*;
> 3. Alguns dos usuários finais podem ter esquecido de alguns requisitos e lembrado de novos requisitos depois que os requisitos foram congelados;
> 4. Uma nova lei, regulamentação ou ato governamental pode causar mudanças depois que os requisitos foram congelados;
> 5. Atividades de melhoria de processos podem fazer com que algumas práticas de negócio sejam modificadas;
> 6. A análise dos dados de projetos encerrados pode revelar algumas anomalias que podem resultar em mudanças nos requisitos.

---

### Pergunta 5 (0,2 Ponto) — Múltipla Escolha

**Enunciado:**
A verificação de requisitos é uma atividade que pode ocorrer de diversas formas, desde a revisão por pares até a utilização de *checklists*. A aplicação de testes de *software*, no entanto, é a técnica mais utilizada para a verificação, especialmente quando o artefato a ser verificado é o código implementado. O planejamento dos testes deve ser realizado em paralelo ou logo após a definição dos requisitos, pois isso auxilia no esclarecimento de pontos obscuros e no refinamento das especificações.

Analise o principal benefício de desenvolver os casos de teste concomitantemente ou logo após a definição dos requisitos de software.

- [x] **A. Os testes ajudam a esclarecer pontos obscuros dos requisitos, facilitando o refinamento das especificações e identificando problemas logo no início do ciclo.** *(Selecionado — CORRETA)*
- [ ] **B.** O desenvolvimento dos testes mais cedo garante que a equipe de testes possa finalizar seu trabalho antes da codificação, acelerando o *deploy*.
- [ ] **C.** A elaboração dos testes é exclusiva para requisitos não funcionais, pois os requisitos funcionais são validados apenas pelo usuário final.
- [ ] **D.** O planejamento antecipado dos testes elimina a necessidade de revisões por pares ou o uso de *checklists* para a verificação de requisitos.
- [ ] **E.** A escrita de casos de teste no início garante que o produto final passe diretamente para o ambiente de produção, sem a necessidade de homologação.

> **Validação no E-book (Unidade 3, Parte 3 — "Verificação de Requisitos de Software", p. 244 do livro / p. 246 do PDF):**
> No quadro **"Fique atento"** da página 244:
> *"O grande benefício do desenvolvimento dos testes concomitantemente aos requisitos, ou logo após esses, é que **os testes ajudam a esclarecer pontos obscuros dos requisitos. Refinamentos são possíveis sobre os requisitos, uma vez que se busca as formas para testá-lo**. Visão similar foi incorporada pelos métodos ágeis, como se verá adiante."*

---

### Pergunta 6 (0,4 Ponto) — Múltipla Escolha

**Enunciado:**
A Verificação de Requisitos é uma atividade essencial na Engenharia de Software, distinta da Validação, mas ambas fazem parte da etapa genérica de validação de requisitos. Seu propósito, segundo a norma ISO/IEC/IEEE 12207, é providenciar evidência objetiva de que o sistema ou elemento do sistema cumpre integralmente os requisitos e características especificados. O processo busca ativamente identificar anomalias (erros, defeitos e falhas) em qualquer item de informação ou artefato do ciclo de vida.

Assinale a alternativa que apresenta corretamente a distinção formal entre Verificação e Validação de requisitos, conforme a norma ISO/IEC/IEEE 12207 e o modelo CMMI-DEV 2.0.

- [x] **A. Verificação é a confirmação de que os requisitos especificados foram atendidos, e Validação é a confirmação de que o requisito foi atendido para um uso ou aplicação pretendidos específicos.** *(Selecionado — CORRETA)*
- [ ] **B.** Verificação é uma atividade realizada exclusivamente pela equipe de desenvolvimento (teste de unidade), e Validação é uma atividade realizada pelo usuário final (teste de aceitação).
- [ ] **C.** Verificação analisa se foi construído o produto certo, ou seja, aquele que os stakeholders desejavam, e Validação analisa se o produto foi construído certo, de forma correta.
- [ ] **D.** Verificação é a atividade de encontrar anomalias nos requisitos, enquanto Validação é a atividade de corrigir os erros nos artefatos de software.
- [ ] **E.** Verificação confirma que o requisito foi atendido para um uso pretendido ("você está construindo a coisa certa"), enquanto Validação confirma que os requisitos especificados foram atendidos ("você está construindo certo").

> **Validação no E-book (Unidade 3, Parte 3, p. 227–228 do livro / p. 229–230 do PDF; e Parte 4, p. 254–255 do livro / p. 256–257 do PDF):**
> De acordo com a norma internacional **ISO/IEC/IEEE 12207 (2017, p. 10–11)**:
> - **Validação** é *"a confirmação, por meio do fornecimento de evidência objetiva, que o requisito foi atendido para um uso ou aplicação pretendidos específicos"*. No **CMMI-DEV 2.0 (2018, p. 525)**: *"demonstra que a solução vai atender seu uso pretendido no ambiente alvo, isto é, 'você está construindo a coisa certa'"* (construir o **produto certo**).
> - **Verificação** é *"a confirmação, por meio do fornecimento de evidência objetiva, que os requisitos especificados foram atendidos"*. No **CMMI-DEV 2.0 (2018, p. 525)**: *"endereça que o produto de trabalho ou a solução refletem adequadamente os requisitos especificados, isto é, 'você está construindo certo'"* (construir o produto **certo / de forma correta**).
>
> *Atenção às pegadinhas:* As alternativas **C** e **E** invertem os conceitos de Verificação e Validação!
