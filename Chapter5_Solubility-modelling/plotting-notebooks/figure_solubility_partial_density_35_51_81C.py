from pathlib import Path
import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_solubility_partial_density_PS_35_51_81C_fitted_params(
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
    # df_exp_CO2_PMMA = {}

    # Exp data for CO2-PS
    for i, T in enumerate(T_list):
        # print(f"Worksheets in CO2-PS.xlsx for T={T-273}C: {pd.ExcelFile('litdata\\CO2-PS.xlsx').sheet_names}")
        df_exp_CO2_PS[T] = pd.read_excel(f'{lit_data_folder_path}/CO2-PS.xlsx', sheet_name=f'S_{T-273}C (8)')

    # Exp data for CO2-PMMA
    # for i, T in enumerate(T_list):
    #     df_exp_CO2_PMMA[T] = pd.read_excel(f'{lit_data_folder_path}/CO2-PMMA.xlsx', sheet_name=f'S_{T-273}C (8)')
        
    df_CO2_PS_default = {}
    df_CO2_PS_fitted = {}
    # df_CO2_PMMA_fitted = {}
    # df_CO2_PMMA_default = {}

    # Calculated EQ data for CO2-PS
    for T in T_list:
        df_CO2_PS_default[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PS_solubility-density_main.xlsx', sheet_name=f'default_{T-273}C')
        df_CO2_PS_fitted[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PS_solubility-density_main.xlsx', sheet_name=f'fitted_{T-273}C')
        # df_CO2_PMMA_default[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PMMA_solubility-density_main.xlsx', sheet_name=f'default_{T-273}C')
        # df_CO2_PMMA_fitted[T] = pd.read_excel(f'{model_data_folder_path}CO2-PMMA_solubility-density_main.xlsx', sheet_name=f'fitted_{T-273}C')

    # Plotting 
    fig, axes = plt.subplots(3, 2, figsize=(width, height), constrained_layout=True)
    ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()  # Flatten for easy iteration
    
    #----------------------------------
    # Solubility plots
    #----------------------------------
    # Plot (a) Solubility 35 C
    T = 35 + 273
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
    
    # Plot (c) Solubility 51 C
    T = 51 + 273
    # Exp solubility
    ax3.plot(df_exp_CO2_PS[T]['P [MPa]'], df_exp_CO2_PS[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
            
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
    ax3.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (e) Solubility 81 C
    T = 81 + 273
    # Exp solubility
    ax5.plot(df_exp_CO2_PS[T]['P [MPa]'], df_exp_CO2_PS[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
            
    # EQ solubility
    ax5.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="solid",
        label="Model (EQ)",
    )

    # NE solubility    
    ax5.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashed", 
        label="Model (NE)",
    )    
    # Labelling
    ax5.set_xlabel('Pressure / MPa')
    ax5.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    #----------------------------------
    # Partial density plots
    #----------------------------------
    # Plot (b) Partial density 35 C
    T = 35 + 273    # [K]
    # EQ calc
    ax2.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="solid",
        label="Model (EQ)",
    )
    # NE solubility    
    ax2.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dashed",
        label=f"Model (NE)",
    )
    # Labelling
    # ax2.set_xlabel(r"p / MPa")
    ax2.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Plot (d) Partial density 51 C
    T = 51 + 273    # [K]
    # EQ calc
    ax4.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="solid",
        label="Model (EQ)",
    )
    # NE solubility    
    ax4.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dashed",
        label=f"Model (NE)",
    )
    # Labelling
    # ax4.set_xlabel(r"p / MPa")
    ax4.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Plot (f) Partial density 81 C
    T = 81 + 273    # [K]
    # EQ calc
    ax6.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="solid",
        label="Model (EQ)",
    )
    # NE solubility    
    ax6.plot(
        df_CO2_PS_fitted[T]['p [MPa]'],
        df_CO2_PS_fitted[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dashed",
        label=f"Model (NE)",
    )

    # Labelling
    ax6.set_xlabel('Pressure / MPa')
    ax6.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Set x-axis limits for all subplots
    ax1.set_xlim(0)
    ax2.set_xlim(0)
    ax3.set_xlim(0)
    ax4.set_xlim(0)
    ax5.set_xlim(0)
    ax6.set_xlim(0)
    
    ax1.set_ylim(0)
    ax3.set_ylim(0)
    ax5.set_ylim(0)
    
    # Set titles for all subplots
    ax1.set_title('(a) 35 °C')
    ax2.set_title('(b) 35 °C')
    ax3.set_title('(c) 51 °C')
    ax4.set_title('(d) 51 °C')
    ax5.set_title('(e) 81 °C')
    ax6.set_title('(f) 81 °C')
    
    # Add legends to each subplot
    ax1.legend(loc='lower right', labelspacing=0.3)
    ax2.legend(labelspacing=0.3)
    ax3.legend(labelspacing=0.3)
    ax4.legend(labelspacing=0.3)
    ax5.legend(labelspacing=0.3)
    ax6.legend(labelspacing=0.3)
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_solubility_PS_35-51-81C_fitted_params.{save_format}"
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()

def plot_solubility_partial_density_PMMA_35_51_81C_fitted_params(
    model_data_folder_path="../data/solubility-prediction-SAFT",
    lit_data_folder_path="../data/literature-data",    
    width=6, height=4,
    colour='black',
    symbol='o',
    display_fig=True, save_fig=True,
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    T_list = [35+273, 51+273, 81+273] # [K]
    df_exp_CO2_PMMA = {}

    # Exp data for CO2-PMMA
    for i, T in enumerate(T_list):
        df_exp_CO2_PMMA[T] = pd.read_excel(f'{lit_data_folder_path}/CO2-PMMA.xlsx', sheet_name=f'S_{T-273}C (8)')
        
    df_CO2_PMMA_fitted = {}
    df_CO2_PMMA_default = {}

    # Calculated EQ data for CO2-PS
    for T in T_list:
        df_CO2_PMMA_default[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PMMA_solubility-density_main.xlsx', sheet_name=f'default_{T-273}C')
        df_CO2_PMMA_fitted[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PMMA_solubility-density_main.xlsx', sheet_name=f'fitted_{T-273}C')

    # Plotting 
    fig, axes = plt.subplots(3, 2, figsize=(width, height), constrained_layout=True)
    ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()  # Flatten for easy iteration
    
    #----------------------------------
    # Solubility plots
    #----------------------------------
    # Plot (a) Solubility 35 C
    T = 35 + 273
    # Exp solubility
    ax1.plot(df_exp_CO2_PMMA[T]['P [MPa]'], df_exp_CO2_PMMA[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
    # EQ solubility
    ax1.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="solid",
        label=f"Model (EQ)",
    )
    # NE solubility    
    ax1.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashed", 
        label=f"Model (NE)",
    )
    # Labelling
    # ax1.set_xlabel('Pressure / MPa')
    ax1.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (c) Solubility 51 C
    T = 51 + 273
    # Exp solubility
    ax3.plot(df_exp_CO2_PMMA[T]['P [MPa]'], df_exp_CO2_PMMA[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
            
    # EQ solubility
    ax3.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="solid",
        label=f"Model (EQ)",
    )

    # NE solubility    
    ax3.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashed", 
        label=f"Model (NE)",
    )    
    # Labelling
    # ax3.set_xlabel('Pressure / MPa')
    ax3.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (e) Solubility 81 C
    T = 81 + 273
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
        label="Model (EQ)",
    )

    # NE solubility    
    ax5.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashed", 
        label="Model (NE)",
    )    
    # Labelling
    ax5.set_xlabel('Pressure / MPa')
    ax5.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    #----------------------------------
    # Partial density plots
    #----------------------------------
    # Plot (b) Partial density 35 C
    T = 35 + 273    # [K]
    # EQ calc
    ax2.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="solid",
        label="Model (EQ)",
    )
    # NE solubility    
    ax2.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dashed",
        label=f"Model (NE)",
    )
    # Labelling
    # ax2.set_xlabel(r"p / MPa")
    ax2.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Plot (d) Partial density 51 C
    T = 51 + 273    # [K]
    # EQ calc
    ax4.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="solid",
        label="Model (EQ)",
    )
    # NE solubility    
    ax4.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dashed",
        label=f"Model (NE)",
    )
    # Labelling
    # ax4.set_xlabel(r"p / MPa")
    ax4.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Plot (f) Partial density 81 C
    T = 81 + 273    # [K]
    # EQ calc
    ax6.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="solid",
        label="Model (EQ)",
    )
    # NE solubility    
    ax6.plot(
        df_CO2_PMMA_fitted[T]['p [MPa]'],
        df_CO2_PMMA_fitted[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dashed",
        label=f"Model (NE)",
    )

    # Labelling
    ax6.set_xlabel('Pressure / MPa')
    ax6.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Set x-axis limits for all subplots
    ax1.set_xlim(0)
    ax2.set_xlim(0)
    ax3.set_xlim(0)
    ax4.set_xlim(0)
    ax5.set_xlim(0)
    ax6.set_xlim(0)
    
    ax1.set_ylim(0)
    ax3.set_ylim(0)
    ax5.set_ylim(0)
    
    # Set titles for all subplots
    ax1.set_title('(a) 35 °C')
    ax2.set_title('(b) 35 °C')
    ax3.set_title('(c) 51 °C')
    ax4.set_title('(d) 51 °C')
    ax5.set_title('(e) 81 °C')
    ax6.set_title('(f) 81 °C')
    
    # Add legends to each subplot
    ax1.legend(loc='lower right', labelspacing=0.3)
    ax2.legend(labelspacing=0.3)
    ax3.legend(labelspacing=0.3)
    ax4.legend(labelspacing=0.3)
    ax5.legend(labelspacing=0.3)
    ax6.legend(labelspacing=0.3)
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_solubility_PMMA_35-51-81C_fitted_params.{save_format}"
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()

def plot_solubility_partial_density_PS_35_51_81C_default_params(
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

    # Exp data for CO2-PS
    for i, T in enumerate(T_list):
        df_exp_CO2_PS[T] = pd.read_excel(f'{lit_data_folder_path}/CO2-PS.xlsx', sheet_name=f'S_{T-273}C (8)')
        
    df_CO2_PS_default = {}

    # Calculated EQ data for CO2-PS
    for T in T_list:
        df_CO2_PS_default[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PS_solubility-density_main.xlsx', sheet_name=f'default_{T-273}C')

    # Plotting 
    fig, axes = plt.subplots(3, 2, figsize=(width, height), constrained_layout=True)
    ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()  # Flatten for easy iteration
    
    #----------------------------------
    # Solubility plots
    #----------------------------------
    # Plot (a) Solubility 35 C
    T = 35 + 273
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
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashdot",
        label=f"Model (EQ)",
    )
    # NE solubility    
    ax1.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dotted", 
        label=f"Model (NE)",
    )
    # Labelling
    # ax1.set_xlabel('Pressure / MPa')
    ax1.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (c) Solubility 51 C
    T = 51 + 273
    # Exp solubility
    ax3.plot(df_exp_CO2_PS[T]['P [MPa]'], df_exp_CO2_PS[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
            
    # EQ solubility
    ax3.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashdot",
        label=f"Model (EQ)",
    )

    # NE solubility    
    ax3.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dotted", 
        label=f"Model (NE)",
    )    
    # Labelling
    # ax3.set_xlabel('Pressure / MPa')
    ax3.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (e) Solubility 81 C
    T = 81 + 273
    # Exp solubility
    ax5.plot(df_exp_CO2_PS[T]['P [MPa]'], df_exp_CO2_PS[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
            
    # EQ solubility
    ax5.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashdot",
        label="Model (EQ)",
    )

    # NE solubility    
    ax5.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dotted", 
        label="Model (NE)",
    )    
    # Labelling
    ax5.set_xlabel('Pressure / MPa')
    ax5.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    #----------------------------------
    # Partial density plots
    #----------------------------------
    # Plot (b) Partial density 35 C
    T = 35 + 273    # [K]
    # EQ calc
    ax2.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="dashdot",
        label="Model (EQ)",
    )
    # NE solubility    
    ax2.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dotted",
        label=f"Model (NE)",
    )
    # Labelling
    # ax2.set_xlabel(r"p / MPa")
    ax2.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Plot (d) Partial density 51 C
    T = 51 + 273    # [K]
    # EQ calc
    ax4.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="dashdot",
        label="Model (EQ)",
    )
    # NE solubility    
    ax4.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dotted",
        label=f"Model (NE)",
    )
    # Labelling
    # ax4.set_xlabel(r"p / MPa")
    ax4.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Plot (f) Partial density 81 C
    T = 81 + 273    # [K]
    # EQ calc
    ax6.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="dashdot",
        label="Model (EQ)",
    )
    # NE solubility    
    ax6.plot(
        df_CO2_PS_default[T]['p [MPa]'],
        df_CO2_PS_default[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dotted",
        label=f"Model (NE)",
    )

    # Labelling
    ax6.set_xlabel('Pressure / MPa')
    ax6.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Set x-axis limits for all subplots
    ax1.set_xlim(0)
    ax2.set_xlim(0)
    ax3.set_xlim(0)
    ax4.set_xlim(0)
    ax5.set_xlim(0)
    ax6.set_xlim(0)
    
    ax1.set_ylim(0)
    ax3.set_ylim(0)
    ax5.set_ylim(0)
    
    # Set titles for all subplots
    ax1.set_title('(a) 35 °C')
    ax2.set_title('(b) 35 °C')
    ax3.set_title('(c) 51 °C')
    ax4.set_title('(d) 51 °C')
    ax5.set_title('(e) 81 °C')
    ax6.set_title('(f) 81 °C')
    
    # Add legends to each subplot
    ax1.legend(loc='lower right', labelspacing=0.3)
    ax2.legend(labelspacing=0.3)
    ax3.legend(labelspacing=0.3)
    ax4.legend(labelspacing=0.3)
    ax5.legend(labelspacing=0.3)
    ax6.legend(labelspacing=0.3)
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_solubility_PS_35-51-81C_default_params.{save_format}"
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()


def plot_solubility_partial_density_PMMA_35_51_81C_default_params(
    model_data_folder_path="../data/solubility-prediction-SAFT",
    lit_data_folder_path="../data/literature-data",    
    width=6, height=4,
    colour='black',
    symbol='o',
    display_fig=True, save_fig=True,
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    T_list = [35+273, 51+273, 81+273] # [K]
    df_exp_CO2_PMMA = {}

    # Exp data for CO2-PMMA
    for i, T in enumerate(T_list):
        df_exp_CO2_PMMA[T] = pd.read_excel(f'{lit_data_folder_path}/CO2-PMMA.xlsx', sheet_name=f'S_{T-273}C (8)')
        
    df_CO2_PMMA_default = {}

    # Calculated EQ data for CO2-PS
    for T in T_list:
        df_CO2_PMMA_default[T] = pd.read_excel(f'{model_data_folder_path}/CO2-PMMA_solubility-density_main.xlsx', sheet_name=f'default_{T-273}C')

    # Plotting 
    fig, axes = plt.subplots(3, 2, figsize=(width, height), constrained_layout=True)
    ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()  # Flatten for easy iteration
    
    #----------------------------------
    # Solubility plots
    #----------------------------------
    # Plot (a) Solubility 35 C
    T = 35 + 273
    # Exp solubility
    ax1.plot(df_exp_CO2_PMMA[T]['P [MPa]'], df_exp_CO2_PMMA[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
    # EQ solubility
    ax1.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashdot",
        label=f"Model (EQ)",
    )
    # NE solubility    
    ax1.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dotted", 
        label=f"Model (NE)",
    )
    # Labelling
    # ax1.set_xlabel('Pressure / MPa')
    ax1.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (c) Solubility 51 C
    T = 51 + 273
    # Exp solubility
    ax3.plot(df_exp_CO2_PMMA[T]['P [MPa]'], df_exp_CO2_PMMA[T]['Solubility [g-sol/g-pol-am]'], 
                color=colour,
                marker=symbol,
                linestyle="None",
                markerfacecolor="None",
                markersize=5,
                label='Exp.',
                )
            
    # EQ solubility
    ax3.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashdot",
        label=f"Model (EQ)",
    )

    # NE solubility    
    ax3.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dotted", 
        label=f"Model (NE)",
    )    
    # Labelling
    # ax3.set_xlabel('Pressure / MPa')
    ax3.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    # Plot (e) Solubility 81 C
    T = 81 + 273
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
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['solubility_EQ [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dashdot",
        label="Model (EQ)",
    )

    # NE solubility    
    ax5.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['solubility_NE [g-sol/g-pol]'],
        color=colour,
        marker="None",
        linestyle="dotted", 
        label="Model (NE)",
    )    
    # Labelling
    ax5.set_xlabel('Pressure / MPa')
    ax5.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    
    #----------------------------------
    # Partial density plots
    #----------------------------------
    # Plot (b) Partial density 35 C
    T = 35 + 273    # [K]
    # EQ calc
    ax2.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="dashdot",
        label="Model (EQ)",
    )
    # NE solubility    
    ax2.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dotted",
        label=f"Model (NE)",
    )
    # Labelling
    # ax2.set_xlabel(r"p / MPa")
    ax2.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Plot (d) Partial density 51 C
    T = 51 + 273    # [K]
    # EQ calc
    ax4.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="dashdot",
        label="Model (EQ)",
    )
    # NE solubility    
    ax4.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dotted",
        label=f"Model (NE)",
    )
    # Labelling
    # ax4.set_xlabel(r"p / MPa")
    ax4.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Plot (f) Partial density 81 C
    T = 81 + 273    # [K]
    # EQ calc
    ax6.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['rho_pol_EQ [g-pol/cm3-mix]'],
        color=colour,
        marker="None",            
        linestyle="dashdot",
        label="Model (EQ)",
    )
    # NE solubility    
    ax6.plot(
        df_CO2_PMMA_default[T]['p [MPa]'],
        df_CO2_PMMA_default[T]['rho_pol_NE [g-pol/cm3-mix]'],
        color=colour,
        marker="None",
        linestyle="dotted",
        label=f"Model (NE)",
    )

    # Labelling
    ax6.set_xlabel('Pressure / MPa')
    ax6.set_ylabel(r"$\rho_\mathrm{p,pol}$ / $\mathrm{g \, cm^{-3}}$")
    
    # Set x-axis limits for all subplots
    ax1.set_xlim(0)
    ax2.set_xlim(0)
    ax3.set_xlim(0)
    ax4.set_xlim(0)
    ax5.set_xlim(0)
    ax6.set_xlim(0)
    
    ax1.set_ylim(0)
    ax3.set_ylim(0, 0.8)
    ax5.set_ylim(0)
    
    # Set titles for all subplots
    ax1.set_title('(a) 35 °C')
    ax2.set_title('(b) 35 °C')
    ax3.set_title('(c) 51 °C')
    ax4.set_title('(d) 51 °C')
    ax5.set_title('(e) 81 °C')
    ax6.set_title('(f) 81 °C')
    
    # Add legends to each subplot
    ax1.legend(loc='upper left', labelspacing=0.3)
    ax2.legend(labelspacing=0.3)
    ax3.legend(loc='upper left', labelspacing=0.3)
    ax4.legend(labelspacing=0.3)
    ax5.legend(loc='upper left', labelspacing=0.3)
    ax6.legend(labelspacing=0.3)
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_solubility_PMMA_35-51-81C_default_params.{save_format}"
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()
