from pathlib import Path
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerTuple

def plot_CO2_density_isotherms(
    model_data_folder_path="../data/CO2-predictions",
    lit_data_folder_path="../data/literature-data",    
    width=4, height=6,
    colours=['black', 'C1', 'C0'],
    symbols=['o', 'x', '^'],
    display_fig=True, save_fig=True,
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    T_list = [35+273, 51+273, 81+273] # [K]
    MW = 44.01  # [g/mol]
    
    # Import experimental data
    df_exp = {}
    for i, T in enumerate(T_list):
        df_exp[T] = pd.read_excel(f'{lit_data_folder_path}/CO2.xlsx', sheet_name=f'{T-273}C (36)')

    # Read CO2 density data from exported CSV file
    df_CO2_density = pd.read_csv(f'{model_data_folder_path}/CO2_density_SAFT_predictions.csv')

    # Group data by temperature
    T_list = df_CO2_density['Temperature / K'].unique()
    P_list = {}
    rhoCO2_SAFT = {}

    for T in T_list:
        # Filter data for this temperature
        temp_data = df_CO2_density[df_CO2_density['Temperature / K'] == T]
        
        # Extract pressure and density data
        P_list[T] = temp_data['Pressure / Pa'].values
        rhoCO2_SAFT[T] = temp_data['Density SAFT / g cm^-3'].values

    # Plot figure
    fig, ax = plt.subplots(1, 1, figsize=(width, height), constrained_layout=True)
    
    for i, T in enumerate(T_list):        
        # Exp measurement, choosing every 2nd data point for better visibility
        ax.plot(df_exp[T]['Pressure (MPa)'][::2], df_exp[T]["Density (mol/m3)"][::2]*MW*1e-6, 
                color=colours[i], 
                marker=symbols[i],
                linestyle="None",
                markerfacecolor="None",
                # label=f'ref {T-273} °C: Span Wagner EoS'
                )
        
        # SAFT predictions from CSV data
        ax.plot(P_list[T]*1e-6, rhoCO2_SAFT[T], 
                color=colours[i], 
                linestyle="solid", 
                marker="None", 
                # label=f" SAFT-γ Mie EoS {T-273} °C"
                )

    # Labelling
    ax.set_xlabel(r"Pressure / MPa")
    ax.set_ylabel(r"$\rho_\mathrm{CO_{2}}$ / $\mathrm{g \, cm^{-3}}$")

    # Set axis limits
    ax.set_xlim(0)
    ax.set_ylim(0, 1.2)
    
    # Custom legend with HandlerTuple for all temperatures
    p1_35, = ax.plot([], [], color=colours[0], marker=symbols[0], linestyle='None', markerfacecolor='None')
    l1_35, = ax.plot([], [], color=colours[0], linestyle='solid')

    p1_51, = ax.plot([], [], color=colours[1], marker=symbols[1], linestyle='None', markerfacecolor='None')
    l1_51, = ax.plot([], [], color=colours[1], linestyle='solid')

    p1_81, = ax.plot([], [], color=colours[2], marker=symbols[2], linestyle='None', markerfacecolor='None')
    l1_81, = ax.plot([], [], color=colours[2], linestyle='solid')

    # Create legend
    ax.legend([(p1_35, l1_35), (p1_51, l1_51), (p1_81, l1_81)], 
              ["35 °C", "51 °C", "81 °C"], 
              handler_map={tuple: HandlerTuple(ndivide=None)},
              handlelength=3,
              loc='lower right')

    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_CO2_density_comparison.{save_format}"
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()

def plot_CO2_fugacityCoeff_isotherms(
    model_data_folder_path="../data/CO2-predictions",
    lit_data_folder_path="../data/literature-data",    
    width=4, height=6,
    colours=['black', 'C1', 'C0'],
    symbols=['o', 'x', '^'],
    display_fig=True, save_fig=True,
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    T_list = [310, 320, 350] # [K], based on exp data temperatures
    
    # Import experimental data
    df_exp_main = pd.read_excel(f'{lit_data_folder_path}/CO2.xlsx', sheet_name='fugCoeff (37)')
    df_exp = {}
    for i, T in enumerate(T_list):
        df_exp[T] = df_exp_main[df_exp_main['T / K'] == T]
    
    # Read CO2 density data from exported CSV file
    df_CO2_fugCoeff = pd.read_csv(f'{model_data_folder_path}/CO2_fugacityCoeff_SAFT_predictions.csv')

    # Group data by temperature
    # T_list = df_CO2_fugCoeff['Temperature / K'].unique()
    P_list = {}
    phiCO2_SAFT = {}

    for T in T_list:
        # Filter data for this temperature
        temp_data = df_CO2_fugCoeff[df_CO2_fugCoeff['Temperature / K'] == T]
        
        # Extract pressure and density data
        P_list[T] = temp_data['Pressure / Pa'].values
        phiCO2_SAFT[T] = temp_data['Fugacity Coefficient SAFT'].values

    # Plot figure
    fig, ax = plt.subplots(1, 1, figsize=(width, height), constrained_layout=True)
    
    for i, T in enumerate(T_list):        
        # Exp data
        ax.plot(df_exp[T]['p / bar']*1e-1, df_exp[T]['Fugacity coefficient'],
                color=colours[i], 
                marker=symbols[i],
                linestyle="None",
                markerfacecolor="None",
                # label=f'ref {T-273} °C: Span Wagner EoS'
                )
        
        # SAFT predictions from CSV data
        ax.plot(P_list[T]*1e-6, phiCO2_SAFT[T], 
                color=colours[i], 
                linestyle="solid", 
                marker="None", 
                # label=f" SAFT-γ Mie EoS {T-273} °C"
                )

    # Labelling
    ax.set_xlabel(r"Pressure / MPa")
    # ax.set_ylabel(r"$\phi_\mathrm{CO_{2}}$")
    ax.set_ylabel(r"$\phi_\mathrm{s,ext}^\mathrm{EQ}$")

    # Set axis limits
    ax.set_xlim(0)
    ax.set_ylim(0,)
    
    # Custom legend with HandlerTuple for all temperatures
    p1_37, = ax.plot([], [], color=colours[0], marker=symbols[0], linestyle='None', markerfacecolor='None')
    l1_37, = ax.plot([], [], color=colours[0], linestyle='solid')

    p1_47, = ax.plot([], [], color=colours[1], marker=symbols[1], linestyle='None', markerfacecolor='None')
    l1_47, = ax.plot([], [], color=colours[1], linestyle='solid')

    p1_77, = ax.plot([], [], color=colours[2], marker=symbols[2], linestyle='None', markerfacecolor='None')
    l1_77, = ax.plot([], [], color=colours[2], linestyle='solid')

    # Create legend
    ax.legend([(p1_37, l1_37), (p1_47, l1_47), (p1_77, l1_77)], 
              ["37 °C", "47 °C", "77 °C"], 
              handler_map={tuple: HandlerTuple(ndivide=None)},
              handlelength=3,
              loc='upper right')

    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_CO2_fugacityCoeff_comparison.{save_format}"
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()
