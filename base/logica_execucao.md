# Lógica de Execução e Engenharia de Dados

Este documento descreve a racionalidade técnica aplicada pelo agente para resolver o problema de análise macroeconômica da Coreia do Sul (1960-2024).

## 1. Estratégia de Aquisição de Dados

### Fontes Utilizadas
- **FRED (St. Louis Fed):** Utilizado para dados de alta frequência (Mensal e Trimestral) por sua rapidez e confiabilidade via API `pandas_datareader`.
- **World Bank (WDI):** Utilizado para indicadores estruturais e anuais (Saúde, Valor Adicionado Setorial, Dívida Pública) via biblioteca `wbgapi`.

### Desafio das Frequências
A análise exige a integração de dados Mensais (M), Trimestrais (Q) e Anuais (A).
- **Abordagem:** Criar um DataFrame mestre com índice mensal.
- **Tratamento:** Não utilizamos interpolação forçada para preservar a integridade das fontes originais. O `SocioEconomicDataLoader` une os datasets mantendo `NaN` nos períodos sem reporte, e o visualizador é instruído a ignorar esses `NaN` para plotar pontos/linhas conforme a disponibilidade (usando `dropna()` no momento da plotagem).

---

## 2. Engenharia de Variáveis e Métricas

### Hiato do Produto (Output Gap)
Fundamental para o modelo IS-PC-MR.
- **Método:** Filtro Hodrick-Prescott (HP) aplicado ao logaritmo do PIB Real Trimestral.
- **Parâmetro:** $\lambda = 1600$ (padrão para dados trimestrais).
- **Cálculo:** $Gap = \frac{y - y_{tendência}}{y_{tendência}} \times 100$.

### Taxa de Juros Real
Calculada para analisar a postura da política monetária.
- **Fórmula:** $r = i - \pi$ (Taxa Nominal - Inflação YoY).

---

## 3. Lógica de Visualização

### Eixo Duplo (Twin Axis) no Modelo AD-BT-ERU
- **Problema:** A inclinação da curva AD é muito maior que a das curvas BT e ERU, fazendo com que estas últimas parecessem "achatadas" no mesmo gráfico.
- **Solução:** O eixo esquerdo foca na escala da AD, enquanto o eixo direito fornece um "zoom" (range reduzido em torno de $\bar{q} = 1$) para as curvas BT e ERU, garantindo legibilidade.

### Formatação de Escalas Dinâmicas
- **Problema:** Valores em Won ou USD frequentemente atingiam magnitudes de trilhões, gerando notação científica (`1e12`) nos eixos.
- **Solução:** Função `_format_axis_labels` que detecta a magnitude do dado e formata o rótulo para "Trilhões", "Bilhões" ou "Milhões", ajustando o sufixo no título do eixo.

### Identidade Visual
- Uso de `plt.axhline(0)` em destaque para o Hiato do Produto e Juros Reais, permitindo identificar instantaneamente períodos de expansão/contração e juros reais negativos.

---

## 4. Estrutura de Arquivos e Funções

- `src/data_loader.py`: Concentra toda a lógica de API e limpeza.
- `src/models.py`: Implementa as classes matemáticas das curvas teóricas.
- `src/visualizer.py`: Motor de plotagem com suporte a PT-BR e escalas dinâmicas.
- `main.py`: Orquestrador que executa o fluxo completo: Carga -> Cálculo -> Plotagem.
- `report/`: Pasta com os achados analíticos finais baseados nas evidências geradas.
