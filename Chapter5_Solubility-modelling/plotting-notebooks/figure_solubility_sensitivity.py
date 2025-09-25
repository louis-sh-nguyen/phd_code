import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os

def plot_solubility_noRepeatUnits_sensitivity(
    data_folder_path="../data/MW-sensitivity",
    width=4, height=6,
    colour='black',    
    display_fig=True, save_fig=True,
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    # Read data
    df_PS = pd.read_csv(f'{data_folder_path}/CO2_PS_sensitivity_noRepeatingUnits_100C_1.0MPa.csv')
    df_PMMA = pd.read_csv(f'{data_folder_path}/CO2_PMMA_sensitivity_noRepeatingUnits_100C_1.0MPa.csv')
    
    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(width, height), constrained_layout=True)
    ax1, ax2 = axes.flatten()  # Flatten for easy iteration
    
    # Plot (a) CO2+PS
    ax1.plot(df_PS['Number of repeating units'], df_PS['Solubility EQ / g-sol g-pol^-1'], marker='None', color=colour, linestyle='dashdot')
    # Labelling
    ax1.set_xlabel('No. of repating units')
    ax1.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    # Title
    ax1.set_title(r'(a) $\mathrm{CO_2}$+PS')
    
    # Plot (b) CO2+PMMA
    ax2.plot(df_PMMA['Number of repeating units'], df_PMMA['Solubility EQ / g-sol g-pol^-1'], marker='None', color=colour, linestyle='dashdot')
    # Labelling
    ax2.set_xlabel('No. of repating units')
    # ax2.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    # Title
    ax2.set_title(r'(b) $\mathrm{CO_2}$+PMMA')
    
    # Set limits
    ax1.set_xlim(0)
    ax2.set_xlim(0)
    ax1.set_ylim(0, 0.02)
    ax2.set_ylim(0, 0.04)
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_solubility_noRepeatUnits_sensitivity_fitted_params.{save_format}"
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()
