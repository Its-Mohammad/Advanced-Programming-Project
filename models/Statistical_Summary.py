import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('energy_dataset_.csv')
df['Type_of_Renewable_Energy'] = pd.Categorical(df['Type_of_Renewable_Energy'])
df['Grid_Integration_Level'] = pd.Categorical(df['Grid_Integration_Level'])
df['Funding_Sources'] = pd.Categorical(df['Funding_Sources'])


pd.options.display.float_format = '{:.2f}'.format

numeric_df = df.select_dtypes(include = 'number')
categorical_col = df.select_dtypes(include = 'category')

summary = df.describe()
mean = numeric_df.mean()
median = numeric_df.median()
mode = df.mode().iloc[0]
range = (numeric_df.max() - numeric_df.min())
variance = numeric_df.var()
