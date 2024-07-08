import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('energy_dataset_.csv')
df['Type_of_Renewable_Energy'] = pd.Categorical(df['Type_of_Renewable_Energy'])
df['Grid_Integration_Level'] = pd.Categorical(df['Grid_Integration_Level'])
df['Funding_Sources'] = pd.Categorical(df['Funding_Sources'])

def ash(type,variable):
    if type == 'countplot':
        if variable=='Type_of_Renewable_Energy':
            energy_type_mapping = {
            1: 'Solar',
            2: 'Wind',
            3: 'Hydroelectric',
            4: 'Geothermal',
            5: 'Biomass',
            6: 'Tidal',
            7: 'Wave'
            }
            plt.figure(figsize = (10,6))
            ax = sns.countplot(x=df[variable])
            plt.title(f'Types of Renewable Energy')
            current_ticks = ax.get_xticks()
            new_labels = [energy_type_mapping.get(int(tick + 1), '') for tick in current_ticks]

            ax.set_xticklabels(new_labels)

            plt.ylim(2000, 2250)
    
            plt.show()
        elif variable == 'Grid_Integration_Level':
            grid_integration_mapping = {
            1: 'Fully Integrated',
            2: 'Partially Integrated',
            3: 'Minimal Integration',
            4: 'Isolated Microgrid'
             }
            plt.figure(figsize=(10, 6))
            ax = sns.countplot(x=df[variable])
            plt.title(f'Grid Integration Levels')
            current_ticks = ax.get_xticks()
            new_labels = [grid_integration_mapping.get(int(tick + 1), '') for tick in current_ticks]
            ax.set_xticklabels(new_labels)

            plt.ylim(3600, 3900)
            plt.show()
        elif variable == 'Funding_Sources':
            funding_sources_mapping = {
                1: 'Government',
                2: 'Private',
                3: 'Public-Private Partnership'
            }

            plt.figure(figsize=(10, 6))
            ax = sns.countplot(x=df['Funding_Sources'])
            plt.title('Funding Sources')

            current_ticks = ax.get_xticks()
            new_labels = [funding_sources_mapping.get(int(tick + 1), '') for tick in current_ticks]

            ax.set_xticklabels(new_labels)

            plt.ylim(4700, 5100)
            plt.show()
        else:
            return 'there is no count plot for this variable'
    elif type == 'histogram':
        plt.figure(figsize=(10, 6))
        sns.histplot(df[variable], kde=True)
        plt.title(f'Distribution of {variable}')
        plt.ylim(500, 700)
        plt.show()
    elif type == 'boxplot':
        plt.figure(figsize=(10, 6))
        sns.boxplot(y=df[variable])
        plt.title(f'Box Plot of {variable}')
        plt.show()
    elif type == 'pie_chart':
            by_energy_type = df.groupby('Type_of_Renewable_Energy')[variable].sum()

            sns.set(style='whitegrid')  
            sns.set_palette('muted')  

            plt.figure(figsize=(8, 8))
            plt.pie(by_energy_type.values, labels=by_energy_type.index, autopct='%1.1f%%')
            plt.title('Jobs Created by Renewable Energy Type')
            plt.axis('equal')
            plt.show()
        
        
