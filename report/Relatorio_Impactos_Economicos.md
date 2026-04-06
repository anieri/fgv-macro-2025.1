---
header-includes:
  - \usepackage{float}
  - \let\origfigure\figure
  - \let\endorigfigure\endfigure
  - \renewenvironment{figure}[1][2]{\origfigure[H]}{\endorigfigure}
---

# Relatório de Análise Macroeconômica: Coreia do Sul (1970-2025)

## 1. Introdução
Este trabalho analisa a trajetória de resiliência da economia da Coreia do Sul frente às grandes crises globais dos últimos 50 anos: as Crises do Petróleo (anos 70/80), a Crise Financeira Global (2008) e a Pandemia de COVID-19, culminando no cenário atual (2022-2025). O objetivo é identificar como os canais de transmissão e o ambiente institucional coreano permitiram que o país passasse de uma economia em desenvolvimento para uma liderança tecnológica global, utilizando o arcabouço teórico de Carlin & Soskice (2015).

## 2. Desempenho Econômico Prévio
Antes da primeira crise do petróleo, a Coreia do Sul iniciou sua "Milagre do Rio Han". Nos anos 60, o país abandonou a substituição de importações em favor de uma Industrialização Orientada para a Exportação (EOI). O PIB crescia a taxas de dois dígitos, impulsionado pela indústria leve (têxteis e calçados) e por uma coordenação centralizada que começou a formar os conglomerados conhecidos como **Chaebols**.

---

## 3. Impactos Econômicos das Crises (Item 3)

### 3.1. As Crises do Petróleo (1970-1985)

#### 3.1.1. Canais de Transmissão e Lado da Oferta
Como um país totalmente dependente de importações de energia, o choque de 1973 e 1979 atingiu a Coreia via **custos de produção**. A transmissão foi imediata para a base industrial pesada (HCI Drive) que estava sendo construída.
*   **Valor Adicionado (V.A.):** A Indústria (Ind_VA) sofreu pressões severas de custos, mas o governo manteve o foco na expansão da infraestrutura e química pesada para garantir o produto potencial futuro.

![Valor Adicionado por Setor: Crise do Petróleo](../plots/pt-br/1.%20Crise%20do%20Petroleo_oferta.png){width=85%}

#### 3.1.2. Lado da Demanda
A demanda foi sustentada artificialmente via **Investimento (I)** massivo. O governo direcionou crédito barato ("Policy Loans") para as Chaebols continuarem seus projetos de siderurgia e construção naval, mesmo com a queda da demanda global por consumo.
*   **Componentes:** O gráfico de demanda mostra que as exportações (X) e o investimento (I) foram os motores que evitaram um colapso total inicial. Note que todos os componentes estão expressos em **USD constantes de 2015** para permitir a comparação direta de escalas.

![Componentes da Demanda (USD 2015): Crise do Petróleo](../plots/pt-br/1.%20Crise%20do%20Petroleo_demanda.png){width=85%}

#### 3.1.3. Desequilíbrios Macroeconômicos e Financeiros
O impacto mais visível foi a **inflação**, que saltou para **29,2% em 1974**. O déficit em conta corrente explodiu devido ao custo da energia, e a dívida externa cresceu rapidamente para financiar o modelo HCI.
*   **Juros Reais:** Durante a fase de acomodação, os juros reais foram frequentemente negativos, o que ajudou no financiamento das empresas mas alimentou a espiral inflacionária.
*   **Gestão da Dívida:** A dívida externa em relação ao RNB saltou durante este período, tornando o país vulnerável ao cenário de juros internacionais.

![Estrutura de Endividamento: Crise do Petróleo](../plots/pt-br/1.%20Crise%20do%20Petroleo_divida.png){width=85%}

![Política Monetária e Hiato: Crise do Petróleo](../plots/pt-br/1.%20Crise%20do%20Petroleo_monetario.png){width=85%}

#### 3.1.4. Política Cambial e Competitividade
A Coreia utilizou desvalorizações agressivas do Won para manter a competitividade das exportações frente ao choque de custos. O câmbio real (q) depreciou significativamente após 1980.

![Evolução do Câmbio (Nominal e Real): Crise do Petróleo](../plots/pt-br/1.%20Crise%20do%20Petroleo_cambio.png){width=85%}

#### 3.1.5. Ambiente Institucional e Confiança
A relação Estado-Chaebol foi o pilar da resiliência. O governo atuava como garantidor de última instância (Decreto de 3 de Agosto). O mercado de trabalho era rigidamente controlado, com o salário real crescendo abaixo da produtividade para garantir a competitividade externa.

### 3.2. A Crise Financeira Global (2007-2012)

#### 3.2.1. Canais de Transmissão e Lado da Demanda
Em 2008, o choque foi de **demanda externa**. A Coreia já era uma potência exportadora integrada. A queda repentina na renda mundial causou um recuo de 40% nas exportações mensais.
*   **Consumo (C) e Investimento (I):** Houve uma queda brusca inicial na confiança, mas a resposta fiscal rápida (Green New Deal) substituiu a demanda externa pela demanda pública (G). Todos os valores estão em USD 2015.

![Componentes da Demanda (USD 2015): Crise de 2008](../plots/pt-br/2.%20Crise%20Financeira_demanda.png){width=85%}

#### 3.2.2. Lado da Oferta e Produção
A Indústria coreana demonstrou agilidade. Setores de semicondutores e automotivo aproveitaram a crise de concorrentes globais para expandir *market share*. O valor adicionado da indústria recuperou-se em formato de "V" já em 2009.

![Valor Adicionado por Setor: Crise de 2008](../plots/pt-br/2.%20Crise%20Financeira_oferta.png){width=85%}

#### 3.2.3. Desequilíbrios Macroeconômicos e Estrutura de Dívida
Diferente de 1997, a Coreia possuía reservas sólidas. O endividamento privado (setor bancário e corporativo) foi monitorado de perto, embora o crédito ao setor privado tenha permanecido em patamares elevados.

![Estrutura de Endividamento: Crise de 2008](../plots/pt-br/2.%20Crise%20Financeira_divida.png){width=85%}

#### 3.2.4. Política Cambial como Amortecedor
A Coreia utilizou a **taxa de câmbio** como principal amortecedor. O Won depreciou de 914 para 1.449 por dólar, restaurando a competitividade das exportações e movendo a economia ao longo da curva BT.

![Evolução do Câmbio (Nominal e Real): Crise de 2008](../plots/pt-br/2.%20Crise%20Financeira_cambio.png){width=85%}

#### 3.2.5. Ambiente Institucional e Confiança
O Índice de Confiança Empresarial (BCI) recuperou-se rapidamente após os pacotes de estímulo. A estabilidade dos salários reais permitiu que as empresas mantivessem margens durante a fase de depreciação cambial.

![Confiança e Ciclo: Crise de 2008](../plots/pt-br/2.%20Crise%20Financeira_institucional.png){width=85%}

### 3.3. A Pandemia COVID-19 (2019-2024)

#### 3.3.1. Canais de Transmissão e Choque Misto
A pandemia foi um choque simultâneo: queda no consumo doméstico (isolamento) e ruptura de oferta global (chips e frete).
*   **Demanda:** O consumo das famílias (C) caiu inicialmente, mas as exportações tecnológicas (X) compensaram. Todos os componentes estão em USD 2015.

![Componentes da Demanda (USD 2015): Pandemia](../plots/pt-br/3.%20Pandemia_demanda.png){width=85%}

#### 3.3.2. Lado da Oferta e Resiliência Setorial
A Coreia evitou lockdowns totais (Estratégia K-Bangyeok), preservando a produção industrial. O setor de Serviços sofreu, mas foi compensado pelo salto no V.A. da Indústria de Alta Tecnologia.

![Valor Adicionado por Setor: Pandemia](../plots/pt-br/3.%20Pandemia_oferta.png){width=85%}

#### 3.3.3. Desequilíbrios Macroeconômicos e Salto na Dívida
Houve um salto inédito na **Dívida Pública**, que passou de 37% para quase 50% do PIB devido aos sucessivos orçamentos suplementares. O crédito ao setor privado também continuou a crescer, gerando preocupações prudenciais.

![Estrutura de Endividamento: Pandemia](../plots/pt-br/3.%20Pandemia_divida.png){width=85%}

#### 3.3.4. Câmbio e Liquidez
A volatilidade do Won foi contida por swaps com o Fed e pelo uso das reservas internacionais, mantendo o câmbio real em níveis competitivos.

![Evolução do Câmbio (Nominal e Real): Pandemia](../plots/pt-br/3.%20Pandemia_cambio.png){width=85%}

#### 3.3.5. Ambiente Institucional e Saúde
A confiança do consumidor (CCI) foi severamente testada, mas a liderança tecnológica (Samsung, SK) e a gestão eficiente da saúde pública (K-Bangyeok) mantiveram a Coreia como um dos melhores desempenhos da OCDE.

![Indicadores de Saúde e Ciclo: Pandemia](../plots/pt-br/3.%20Pandemia_saude.png){width=85%}

### 3.4. Quadro Atual e Novos Desafios (2022-2025)

#### 3.4.1. Demanda e Inflação Pós-Pandemia
O cenário atual é de normalização monetária. A inflação retornou gradualmente à meta, mas o alto endividamento privado limita o crescimento do consumo (C).

![Componentes da Demanda (USD 2015): Quadro Atual](../plots/pt-br/4.%20Quadro%20Atual_demanda.png){width=85%}

#### 3.4.2. Ambiente de Confiança e Dívida Privada
O grande desequilíbrio atual não é público, mas **privado**. O crédito ao setor privado é o maior componente do endividamento coreano, tornando a economia sensível aos juros.

![Estrutura de Endividamento: Quadro Atual](../plots/pt-br/4.%20Quadro%20Atual_divida.png){width=85%}

#### 3.4.3. Câmbio e Geopolítica
O Won enfrenta pressões pela divergência de juros com os EUA e pelas tensões geopolíticas nas cadeias de suprimentos.

![Evolução do Câmbio (Nominal e Real): Quadro Atual](../plots/pt-br/4.%20Quadro%20Atual_cambio.png){width=85%}

#### 3.4.4. Confiança e Ciclo

---

## 4. Ações de Política Econômica (Item 4)

### 4.1. Política Fiscal
*   **Anos 70/80:** HCI Drive – Investimento direto do Estado em indústria pesada e química.
*   **2008:** Green New Deal – Foco em infraestrutura sustentável e estímulo à demanda agregada.
*   **Pandemia:** Korean New Deal – Estímulo à digitalização e auxílios emergenciais diretos.

### 4.2. Política Monetária
O Banco da Coreia (BoK) evoluiu para um regime de metas de inflação rigoroso. Em 2008, o corte agressivo de juros foi coordenado com swaps cambiais. Na pandemia, o juro foi a zero, seguido por uma reancoragem preventiva (MR) que colocou a taxa em 2,0% em 2023 para combater o repasse inflacionário.

---

## 5. Análise via Modelos Teóricos (Item 5)

### 5.1. O Modelo IS-PC-MR
A evolução da Coreia pode ser visualizada pelos deslocamentos das curvas:
*   **Choques de Oferta (Petróleo):** PC desloca para cima. A resposta foi "subir" pela MR com juros altos para quebrar a inércia (Estado C).
*   **Choques de Demanda (2008):** IS desloca para a esquerda. A resposta foi "descer" pela MR e usar a política fiscal para empurrar a IS de volta (Estado C).

![Evolução Teórica IS-PC-MR: Pandemia](../plots/pt-br/3.%20Pandemia_evolucao_ISPCMR.png){width=85%}

### 5.2. O Modelo AD-BT-ERU
A competitividade coreana reside na gestão do câmbio real ($q$) e na produtividade:
*   Nas crises, a depreciação de $q$ move a economia para a direita ao longo da curva **BT**.
*   A política industrial (K-Chips Act) visa deslocar a curva **ERU para a direita**, aumentando o salário real sustentável através da liderança tecnológica.

![Evolução Teórica AD-BT-ERU: 2008](../plots/pt-br/2.%20Crise%20Financeira_evolucao_ADBTERU.png){width=85%}

---

## 6. Desempenho Após as Crises
A Coreia do Sul demonstrou recuperações em "V" em quase todos os episódios. Após 1980, consolidou a indústria pesada; após 2008, dominou o mercado de eletrônicos; após 2020, emergiu como líder na transição para veículos elétricos e biotecnologia.

## 7. Lições das Crises
1.  **Flexibilidade Cambial:** Atuou como amortecedor vital em 2008 e 2020.
2.  **Coordenação Institucional:** A agilidade na resposta fiscal e monetária conjunta é o diferencial coreano.
3.  **Investimento em Oferta:** Nunca negligenciar o lado da produtividade (PS/ERU) mesmo em crises de demanda.

## 8. Conclusão
A análise das crises revela que a Coreia do Sul não apenas sobreviveu aos choques, mas os utilizou para reestruturar sua base produtiva. A transição de um modelo de custos baixos para um de alta tecnologia permitiu que o país mantivesse sua resiliência exportadora, embora os desafios da dívida privada e da demografia exijam novas rodadas de inovação institucional.

---
*Relatório Macroeconômico (2026.1). Fontes: FRED, Banco Mundial (WDI), Bank of Korea (BoK), OCDE.*
