import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
from pathlib import Path

def plot_solubility_comparison_hdpe(    
    data_path,
    width=5., height=3.5,
    y_lo=None, y_up=None, x_lo=None, x_up=None,
    colour='black',
    rep_colours = ['C0', 'C1', 'C2'],
    symbols=['o', 's', '^'],
    markerfacecolor='None',
    display_legend=True, display_fig=True, save_fig=False, folder_to_save ='../figures', save_format='pdf', dpi=400):
    
    barToMPa = 1e-1
    
    # Read data
    df_fvt = pd.read_excel(data_path, sheet_name='FVT')
    df_timelag = pd.read_excel(data_path, sheet_name='timelag')
    df_exp = pd.read_excel(data_path, sheet_name='sorption_exp')
    
    # Temperature list
    all_temp = [25, 50, 75]     # [C]
    
    # Source-symbol map
    source_symbol_mapping = {'Time-lag': symbols[0], 
                             'FVT': symbols[1], 
                             'MSB Exp.': symbols[2]}
    
    fig, axes = plt.subplots(2, 2, figsize=(width, height), constrained_layout=True)
    axes = axes.flatten()
    letters = ['(a)', '(b)', '(c)']
    for i, temp in enumerate(all_temp):
        ax = axes[i]
        group = df_timelag[df_timelag['temperature / C'] == temp]

        # Plot time lag
        # Dictionary to track occurrences of each (temp, pressure) combination for timelag
        temp_pressure_count_tl = {}
        
        for pressure, solubility in zip(group['pressure / bar'], group['solubility_am / g-co2/g_pol_amor']):
            # Create key for temp-pressure combination
            key = (temp, pressure)
            
            # Count occurrences
            if key not in temp_pressure_count_tl:
                temp_pressure_count_tl[key] = 0
            temp_pressure_count_tl[key] += 1
            
            # Determine color based on occurrence number
            occurrence = temp_pressure_count_tl[key]
            if occurrence <= len(rep_colours):
                color = rep_colours[occurrence - 1]  # -1 for 0-based indexing
            else:
                color = rep_colours[-1]  # Use last color for 4th+ occurrences
            
            ax.scatter(pressure*barToMPa, solubility,
                        marker=source_symbol_mapping['Time-lag'],
                        color=color,
                        facecolor=markerfacecolor)
    
        # Plot FVT data
        group = df_fvt[df_fvt['temperature / C'] == temp]
        
        # Dictionary to track occurrences of each (temp, pressure) combination for FVT
        temp_pressure_count_fvt = {}
        
        for pressure, solubility in zip(group['pressure / bar'], group['solubility_am / g-co2/g_pol_amor']):
            # Create key for temp-pressure combination
            key = (temp, pressure)
            
            # Count occurrences
            if key not in temp_pressure_count_fvt:
                temp_pressure_count_fvt[key] = 0
            temp_pressure_count_fvt[key] += 1
            
            # Determine color based on occurrence number
            occurrence = temp_pressure_count_fvt[key]
            if occurrence <= len(rep_colours):
                color = rep_colours[occurrence - 1]  # -1 for 0-based indexing
            else:
                color = rep_colours[-1]  # Use last color for 4th+ occurrences

            ax.scatter(pressure*barToMPa, solubility,
                      marker=source_symbol_mapping['FVT'],
                      color=color,
                      facecolor=markerfacecolor)

        # Plot experimental data
        group = df_exp[df_exp['temperature / C'] == temp]
        ax.scatter(group['pressure / bar']*barToMPa, 
                group['solubility_am / g-co2/g_pol_amor'], 
                marker=source_symbol_mapping['MSB Exp.'],
                color=colour,
                facecolor=markerfacecolor,
                label='MSB Exp.')

        # Set title
        ax.set_title(f'{letters[i]} {temp} °C')

        # Add legend entries for this pressure
        max_count = max(temp_pressure_count_fvt.values()) if temp_pressure_count_fvt else 1

        # Extract unique pressures from the keys
        marker_legend = [matplotlib.lines.Line2D([], [], color='black',
                                                    marker=source_symbol_mapping[source],
                                                    markerfacecolor='None',
                                                    linestyle='None',
                                                    label=source) for source in ['FVT', 'Time-lag', 'MSB Exp.']]
        colour_legend = [matplotlib.lines.Line2D([], [], color=rep_colours[repeat], 
                                                    marker='None', 
                                                    linestyle='solid',
                                                    linewidth=5,
                                                    label=f'Repeat {repeat+1}') for repeat in range(max_count)]
        custom_legend = marker_legend + colour_legend
        # ax.legend(handles=custom_legend, loc='best', ncol=2).set_visible(True)
    
    # Custom legend
    # 25 C
    marker_legend = [matplotlib.lines.Line2D([], [], color='black',
                                                marker=source_symbol_mapping[source],
                                                markerfacecolor='None',
                                                linestyle='None',
                                                label=source) for source in ['Time-lag', 'FVT', 'MSB Exp.']]
    colour_legend = [matplotlib.lines.Line2D([], [], color=rep_colours[repeat], 
                                                marker='None', 
                                                linestyle='solid',
                                                linewidth=5,
                                                label=f'Repeat {repeat+1}') for repeat in range(3)]
    custom_legend = marker_legend + colour_legend
    axes[0].legend(handles=custom_legend, loc='upper left', ncol=2).set_visible(True)
    
    # 50 C
    marker_legend = [matplotlib.lines.Line2D([], [], color='black',
                                                marker=source_symbol_mapping[source],
                                                markerfacecolor='None',
                                                linestyle='None',
                                                label=source) for source in ['Time-lag', 'FVT', 'MSB Exp.']]
    colour_legend = [matplotlib.lines.Line2D([], [], color=rep_colours[repeat], 
                                                marker='None', 
                                                linestyle='solid',
                                                linewidth=5,
                                                label=f'Repeat {repeat+1}') for repeat in range(1)]
    custom_legend = marker_legend + colour_legend
    axes[1].legend(handles=custom_legend, loc='best', ncol=1).set_visible(True)

    # 75 C
    marker_legend = [matplotlib.lines.Line2D([], [], color='black',
                                                marker=source_symbol_mapping[source],
                                                markerfacecolor='None',
                                                linestyle='None',
                                                label=source) for source in ['Time-lag', 'FVT']]
    colour_legend = [matplotlib.lines.Line2D([], [], color=rep_colours[repeat], 
                                                marker='None', 
                                                linestyle='solid',
                                                linewidth=5,
                                                label=f'Repeat {repeat+1}') for repeat in range(1)]
    custom_legend = marker_legend + colour_legend
    axes[2].legend(handles=custom_legend, loc='upper left', ncol=1).set_visible(True)

    # Set label
    for i in [1, 2]:
        axes[i].set_xlabel('Pressure / MPa')
    for i in [0, 2]:
        axes[i].set_ylabel(r'$q_{\mathrm{am}}$ / $\mathrm{g \, g^{-1}}$')
    
    # Set limit
    axes[0].set_xlim(0, 30)
    axes[1].set_xlim(0, 30)
    axes[2].set_xlim(0, 15)
    axes[0].set_ylim(0.04, 0.12)
    axes[1].set_ylim(0.02, 0.10)
    axes[2].set_ylim(0.02, 0.12)
    # Hide unused subplots
    axes[3].set_visible(False)
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        save_fig_path = Path(folder_to_save) / f'fig_solubility_comparison.{save_format}'
        fig.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {save_fig_path}.")
        
    if display_fig:
        plt.show()

# def plot_solubility_comparison_hdpe(    
#     data_path,
#     width=5., height=3.5,
#     y_lo=None, y_up=None,
#     colours=['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'], 
#     symbols=['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h'],
#     markerfacecolor='None',
#     display_legend=True, display_fig=True, save_fig=False, folder_to_save ='../figures', save_format='pdf', dpi=400):
    
#     barToMPa = 1e-1
    
#     # Read data
#     df_fvt = pd.read_excel(data_path, sheet_name='FVT')
#     df_timelag = pd.read_excel(data_path, sheet_name='timelag')
#     df_exp = pd.read_excel(data_path, sheet_name='sorption_exp')
    
#     # Get all unique pressures from both datasets
#     all_pressures = sorted(pd.concat([df_fvt['pressure / bar'], df_timelag['pressure / bar'], df_exp['_pressure / bar']]).unique())

#     # Create pressure-to-marker mapping
#     pressure_marker_map = {pressure: symbols[i % len(symbols)] for i, pressure in enumerate(all_pressures)}
    
#     # Create source-to-colour mapping
#     source_colour_map = {
#         'FVT': colours[0],
#         'timelag': colours[1],
#         'exp': colours[2],
#     }
    
#     # Get unique pressures for each dataset
#     unique_pressures_fvt = sorted(df_fvt['pressure / bar'].unique())
#     unique_pressures_timelag = sorted(df_timelag['pressure / bar'].unique())
#     unique_pressures_exp = sorted(df_exp['_pressure / bar'].unique())
    
#     fig = plt.figure(figsize=(width, height))
#     ax = fig.add_subplot(111)
    
#     # Plot timelag data
#     for pressure in unique_pressures_timelag:
#         group = df_timelag[df_timelag['pressure / bar'] == pressure]
#         ax.scatter(group['temperature / C'], 
#                 group['solubility_am / g-co2/g_pol_amor'], 
#                 marker=pressure_marker_map[pressure],
#                 color=source_colour_map['timelag'],
#                 facecolor=markerfacecolor,
#                 label=f'{pressure*barToMPa:.0f} MPa')
        
#     # Plot FVT data
#     for pressure in unique_pressures_fvt:
#         group = df_fvt[df_fvt['pressure / bar'] == pressure]
#         ax.scatter(group['temperature / C'], 
#                 group['solubility_am / g-co2/g_pol_amor'], 
#                 marker=pressure_marker_map[pressure],
#                 color=source_colour_map['FVT'],
#                 facecolor=markerfacecolor,
#                 label=f'{pressure*barToMPa:.0f} MPa')

#     # Plot experimental data
#     for pressure in unique_pressures_exp:
#         group = df_exp[df_exp['_pressure / bar'] == pressure]
#         ax.scatter(group['temperature / C'], 
#                 group['solubility_am / g-co2/g_pol_amor'], 
#                 marker=pressure_marker_map[pressure],
#                 color=source_colour_map['exp'],
#                 facecolor=markerfacecolor,
#                 label=f'{pressure:.0f} MPa')

#     ax.set_xlabel('Temperature / °C')
#     ax.set_ylabel(r'$q_{\mathrm{am}}$ / $\mathrm{g \, g^{-1}}$')
#     # ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
    
#     # Set y-axis limits 
#     if y_lo is not None:
#         ax.set_ylim(bottom=y_lo)
#     if y_up is not None:
#         ax.set_ylim(top=y_up)
        
#     # Add legend by colours and symbols
#     if display_legend == True:
#         # Legend dict
#         legend_source_dict = {
#             'FVT': 'FVT',
#             'timelag': 'Time-lag',
#             'exp': 'Exp.',
#         }
#         # Use symbols for type 
#         marker_legend = [matplotlib.lines.Line2D([], [], color='black', marker=pressure_marker_map[pressure], markersize=6, markerfacecolor='None', linestyle='None', label=f'{pressure*barToMPa:.0f} MPa') for pressure in pressure_marker_map.keys()]
#         # Use colours for sources
#         colour_legend = [matplotlib.lines.Line2D([], [], color=source_colour_map[type], marker='None', linestyle='solid', linewidth=3, label=f'{legend_source_dict[type]}') for type in source_colour_map.keys()]
#         custom_legend =  marker_legend + colour_legend
#         ax.legend(handles=custom_legend, bbox_to_anchor=(1.05, 1), loc='upper left').set_visible(True)
    
#     if save_fig:
#         os.makedirs(folder_to_save, exist_ok=True)
#         save_fig_path = Path(folder_to_save) / f'fig_solubility_comparison.{save_format}'
#         fig.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
#         print(f"Plot successfully exported to {save_fig_path}.")
        
#     if display_fig:
#         plt.show()

# def plot_solubility_comparison_hdpe(    
#     data_path,
#     width=5., height=3.5,
#     y_lo=None, y_up=None,
#     colours=['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'], 
#     symbols=['o', 's', '^', 'D', 'v', '<', '>', 'p', '*', 'h'],
#     markerfacecolor='None',
#     display_legend=True, display_fig=True, save_fig=False, folder_to_save ='../figures', save_format='pdf', dpi=400):
    
#     barToMPa = 1e-1
    
#     # Read data
#     df_fvt = pd.read_excel(data_path, sheet_name='FVT')
#     df_timelag = pd.read_excel(data_path, sheet_name='timelag')
#     df_exp = pd.read_excel(data_path, sheet_name='sorption_exp')
    
#     # Get all unique pressures from both datasets
#     all_pressures = sorted(pd.concat([df_fvt['pressure / bar'], df_timelag['pressure / bar'], df_exp['_pressure / bar']]).unique())

#     # Create pressure-to-colour mapping
#     pressure_colour_map = {pressure: colours[i % len(colours)] for i, pressure in enumerate(all_pressures)}
    
#     # Create source-to-colour mapping
#     source_symbol_map = {
#         'FVT': symbols[0],
#         'timelag': symbols[1],
#         'exp': symbols[2],
#     }
    
#     # Get unique pressures for each dataset
#     unique_pressures_fvt = sorted(df_fvt['pressure / bar'].unique())
#     unique_pressures_timelag = sorted(df_timelag['pressure / bar'].unique())
#     unique_pressures_exp = sorted(df_exp['_pressure / bar'].unique())
    
#     fig = plt.figure(figsize=(width, height))
#     ax = fig.add_subplot(111)
    
#     # Plot FVT data
#     for pressure in unique_pressures_fvt:
#         group = df_fvt[df_fvt['pressure / bar'] == pressure]
#         ax.scatter(group['temperature / C'], 
#                 group['solubility_am / g-co2/g_pol_amor'], 
#                 marker=source_symbol_map['FVT'],
#                 color=pressure_colour_map[pressure],
#                 facecolor=markerfacecolor,
#                 )

#     # Plot timelag data
#     for pressure in unique_pressures_timelag:
#         group = df_timelag[df_timelag['pressure / bar'] == pressure]
#         ax.scatter(group['temperature / C'], 
#                 group['solubility_am / g-co2/g_pol_amor'], 
#                 marker=source_symbol_map['timelag'],
#                 color=pressure_colour_map[pressure],
#                 facecolor=markerfacecolor,
#                 )
    
#     # Plot experimental data
#     for pressure in unique_pressures_exp:
#         group = df_exp[df_exp['_pressure / bar'] == pressure]
#         ax.scatter(group['temperature / C'], 
#                 group['solubility_am / g-co2/g_pol_amor'], 
#                 marker=source_symbol_map['exp'],
#                 color=pressure_colour_map[pressure],
#                 facecolor=markerfacecolor,
#                 )

#     ax.set_xlabel('Temperature / °C')
#     ax.set_ylabel(r'$q_{\mathrm{am}}$ / $\mathrm{g \, g^{-1}}$')
#     # ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
    
#     # Set y-axis limits 
#     if y_lo is not None:
#         ax.set_ylim(bottom=y_lo)
#     if y_up is not None:
#         ax.set_ylim(top=y_up)
    
#     # Add legend by colours and symbols
#     if display_legend == True:
#         # Legend dict
#         legend_source_dict = {
#             'FVT': 'FVT',
#             'timelag': 'Time Lag',
#             'exp': 'Exp.',
#         }
#         # Use colours for sources
#         colour_legend = [matplotlib.lines.Line2D([], [], color=pressure_colour_map[pressure], marker='None', linestyle='solid', linewidth=3, label=f'{pressure*barToMPa:.0f} MPa') for pressure in pressure_colour_map.keys()]
#         # Use symbols for type 
#         marker_legend = [matplotlib.lines.Line2D([], [], color='black', marker=source_symbol_map[source], markersize=6, markerfacecolor='None', linestyle='None', label=legend_source_dict[source]) for source in source_symbol_map.keys()]
#         custom_legend = colour_legend + marker_legend
#         ax.legend(handles=custom_legend, bbox_to_anchor=(1.05, 1), loc='upper left').set_visible(True)
    
#     if save_fig:
#         os.makedirs(folder_to_save, exist_ok=True)
#         save_fig_path = Path(folder_to_save) / f'fig_solubility_comparison.{save_format}'
#         fig.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
#         print(f"Plot successfully exported to {save_fig_path}.")
        
#     if display_fig:
#         plt.show()
