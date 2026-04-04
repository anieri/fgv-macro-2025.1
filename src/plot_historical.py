import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_historical_crises():
    # Load data
    file_path = 'data/kor_monthly_macro.csv'
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return
    
    df = pd.read_csv(file_path, index_col=0, parse_dates=True)
    
    # Forward fill quarterly GDP to make it "monthly" for plotting purposes
    # and interpolate other series if needed for smooth lines
    df_plot = df.copy()
    df_plot['Real_GDP_Q'] = df_plot['Real_GDP_Q'].ffill()
    
    os.makedirs('plots/historical', exist_ok=True)
    sns.set_theme(style="whitegrid")

    # 1. Long term Inflation and M2 (1960-2024)
    plt.figure(figsize=(12, 6))
    plt.plot(df_plot.index, df_plot['CPI_YoY'], label='CPI Inflation (YoY %)', color='red')
    plt.title('South Korea: Long-term Inflation (1960-2024)')
    plt.ylabel('Percentage %')
    plt.legend()
    plt.savefig('plots/historical/long_term_inflation.png')
    plt.close()

    # 2. Oil Crises Focus (1970-1985)
    df_oil = df_plot.loc['1970-01-01':'1985-12-31']
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(df_oil.index, df_oil['CPI_YoY'], label='CPI Inflation', color='red', lw=2)
    ax1.set_ylabel('Inflation Rate (%)', color='red')
    ax2 = ax1.twinx()
    ax2.plot(df_oil.index, df_oil['Real_GDP_Q'], label='Real GDP (Proxy)', color='blue', alpha=0.5)
    ax2.set_ylabel('Real GDP Level', color='blue')
    plt.title('South Korea: The Oil Crises Period (1970-1985)')
    fig.tight_layout()
    plt.savefig('plots/historical/oil_crises_detailed.png')
    plt.close()

    # 3. 2008 Crisis Focus (2005-2012)
    df_2008 = df_plot.loc['2005-01-01':'2012-12-31']
    plt.figure(figsize=(12, 6))
    plt.plot(df_2008.index, df_2008['Ind_Prod'], label='Industrial Production', color='green')
    plt.plot(df_2008.index, df_2008['Unemployment'], label='Unemployment Rate', color='orange')
    plt.title('South Korea: 2008 Financial Crisis Impact')
    plt.ylabel('Index / Percentage')
    plt.legend()
    plt.savefig('plots/historical/crisis_2008_detailed.png')
    plt.close()

    # 4. Pandemic Focus (2018-2024)
    df_covid = df_plot.loc['2018-01-01':'2024-12-31']
    plt.figure(figsize=(12, 6))
    plt.plot(df_covid.index, df_covid['CPI_YoY'], label='Inflation (YoY)', color='red')
    plt.plot(df_covid.index, df_covid['Unemployment'], label='Unemployment', color='orange')
    plt.title('South Korea: COVID-19 Pandemic and Post-Pandemic Inflation')
    plt.ylabel('Percentage %')
    plt.legend()
    plt.savefig('plots/historical/covid_pandemic_detailed.png')
    plt.close()

    print("Historical plots saved to plots/historical/")

if __name__ == "__main__":
    plot_historical_crises()
