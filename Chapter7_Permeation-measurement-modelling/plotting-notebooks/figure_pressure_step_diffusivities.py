import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path
from utils import exp_dict

def plot_pressure_step_diffusivities(
    file_path,
    width=6., height=4.1,
    colour='black', markerfacecolor='None',
    symbols=['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h'],
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400):
    
    barToMPa = 1e-1
    
    df1 = pd.read_excel(file_path, sheet_name='S4R6')
    df2 = pd.read_excel(file_path, sheet_name='S4R5')

    # Create side-by-side subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(width, height), constrained_layout=True)

    # Left plot: D'0i
    ax1.scatter(df1['_pressure / bar']*barToMPa, 
            df1['D0_i'], 
            marker=symbols[0],
            color=colour,
            facecolor=markerfacecolor,
            label=f'{exp_dict['S4R6']}')
    
    ax1.scatter(df2['_pressure / bar']*barToMPa, 
            df2['D0_i'], 
            marker=symbols[1],
            color=colour,
            facecolor=markerfacecolor,
            label=f'{exp_dict['S4R5']}')
    ax1.set_xlim(left=0.)
    ax1.set_xlabel('Pressure / MPa')
    ax1.set_ylabel(r"$D'_\mathrm{0,i}$")
    ax1.set_title('(a)')
    ax1.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
    ax1.legend(loc='lower right')

    # Right plot: DT0
    ax2.scatter(df1['_pressure / bar']*barToMPa, 
            df1['DT0_i'], 
            marker=symbols[0],
            color=colour,
            facecolor=markerfacecolor,
            label=f'{exp_dict['S4R6']}')
    
    ax2.scatter(df2['_pressure / bar']*barToMPa, 
            df2['DT0_i'], 
            marker=symbols[1],
            color=colour,
            facecolor=markerfacecolor,
            label=f'{exp_dict['S4R5']}')
    ax2.set_xlim(left=0.)
    ax2.set_ylim(bottom=0.4e-8)
    ax2.set_xlabel('Pressure / MPa')
    ax2.set_ylabel(r'$D_\mathrm{T,i}(T,p,0)$ / $\mathrm{cm^{2} \, s^{-1}}$')
    ax2.set_title('(b)')
    ax2.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
    ax2.legend(loc='lower right')

    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_pressure_step_diffusivities.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}.")
        
    if display_fig:
        plt.show()
