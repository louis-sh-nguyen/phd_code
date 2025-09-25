import os
import pandas as pd
import matplotlib.pyplot as plt
import os
from utils import exp_dict

def plot_pressure_step_raw(
    data_folder_path,
    width=6., height=4.0,
    x_lo=0., y_lo=0., 
    flux_colour='black',
    pressure_colour='grey',
    temperature_colour='red',
    symbol='None',
    markersize=2,
    linestyle='solid',
    linewidth=1,
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    barToMPa = 0.1  # Conversion factor from bar to MPa
    
    S4R3_exp_data = pd.read_csv(f'{data_folder_path}/S4R3_processed.csv')
    S4R4_exp_data = pd.read_csv(f'{data_folder_path}/S4R4_processed.csv')
    S4R5_exp_data = pd.read_csv(f'{data_folder_path}/S4R5_processed.csv')
    S4R6_exp_data = pd.read_csv(f'{data_folder_path}/S4R6_processed.csv')

    # Shorten the raw data for plotting
    S4R4_exp_data = S4R4_exp_data[S4R4_exp_data['time'] < 5.7e5]
    S4R6_exp_data = S4R6_exp_data[S4R6_exp_data['time'] < 2.9e5]
    S4R5_exp_data = S4R5_exp_data[S4R5_exp_data['time'] < 4.5e5]
    
    # Create 4x1 subplots
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(width, height), constrained_layout=True)

    # Plot S4R3
    line1 = ax1.plot(S4R3_exp_data['time'], S4R3_exp_data['flux'], color=flux_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Flux')
    # Create second y-axis for pressure
    ax1_pressure = ax1.twinx()
    line2 = ax1_pressure.plot(S4R3_exp_data['time'], S4R3_exp_data['pressure']*barToMPa, color=pressure_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Pressure')
    ax1_pressure.set_ylabel('Pressure / MPa', color='black')
    ax1_pressure.tick_params(axis='y', labelcolor='black')
    ax1_pressure.set_ylim(bottom=0., top=40)
    # Create third y-axis for temperature
    ax1_temperature = ax1.twinx()
    ax1_temperature.spines['right'].set_position(('outward', 40))
    line3 = ax1_temperature.plot(S4R3_exp_data['time'], S4R3_exp_data['temperature'], color=temperature_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Temperature')
    ax1_temperature.set_ylabel('Temperature / °C', color='black')
    ax1_temperature.tick_params(axis='y', labelcolor='black')
    ax1_temperature.set_ylim(bottom=0., top=30)
    
    ax1.set_xlim(right=4e6)
    ax1.set_ylim(top=5e-5)
    ax1.set_title(f'(a) {exp_dict['S4R3']}')

    # Plot S4R4
    line1_s4r4 = ax2.plot(S4R4_exp_data['time'], S4R4_exp_data['flux'], color=flux_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Flux')
    # Create second y-axis for pressure
    ax2_pressure = ax2.twinx()
    line2_s4r4 = ax2_pressure.plot(S4R4_exp_data['time'], S4R4_exp_data['pressure']*barToMPa, color=pressure_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Pressure')
    ax2_pressure.set_ylabel('Pressure / MPa', color='black')
    ax2_pressure.tick_params(axis='y', labelcolor='black')
    ax2_pressure.set_ylim(bottom=0., top=40)
    # Create third y-axis for temperature
    ax2_temperature = ax2.twinx()
    ax2_temperature.spines['right'].set_position(('outward', 40))
    line3_s4r4 = ax2_temperature.plot(S4R4_exp_data['time'], S4R4_exp_data['temperature'], color=temperature_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Temperature')
    ax2_temperature.set_ylabel('Temperature / °C', color='black')
    ax2_temperature.tick_params(axis='y', labelcolor='black')
    ax2_temperature.set_ylim(bottom=0., top=60)

    ax2.set_ylim(bottom=0., top=1e-4)
    ax2.set_title(f'(b) {exp_dict['S4R4']}')

    # Plot S4R6
    line1_s4r6 = ax3.plot(S4R6_exp_data['time'], S4R6_exp_data['flux'], color=flux_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Flux')
    # Create second y-axis for pressure
    ax3_pressure = ax3.twinx()
    line2_s4r6 = ax3_pressure.plot(S4R6_exp_data['time'], S4R6_exp_data['pressure']*barToMPa, color=pressure_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Pressure')
    ax3_pressure.set_ylabel('Pressure / MPa', color='black')
    ax3_pressure.tick_params(axis='y', labelcolor='black')
    ax3_pressure.set_ylim(bottom=0., top=40)
    # Create third y-axis for temperature
    ax3_temperature = ax3.twinx()
    ax3_temperature.spines['right'].set_position(('outward', 40))
    line3_s4r6 = ax3_temperature.plot(S4R6_exp_data['time'], S4R6_exp_data['temperature'], color=temperature_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Temperature')
    ax3_temperature.set_ylabel('Temperature / °C', color='black')
    ax3_temperature.tick_params(axis='y', labelcolor='black')
    ax3_temperature.set_ylim(bottom=0., top=60)
    
    ax3.set_ylim(top=1e-4)
    ax3.set_title(f'(c) {exp_dict['S4R6']}')

    # Plot S4R5
    line1_s4r5 = ax4.plot(S4R5_exp_data['time'], S4R5_exp_data['flux'], color=flux_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Flux')
    # Create second y-axis for pressure
    ax4_pressure = ax4.twinx()
    line2_s4r5 = ax4_pressure.plot(S4R5_exp_data['time'], S4R5_exp_data['pressure']*barToMPa, color=pressure_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Pressure')
    ax4_pressure.set_ylabel('Pressure / MPa', color='black')
    ax4_pressure.tick_params(axis='y', labelcolor='black')
    ax4_pressure.set_ylim(bottom=0., top=40)
    # Create third y-axis for temperature
    ax4_temperature = ax4.twinx()
    ax4_temperature.spines['right'].set_position(('outward', 40))
    line3_s4r5 = ax4_temperature.plot(S4R5_exp_data['time'], S4R5_exp_data['temperature'], color=temperature_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Temperature')
    ax4_temperature.set_ylabel('Temperature / °C', color='black')
    ax4_temperature.tick_params(axis='y', labelcolor='black')
    ax4_temperature.set_ylim(bottom=0., top=80)
    
    ax4.set_title(f'(d) {exp_dict['S4R5']}')

    for i, ax in enumerate([ax1, ax2, ax3, ax4]):
        # Set axis labels
        if i == 3:
            ax.set_xlabel('Time / s')
        ax.set_ylabel(r'Flux / $\mathrm{cm^{3}(STP) \, cm^{-2} \, s^{-1}}$')
        
        # Set axis limits
        if x_lo is not None:
            ax.set_xlim(left=x_lo)
        if y_lo is not None:
            ax.set_ylim(bottom=y_lo)
        ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
        ax.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
        
    # Set legend for the first subplot (all others will use the same)
    lines_all = line1 + line2 + line3
    labels_all = [l.get_label() for l in lines_all]        
    
    ax1.legend(lines_all, labels_all, loc='lower right', labelspacing=0.3)
    ax2.legend(lines_all, labels_all, loc='lower right', labelspacing=0.3)
    ax3.legend(lines_all, labels_all, loc='lower right', labelspacing=0.3)
    ax4.legend(lines_all, labels_all, loc='lower right', labelspacing=0.3)
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_pressure_step_raw.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()
