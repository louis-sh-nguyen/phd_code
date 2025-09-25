from pathlib import Path
from utils import get_lit_data
from matplotlib import pyplot as plt
import os

def plot_lit_data_100C(
    data_folder_path='../data/literature-data',
    width=6., height=4.1,
    colour='black', symbols=["o", "x", "^", "*", "s", "D"], linestyle='None', markerfacecolor='None',
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400):
    
    T = 100+273  # [K]
    xlxs_sheet_refno_list_PS=['18', '21', '15', '8']
    xlxs_sheet_refno_list_PMMA=['29', '8', '4']
    
    # Get data for CO2-PS
    # Extract data
    hasExpData_PS, matched_sheets_PS, ref_no_PS, ref_ID_PS, dict_PS = get_lit_data(data_folder_path, 'CO2', 'PS', T, xlxs_sheet_refno_list_PS)
        
    # Get data for CO2-PMMA
    hasExpData_PMMA, matched_sheets_PMMA, ref_no_PMMA, ref_ID_PMMA, dict_PMMA = get_lit_data(data_folder_path, 'CO2', 'PMMA', T, xlxs_sheet_refno_list_PMMA)
    
    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(width, height), constrained_layout=True)
    ax1, ax2 = axes.flatten()  # Flatten for easy iteration
    
    # Plot (a)
    for j, sheet in enumerate(matched_sheets_PS):
        ax1.plot(dict_PS[sheet]['P [MPa]'],
                dict_PS[sheet]['Solubility [g-sol/g-pol-am]'],
                color=colour,
                marker=symbols[j],
                linestyle=linestyle,
                markerfacecolor=markerfacecolor,
                label=f"{ref_ID_PS[j]}",
                )
    ax1.set_xlim(0, 50)
    ax1.set_ylim(0, 0.15)
    ax1.set_xlabel('Pressure / MPa')
    ax1.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    ax1.set_title(r'(a) $\mathrm{CO_2}$+PS')
    ax1.legend(loc='lower right')
    
    # Plot (b)
    for j, sheet in enumerate(matched_sheets_PMMA):
        ax2.plot(dict_PMMA[sheet]['P [MPa]'],
                dict_PMMA[sheet]['Solubility [g-sol/g-pol-am]'],
                color=colour,
                marker=symbols[j],
                linestyle=linestyle,
                markerfacecolor=markerfacecolor,
                label=f"{ref_ID_PMMA[j]}",
                )
    ax2.set_xlim(0)
    ax2.set_ylim(0, 0.25)
    ax2.set_xlabel('Pressure / MPa')
    # ax2.set_ylabel(r'$q$ / $\mathrm{g \, g^{-1}}$')
    ax2.set_title(r'(b) $\mathrm{CO_2}$+PMMA')
    ax2.legend(loc='lower right')
        
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_lit_data_100C.{save_format}"
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()
