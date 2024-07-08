import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('energy_dataset_.csv')
df['Type_of_Renewable_Energy'] = pd.Categorical(df['Type_of_Renewable_Energy'])
df['Grid_Integration_Level'] = pd.Categorical(df['Grid_Integration_Level'])
df['Funding_Sources'] = pd.Categorical(df['Funding_Sources'])

contingency_table1 = pd.crosstab(df['Type_of_Renewable_Energy'],df['Grid_Integration_Level'])
contingency_table2 = pd.crosstab(df['Type_of_Renewable_Energy'],df['Funding_Sources'])
contingency_table3 = pd.crosstab(df['Grid_Integration_Level'],df['Funding_Sources'])