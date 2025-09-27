import pandas as pd
import matplotlib.pyplot as plt
import os
import re
from matplotlib.patches import Patch

# Using scatter plots
def plot_crystallinity_from_excel(
    excel_file_path,
    colours=['C0', 'C2'],
    width=6, height=6,
    symbol='s', linestyle='None', markerfacecolor='None',
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400    
    ):
    # Define the desired order
    desired_order = [
        'PEEK500907_26C_1.csv',
        'PEEK500907_50C_1.csv',
        'PEEK500907_100C_1.csv',
        'PEEK500907_150C_1.csv',
        'PEEK500907_200C_1.csv',
        'PEEK500907_250C_1.csv',
        'PEEK500907_300C_1.csv',
        'PEEK500907_30C_after_1.csv',
        'HDPE_29C_1.csv',
        'HDPE_50C_1.csv',
        'HDPE_75C_1.csv',
        'HDPE_100C_1.csv',
        'HDPE_110C_1.csv',
        'HDPE_120C_1.csv',
        'HDPE_31C_after_1.csv'
    ]
    
    # Function to extract temperature from filename
    def extract_temperature_str(filename):
        match = re.search(r'(\d+)C', filename)
        if match:
            return str(match.group(1))
        return 0
    
    # Store results
    overview_df = pd.read_excel(excel_file_path, sheet_name='Overview')
    cryst_dict = dict(zip(overview_df['Filename'], overview_df['Crystallinity_percent']/100))   # fractional crystallinity
    
    # Separate PEEK and HDPE data
    peek_temps = []
    peek_crystallinity = []
    hdpe_temps = []
    hdpe_crystallinity = []
    
    for file in desired_order:
        if file in cryst_dict:
            temp = extract_temperature_str(file)
            if 'HDPE' in file:
                hdpe_temps.append(temp)
                hdpe_crystallinity.append(cryst_dict[file])
            else:
                peek_temps.append(temp)
                peek_crystallinity.append(cryst_dict[file])

    # Create side-by-side subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(width, height), constrained_layout=True)

    # HDPE plot
    # Create colors for HDPE bars - red for heating steps, blue for final cooling step
    hdpe_colors = [colours[1] if '31C_after' not in desired_order[i] else colours[0] 
                   for i, file in enumerate(desired_order) if 'HDPE' in file and file in cryst_dict]
    ax1.scatter(hdpe_temps, hdpe_crystallinity, color=hdpe_colors, marker=symbol, linestyle=linestyle, )
    # for temp, value in zip(hdpe_temps, hdpe_crystallinity):
    #     ax2.text(temp, value + 0.005, f'{value/100:.2f}', ha='center', va='bottom')
    
    ax1.set_ylim(bottom=0.0, top=1.0)  
    ax1.set_xlabel('Temperature / °C')
    ax1.set_ylabel(r'$X_{\mathrm{c}}$ / $\mathrm{g \, g^{-1}}$')
    ax1.set_title('(a) HDPE')
    
    # Remove tick marks but keep labels
    ax1.tick_params(axis='x', length=0)
    
    # Add custom legend
    legend_elements = [Patch(facecolor='C2', label='Heating'),
                       Patch(facecolor='C0', label='Cooling')]
    ax1.legend(handles=legend_elements, loc='upper left', ncols=2)
    
    # PEEK plot
    peek_colors = [colours[1] if '30C_after' not in desired_order[i] else colours[0]
                for i, file in enumerate(desired_order) if 'PEEK' in file and file in cryst_dict]
    ax2.scatter(peek_temps, peek_crystallinity, color=peek_colors, marker=symbol, linestyle=linestyle, )
    # for temp, value in zip(peek_temps, peek_crystallinity):
    #     ax2.text(temp, value + 0.005, f'{value/100:.2f}', ha='center', va='bottom')

    ax2.set_ylim(bottom=0.0, top=0.2)
    ax2.set_xlabel('Temperature / °C')
    # ax2.set_ylabel(r'$X_{\mathrm{c}}$ / $\mathrm{g \, g^{-1}}$')
    ax2.set_title('(b) PEEKa')
    
    # Remove tick marks but keep labels
    ax2.tick_params(axis='x', length=0)
    
    ax2.legend(handles=legend_elements, loc='upper left', ncols=2)
    
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_crystalliinity_XRD_heated.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()


# Using bars
# def plot_crystallinity_from_excel(
#     excel_file_path,
#     colours=['C0', 'C2'],
#     width=6, height=6,
#     display_fig=True, save_fig=True, 
#     folder_to_save='../figures', save_format='pdf', dpi=400    
#     ):
#     # Define the desired order
#     desired_order = [
#         'PEEK500907_26C_1.csv',
#         'PEEK500907_50C_1.csv',
#         'PEEK500907_100C_1.csv',
#         'PEEK500907_150C_1.csv',
#         'PEEK500907_200C_1.csv',
#         'PEEK500907_250C_1.csv',
#         'PEEK500907_300C_1.csv',
#         'PEEK500907_30C_after_1.csv',
#         'HDPE_29C_1.csv',
#         'HDPE_50C_1.csv',
#         'HDPE_75C_1.csv',
#         'HDPE_100C_1.csv',
#         'HDPE_110C_1.csv',
#         'HDPE_120C_1.csv',
#         'HDPE_31C_after_1.csv'
#     ]
    
#     # Function to extract temperature from filename
#     def extract_temperature_str(filename):
#         match = re.search(r'(\d+)C', filename)
#         if match:
#             return str(match.group(1))
#         return 0
    
#     # Store results
#     overview_df = pd.read_excel(excel_file_path, sheet_name='Overview')
#     cryst_dict = dict(zip(overview_df['Filename'], overview_df['Crystallinity_percent']/100))   # fractional crystallinity
    
#     # Separate PEEK and HDPE data
#     peek_temps = []
#     peek_crystallinity = []
#     hdpe_temps = []
#     hdpe_crystallinity = []
    
#     for file in desired_order:
#         if file in cryst_dict:
#             temp = extract_temperature_str(file)
#             if 'HDPE' in file:
#                 hdpe_temps.append(temp)
#                 hdpe_crystallinity.append(cryst_dict[file])
#             else:
#                 peek_temps.append(temp)
#                 peek_crystallinity.append(cryst_dict[file])

#     # Create side-by-side subplots
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(width, height), constrained_layout=True)

#     # HDPE plot
#     # Create colors for HDPE bars - red for heating steps, blue for final cooling step
#     hdpe_colors = [colours[1] if '31C_after' not in desired_order[i] else colours[0] 
#                    for i, file in enumerate(desired_order) if 'HDPE' in file and file in cryst_dict]
#     bars1 = ax1.bar(hdpe_temps, hdpe_crystallinity, color=hdpe_colors)
#     # for temp, value in zip(hdpe_temps, hdpe_crystallinity):
#     #     ax2.text(temp, value + 0.005, f'{value/100:.2f}', ha='center', va='bottom')
    
#     ax1.set_ylim(top=1.0)  
#     ax1.set_xlabel('Temperature / °C')
#     ax1.set_ylabel(r'$X_{\mathrm{c}}$ / $\mathrm{g \, g^{-1}}$')
#     ax1.set_title('(b) HDPE')
    
#     # Remove tick marks but keep labels
#     ax1.tick_params(axis='x', length=0)
    
#     # Add custom legend
#     legend_elements = [Patch(facecolor='C2', label='Heating'),
#                        Patch(facecolor='C0', label='Cooling')]
#     ax1.legend(handles=legend_elements, loc='upper left', ncols=2)
    
#     # PEEK plot
#     peek_colors = [colours[1] if '30C_after' not in desired_order[i] else colours[0]
#                 for i, file in enumerate(desired_order) if 'PEEK' in file and file in cryst_dict]
#     bars2 = ax2.bar(peek_temps, peek_crystallinity, color=peek_colors)
#     # for temp, value in zip(peek_temps, peek_crystallinity):
#     #     ax2.text(temp, value + 0.005, f'{value/100:.2f}', ha='center', va='bottom')
    
#     ax2.set_ylim(top=0.2)
#     ax2.set_xlabel('Temperature / °C')
#     # ax2.set_ylabel(r'$X_{\mathrm{c}}$ / $\mathrm{g \, g^{-1}}$')
#     ax2.set_title('(a) PEEKa')
    
#     # Remove tick marks but keep labels
#     ax2.tick_params(axis='x', length=0)
    
#     ax2.legend(handles=legend_elements, loc='upper left', ncols=2)
    
#     # Save figure
#     if save_fig:
#         # Create directory if it doesn't exist
#         os.makedirs(folder_to_save, exist_ok=True)
        
#         # Create filename
#         filename = f"fig_crystalliinity_XRD_heated.{save_format}"
#         filepath = os.path.join(folder_to_save, filename)
        
#         # Save figure
#         plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
#         print(f"Plot successfully exported to {filepath}")
    
#     # Display figure
#     if display_fig:
#         plt.show()
