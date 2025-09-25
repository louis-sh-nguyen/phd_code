import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path
from utils import exp_dict

def plot_example_flux_curves(
    breakthrough_file_path='../data/FVT/RUN_H_25C-50bar/experimental_data_20250710-182627.csv',
    pressure_step_file_path='../data/multi-step/S4R6_processed.csv',
    width=6., height=4.1,
    flux_colour='black', 
    pressure_colour='grey',
    symbol='None', markersize=2, linestyle='solid', linewidth=1,
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400):
        
        barToMPa = 1e-1
        
        # Read data
        df_single = pd.read_csv(breakthrough_file_path)
        df_step = pd.read_csv(pressure_step_file_path)
        
        # Trim data
        df_step = df_step[df_step['time'] < 2.9e5]

        # Create 2x1 subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(width, height), constrained_layout=True)

        # Left plot: breakthrough curves
        line1 = ax1.plot(df_single['time'], df_single['flux'], color=flux_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Flux')
        # ax1.set_xlabel('Time / s')
        ax1.set_ylabel(r'Flux / $\mathrm{cm^{3}(STP) \, cm^{-2} \, s^{-1}}$')
        # Set axis apperance
        ax1.set_xlim(0)
        ax1.set_ylim(0)
        # ax1.set_xticks([])
        # ax1.set_yticks([])
        # Create pressure axis
        ax1_pressure = ax1.twinx()
        line2 = ax1_pressure.plot(df_single['time'], df_single['pressure']*barToMPa, color=pressure_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Pressure')
        # Set axis appearance
        ax1_pressure.set_ylabel('Pressure / MPa', color='black')
        ax1_pressure.tick_params(axis='y', labelcolor='black')
        ax1_pressure.set_ylim(bottom=0., top=6.)
        # ax1_pressure.set_yticks([])
        ax1.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
        ax1.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
        # ax1_pressure.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
        # Set title
        ax1.set_title(f'(a) Single-pressure-step')

        # Right plot: pressure step curves
        line3 = ax2.plot(df_step['time'], df_step['flux'], color=flux_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Flux')
        ax2.set_xlim(0)
        ax2.set_ylim(0)
        # ax2.set_xticks([])
        # ax2.set_yticks([])        
        
        # Create second y-axis for pressure
        ax2_pressure = ax2.twinx()
        line4 = ax2_pressure.plot(df_step['time'], df_step['pressure']*barToMPa, color=pressure_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, alpha=0.7, label='Pressure')
        ax2.set_xlabel('Time / s')
        ax2.set_ylabel(r'Flux / $\mathrm{cm^{3}(STP) \, cm^{-2} \, s^{-1}}$')
        # Set axis appearance
        ax2_pressure.set_ylabel('Pressure / MPa', color='black')
        ax2_pressure.tick_params(axis='y', labelcolor='black')
        ax2_pressure.set_ylim(bottom=0.)
        # ax2_pressure.set_yticks([])
        ax2.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
        ax2.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
        # ax2_pressure.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
        # Set title
        ax2.set_title(f'(b) Multiple-pressure-step')
        
        # Set legend for the first subplot (all others will use the same)
        lines_all = line1 + line2
        labels_all = [l.get_label() for l in lines_all]        
        
        ax1.legend(lines_all, labels_all, loc='lower right', labelspacing=0.3)
        ax2.legend(lines_all, labels_all, loc='lower right', labelspacing=0.3)
        
        if save_fig:
                os.makedirs(folder_to_save, exist_ok=True)
                filename = f"fig_example_flux_curves.{save_format}"
                filepath = os.path.join(folder_to_save, filename)
                filepath = Path(folder_to_save) / filename
                fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
                print(f"Plot successfully exported to {filepath}.")
                
        if display_fig:
                plt.show()

