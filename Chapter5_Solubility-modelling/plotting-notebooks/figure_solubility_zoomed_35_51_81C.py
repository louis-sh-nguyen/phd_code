from pathlib import Path
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_solubility_zoomed_35_51_81C_fitted_params(
    model_data_folder_path="../data/solubility-prediction-SAFT",
    lit_data_folder_path="../data/literature-data",    
    width=6, height=4,
    colour='black',
    symbol='o',
    display_fig=True, save_fig=True,
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    
    T_list = [35+273, 51+273, 81+273] # [K]
    df_exp_CO2_PS = {}
    df_exp_CO2_PMMA = {}

    # Exp data
    for i, T in enumerate(T_list):
        df_exp_CO2_PS[T] = pd.read_excel(f'{lit_data_folder_path}/CO2-PS.xlsx', sheet_name=f'S_{T-273}C (8)')
        df_exp_CO2_PMMA[T] = pd.read_excel(f'{lit_data_folder_path}/CO2-PMMA.xlsx', sheet_name=f'S_{T-273}C (8)')
        
    df_CO2_PS_default = {}
    df_CO2_PS_fitted = {}
    df_CO2_PMMA_fitted = {}
    df_CO2_PMMA_default = {}

    # Calculated data
    for T in T_list:
        df_CO2_PS_default[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PS_solubility-density_main.xlsx', sheet_name=f'default_{T-273}C')
        df_CO2_PS_fitted[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PS_solubility-density_main.xlsx', sheet_name=f'fitted_{T-273}C')
        df_CO2_PMMA_default[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PMMA_solubility-density_main.xlsx', sheet_name=f'default_{T-273}C')
        df_CO2_PMMA_fitted[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PMMA_solubility-density_main.xlsx', sheet_name=f'fitted_{T-273}C')
    
    # Plotting 
    fig, axes = plt.subplots(2, 3, figsize=(width, height), constrained_layout=True)
    ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()  # Flatten for easy iteration
    
    #----------------------------------
    # PS plots
    #----------------------------------
    # Plot (a) 35 C
    T = 35 + 273
    # Filter data
    # df_exp_CO2_PS[T] = df_exp_CO2_PS[T][df_exp_CO2_PS[T]['P [MPa]'] < x_lims[0]]
    # df_CO2_PS_fitted[T] = df_CO2_PS_fitted[T][df_CO2_PS_fitted[T]['p [MPa]'] < x_lims[0]]
    # Exp solubility
    ax1.plot(df_exp_CO2_PS[T]['P [MPa]'], df_exp_CO2_PS[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
    # EQ solubility
    ax1.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="solid",
        label=f"Model (EQ)",
    )
    # NE solubility    
    ax1.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashed", 
        label=f"Model (NE)",
    )
    # Labelling
    # ax1.set_xlabel('Pressure / MPa')
    ax1.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (b) 51 C
    T = 51 + 273
    # Filter data
    # df_exp_CO2_PS[T] = df_exp_CO2_PS[T][df_exp_CO2_PS[T]['P [MPa]'] < x_lims[1]]
    # df_CO2_PS_fitted[T] = df_CO2_PS_fitted[T][df_CO2_PS_fitted[T]['p [MPa]'] < x_lims[1]]
    # Exp solubility
    ax2.plot(df_exp_CO2_PS[T]['P [MPa]'], df_exp_CO2_PS[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
    # EQ solubility
    ax2.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="solid",
        label=f"Model (EQ)",
    )
    # NE solubility    
    ax2.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashed", 
        label=f"Model (NE)",
    )    
    # Labelling
    # ax3.set_xlabel('Pressure / MPa')
    # ax2.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (c) 81 C
    T = 81 + 273
    # Filter data
    # df_exp_CO2_PS[T] = df_exp_CO2_PS[T][df_exp_CO2_PS[T]['P [MPa]'] < x_lims[2]]
    # df_CO2_PS_fitted[T] = df_CO2_PS_fitted[T][df_CO2_PS_fitted[T]['p [MPa]'] < x_lims[2]]
    # Exp solubility
    # ax3.plot(df_exp_CO2_PS[T]['P [MPa]'], df_exp_CO2_PS[T]['Solubility [g-sol/g-pol-am]'], 
    #             color=colour,
    #             marker=symbol,
    #             linestyle="None",
    #             markerfacecolor="None",
    #             markersize=5,
    #             label='Exp.',
    #             )
    # EQ solubility
    ax3.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="solid",
        label=f"Model (EQ)",
    )
    # NE solubility    
    ax3.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashed", 
        label=f"Model (NE)",
    )    
    # Labelling
    # ax3.set_xlabel('Pressure / MPa')
    # ax3.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    #----------------------------------
    # PMMA plots
    #----------------------------------
    # Plot (d) 35 C
    T = 35 + 273
    # Filter data
    # df_exp_CO2_PMMA[T] = df_exp_CO2_PMMA[T][df_exp_CO2_PMMA[T]['P [MPa]'] < x_lims[3]]
    # df_CO2_PMMA_fitted[T] = df_CO2_PMMA_fitted[T][df_CO2_PMMA_fitted[T]['p [MPa]'] < x_lims[3]]
    # Exp solubility
    ax4.plot(df_exp_CO2_PMMA[T]['P [MPa]'], df_exp_CO2_PMMA[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
    # EQ solubility
    ax4.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="solid",
        label=f"Model (EQ)",
    )
    # NE solubility    
    ax4.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashed", 
        label=f"Model (NE)",
    )
    # Labelling
    ax4.set_xlabel('Pressure / MPa')
    ax4.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (e) 51 C
    T = 51 + 273
    # Filter data
    # df_exp_CO2_PMMA[T] = df_exp_CO2_PMMA[T][df_exp_CO2_PMMA[T]['P [MPa]'] < x_lims[4]]
    # df_CO2_PMMA_fitted[T] = df_CO2_PMMA_fitted[T][df_CO2_PMMA_fitted[T]['p [MPa]'] < x_lims[4]]
    # Exp solubility
    ax5.plot(df_exp_CO2_PMMA[T]['P [MPa]'], df_exp_CO2_PMMA[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
    # EQ solubility
    ax5.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="solid",
        label=f"Model (EQ)",
    )
    # NE solubility    
    ax5.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashed", 
        label=f"Model (NE)",
    )
    # Labelling
    ax5.set_xlabel('Pressure / MPa')
    # ax5.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (f) 81 C
    T = 81 + 273
    # Filter data
    # df_exp_CO2_PMMA[T] = df_exp_CO2_PMMA[T][df_exp_CO2_PMMA[T]['P [MPa]'] < x_lims[5]]
    # df_CO2_PMMA_fitted[T] = df_CO2_PMMA_fitted[T][df_CO2_PMMA_fitted[T]['p [MPa]'] < x_lims[5]]
    # Exp solubility
    ax6.plot(df_exp_CO2_PMMA[T]['P [MPa]'], df_exp_CO2_PMMA[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
    # EQ solubility
    ax6.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="solid",
        label=f"Model (EQ)",
    )
    # NE solubility    
    ax6.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashed", 
        label=f"Model (NE)",
    )
    # Labelling
    ax6.set_xlabel('Pressure / MPa')
    # ax6.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Custom axis upper limits
    x_lims = [2.0, 2.0, 0.2,    # PS 
              4.0, 4.0, 6.0]    # PMMA
    
    y_lims = [0.04, 0.03, 0.002,  # PS
              0.20, 0.15, 0.12]   # PMMA
    
    # Set x-axis limits for all subplots
    for i, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6]):
        ax.set_xlim(0, x_lims[i])
    
    for i, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6]):
        ax.set_ylim(0, y_lims[i])
    
    # Set y-ticks
    ax6.set_yticks(np.linspace(0, 0.12, 5))
    
    # Set titles for all subplots
    ax1.set_title('(a) 35 °C')
    ax2.set_title('(b) 51 °C')
    ax3.set_title('(c) 81 °C')
    ax4.set_title('(d) 35 °C')
    ax5.set_title('(e) 51 °C')
    ax6.set_title('(f) 81 °C')
    
    # Add legends to each subplot
    ax1.legend(labelspacing=0.2, handlelength=1.4, loc='upper left')
    ax2.legend(labelspacing=0.2, handlelength=1.4, loc='upper left')
    ax3.legend(labelspacing=0.2, handlelength=1.4, loc='upper left')
    ax4.legend(labelspacing=0.2, handlelength=1.4, loc='upper left')
    ax5.legend(labelspacing=0.2, handlelength=1.4, loc='upper left')
    ax6.legend(labelspacing=0.2, handlelength=1.4, loc='upper left')
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_solubility_zoomed_35-51-81C_fitted_params.{save_format}"
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()
