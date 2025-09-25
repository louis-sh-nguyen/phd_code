import os
import pandas as pd
import matplotlib.pyplot as plt
import os
from utils import exp_dict


def plot_pressure_step_fit(
    data_folder_path,
    width=6., height=4.0,
    x_lo=0., y_lo=0., x_up=None, y_up=1.25,
    pressure_colour='grey',
    flux_exp_colour='black',
    flux_model_colour='C2',
    symbol='None',
    markersize=2,
    linestyle='solid',
    linewidth=1,
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    barToMPa = 0.1  # Conversion factor from bar to MPa
    
    S4R5_exp_data = pd.read_csv(f'{data_folder_path}/S4R5_exp_data.csv')
    S4R5_model_data = pd.read_csv(f'{data_folder_path}/S4R5_model_data.csv')
    S4R6_exp_data = pd.read_csv(f'{data_folder_path}/S4R6_exp_data.csv')
    S4R6_model_data = pd.read_csv(f'{data_folder_path}/S4R6_model_data.csv')

    # Create side-by-side subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(width, height), constrained_layout=True)

    # Plot S4R6
    line1 = ax1.plot(S4R6_exp_data['time'], S4R6_exp_data['normalised_flux'], color=flux_exp_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Exp. Flux')
    line2 = ax1.plot(S4R6_model_data['time'], S4R6_model_data['normalised_flux'], color=flux_model_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Model Flux')
    # Create second y-axis for S4R6 pressure
    ax1_pressure = ax1.twinx()
    line3 = ax1_pressure.plot(S4R6_exp_data['time'], S4R6_exp_data['pressure']*barToMPa, color=pressure_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Pressure')
    ax1_pressure.set_ylabel('Pressure / MPa', color='black')
    ax1_pressure.tick_params(axis='y', labelcolor='black')
    ax1_pressure.set_ylim(bottom=0., top=40)
    # Set title
    ax1.set_title(f'(a) {exp_dict['S4R6']}')

    # Plot S4R5
    line4 = ax2.plot(S4R5_exp_data['time'], S4R5_exp_data['normalised_flux'], color=flux_exp_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Exp. Flux')
    line5 = ax2.plot(S4R5_model_data['time'], S4R5_model_data['normalised_flux'], color=flux_model_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Model Flux')
    # Create second y-axis for S4R5 pressure
    ax2_pressure = ax2.twinx()
    line6 = ax2_pressure.plot(S4R5_exp_data['time'], S4R5_exp_data['pressure']*barToMPa, color=pressure_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Pressure')
    ax2_pressure.set_ylabel('Pressure / MPa', color='black')
    ax2_pressure.tick_params(axis='y', labelcolor='black')
    ax2_pressure.set_ylim(bottom=0., top=40)
    # Set title
    ax2.set_title(f'(b) {exp_dict['S4R5']}')

    for i, ax in enumerate([ax1, ax2]):
        # Set axis labels
        if i == 1:
            ax.set_xlabel('Time / s')
        ax.set_ylabel('Norm. Flux')
        
        # Set axis limits
        if x_lo is not None:
            ax.set_xlim(left=x_lo)
        if x_up is not None:
            ax.set_xlim(right=x_up)
        if y_lo is not None:
            ax.set_ylim(bottom=y_lo)
        if y_up is not None:
            ax.set_ylim(top=y_up)
        ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
        ax.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
        
        # Set combined legend
        lines1 = line1 + line2 + line3
        labels1 = [l.get_label() for l in lines1]
        ax1.legend(lines1, labels1, loc='lower right')

        lines2 = line4 + line5 + line6
        labels2 = [l.get_label() for l in lines2]
        ax2.legend(lines2, labels2, loc='lower right')
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_pressure_step_fit.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")

    if display_fig:
        plt.show()