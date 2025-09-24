import pandas as pd
import matplotlib.pyplot as plt
import os
from utils import sample_ids

def plot_comparison_xrd_dsc_1st_cycle_roomTemp(
    dsc_file_path,
    xrd_file_path,
    y_lo=0, y_up=None,
    symbols=['o', 's'], colour='black', linestyle='None', markerfacecolor='None',
    width=6, height=6,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
):

    # Sample ID refrence
    sample_ids = {
        '500907': 'PEEKa',
        '501023': 'PEEKb',
        '501024': 'PEEKc',
        'HDPE': 'HDPE',
    }


    dsc_overview = pd.read_excel(dsc_file_path, sheet_name='Overview')
    xrd_overview = pd.read_excel(xrd_file_path, sheet_name='Overview')

    # dsc processing
    dsc_overview['polymer type'] = dsc_overview['sample'].str.split('_').str[0]
    mask = dsc_overview['cycle'].astype(str) == '1'
    dsc_1st_cycle = dsc_overview.loc[mask, :]
    # Caclulate average crystallinity
    dsc_gb = dsc_1st_cycle.groupby('polymer type')['CF / g g^-1'].mean().reset_index()
    dsc_gb['crystallinity'] = dsc_gb['CF / g g^-1']
    dsc_gb['polymer type'] = dsc_gb['polymer type'].map(sample_ids)
    dsc_gb.sort_values('polymer type', inplace=True)

    # XRD processing
    xrd_overview['polymer type'] = xrd_overview['Filename'].str.split('.csv').str[0]
    xrd_overview['polymer type'] = xrd_overview['polymer type'].str.split('_').str[0]
    # Caculate average for each polymer type
    xrd_gb = xrd_overview.groupby('polymer type')['Crystallinity_percent'].mean().reset_index()
    xrd_gb['crystallinity'] = xrd_gb['Crystallinity_percent'] / 100
    xrd_gb['polymer type'] = xrd_gb['polymer type'].map(sample_ids)
    xrd_gb.sort_values('polymer type', inplace=True)

    # Create a figure with two subplots side by side
    fig, ax1 = plt.subplots(1, 1, figsize=(width, height), constrained_layout=True)

    # Plot DSC crystallinity vs polymer type
    ax1.plot(dsc_gb['polymer type'], dsc_gb['crystallinity'], label='DSC', 
                marker=symbols[0], color=colour, linestyle=linestyle, markerfacecolor=markerfacecolor)
    ax1.plot(xrd_gb['polymer type'], xrd_gb['crystallinity'], label='XRD', 
                marker=symbols[1], color=colour, linestyle=linestyle, markerfacecolor=markerfacecolor)
    ax1.set_xlabel('Polymer')
    ax1.set_ylabel(r'$X_{\mathrm{c}}$ / $\mathrm{g \, g^{-1}}$')
    
    if y_lo is not None:
        ax1.set_ylim(bottom=y_lo)
    if y_up is not None:
        ax1.set_ylim(top=y_up)
    
    if display_legend:
        ax1.legend()

    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_crystallinity_comparison_XRD_DSC_RT.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()

def plot_comparison_xrd_dsc_2nd_cycle_roomTemp(
    dsc_file_path,
    xrd_file_path,
    y_lo=0, y_up=None,
    symbols=['o', 's'], colour='black', linestyle='None', markerfacecolor='None',
    width=6, height=6,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
):

    # Sample ID refrence
    sample_ids = {
        '500907': 'PEEKa',
        '501023': 'PEEKb',
        '501024': 'PEEKc',
        'HDPE': 'HDPE',
    }


    dsc_overview = pd.read_excel(dsc_file_path, sheet_name='Overview')
    xrd_overview = pd.read_excel(xrd_file_path, sheet_name='Overview')

    # dsc processing
    dsc_overview['polymer type'] = dsc_overview['sample'].str.split('_').str[0]
    mask = dsc_overview['cycle'].astype(str) == '2'
    dsc_2nd_cycle = dsc_overview.loc[mask, :]
    # Caclulate average crystallinity
    dsc_gb = dsc_2nd_cycle.groupby('polymer type')['CF / g g^-1'].mean().reset_index()
    dsc_gb['crystallinity'] = dsc_gb['CF / g g^-1']
    dsc_gb['polymer type'] = dsc_gb['polymer type'].map(sample_ids)
    dsc_gb.sort_values('polymer type', inplace=True)

    # XRD processing
    xrd_overview['polymer type'] = xrd_overview['Filename'].str.split('.csv').str[0]
    xrd_overview['polymer type'] = xrd_overview['polymer type'].str.split('_').str[0]
    # Caculate average for each polymer type
    xrd_gb = xrd_overview.groupby('polymer type')['Crystallinity_percent'].mean().reset_index()
    xrd_gb['crystallinity'] = xrd_gb['Crystallinity_percent'] / 100
    xrd_gb['polymer type'] = xrd_gb['polymer type'].map(sample_ids)
    xrd_gb.sort_values('polymer type', inplace=True)

    # Create a figure with two subplots side by side
    fig, ax1 = plt.subplots(1, 1, figsize=(width, height), constrained_layout=True)

    # Plot DSC crystallinity vs polymer type
    ax1.plot(dsc_gb['polymer type'], dsc_gb['crystallinity'], label='DSC', 
                marker=symbols[0], color=colour, linestyle=linestyle, markerfacecolor=markerfacecolor)
    ax1.plot(xrd_gb['polymer type'], xrd_gb['crystallinity'], label='XRD', 
                marker=symbols[1], color=colour, linestyle=linestyle, markerfacecolor=markerfacecolor)
    ax1.set_xlabel('Polymer')
    ax1.set_ylabel(r'$X_{\mathrm{c}}$ / $\mathrm{g \, g^{-1}}$')
    
    if y_lo is not None:
        ax1.set_ylim(bottom=y_lo)
    if y_up is not None:
        ax1.set_ylim(top=y_up)
    
    if display_legend:
        ax1.legend()

    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_crystallinity_comparison_XRD_DSC_RT.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()
