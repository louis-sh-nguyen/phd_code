import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os
from matplotlib.legend_handler import HandlerTuple

def plot_solubility_validation_data_fitted_params(
    model_data_folder_path="../data/solubility-prediction-SAFT",
    lit_data_folder_path="../data/literature-data",    
    width=4, height=6,
    colours=['black', 'C1'],
    symbols=['o', 'x'],
    display_fig=True, save_fig=True,
    folder_to_save='../figures', save_format='pdf', dpi=400,
):

    # Get exp data for CO2-PS
    T_list_PS = [100+273, 132+273] # [K]
    df_exp_CO2_PS = {}
    for i, T in enumerate(T_list_PS):
        df_exp_CO2_PS[T] = pd.read_excel(f'{lit_data_folder_path}/CO2-PS.xlsx', sheet_name=f'S_{T-273}C (8)')
    df_calc_CO2_PS_default = {}
    df_calc_CO2_PS_fitted = {}
    # Get EQ data for CO2-PS
    for T in T_list_PS:
        df_calc_CO2_PS_default[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PS_solubility_main.xlsx', sheet_name=f'default_{T-273}C')
        df_calc_CO2_PS_fitted[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PS_solubility_main.xlsx', sheet_name=f'fitted_{T-273}C')

    # Get exp data for CO2-PMMA
    T_list_PMMA = [100+273, 132+273] # [K]
    df_exp_CO2_PMMA = {}
    for i, T in enumerate(T_list_PMMA):
        df_exp_CO2_PMMA[T] = pd.read_excel(f'{lit_data_folder_path}/CO2-PMMA.xlsx', sheet_name=f'S_{T-273}C (8)')
    df_calc_CO2_PMMA_default = {}
    df_calc_CO2_PMMA_fitted = {}
    # Get EQ data for CO2-PMMA
    for T in T_list_PMMA:
        df_calc_CO2_PMMA_default[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PMMA_solubility_main.xlsx', sheet_name=f'default_{T-273}C')
        df_calc_CO2_PMMA_fitted[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PMMA_solubility_main.xlsx', sheet_name=f'fitted_{T-273}C')
    
    # Plotting 
    fig, axes = plt.subplots(1, 2, figsize=(width, height), constrained_layout=True)
    ax1, ax2 = axes.flatten()  # Flatten for easy iteration

    # Left plot: CO2-PS
    for i, T in enumerate(T_list_PS):        
        # EQ data with fitted parameters
        ax1.plot(df_calc_CO2_PS_fitted[T]['p [MPa]'], df_calc_CO2_PS_fitted[T]['solubility_EQ [g-sol/g-pol]'], 
                color=colours[i],
                marker='None',
                linestyle='solid',
                label=f'Model (refined) {T-273} °C'
                )
        # EQ data with default parameters
        ax1.plot(df_calc_CO2_PS_default[T]['p [MPa]'], df_calc_CO2_PS_default[T]['solubility_EQ [g-sol/g-pol]'], 
                color=colours[i],
                marker='None',
                linestyle='dashdot',
                label=f'Model (default) {T-273} °C'
                )
        # Exp data
        ax1.plot(df_exp_CO2_PS[T]['P [MPa]'], df_exp_CO2_PS[T]['Solubility [g-sol/g-pol-am]'], 
                color=colours[i],
                marker=symbols[i],
                linestyle="None",
                markerfacecolor="None",
                # markersize=5,
                label=f'Exp. {T-273} °C'
                )
    # Set ticks
    ax1.set_xlim(0, 50)
    ax1.set_ylim(0, 0.15)
    # Labelling
    ax1.set_xlabel('Pressure / MPa')
    ax1.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    ax1.set_title(r'(a) $\mathrm{CO_2}$+PS')
    # ax1.legend(labelspacing=0.3)
    
    # Right plot: CO2-PMMA
    for i, T in enumerate(T_list_PMMA):
        # EQ data with fitted parameters
        ax2.plot(df_calc_CO2_PMMA_fitted[T]['p [MPa]'], df_calc_CO2_PMMA_fitted[T]['solubility_EQ [g-sol/g-pol]'], 
                color=colours[i],
                marker='None',
                linestyle='solid',
                label=f'Model (refined) {T-273} °C'
                )
        # EQ data with default parameters
        ax2.plot(df_calc_CO2_PMMA_default[T]['p [MPa]'], df_calc_CO2_PMMA_default[T]['solubility_EQ [g-sol/g-pol]'], 
                color=colours[i],
                marker='None',
                linestyle='dashdot',
                label=f'Model (default) {T-273} °C'
                )
        # Exp data
        ax2.plot(df_exp_CO2_PMMA[T]['P [MPa]'], df_exp_CO2_PMMA[T]['Solubility [g-sol/g-pol-am]'], 
                color=colours[i],
                marker=symbols[i],
                linestyle="None",
                markerfacecolor="None",
                # markersize=5,
                label=f'Exp. {T-273} °C'
                )
    # Set ticks
    ax2.set_xlim(0, 40)
    ax2.set_ylim(0, 0.50)
    # ax2.set_yticks(np.linspace(0, 0.12, 7))
    # Labelling
    ax2.set_xlabel('Pressure / MPa')
    # ax2.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    ax2.set_title(r'(b) $\mathrm{CO_2}$+PMMA')
    # ax2.legend(labelspacing=0.3)
    
    # Custom legend with HandlerTuple for both temperatures
    p1_100, = ax2.plot([], [], color='black', marker='o', linestyle='None', markerfacecolor='None')
    l1_100, = ax2.plot([], [], color='black', linestyle='solid')
    l2_100, = ax2.plot([], [], color='black', linestyle='dashdot')

    p1_132, = ax2.plot([], [], color='C1', marker='x', linestyle='None', markerfacecolor='None')
    l1_132, = ax2.plot([], [], color='C1', linestyle='solid')
    l2_132, = ax2.plot([], [], color='C1', linestyle='dashdot')

    ax1.legend([(p1_100, l1_100, l2_100), (p1_132, l1_132, l2_132)], 
                ['100 °C', '132 °C'],
                handler_map={tuple: HandlerTuple(ndivide=None)},
                handlelength=9,
                # labelspacing=0.3
                )
    ax2.legend([(p1_100, l1_100, l2_100), (p1_132, l1_132, l2_132)], 
                ['100 °C', '132 °C'],
                handler_map={tuple: HandlerTuple(ndivide=None)},
                handlelength=9,
                # labelspacing=0.3
                )
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_solubility_validation_data_fitted_params.{save_format}"
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()
