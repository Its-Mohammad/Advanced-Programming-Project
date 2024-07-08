import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from scipy.stats import chi2_contingency
from sklearn.preprocessing import StandardScaler
# Load the dataset
df = pd.read_csv('energy_dataset_.csv')


# Convert columns to categorical
df['Type_of_Renewable_Energy'] = pd.Categorical(df['Type_of_Renewable_Energy'])
df['Grid_Integration_Level'] = pd.Categorical(df['Grid_Integration_Level'])
df['Funding_Sources'] = pd.Categorical(df['Funding_Sources'])

# Title and introduction
st.title('Energy Dataset Analysis')
st.write('This dashboard provides insights and visualizations for the energy dataset.')

# Sidebar Filters
st.sidebar.title('Filters')
energy_types = st.sidebar.multiselect(
    'Choose Energy Types',
    ['Solar','Wind','Hydroelectric','Geothermal','Biomass','Tidal','Wave'])
grid_integration_levels = st.sidebar.multiselect(
    'Choose Grid Integration Levels',
    ['Fully Integrated', 'Partially Integrated', 'Minimal Integration', 'Isolated Microgrid'])

# Filter Data
filtered_df = df.copy()


# Create Tabs
tabs = st.tabs(["Overview", "Distributions", "Relationships","pie chart","Line Graphs", "Network Graph", "Correlation", "Statistical Tests"])

with tabs[0]:
    st.header("Overview")
    st.write("## Dataset")
    st.write(filtered_df)
    st.write("## Summary Statistics")
    st.write(filtered_df.describe())

with tabs[1]:
    st.header("Distributions")
    # Types of Renewable Energy
    st.write("## Types of Renewable Energy")
    energy_type_mapping = {
        1: 'Solar',
        2: 'Wind',
        3: 'Hydroelectric',
        4: 'Geothermal',
        5: 'Biomass',
        6: 'Tidal',
        7: 'Wave'
    }

    plt.figure(figsize=(10, 6))
    ax = sns.countplot(x='Type_of_Renewable_Energy', data=filtered_df,color='darkslategray')
    plt.title('Types of Renewable Energy')

    current_ticks = ax.get_xticks()
    new_labels = [energy_type_mapping.get(int(tick + 1), '') for tick in current_ticks]
    ax.set_xticklabels(new_labels)
    plt.ylim(2000,2250)
    st.pyplot(plt)

    # Installed Capacity
    st.write("## Installed Capacity")
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_df['Installed_Capacity_MW'], kde=True, color='darkslategray')
    plt.title('Distribution of Installed Capacity')
    plt.ylim(500, 700)
    st.pyplot(plt)
    
    # Energy Production
    st.write("## Energy Production")
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_df['Energy_Production_MWh'], kde=True, color='darkslategray')
    plt.title('Distribution of Energy Production')
    plt.ylim(500, 650)
    st.pyplot(plt)

    # Energy Consumption
    st.write("## Energy Consumption")
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_df['Energy_Consumption_MWh'], kde=True,color='darkslategray')
    plt.title('Distribution of Energy Consumption')
    plt.ylim(500, 650)
    st.pyplot(plt)

    # Energy Storage Capacity
    st.write("## Energy Storage Capacity")
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_df['Energy_Storage_Capacity_MWh'], kde=True,color='darkslategray')
    plt.title('Distribution of Energy Storage Capacity')
    plt.ylim(500, 640)
    st.pyplot(plt)

    # Storage Efficiency
    st.write("## Storage Efficiency")
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_df['Storage_Efficiency_Percentage'], kde=True,color='darkslategray')
    plt.title('Distribution of Storage Efficiency')
    plt.ylim(500, 700)
    st.pyplot(plt)
    
    #Grid Integration Level
    grid_integration_mapping = {
        1: 'Fully Integrated',
        2: 'Partially Integrated',
        3: 'Minimal Integration',
        4: 'Isolated Microgrid'
    }
    filtered_df['Grid_Integration_Level_Label'] = filtered_df['Grid_Integration_Level'].map(grid_integration_mapping)
    st.write('## Grid Integration Level')
    plt.figure(figsize=(10, 6))
    ki = sns.countplot(x=filtered_df['Grid_Integration_Level_Label'], color='darkslategray')
    plt.title('Grid Integration Levels')

    plt.ylim(3600, 3900)
    st.pyplot(plt)
    
    #Initial Investment
    
    st.warning("## Initial Investment")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Initial_Investment_USD'], kde=True, color='darkslategray')
    plt.title('Distribution of Initial Investment')
    plt.ylim(500, 680)
    st.pyplot(plt)
    
    #Funding Sources
    st.write("## Funding Sources")
    funding_sources_mapping = {
    1: 'Government',
    2: 'Private',
    3: 'Public-Private Partnership'
    }
    filtered_df['Funding_Sources_Label'] = filtered_df['Funding_Sources'].map(funding_sources_mapping)

    plt.figure(figsize=(10, 6))
    ax = sns.countplot(x=filtered_df['Funding_Sources_Label'], color='darkslategray')
    plt.title('Funding Sources')

    plt.ylim(4700, 5100)
    st.pyplot(plt)
    
    #Financial Incentives
    st.write('## Financial Incentives')
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Financial_Incentives_USD'], kde=True, color='darkslategray')
    plt.title('Distribution of Financial Incentives')
    plt.ylim(500, 680)
    st.pyplot(plt)
    #GHG Emission Reduction tCO2e
    st.write('## GHG Emission Reduction tCO2e')
    plt.figure(figsize=(10, 6))
    sns.histplot(df['GHG_Emission_Reduction_tCO2e'], kde=True, color='darkslategray')
    plt.title('Distribution of GHG Emission Reduction tCO2e')
    plt.ylim(500, 680)
    st.pyplot(plt)
    
    #Air Pollution Reduction
    st.write("## Air Pollution Reduction")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Air_Pollution_Reduction_Index'], kde=True, color='darkslategray')
    plt.title('Distribution of Air Pollution Reduction')
    plt.ylim(500, 660)
    st.pyplot(plt)

    #Jobs Created
    st.write("## Jobs Created")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Jobs_Created'], kde=False, color='darkslategray')
    plt.title('Histogram for Jobs Created')
    plt.ylim(540, 660)
    st.pyplot(plt)

with tabs[2]:

    # Violin Plot of Energy Production by Grid Integration Level
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='Type_of_Renewable_Energy', y='Energy_Production_MWh', data=df, color='lightblue')
    plt.title('Violin Plot of Energy Production by Type of Renewable Energy')
    st.pyplot(plt)

    # Density Plot of Energy Production and Consumption
    st.write("## Density Plot of Energy Production and Consumption")
    plt.figure(figsize=(10, 6))
    sns.kdeplot(filtered_df['Energy_Production_MWh'], shade=True, label='Energy Production')
    sns.kdeplot(filtered_df['Energy_Consumption_MWh'], shade=True, label='Energy Consumption')
    plt.title('Density Plot of Energy Production and Consumption')
    plt.legend()
    st.pyplot(plt)

with tabs[3]:
    st.header("Pie Charts")
    energy_type_mapping = {
        1: 'Solar',
        2: 'Wind',
        3: 'Hydroelectric',
        4: 'Geothermal',
        5: 'Biomass',
        6: 'Tidal',
        7: 'Wave'
    }

    # Convert values in 'Type_of_Renewable_Energy' to names
    filtered_df['Type_of_Renewable_Energy'] = filtered_df['Type_of_Renewable_Energy'].map(energy_type_mapping)
    # Jobs Created by Renewable Energy Type
    st.write("## Jobs Created by Renewable Energy Type")
    jobs_by_energy_type = filtered_df.groupby('Type_of_Renewable_Energy')['Jobs_Created'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(jobs_by_energy_type.values, labels=jobs_by_energy_type.index, autopct='%1.1f%%')
    plt.title('Jobs Created by Renewable Energy Type')
    plt.axis('equal')
    st.pyplot(plt)
    st.write("## Installed Capacity by MW Renewable Energy Type")
    Installed_Capacity_MW_energy_type = filtered_df.groupby('Type_of_Renewable_Energy')['Installed_Capacity_MW'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(Installed_Capacity_MW_energy_type.values, labels=Installed_Capacity_MW_energy_type.index, autopct='%1.1f%%')
    plt.title('Installed Capacity MW by Renewable Energy Type')
    plt.axis('equal')
    st.pyplot(plt)
    
    st.write("## Energy Production MWh by MW Renewable Energy Type")
    Energy_Production_MWh_energy_type = filtered_df.groupby('Type_of_Renewable_Energy')['Energy_Production_MWh'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(Energy_Production_MWh_energy_type.values, labels=Energy_Production_MWh_energy_type.index, autopct='%1.1f%%')
    plt.title('Energy Production MWh by Renewable Energy Type')
    plt.axis('equal')
    st.pyplot(plt)
    
    st.write("## Energy Consumption MWh by MW Renewable Energy Type")
    Energy_Consumption_MWh_energy_type = filtered_df.groupby('Type_of_Renewable_Energy')['Energy_Consumption_MWh'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(Energy_Consumption_MWh_energy_type.values, labels=Energy_Consumption_MWh_energy_type.index, autopct='%1.1f%%')
    plt.title('Energy Consumption MWh by Renewable Energy Type')
    plt.axis('equal')
    st.pyplot(plt)
    
    st.write("## Energy Storage Capacity MWh by MW Renewable Energy Type")
    Energy_Storage_Capacity_MWh_energy_type = filtered_df.groupby('Type_of_Renewable_Energy')['Energy_Storage_Capacity_MWh'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(Energy_Storage_Capacity_MWh_energy_type.values, labels=Energy_Storage_Capacity_MWh_energy_type.index, autopct='%1.1f%%')
    plt.title('Energy Storage Capacity MWh by Renewable Energy Type')
    plt.axis('equal')
    st.pyplot(plt)
    
    st.write("## Initial Investment USD by Renewable Energy Type")
    Initial_Investment_USD_energy_type = filtered_df.groupby('Type_of_Renewable_Energy')['Initial_Investment_USD'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(Initial_Investment_USD_energy_type.values, labels=Initial_Investment_USD_energy_type.index, autopct='%1.1f%%')
    plt.title('Initial Investment USD by Renewable Energy Type')
    plt.axis('equal')
    st.pyplot(plt)

    st.write("## Financial Incentives USD by Renewable Energy Type")
    Financial_Incentives_USD_energy_type = filtered_df.groupby('Type_of_Renewable_Energy')['Financial_Incentives_USD'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(Financial_Incentives_USD_energy_type.values, labels=Financial_Incentives_USD_energy_type.index, autopct='%1.1f%%')
    plt.title('Financial Incentives USD by Renewable Energy Type')
    plt.axis('equal')
    st.pyplot(plt)
    
    st.write("## GHG Emission Reduction tCO2e by Renewable Energy Type")
    GHG_Emission_Reduction_tCO2e_energy_type = filtered_df.groupby('Type_of_Renewable_Energy')['GHG_Emission_Reduction_tCO2e'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(GHG_Emission_Reduction_tCO2e_energy_type.values, labels=GHG_Emission_Reduction_tCO2e_energy_type.index, autopct='%1.1f%%')
    plt.title('Financial Incentives USD by Renewable Energy Type')
    plt.axis('equal')
    st.pyplot(plt)
    
    st.write("## Air Pollution Reduction Index by Renewable Energy Type")
    Air_Pollution_Reduction_Index_energy_type = filtered_df.groupby('Type_of_Renewable_Energy')['Air_Pollution_Reduction_Index'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(Air_Pollution_Reduction_Index_energy_type.values, labels=Air_Pollution_Reduction_Index_energy_type.index, autopct='%1.1f%%')
    plt.title('Financial Incentives USD by Renewable Energy Type')
    plt.axis('equal')
    st.pyplot(plt)
    
    
    
with tabs[4]:
    st.header("Line Graphs")
    df2 = df.copy(deep = True)
    numeric_columns = df2.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()

    df2[numeric_columns] = scaler.fit_transform(df2[numeric_columns])
    grid_integration_mapping = {
            1: 'Fully Integrated',
            2: 'Partially Integrated',
            3: 'Minimal Integration',
            4: 'Isolated Microgrid'
        }
    df2['Grid_Integration_Level_Label'] = df2['Grid_Integration_Level'].map(grid_integration_mapping)
    variables = ['Installed_Capacity_MW','Storage_Efficiency_Percentage', 'Initial_Investment_USD', 'Financial_Incentives_USD']

    plt.figure(figsize=(15, 10))
    for variable in variables:
     sns.lineplot(x='Grid_Integration_Level_Label', y=variable, data=df2, marker='o', label=variable)

    plt.xlabel('Grid Integration Level')
    plt.ylabel('Value')
    plt.title('Relationship between Grid Integration Level and other Variables')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    
    energy_type_mapping = {
        1: 'Solar',
        2: 'Wind',
        3: 'Hydroelectric',
        4: 'Geothermal',
        5: 'Biomass',
        6: 'Tidal',
        7: 'Wave'
    }
    df2['Type_of_Renewable_Energy_Label'] = df2['Type_of_Renewable_Energy'].map(energy_type_mapping)
    variables = ['Installed_Capacity_MW', 'Energy_Production_MWh', 'Energy_Consumption_MWh', 'Energy_Storage_Capacity_MWh',
             'Storage_Efficiency_Percentage','Air_Pollution_Reduction_Index']

    plt.figure(figsize=(15, 10))
    for variable in variables:
      sns.lineplot(x='Type_of_Renewable_Energy_Label', y=variable, data=df2, marker='o', label=variable)

    plt.xlabel('Grid Integration Level')
    plt.ylabel('Value')
    plt.title('Relationship between Type of Renewable Energy and other Variables')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    
    funding_sources_mapping = {
    1: 'Government',
    2: 'Private',
    3: 'Public-Private Partnership'
    }
    df2['Funding_Sources_Label'] = df2['Funding_Sources'].map(funding_sources_mapping)
    variables = ['Installed_Capacity_MW', 'Energy_Production_MWh', 'Energy_Consumption_MWh', 'Energy_Storage_Capacity_MWh',
             'Storage_Efficiency_Percentage', 'Initial_Investment_USD', 'Financial_Incentives_USD', 'GHG_Emission_Reduction_tCO2e',
             'Air_Pollution_Reduction_Index', 'Jobs_Created']

    plt.figure(figsize=(15, 10))
    for variable in variables:
     sns.lineplot(x='Funding_Sources_Label', y=variable, data=df2, marker='o', label=variable)

    plt.xlabel('Funding Sources')
    plt.ylabel('Value')
    plt.title('Relationship between Funding Sources and other Variables')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

with tabs[5]:
    st.header("Network Graph")

    # Network Graph
    st.write("## Network Graph of Renewable Energy Types and Attributes")

    # Create a new graph
    G = nx.Graph()

    energy_types = df['Type_of_Renewable_Energy'].unique()
    for energy_type in energy_types:
        G.add_node(energy_type, type='energy')

    attributes = ['Jobs_Created', 'Energy_Production_MWh']
    for attribute in attributes:
        G.add_node(attribute, type='attribute')

    for energy_type in energy_types:
        subset = df[df['Type_of_Renewable_Energy'] == energy_type]
        for attribute in attributes:
            if subset[attribute].sum() > 0:
                G.add_edge(energy_type, attribute, weight=subset[attribute].sum())

    plt.figure(figsize=(15, 15))
    pos = nx.spring_layout(G, k=0.3, iterations=300, seed=42)

    node_colors = ['skyblue' if G.nodes[node]['type'] == 'energy' else 'lightgreen' for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=3000, edgecolors='k', linewidths=1.5)

    nx.draw_networkx_edges(G, pos, width=2)

    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    edge_labels = {(u, v): G[u][v]['weight'] for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title('Network Graph of Renewable Energy Types and Attributes')
    st.pyplot(plt)

with tabs[6]:
    st.header("Correlation")

    # Correlation Heatmap
    st.write("## Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(df.corr(), annot = True, cmap='Blues', linewidths=0.5)
    st.pyplot(fig)

with tabs[7]:
    st.header("Statistical Tests")

    
    contingency_table1 = pd.crosstab(filtered_df['Type_of_Renewable_Energy'], filtered_df['Grid_Integration_Level_Label'])
    st.write("### Contingency Table 1: Type of Renewable Energy vs Grid Integration Level")
    st.write(contingency_table1)
    st.write("Chi-square Test:")
    chi2, p, dof, ex = chi2_contingency(contingency_table1)
    st.write(f"Chi2: {chi2}, p-value: {p}, dof: {dof}")

    contingency_table2 = pd.crosstab(filtered_df['Type_of_Renewable_Energy'], filtered_df['Funding_Sources_Label'])
    st.write("### Contingency Table 2: Type of Renewable Energy vs Funding Sources")
    st.write(contingency_table2)
    st.write("Chi-square Test:")
    chi2, p, dof, ex = chi2_contingency(contingency_table2)
    st.write(f"Chi2: {chi2}, p-value: {p}, dof: {dof}")

    contingency_table3 = pd.crosstab(filtered_df['Grid_Integration_Level_Label'], filtered_df['Funding_Sources_Label'])
    st.write("### Contingency Table 3: Grid Integration Level vs Funding Sources")
    st.write(contingency_table3)
    st.write("Chi-square Test:")
    chi2, p, dof, ex = chi2_contingency(contingency_table3)
    st.write(f"Chi2: {chi2}, p-value: {p}, dof: {dof}")

# Footer
st.markdown("---")
st.markdown("Created by Mohammad Babaee/Pooneh Rahiminejad/Mahdis Shahkolaei")







