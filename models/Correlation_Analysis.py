import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('energy_dataset_.csv')
df['Type_of_Renewable_Energy'] = pd.Categorical(df['Type_of_Renewable_Energy'])
df['Grid_Integration_Level'] = pd.Categorical(df['Grid_Integration_Level'])
df['Funding_Sources'] = pd.Categorical(df['Funding_Sources'])
def heat_map():
    correlation_matrix = df.corr()

    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot = True, cmap='Blues', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()
def corr_scatter():
    df_continus = df[['Installed_Capacity_MW','Energy_Production_MWh','Energy_Consumption_MWh','Energy_Storage_Capacity_MWh','Initial_Investment_USD',
                  'Financial_Incentives_USD','GHG_Emission_Reduction_tCO2e','Air_Pollution_Reduction_Index']]
    sns.set_theme(style="ticks")
    sns.pairplot(df_continus)