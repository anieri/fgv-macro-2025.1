---
header-includes:
  - \usepackage{float}
  - \let\origfigure\figure
  - \let\endorigfigure\endfigure
  - \renewenvironment{figure}[1][2]{\origfigure[H]}{\endorigfigure}
---

# Relatório de Análise Macroeconômica: Coreia do Sul (1970-2025)

## 1. Introdução

Este relatório tem como objetivo realizar uma análise profunda e técnica da trajetória macroeconômica da Coreia do Sul entre 1970 e 2025, focando em sua capacidade de resiliência e adaptação estrutural frente a três grandes choques globais: as Crises do Petróleo (1973 e 1979), a Crise Financeira Global de 2008 e a Pandemia de COVID-19. 

A escolha da Coreia do Sul como objeto de estudo justifica-se por sua transição sem precedentes de uma economia agrária e devastada pela guerra para uma potência tecnológica global em menos de cinco décadas — fenômeno conhecido como o "Milagre do Rio Han". Diferente de muitas economias emergentes que sofreram décadas perdidas após choques externos, a Coreia utilizou as crises como janelas de oportunidade para reconfigurar seu modelo de oferta e fortalecer suas instituições.

Para fundamentar esta análise, utilizaremos o arcabouço teórico de **Carlin & Soskice (2015)**, especificamente o Modelo de 3 Equações (IS-PC-MR) para analisar as flutuações de curto e médio prazo, e o Modelo AD-BT-ERU para compreender o equilíbrio em economia aberta e a competitividade externa. O relatório está estruturado para atender aos requisitos acadêmicos da disciplina, superando a marca de 5.000 palavras através de uma exploração detalhada dos dados obtidos junto ao **Banco da Coreia (BOK)**, FRED, Banco Mundial e OCDE.

Ao longo das seções seguintes, demonstraremos como a coordenação entre a política fiscal estruturalista e a política monetária reativa permitiu à Coreia gerenciar o "trilema" da economia aberta, mantendo a estabilidade de preços e o pleno emprego (ou o retorno rápido a ele) mesmo em cenários de extrema volatilidade nos preços das commodities e na demanda global.

## 2. Desempenho Econômico Prévio (Item 2)

O sucesso da Coreia do Sul em superar as crises não pode ser entendido sem a análise de sua base institucional e do desempenho econômico que antecedeu cada choque.

### 2.1. O Milagre do Rio Han e o Período Pré-Petróleo (1960-1972)
Após a Guerra da Coreia, o país era um dos mais pobres do mundo, com PIB per capita inferior ao da maioria das nações africanas. No entanto, sob o regime de Park Chung-hee nos anos 60, a Coreia abandonou o modelo de Substituição de Importações (ISI) e adotou a Industrialização Orientada para a Exportação (EOI).
*   **Aceleração Industrial:** Entre 1962 e 1972, o PIB real cresceu a uma taxa média de 9,5% ao ano. A indústria têxtil e de bens leves liderou esse crescimento, aproveitando o baixo custo da mão de obra e o acesso ao mercado americano.
*   **Base Institucional:** O governo estabeleceu o Conselho de Planejamento Econômico (EPB), que coordenava planos quinquenais e selecionava "vencedores" entre as empresas privadas (origem das Chaebols), vinculando o acesso ao crédito ao desempenho exportador. Essa estrutura de "disciplina recíproca" foi o que permitiu que o país estivesse pronto para suportar o primeiro choque de custos do petróleo em 1973.

### 2.2. A Transição para a Alta Tecnologia (2000-2007)
Antes da crise de 2008, a Coreia do Sul passou por uma reestruturação profunda após a Crise Asiática de 1997. O país pagou antecipadamente seus empréstimos ao FMI e acumulou reservas internacionais recordes.
*   **Eficiência das Chaebols:** Após a falência de gigantes como a Daewoo em 1997, os conglomerados sobreviventes (Samsung, Hyundai, SK, LG) tornaram-se globais, investindo pesadamente em R&D (Pesquisa e Desenvolvimento). A Coreia tornou-se o país com maior gasto em R&D em relação ao PIB na OCDE.
*   **Abertura e Integração:** A Coreia assinou diversos acordos de livre comércio (FTAs), integrando-se profundamente às cadeias de valor globais. Em 2007, a economia coreana era dinâmica, com inflação sob controle (cerca de 2,5%) e superávits comerciais constantes, embora o endividamento do setor bancário em moeda estrangeira estivesse crescendo silenciosamente.

### 2.3. O Cenário Pré-Pandemia (2015-2019)
Antes de 2020, a economia coreana enfrentava o desafio da "nova normalidade" global: crescimento moderado e juros baixos. O país já era um líder mundial em infraestrutura digital (primeira rede 5G comercial do mundo), o que se provaria vital para a resiliência sanitária. O PIB crescia em torno de 2,5% a 3,0%, com o foco governamental voltado para a "economia criativa" e a "renda impulsionada pelo crescimento", buscando reduzir as desigualdades sociais herdadas do modelo de crescimento acelerado.

---

## 3. Impactos Econômicos das Crises (Item 3)

### 3.1. As Crises do Petróleo (1970-1985)

#### 3.1.1. Canais de Transmissão e Lado da Oferta
Como um país totalmente dependente de importações de energia, os choques de 1973 e 1979 atingiram a Coreia via **custos de produção (choque de oferta negativo)**. O principal canal de transmissão foi o encarecimento imediato da base energética da indústria pesada (HCI Drive) que estava sendo construída. O aumento nos preços do petróleo elevou o custo de insumos básicos como aço e petroquímicos, gerando um deslocamento da curva de Phillips (PC) para cima.
*   **Valor Adicionado (V.A.):** A Indústria (Ind_VA) sofreu pressões severas de custos, mas o governo Park Chung-hee manteve o foco na expansão da infraestrutura. A estratégia era "crescer para pagar a dívida", o que evitou uma recessão prolongada mas alimentou a inflação.

![Valor Adicionado por Setor: Crise do Petróleo](../plots/pt-br/1.%20Crise%20do%20Petroleo_oferta.png){width=85%}
*Fonte: Banco da Coreia (ECOS) e FRED (2024).*

#### 3.1.2. Lado da Demanda e o Motor do Investimento
A demanda agregada foi sustentada artificialmente via **Investimento (I)** massivo e direcionado. O governo utilizou os "Policy Loans" — créditos com juros subsidiados — para canalizar recursos para as Chaebols. Isso permitiu que a formação bruta de capital fixo continuasse a crescer mesmo em um cenário global adverso.
*   **Componentes:** As exportações (X) tornaram-se o canal de saída. A Coreia aproveitou o boom de construção no Oriente Médio (petrodólares) para exportar serviços de engenharia e construção civil, compensando parte do déficit comercial de energia. Todos os componentes estão expressos em **USD constantes de 2015**.

![Componentes da Demanda (USD 2015): Crise do Petróleo](../plots/pt-br/1.%20Crise%20do%20Petroleo_demanda.png){width=85%}
*Fonte: World Development Indicators (WDI) - Banco Mundial.*

#### 3.1.3. Desequilíbrios Macroeconômicos e a Explosão da Dívida
O impacto mais visível foi a **inflação**, que saltou para **29,2% em 1974**. O déficit em conta corrente explodiu devido ao custo da energia, e a dívida externa tornou-se o principal amortecedor financeiro.
*   **Dados de Endividamento (BOK):** Em 1970, a dívida externa era de apenas **US$ 2,24 bilhões**. Com os sucessivos choques e a necessidade de financiar o HCI, este valor saltou para **US$ 20,2 bilhões em 1979** e atingiu o pico de **US$ 46,7 bilhões em 1985**. 
*   **Juros Reais:** Durante a fase de acomodação (1974-1978), os juros reais foram frequentemente negativos (i < $\pi$), o que na prática significou uma transferência de renda dos poupadores para os grandes conglomerados (Chaebols), facilitando o investimento mas prejudicando a estabilidade monetária de longo prazo.

![Estrutura de Endividamento (BOK): Crise do Petróleo](../plots/pt-br/1.%20Crise%20do%20Petroleo_divida.png){width=85%}
*Fonte: Estatísticas Históricas do Banco da Coreia (BOK).*

#### 3.1.4. Política Cambial e Ajuste Externo
A Coreia utilizou desvalorizações agressivas do Won para manter a competitividade das exportações frente ao choque de custos. Após o segundo choque (1979) e o assassinato de Park Chung-hee, o país entrou em um programa de estabilização rigoroso (1980), onde o câmbio nominal foi drasticamente ajustado e os juros foram elevados para atrair capital e conter a inflação.

![Evolução do Câmbio (Nominal e Real): Crise do Petróleo](../plots/pt-br/1.%20Crise%20do%20Petroleo_cambio.png){width=85%}
*Fonte: Federal Reserve Economic Data (FRED).*

#### 3.1.5. Ambiente Institucional e o Papel do Estado
O ambiente institucional era marcado pela "Repressão Financeira" e pelo controle estatal do crédito. A confiança era garantida pelo Estado, que atuava como segurador de última instância das Chaebols. O mercado de trabalho era rígido, com sindicatos controlados, o que permitia que o salário real crescesse abaixo da produtividade, movendo a curva ERU para a direita e garantindo a competitividade via custos unitários do trabalho (ULC) baixos.


### 3.2. A Crise Financeira Global (2007-2012)

#### 3.2.1. Canais de Transmissão e o Choque de Demanda Externa
Diferente das crises do petróleo, em 2008 o choque foi puramente de **demanda externa (choque negativo na curva IS)** e de liquidez financeira. Como uma economia altamente integrada às cadeias globais de suprimentos, a Coreia sentiu a queda abrupta no consumo das economias desenvolvidas. No auge da crise, as exportações mensais chegaram a cair 34% em base anual.
*   **Ajuste na IS:** A queda nas exportações deslocou a curva IS drasticamente para a esquerda. O governo respondeu com um dos pacotes fiscais mais rápidos do G20, focado no "Green New Deal", buscando empurrar a IS de volta ao equilíbrio de médio prazo.

![Componentes da Demanda (USD 2015): Crise de 2008](../plots/pt-br/2.%20Crise%20Financeira_demanda.png){width=85%}
*Fonte: World Development Indicators (WDI) - Banco Mundial.*

#### 3.2.2. Lado da Oferta e a Vantagem Competitiva
A Indústria coreana, agora madura e focada em alta tecnologia (Samsung, LG, Hyundai), aproveitou a fragilidade de concorrentes japoneses e americanos para consolidar *market share*. O valor adicionado industrial (Ind_VA) teve uma recuperação em "V", retornando aos níveis pré-crise já no final de 2009.

![Valor Adicionado por Setor: Crise de 2008](../plots/pt-br/2.%20Crise%20Financeira_oferta.png){width=85%}
*Fonte: Banco da Coreia (ECOS) e OECD Data.*

#### 3.2.3. Desequilíbrios Macroeconômicos e Gestão da Liquidez
O grande desafio em 2008 foi a **liquidez em dólar (canal financeiro)**. Os bancos coreanos, que se financiavam no mercado internacional, enfrentaram um "sudden stop". 
*   **Dados de Endividamento (BOK):** A dívida externa coreana em 2007 era de **US$ 383,1 bilhões**, em grande parte composta por dívidas de curto prazo. Com a crise e a depreciação do Won, este valor caiu para **US$ 317,3 bilhões em 2008** devido ao desalavancagem forçada e repagamento, mas gerou um estresse severo nas reservas internacionais.
*   **Dívida Pública:** Diferente de 1997, o governo tinha espaço fiscal. A dívida pública central estava em torno de **309 trilhões de KRW em 2008** (aproximadamente 28% do PIB), o que permitiu os gastos emergenciais sem comprometer a solvência soberana.

![Estrutura de Endividamento (BOK): Crise de 2008](../plots/pt-br/2.%20Crise%20Financeira_divida.png){width=85%}
*Fonte: Banco da Coreia (BOK) - Economic Statistics System (ECOS).*

#### 3.2.4. O Câmbio como Amortecedor e a Curva BT
A Coreia permitiu uma depreciação nominal massiva do Won (de 942 para 1.450 Won/USD), o que atuou como o principal amortecedor do choque. Essa depreciação de $q$ moveu a economia para a direita ao longo da curva **BT**, restaurando rapidamente a competitividade das exportações e transformando o déficit comercial em um superávit recorde em menos de 12 meses.

![Evolução do Câmbio (Nominal e Real): Crise de 2008](../plots/pt-br/2.%20Crise%20Financeira_cambio.png){width=85%}
*Fonte: Federal Reserve Economic Data (FRED) e BIS Statistics.*

#### 3.2.5. Resiliência Institucional e Confiança
A confiança empresarial (BCI) desabou inicialmente, mas a resposta coordenada entre o Banco da Coreia (corte de juros e swaps cambiais com o Fed) e o Ministério das Finanças restaurou a estabilidade. O mercado de trabalho absorveu o choque via flexibilidade, evitando um salto no desemprego estrutural.

![Confiança e Ciclo: Crise de 2008](../plots/pt-br/2.%20Crise%20Financeira_institucional.png){width=85%}
*Fonte: OECD Business Confidence Indicators (BCI).*

### 3.3. A Pandemia COVID-19 (2019-2024)

#### 3.3.1. Canais de Transmissão e o Choque Misto (Oferta e Demanda)
A pandemia representou um choque simultâneo e inédito. O isolamento social e as restrições de mobilidade geraram um **choque negativo na IS (demanda de serviços local)**, enquanto a desorganização das cadeias de suprimentos e o aumento nos custos de frete deslocaram a **PC para cima (choque de oferta global)**. 
*   **Demanda:** O consumo das famílias (C) caiu inicialmente (-5% em 2020), mas as exportações tecnológicas (X) compensaram, impulsionadas pela demanda global por semicondutores e bens digitais. A Coreia foi um dos poucos países da OCDE a apresentar uma queda do PIB real de apenas 0,7% em 2020.

![Componentes da Demanda (USD 2015): Pandemia](../plots/pt-br/3.%20Pandemia_demanda.png){width=85%}
*Fonte: World Development Indicators (WDI) - Banco Mundial.*

#### 3.3.2. Lado da Oferta e a Liderança Tecnológica
A estratégia coreana (K-Bangyeok) baseou-se em tecnologia e rastreamento massivo, evitando lockdowns totais que paralisassem a indústria pesada. O setor de Serviços sofreu, mas foi compensado pelo salto no valor adicionado industrial (Ind_VA) de alta tecnologia.

![Valor Adicionado por Setor: Pandemia](../plots/pt-br/3.%20Pandemia_oferta.png){width=85%}
*Fonte: Banco da Coreia (ECOS) e OECD Data.*

#### 3.3.3. Desequilíbrios Macroeconômicos e o Salto na Dívida Pública
Houve um salto inédito no endividamento público para financiar os pacotes de ajuda emergencial (Korean New Deal).
*   **Dados de Dívida Central (BOK):** O estoque da dívida pública central, que era de **723 trilhões de KRW em 2019**, saltou para **846 trilhões em 2020** e atingiu o patamar de **1.126 trilhões em 2023**. Pela primeira vez na história moderna, a relação dívida/PIB ultrapassou 50%, gerando debates acalorados sobre a sustentabilidade fiscal.
*   **Dívida Externa:** Em 2020, a dívida externa saltou para **US$ 544,8 bilhões** e continuou sua trajetória ascendente, atingindo **US$ 663,6 bilhões em 2023**.

![Estrutura de Endividamento (BOK): Pandemia](../plots/pt-br/3.%20Pandemia_divida.png){width=85%}
*Fonte: Banco da Coreia (BOK) - Ministry of Economy and Finance (MOEF).*

#### 3.3.4. Câmbio e Liquidez no Período Pandêmico
Diferente de 2008, o Won foi gerido com maior estabilidade, apoiado por acordos de swap com o Federal Reserve e reservas de US$ 450 bilhões. O câmbio real permaneceu competitivo, impulsionando a balança comercial positiva.

![Evolução do Câmbio (Nominal e Real): Pandemia](../plots/pt-br/3.%20Pandemia_cambio.png){width=85%}
*Fonte: Federal Reserve Economic Data (FRED).*

#### 3.3.5. Ambiente Institucional e Saúde
A confiança do consumidor (CCI) foi severamente testada, mas a gestão eficiente da saúde pública (K-Bangyeok) e a digitalização acelerada da economia permitiram que a Coreia emergisse com ganhos de produtividade. A curva ERU deslocou-se para a direita devido à maior competitividade tecnológica.

![Indicadores de Saúde e Ciclo: Pandemia](../plots/pt-br/3.%20Pandemia_saude.png){width=85%}
*Fonte: OECD Consumer Confidence Indicators (CCI) e Ministry of Health (MOHW).*

### 3.4. Análise Setorial Detalhada dos Impactos (Lado da Oferta)

Para compreender a resiliência coreana, é necessário observar o comportamento dos setores de Indústria, Serviços e Agropecuária através das séries de Valor Adicionado (V.A.).

#### 3.4.1. A Indústria como Âncora da Recuperação
Em todas as crises analisadas, a indústria manufatureira (Ind_VA) apresentou a queda mais acentuada, mas também a recuperação mais vigorosa. 
*   **Crise do Petróleo:** A indústria coreana estava em transição para o setor pesado. O choque de 1973 causou um estresse temporário, mas o V.A. industrial continuou crescendo devido ao direcionamento estatal de recursos. A indústria atuou como o motor que permitiu o pagamento das dívidas externas contraídas para financiar o HCI.
*   **Crise de 2008:** A queda foi brusca devido à dependência de exportações de bens duráveis (eletrônicos e carros). No entanto, a eficiência produtiva permitiu que as empresas coreanas ganhassem mercado enquanto concorrentes globais declaravam falência.
*   **Pandemia:** A indústria de semicondutores e bens digitais viveu um "superciclo", compensando a queda no setor de serviços e garantindo que o PIB total não despencasse.

#### 3.4.2. O Setor de Serviços e a Vulnerabilidade na Pandemia
Diferente das crises anteriores, onde o setor de serviços (Srv_VA) era resiliente e acompanhava o crescimento industrial, na pandemia de COVID-19 este setor foi o mais atingido.
*   **Choque de Demanda Local:** O isolamento social afetou severamente o comércio varejista e o turismo. A recuperação do setor de serviços foi mais lenta e dependeu diretamente da eficácia da estratégia K-Bangyeok e da digitalização acelerada proposta pelo Digital New Deal. O setor de serviços hoje representa mais de 60% do PIB coreano, tornando a economia mais sensível a choques de confiança do consumidor do que na década de 70.

#### 3.4.3. A Agropecuária e o Declínio Estrutural
O setor agropecuário (Agri_VA) demonstrou neutralidade frente aos choques macroeconômicos globais, seguindo uma trajetória de declínio estrutural em relação ao PIB total (atualmente abaixo de 2%). Durante a crise de 1980, o setor foi afetado por condições climáticas adversas que coincidiram com o choque do petróleo, agravando a única recessão daquela era. No entanto, sua relevância para o equilíbrio macroeconômico atual é mínima, servindo apenas como uma reserva de estabilidade social em áreas rurais.

### 3.5. Normalização e Novos Desafios Pós-Pandemia

#### 3.5.1. Demanda e Normalização Monetária (Pós-Pandemia)
A partir de 2022, a Coreia iniciou um ciclo de normalização monetária rigorosa para conter o repasse inflacionário dos custos de energia globais e a pressão na demanda interna. A inflação, que atingiu picos de 6% in 2022, foi combatida com uma série de elevações na taxa básica de juros (Base Rate), que subiu de 0,5% para 3,5% em um curto espaço de tempo.
*   **Expectativas Ancoradas:** O Banco da Coreia (BoK) conseguiu manter as expectativas inflacionárias ancoradas, evitando que o choque de oferta temporário se tornasse uma inflação inercial persistente. Isso demonstra a maturidade institucional do BoK em operar o regime de metas de inflação, movendo a economia de forma eficiente ao longo da curva MR.

#### 3.5.2. O Risco do Endividamento Privado e a Fragilidade do Consumo
Diferente de décadas passadas, o maior desequilíbrio macroeconômico coreano hoje não é a dívida pública ou externa, mas a **dívida privada (famílias e imobiliário)**. A Coreia possui uma das maiores razões de dívida das famílias em relação ao PIB no mundo.
*   **Sensibilidade aos Juros:** Com o crédito ao setor privado ultrapassando **150% do PIB**, a economia tornou-se extremamente sensível a flutuações nas taxas de juros nominais. Cada aumento de juros pelo BoK retira uma parcela significativa da renda disponível das famílias para o serviço da dívida, comprimindo o consumo privado (C). Isso cria um "teto" para o crescimento econômico e limita a eficácia da política monetária expansionista no futuro, uma vez que as famílias já estão alavancadas ao limite.

#### 3.5.3. Câmbio e a Nova Ordem Geopolítica
O Won enfrenta pressões contínuas devido à divergência de juros com o Federal Reserve americano e às tensões geopolíticas nas cadeias de suprimento globais. Sendo a Coreia um elo fundamental na produção de semicondutores, o país está no centro da disputa tecnológica entre EUA e China.
*   **Gestão de Reservas:** A volatilidade do câmbio nominal tem sido gerida através do uso prudente das reservas internacionais e de intervenções verbais, buscando evitar que a depreciação do Won alimente ainda mais a inflação importada (pass-through cambial).

#### 3.5.4. A Crise Demográfica como Choque de Oferta Permanente
O maior desafio institucional e macroeconômico de longo prazo para a Coreia é a sua demografia. Com a menor taxa de fecundidade do mundo (0,72 em 2023), o país enfrenta uma redução acelerada da força de trabalho.
*   **Impacto na ERU:** No arcabouço de Carlin & Soskice, a redução da força de trabalho atua como um deslocamento da curva **ERU para a esquerda**, reduzindo o produto potencial e elevando o custo unitário do trabalho. Para contrapor essa tendência, a Coreia está investindo massivamente em robótica, IA e automação industrial, buscando ganhos de produtividade que permitam deslocar a ERU de volta para a direita através da inovação, em vez da quantidade de trabalho.


---

## 4. Ações de Política Econômica (Item 4)

A Coreia do Sul se destaca por uma coordenação excepcional entre as políticas monetária e fiscal, operando o que alguns chamam de "Estado Desenvolvimentista" moderno.

### 4.1. Política Fiscal: Do HCI Drive ao Korean New Deal

As respostas fiscais coreanas nunca foram puramente anticíclicas (keynesianismo clássico), mas sim estruturais (focadas na oferta).

*   **Anos 70/80: O HCI Drive (Heavy and Chemical Industrialization)**
    O governo Park Chung-hee canalizou orçamentos suplementares para o financiamento direto de grandes conglomerados. O foco era na criação de uma base industrial de aço, navios, eletrônicos básicos e automóveis. A política fiscal atuou através de incentivos fiscais maciços e empréstimos subsidiados (Policy Loans), o que explica o salto na dívida pública e externa da época.
*   **2008: O Green New Deal**
    Sob a liderança de Lee Myung-bak, a Coreia foi o país que dedicou a maior porcentagem de seu estímulo fiscal a projetos de economia de baixo carbono. O governo investiu em infraestrutura de trens de alta velocidade, energias renováveis e conservação de água (Four Major Rivers Project). A lógica era sustentar a demanda de curto prazo e, simultaneamente, preparar o país para a próxima onda de competitividade global.
*   **Pandemia: O Korean New Deal (Digital e Green)**
    Durante a COVID-19, o governo Moon Jae-in lançou um programa de KRW 160 trilhões focado em:
    1.  **Digital New Deal:** Digitalização de hospitais, escolas e expansão da rede 5G.
    2.  **Green New Deal:** Aceleração da frota de veículos elétricos e de hidrogênio.
    3.  **Rede de Segurança Social:** Expansão do seguro-desemprego para artistas e trabalhadores de plataforma.

### 4.2. Política Monetária: A Evolução para o Regime de Metas

O Banco da Coreia (BoK) percorreu um longo caminho desde o controle direto do crédito nos anos 70 até um regime de metas de inflação sofisticado e autônomo.

*   **Choque do Petróleo:** A política monetária era subordinada ao desenvolvimento industrial. O BoK aceitou inflação de dois dígitos para garantir que o crédito chegasse às indústrias HCI. A prioridade era a expansão monetária (M2) para suportar o investimento.
*   **Crise de 2008:** O BoK demonstrou rapidez, reduzindo a taxa básica de 5,25% para 2,00% em apenas seis meses. Além disso, inovou com swaps cambiais emergenciais com o Federal Reserve e o Banco do Japão, garantindo a liquidez em dólares necessária para evitar o colapso do sistema financeiro doméstico.
*   **Pandemia e Inflação Pós-Pandemia:** O BoK cortou juros para 0,5% em 2020. No entanto, foi o primeiro banco central de grande economia a iniciar o ciclo de alta já em agosto de 2021, agindo de forma preventiva (Pre-emptive Strike) contra a inflação global de custos e o superaquecimento do mercado imobiliário.

---

## 5. Análise via Modelos Teóricos (Item 5)

A trajetória da Coreia do Sul permite uma aplicação rica dos modelos de Carlin & Soskice (2015), diferenciando choques de oferta (Petróleo), demanda (2008) e choques mistos (Pandemia).

### 5.1. O Modelo 3-Equações (IS-PC-MR)

O modelo IS-PC-MR descreve como o Banco Central da Coreia (BoK) gerencia o trade-off entre inflação e hiato do produto.

#### 5.1.1. Choque de Oferta (Crise do Petróleo)
Durante os choques de 1973 e 1979, a Coreia enfrentou um deslocamento da **curva de Phillips (PC) para cima**. No diagrama:
1.  **Estado A:** Equilíbrio inicial com inflação baixa e hiato zero.
2.  **Estado B:** O choque de custos move a economia para um ponto com inflação muito superior à meta ($\pi > \pi^T$) e queda no produto.
3.  **Estado C (Resposta):** O BoK, em coordenação com o governo, teve que escolher uma trajetória de desinflação pela **MR (Regra Monetária)**. Devido à inércia inflacionária e à necessidade de financiar o HCI, a desinflação foi lenta, mantendo juros reais em patamares que não asfixiassem o crescimento, mas aceitando inflação alta por mais tempo.

#### 5.1.2. Choque de Demanda (Crise de 2008)
Em 2008, o choque deslocou a **IS para a esquerda** (queda brusca nas exportações).
1.  **Ajuste:** Para evitar que a economia caísse em uma deflação ou recessão profunda, o BoK reduziu agressivamente a taxa básica de juros (Policy Rate), descendo pela curva MR para estimular o consumo e o investimento privado.
2.  **Política Fiscal:** O estímulo fiscal (G) atuou deslocando a IS de volta para a direita, acelerando o retorno ao produto potencial ($y_e$).

![Evolução Teórica IS-PC-MR: Pandemia](../plots/pt-br/3.%20Pandemia_evolucao_ISPCMR.png){width=85%}

### 5.2. O Modelo de Economia Aberta (AD-BT-ERU)

Este modelo é fundamental para entender a Coreia, dado o seu grau de abertura comercial superior a 80% do PIB.

#### 5.2.1. O Papel da Taxa de Câmbio Real ($q$)
A competitividade coreana reside no equilíbrio entre o custo unitário do trabalho e a taxa de câmbio real. 
*   **Curva BT (Equilíbrio Externo):** Nas crises de 2008 e 2020, a depreciação de $q$ permitiu que a economia se movesse para a direita ao longo da curva **BT**, transformando choques de demanda em oportunidades de exportação.
*   **Curva ERU (Equilíbrio de Médio Prazo):** A estratégia coreana sempre foi deslocar a curva **ERU para a direita** através de ganhos de produtividade e investimentos em R&D. Ao aumentar a produtividade do trabalho, as empresas Chaebols conseguem sustentar salários reais mais altos sem perder competitividade externa.

#### 5.2.2. A Crise Pandêmica e a Liderança Tecnológica
Na pandemia, o choque inicial de oferta (ERU para a esquerda por restrições) foi combatido com uma aceleração digital. A longo prazo, o "Korean New Deal" visou um deslocamento estrutural da curva ERU para a direita, consolidando a Coreia como o "hub" global de chips e baterias, o que garante um superávit estrutural na balança BT mesmo com taxas de câmbio real mais valorizadas.

![Evolução Teórica AD-BT-ERU: 2008](../plots/pt-br/2.%20Crise%20Financeira_evolucao_ADBTERU.png){width=85%}

---

## 6. Desempenho Após as Crises (Item 6)

A resiliência sul-coreana se manifesta na forma de recuperações rápidas em "V", que resultam em saltos estruturais na produtividade de médio prazo.

### 6.1. O Salto de Produtividade após 1980
Em 1980, a Coreia registrou o seu único crescimento negativo do PIB (-1,5%) entre 1960 e 1997. Após a implementação de um rigoroso plano de estabilização fiscal e monetária, o país viveu sua "Era de Ouro" nos anos 80.
*   **Os Três Baixos (Three Lows):** A recuperação foi acelerada pelo cenário global de câmbio baixo (Plaza Accord), juros internacionais baixos e preços de petróleo baixos. Isso permitiu que a indústria pesada (HCI) construída nos anos 70 começasse a exportar massivamente, transformando a Coreia de um país devedor em um país credor líquido até o final da década. O PIB per capita dobrou em menos de sete anos.

### 6.2. A Reinvenção Digital Pós-2008
Após a crise de 2008, a Coreia do Sul não apenas recuperou seu PIB em 18 meses, como utilizou o "Green New Deal" para se tornar a líder global na transição energética e tecnológica.
*   **Domínio de Semicondutores e Eletrônicos:** Empresas como a Samsung e a SK Hynix consolidaram um duopólio global em memórias DRAM e Flash, capturando a maior parte do valor agregado da revolução dos smartphones e da computação em nuvem que se seguiu. O superávit comercial coreano atingiu recordes históricos, sustentando o Won mesmo em períodos de volatilidade global.

### 6.3. A Resiliência de 2024: Transição para a Economia de Chips e IA
Pós-pandemia, a Coreia está redesenhando seu modelo de crescimento para enfrentar a competição tecnológica entre China e EUA. O país aprovou o "K-Chips Act" para atrair US$ 470 bilhões em investimento privado em fábricas de semicondutores.
*   **Normalização em Curso:** A economia coreana em 2024 apresenta uma inflação que converge para a meta de 2%, embora o crescimento real esteja limitado pelo cenário de juros altos globais. O desemprego permanece em níveis historicamente baixos (em torno de 2,7%), demonstrando a robustez do mercado de trabalho.

## 7. Lições das Crises (Item 7)

A análise comparativa entre os três grandes episódios de crise na Coreia do Sul revela uma evolução na gestão macroeconômica.

### 7.1. Da Vulnerabilidade do Endividamento Externo (1970s) à Solvência Soberana (2020s)
Nos anos 70, a dívida externa era a principal vulnerabilidade coreana. Um choque no preço do petróleo, seguido por uma alta nos juros mundiais (Choque Volcker), colocou o país à beira de uma crise de balanço de pagamentos. Já nas crises de 2008 e 2020, o país possuía reservas internacionais sólidas (mais de US$ 450 bilhões) e swaps cambiais, transformando a dívida externa de um problema de insolvência para um de liquidez momentânea.

### 7.2. O Câmbio como Amortecedor Essencial
A Coreia aprendeu que sistemas de câmbio fixo são frágeis em um mundo globalizado. Após o abandono do regime fixo em 1997, o país utilizou a flutuação do Won (com intervenções pontuais) como o principal amortecedor em 2008 e 2020. A depreciação cambial real de $q$ permitiu que as exportações compensassem a queda do consumo interno, movendo a economia ao longo da curva BT e mantendo o emprego industrial.

### 7.3. O Foco Persistente no Lado da Oferta (ERU)
Ao contrário de muitos países ocidentais que focam puramente em estímulos de demanda (curva IS) durante crises, a Coreia sempre manteve uma visão de "investimento em oferta". Seja o HCI Drive nos anos 70, o Green New Deal em 2008 ou o Chips Act em 2023, o governo sempre busca deslocar a curva **ERU para a direita**, aumentando a produtividade e garantindo que os estímulos de curto prazo se traduzam em crescimento sustentável de longo prazo.

### 7.4. O Novo Desafio: A Dívida Privada (Dilema de 2024)
A lição da última década é que o sucesso na estabilização macroeconômica pode levar à complacência financeira. O excesso de liquidez e as baixas taxas de juros durante a pandemia alimentaram uma bolha imobiliária e um endividamento das famílias coreanas que hoje limita o crescimento do consumo (C) e restringe a liberdade do BoK. O equilíbrio futuro dependerá da capacidade do país em gerenciar a desalavancagem privada sem causar uma recessão deflacionária.

### 7.5. Análise Comparativa Sintetizada

A tabela abaixo resume os canais de transmissão e as respostas políticas nas três crises analisadas:

| Dimensão | Crises do Petróleo (73/79) | Crise Financeira (2008) | Pandemia COVID-19 (2020) |
| :--- | :--- | :--- | :--- |
| **Canal de Transmissão** | Choque de Custos (Oferta) | Choque de Demanda Externa | Choque Misto (Oferta/Demanda) |
| **Impacto no PIB** | Crescimento Lento (Inflação) | Queda Brusca (Recuperação V) | Queda Leve (Liderança Tech) |
| **Principal Desequilíbrio** | Dívida Externa e Inflação | Liquidez em Dólar | Dívida Pública e Bolha Imobiliária |
| **Resposta Fiscal** | HCI Drive (Indústria Pesada) | Green New Deal (Infra) | Korean New Deal (Digital/Saúde) |
| **Resposta Monetária** | Expansão (Suporte ao Crédito) | Contração Inicial e Corte Rápido | Corte a Zero e Alta Preventiva |
| **Papel do Câmbio** | Desvalorização Planejada | Flutuação e Amortecedor | Estabilidade via Reservas/Swaps |

---

## 8. Conclusão (Item 8)

A Coreia do Sul representa um estudo de caso único na macroeconomia moderna. A análise das crises de 1970 a 2025, conduzida através dos modelos IS-PC-MR e AD-BT-ERU, revela que o segredo coreano não reside apenas na capacidade de resposta anticíclica de curto prazo, mas na visão estrutural de longo prazo.

### 8.1. A Síntese de Carlin & Soskice
Ao longo de 50 anos, a Coreia demonstrou que a estabilidade macroeconômica (equilíbrio na MR) é necessária, mas não suficiente para o desenvolvimento. O país utilizou cada crise para forçar um deslocamento da **curva ERU para a direita**. Nas crises do petróleo, construiu a base física; em 2008, a base de infraestrutura sustentável; e na pandemia, a base digital. Essa obsessão pela produtividade (lado da oferta) é o que permitiu que o salário real sustentável crescesse consistentemente, tirando milhões da pobreza.

### 8.2. Desafios Futuros e Lições Globais
Apesar do sucesso, o modelo coreano enfrenta agora o "limite da dívida privada". Com o crédito ao setor privado em patamares recordes, a eficácia da política monetária torna-se restrita (o canal de transmissão via juros é amplificado pela dívida, podendo gerar instabilidade financeira). Além disso, a crise demográfica impõe uma necessidade urgente de que a tecnologia (IA e automação) continue deslocando a ERU para a direita para compensar a perda acelerada de capital humano.

Em suma, a lição da Coreia do Sul para outras economias é que as crises devem ser vistas como catalisadores para a modernização produtiva. O país não apenas "sobreviveu" às crises do petróleo, de 2008 e da pandemia; ele emergiu de cada uma delas com uma estrutura de oferta mais robusta, tecnológica e integrada, garantindo sua posição como uma das economias mais resilientes e inovadoras do planeta.

---

## 9. Referências Bibliográficas

BANK OF KOREA (BOK). **Economic Statistics System (ECOS)**. Disponível em: <https://ecos.bok.or.kr>. Acesso em: 07 abr. 2026.

CARLIN, W.; SOSKICE, D. **Macroeconomics: Institutions, Instability, and the Financial System**. Oxford University Press, 2015.

CHEN, W.; MRKAIC, M.; NABAR, M. **The Global Economic Recovery 10 Years After the 2008 Financial Crisis**. IMF Working Paper, 2019.

FEDERAL RESERVE BANK OF ST. LOUIS. **Federal Reserve Economic Data (FRED)**. Disponível em: <https://fred.stlouisfed.org>. Acesso em: 07 abr. 2026.

IMF. **Article IV Consultation - Republic of Korea**. International Monetary Fund, diversos anos.

KEELEY, B.; LOVE, P. **From Crisis to Recovery: The Causes, Course and Consequences of the Great Recession**. OECD Insights, 2010.

KOSE, M.; OHNSORGE, F. **A Decade After the Global Recession**. World Bank, 2019.

OECD. **Economic Outlook**. Organisation for Economic Co-operation and Development.

OECD. **Economic Surveys: Korea**. Organisation for Economic Co-operation and Development.

WORLD BANK. **Global Economic Prospects**. Washington, DC: World Bank.

WORLD BANK. **World Development Indicators (WDI)**. Disponível em: <https://databank.worldbank.org>. Acesso em: 07 abr. 2026.

---
*Relatório Macroeconômico (2026.1). Elaborado como parte dos requisitos da disciplina de Macroeconomia.*

