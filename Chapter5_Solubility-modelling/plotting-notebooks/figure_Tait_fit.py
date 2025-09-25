import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colour import Color
from pathlib import Path
import os

def plot_Tait_fit(
    param_data_file_path='../data/Tait-fit/Tait-fit-params.xlsx',
    exp_file_path='../data/literature-data/pol_PVT.xlsx',
    width=6, height=4,
    display_fig=True, save_fig=True,
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    # Function to calculate the specific volume using the Tait equation
    def V_pol_0(X, a0, a1, a2, B0, B1):
        T_C, p_MPa = X
        C = 0.0894
        B = B0 * np.exp(-B1 * T_C)
        V0 = a0 + a1 * T_C + a2 * T_C**2
        V = V0 * (1 - C * np.log(1 + p_MPa / B))
        
        return V  # [cm^3/g]
    
    # Function to get Tait parameters for a given polymer type
    def get_Tait_params(param_data_file_path, type_name):
        df = pd.read_excel(param_data_file_path)
        
        # Filter
        df = df[df['Polymer'] == type_name].iloc[0]
        
        # Extract Tait parameters
        a0 = df['a0 / cm^3 g^-1']
        a1 = df['a1 / cm^3 g^-1 C^-1']
        a2 = df['a2 / cm^3 g^-1 C^-2']
        B0 = df['B0 / MPa']
        B1 = df['B1 / C^-1']
        
        return a0, a1, a2, B0, B1
    
    # Function to filter experimental data for a given polymer type
    def filter_exp_data(exp_file_path, type_name):
        # df_temp = df[type_name].copy()
        df_exp_filtered = pd.read_excel(exp_file_path, sheet_name=type_name, engine='openpyxl')
        T_C_list = df_exp_filtered['T (°C)'].values.tolist()  # [°C]
        p_MPa_list = df_exp_filtered['P (MPa)'].values.tolist()  # [MPa]
        V_exp = df_exp_filtered['V_pol (cm3/g)'].values.tolist()  # [cm3/g]
        
        return df_exp_filtered, T_C_list, p_MPa_list, V_exp
    
    df_exp = {}
    for name in ['PS_rubbery', 'PS_glassy', 'PMMA_rubbery', 'PMMA_glassy']:
        df_exp[name] = pd.read_excel(exp_file_path, sheet_name=name, engine='openpyxl')
    
    # Function to get variables for plotting
    def get_vars_for_plots(exp_file_path, param_data_file_path, state):
        # Extract values
        df_exp_filtered, T_C_list, p_MPa_list, V_exp = filter_exp_data(exp_file_path, state)
        a0, a1, a2, B0, B1 = get_Tait_params(param_data_file_path, state)
        
        # Get unique values
        pMPa_unq_list = list(set(p_MPa_list))  # [MPa]
        pMPa_unq_list.sort()
        T_C_unq_list = list(set(T_C_list))  # [°C]
        T_C_unq_list.sort()
        
        # Temperature values
        T_C = [None for i in range(len(pMPa_unq_list))]
        V_exp = [None for i in range(len(pMPa_unq_list))]
        V_multiTait = [None for i in range(len(pMPa_unq_list))]
        
        # Temperature values
        for i, p in enumerate(pMPa_unq_list):
            T_C[i] = df_exp_filtered[(df_exp_filtered['P (MPa)'] == p)]['T (°C)'].values.tolist()  # [MPa]
        
        # Get specific volume values
        for i, p in enumerate(pMPa_unq_list):
            V_exp[i] = df_exp_filtered[(df_exp_filtered['P (MPa)'] == p)]['V_pol (cm3/g)'].values.tolist()
            V_multiTait[i] = [V_pol_0((_T_C, p), a0, a1, a2, B0, B1) for _T_C in T_C[i]]
        
        return T_C, V_exp, V_multiTait, pMPa_unq_list
    
    # Plotting
    fig, axes = plt.subplots(2, 2, figsize=(width, height), constrained_layout=True)
    axes = axes.flatten()
    
    for i, state in enumerate(['PS_glassy', 'PS_rubbery', 'PMMA_glassy', 'PMMA_rubbery']):
        # Axis 
        ax = axes[i]
        
        # Get variables for plotting
        T_C, V_exp, V_multiTait, pMPa_unq_list = get_vars_for_plots(exp_file_path, param_data_file_path, state)
        
        # Colour gradient
        colours = list(Color('silver').range_to(Color('maroon'), len(pMPa_unq_list)))  # colour gradient
        
        for j, p in enumerate(pMPa_unq_list):
            # Tait values
            ax.plot(
                T_C[j],
                V_multiTait[j],
                color='%s' % colours[j],
                marker='None',
                linestyle='solid',
                label=f'{p:.0f} MPa',
            )
            # Experimental values
            ax.scatter(
                T_C[j],
                V_exp[j],
                color='%s' % colours[j],
                marker='x',
                label='None',
            )
    
    # Set axis labels
    axes[2].set_xlabel('Temperature / °C')
    axes[3].set_xlabel('Temperature / °C')
    axes[0].set_ylabel(r'$\hat{V}^{0}_\mathrm{pol}$ / $\mathrm{cm^{3} \, g^{-1}}$')
    axes[2].set_ylabel(r'$\hat{V}^{0}_\mathrm{pol}$ / $\mathrm{cm^{3} \, g^{-1}}$')
    
    # Titles
    axes[0].set_title('(a) Glassy PS')
    axes[1].set_title('(b) Rubbery PS')
    axes[2].set_title('(c) Glassy PMMA')
    axes[3].set_title('(d) Rubbery PMMA')
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f'fig_Tait_fit.{save_format}'
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f'Figure saved to {filepath}')
    
    if display_fig:
        plt.show()
