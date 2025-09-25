import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import os
from pathlib import Path

def plot_fvt_DT0(
    file_path,
    width=6., height=4.1,
    colours=['C0', 'C1', 'C2'], markerfacecolor='None',
    symbols=['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h'],
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400):
    
    barToMPa = 1e-1
    
    df = pd.read_excel(file_path)

    # Filter data for the two experiment groups
    hdpe_data = df[df['file_name'].str.startswith('RUN_H_')]
    peeka_data = df[df['file_name'].str.startswith('S4')]

    # Create side-by-side subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(width, height), constrained_layout=True)

    # Get all unique pressures from both datasets
    all_pressures = sorted(pd.concat([hdpe_data['pressure / bar'], peeka_data['pressure / bar']]).unique())

    # Create pressure-to-marker mapping
    pressure_marker_map = {pressure: symbols[i % len(symbols)] for i, pressure in enumerate(all_pressures)}

    # Left plot: RUN_H_ experiments
    unique_pressures_hdpe = sorted(hdpe_data['pressure / bar'].unique())
    
    # Initialize a global dictionary to track all occurrences
    all_temp_pressure_counts_hdpe = {}
    
    for pressure in unique_pressures_hdpe:
        group = hdpe_data[hdpe_data['pressure / bar'] == pressure]
        dt0_values = group['DT_0 / cm^2 s^-1']

        # Dictionary to track occurrences of each (temp, pressure) combination
        temp_pressure_count = {}
        
        for temp, dt0 in zip(group['temperature / C'], dt0_values):
            # Create key for temp-pressure combination
            key = (temp, pressure)
            
            # Count occurrences
            if key not in temp_pressure_count:
                temp_pressure_count[key] = 0
            temp_pressure_count[key] += 1
            
            # Update global count tracker
            all_temp_pressure_counts_hdpe[key] = temp_pressure_count[key]

            # Determine color based on occurrence number
            occurrence = temp_pressure_count[key]
            if occurrence <= len(colours):
                color = colours[occurrence - 1]  # -1 for 0-based indexing
            else:
                color = colours[-1]  # Use last color for 4th+ occurrences
            
            ax1.scatter(temp, dt0,
                       marker=pressure_marker_map[pressure],
                       color=color,
                       facecolor=markerfacecolor)
        
    ax1.set_ylim(bottom=0.)
    ax1.set_xlabel('Temperature / °C')
    ax1.set_ylabel(r'$D_\mathrm{T} \, (T,p,0)$ / $\mathrm{cm^{2} \, s^{-1}}$')
    ax1.set_title('(a) HDPE')
    ax1.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
    
    # Add legend entries for this pressure
    max_count = max(all_temp_pressure_counts_hdpe.values()) if all_temp_pressure_counts_hdpe else 1
    marker_legend = [matplotlib.lines.Line2D([], [], color='black',
                                                marker=pressure_marker_map[pressure],
                                                markerfacecolor='None',
                                                linestyle='None',
                                                label=f'{pressure*barToMPa:.2g} MPa') for pressure in unique_pressures_hdpe]
    colour_legend = [matplotlib.lines.Line2D([], [], color=colours[repeat], 
                                                marker='None', 
                                                linestyle='solid',
                                                linewidth=5,
                                                label=f'Repeat {repeat+1}') for repeat in range(max_count)]
    custom_legend =  marker_legend + colour_legend
    ax1.legend(handles=custom_legend, loc='upper left', ncol=2).set_visible(True)

    # Right plot: S4 experiments
    unique_pressures_peeka = sorted(peeka_data['pressure / bar'].unique())
    
    # Initialize a global dictionary to track all occurrences
    all_temp_pressure_counts_peeka = {}

    for pressure in unique_pressures_peeka:
        group = peeka_data[peeka_data['pressure / bar'] == pressure]
        dt0_values = group['DT_0 / cm^2 s^-1']
        
        # Dictionary to track occurrences of each (temp, pressure) combination
        temp_pressure_count = {}
        
        for temp, dt0 in zip(group['temperature / C'], dt0_values):
            # Create key for temp-pressure combination
            key = (temp, pressure)
            
            # Count occurrences
            if key not in temp_pressure_count:
                temp_pressure_count[key] = 0
            temp_pressure_count[key] += 1
            
            # Update global count tracker
            all_temp_pressure_counts_peeka[key] = temp_pressure_count[key]

            # Determine color based on occurrence number
            occurrence = temp_pressure_count[key]
            if occurrence <= len(colours):
                color = colours[occurrence - 1]  # -1 for 0-based indexing
            else:
                color = colours[-1]  # Use last color for 4th+ occurrences
            
            ax2.scatter(temp, dt0,
                       marker=pressure_marker_map[pressure],
                       color=color,
                       facecolor=markerfacecolor)

    ax2.set_ylim(bottom=0., top=1.5e-8)
    ax2.set_xlabel('Temperature / °C')
    ax2.set_title('(b) PEEKa')
    ax2.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

    # Add legend entries for this pressure
    max_count = max(all_temp_pressure_counts_peeka.values()) if all_temp_pressure_counts_peeka else 1
    marker_legend = [matplotlib.lines.Line2D([], [], color='black',
                                                marker=pressure_marker_map[pressure],
                                                markerfacecolor='None',
                                                linestyle='None',
                                                label=f'{pressure*barToMPa:.2g} MPa') for pressure in unique_pressures_peeka]
    colour_legend = [matplotlib.lines.Line2D([], [], color=colours[repeat], 
                                                marker='None', 
                                                linestyle='solid',
                                                linewidth=5,
                                                label=f'Repeat {repeat+1}') for repeat in range(max_count)]
    custom_legend =  marker_legend + colour_legend
    ax2.legend(handles=custom_legend, loc='upper left', ncol=2).set_visible(True)

    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_fvt_DT0.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}.")
        
    if display_fig:
        plt.show()

def plot_fvt_Dprime(
    file_path,
    width=6., height=4.1,
    colours=['C0', 'C1', 'C2'], markerfacecolor='None',
    symbols=['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h'],
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400):
    
    barToMPa = 1e-1
    
    df = pd.read_excel(file_path)

    # Filter data for the two experiment groups
    hdpe_data = df[df['file_name'].str.startswith('RUN_H_')]
    peeka_data = df[df['file_name'].str.startswith('S4')]

    # Create side-by-side subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(width, height), constrained_layout=True)

    # Get all unique pressures from both datasets
    all_pressures = sorted(pd.concat([hdpe_data['pressure / bar'], peeka_data['pressure / bar']]).unique())

    # Create pressure-to-marker mapping
    pressure_marker_map = {pressure: symbols[i % len(symbols)] for i, pressure in enumerate(all_pressures)}

    # Left plot: RUN_H_ experiments
    unique_pressures_hdpe = sorted(hdpe_data['pressure / bar'].unique())
    
    # Initialize a global dictionary to track all occurrences
    all_temp_pressure_counts_hdpe = {}
    
    for pressure in unique_pressures_hdpe:
        group = hdpe_data[hdpe_data['pressure / bar'] == pressure]
        dprime_values = group['D1_prime']

        # Dictionary to track occurrences of each (temp, pressure) combination
        temp_pressure_count = {}
        
        for temp, dprime in zip(group['temperature / C'], dprime_values):
            # Create key for temp-pressure combination
            key = (temp, pressure)
            
            # Count occurrences
            if key not in temp_pressure_count:
                temp_pressure_count[key] = 0
            temp_pressure_count[key] += 1
            
            # Update global count tracker
            all_temp_pressure_counts_hdpe[key] = temp_pressure_count[key]

            # Determine color based on occurrence number
            occurrence = temp_pressure_count[key]
            if occurrence <= len(colours):
                color = colours[occurrence - 1]  # -1 for 0-based indexing
            else:
                color = colours[-1]  # Use last color for 4th+ occurrences
            
            ax1.scatter(temp, dprime,
                       marker=pressure_marker_map[pressure],
                       color=color,
                       facecolor=markerfacecolor)
        
    ax1.set_ylim(bottom=0., top=5.)
    ax1.set_xlabel('Temperature / °C')
    ax1.set_ylabel(r"$D'_{0}$")
    ax1.set_title('(a) HDPE')
    ax1.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
    
    # Add legend entries for this pressure
    max_count = max(all_temp_pressure_counts_hdpe.values()) if all_temp_pressure_counts_hdpe else 1
    marker_legend = [matplotlib.lines.Line2D([], [], color='black',
                                                marker=pressure_marker_map[pressure],
                                                markerfacecolor='None',
                                                linestyle='None',
                                                label=f'{pressure*barToMPa:.2g} MPa') for pressure in unique_pressures_hdpe]
    colour_legend = [matplotlib.lines.Line2D([], [], color=colours[repeat], 
                                                marker='None', 
                                                linestyle='solid',
                                                linewidth=5,
                                                label=f'Repeat {repeat+1}') for repeat in range(max_count)]
    custom_legend =  marker_legend + colour_legend
    ax1.legend(handles=custom_legend, loc='upper left', ncol=2).set_visible(True)

    # Right plot: S4 experiments
    unique_pressures_peeka = sorted(peeka_data['pressure / bar'].unique())
    
    # Initialize a global dictionary to track all occurrences
    all_temp_pressure_counts_peeka = {}

    for pressure in unique_pressures_peeka:
        group = peeka_data[peeka_data['pressure / bar'] == pressure]
        dprime_values = group['D1_prime']
        
        # Dictionary to track occurrences of each (temp, pressure) combination
        temp_pressure_count = {}
        
        for temp, dprime in zip(group['temperature / C'], dprime_values):
            # Create key for temp-pressure combination
            key = (temp, pressure)
            
            # Count occurrences
            if key not in temp_pressure_count:
                temp_pressure_count[key] = 0
            temp_pressure_count[key] += 1
            
            # Update global count tracker
            all_temp_pressure_counts_peeka[key] = temp_pressure_count[key]

            # Determine color based on occurrence number
            occurrence = temp_pressure_count[key]
            if occurrence <= len(colours):
                color = colours[occurrence - 1]  # -1 for 0-based indexing
            else:
                color = colours[-1]  # Use last color for 4th+ occurrences

            ax2.scatter(temp, dprime,
                       marker=pressure_marker_map[pressure],
                       color=color,
                       facecolor=markerfacecolor)

    ax2.set_ylim(bottom=0., top=4.)
    ax2.set_xlabel('Temperature / °C')
    ax2.set_title('(b) PEEKa')
    ax2.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))

    # Add legend entries for this pressure
    max_count = max(all_temp_pressure_counts_peeka.values()) if all_temp_pressure_counts_peeka else 1
    marker_legend = [matplotlib.lines.Line2D([], [], color='black',
                                                marker=pressure_marker_map[pressure],
                                                markerfacecolor='None',
                                                linestyle='None',
                                                label=f'{pressure*barToMPa:.2g} MPa') for pressure in unique_pressures_peeka]
    colour_legend = [matplotlib.lines.Line2D([], [], color=colours[repeat], 
                                                marker='None', 
                                                linestyle='solid',
                                                linewidth=5,
                                                label=f'Repeat {repeat+1}') for repeat in range(max_count)]
    custom_legend =  marker_legend + colour_legend
    ax2.legend(handles=custom_legend, loc='upper left', ncol=2).set_visible(True)

    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_fvt_Dprime.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        filepath = Path(folder_to_save) / filename
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}.")
        
    if display_fig:
        plt.show()