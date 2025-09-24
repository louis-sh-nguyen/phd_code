import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import pandas as pd
import os

from utils import sample_ids

def plot_DSC_spectrum_roomTemp_1st_cycle(
    file_path, 
    width=6., height=6.,
    colours=['C0', 'C1', 'C2', 'C3'], symbol='None', linestyle='solid', linewidth=1,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    


    # Read the overview sheet to get spectrum descriptions
    overview = pd.read_excel(file_path, sheet_name='Overview')
    print("Overview data:")
    print(overview.head())

    # Get all sheet names to identify spectrum sheets
    xl_file = pd.ExcelFile(file_path)
    sheet_names = xl_file.sheet_names
    print(f"\nAvailable sheets: {sheet_names}")

    # Filter out the Overview sheet to get spectrum sheet names
    spectrum_sheets = [sheet for sheet in sheet_names if sheet != 'Overview']

    # Filter out the 1st cycle sheets
    spectrum_sheets_1st_cycle = [sheet for sheet in spectrum_sheets if '_cycle1' in sheet]

    # Group sheets by sample name (everything before the first underscore)
    sample_groups = defaultdict(list)
    for sheet in spectrum_sheets_1st_cycle:
        if '_' in sheet:
            sample_name = sheet.split('_')[0]
        else:
            sample_name = sheet
        sample_groups[sample_name].append(sheet)

    # Match sample groups to sample IDs
    sample_groups = {sample_id: sheets for sample_id, sheets in sample_groups.items() if sample_id in sample_ids}

    # Order sample_groups to start with HDPE
    if 'HDPE' in sample_groups:
        sample_groups = {'HDPE': sample_groups['HDPE'], **{k: v for k, v in sample_groups.items() if k != 'HDPE'}}

    print(f"Sample groups: {dict(sample_groups)}")

    # Create subplots - 2x2 grid for 4 samples
    fig, axes = plt.subplots(2, 2, figsize=(width, height), constrained_layout=True)
    axes = axes.flatten()  # Flatten to make indexing easier

    # Set titles for each subplot e.g. (a) HDPE, (b) PEEKa, etc.
    titles = [f'({letter}) {sample_ids[sample_group]}' for letter, sample_group in zip(['a', 'b', 'c', 'd'], sample_groups.keys())]

    # Plot each sample group in its own subplot
    for idx, (sample_name, sheets) in enumerate(sample_groups.items()):
        ax = axes[idx]    

        # Plot each spectrum
        for i, sheet_name in enumerate(sheets):
            try:
                # Read spectrum data
                spectrum_data = pd.read_excel(file_path, sheet_name=sheet_name)
                
                # Assuming the first column is 2-theta (angle) and second column is intensity
                x_data = spectrum_data['T / °C']
                y_data = spectrum_data['q / W g^-1']
                
                # Get description from overview if available
                # description = sheet_name
                ax.plot(x_data, y_data, label=f'Repetion {i+1}', color=colours[i], marker=symbol, linestyle=linestyle, linewidth=linewidth)
                    
            except Exception as e:
                print(f"Error reading sheet {sheet_name}: {e}")

        # Set up individual subplot
        # with plt.rc_context({'text.usetex': False}):
        if idx in [2,3 ]:
            ax.set_xlabel('Temperature / °C')
        if idx in [0, 2]:
            ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
        # Set xlimit for each polyme class
        if sample_name == 'HDPE':
            ax.set_xlim(0, 250)
        # else:
        #     ax.set_xlim(20, 300)
            
        # Add title        
        ax.set_title(titles[idx])
        
        if display_legend:
            ax.legend(loc='lower right')
            
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_specturm_1st_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()

def plot_DSC_spectrum_roomTemp_2nd_cycle(
    file_path, 
    width=6., height=6.,
    colours=['C0', 'C1', 'C2', 'C3'], symbol='None', linestyle='solid', linewidth=1,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    


    # Read the overview sheet to get spectrum descriptions
    overview = pd.read_excel(file_path, sheet_name='Overview')
    print("Overview data:")
    print(overview.head())

    # Get all sheet names to identify spectrum sheets
    xl_file = pd.ExcelFile(file_path)
    sheet_names = xl_file.sheet_names
    print(f"\nAvailable sheets: {sheet_names}")

    # Filter out the Overview sheet to get spectrum sheet names
    spectrum_sheets = [sheet for sheet in sheet_names if sheet != 'Overview']

    # Filter out the 2nd cycle sheets
    spectrum_sheets_2nd_cycle = [sheet for sheet in spectrum_sheets if '_cycle2' in sheet]

    # Group sheets by sample name (everything before the first underscore)
    sample_groups = defaultdict(list)
    for sheet in spectrum_sheets_2nd_cycle:
        if '_' in sheet:
            sample_name = sheet.split('_')[0]
        else:
            sample_name = sheet
        sample_groups[sample_name].append(sheet)

    # Match sample groups to sample IDs
    sample_groups = {sample_id: sheets for sample_id, sheets in sample_groups.items() if sample_id in sample_ids}

    # Order sample_groups to start with HDPE
    if 'HDPE' in sample_groups:
        sample_groups = {'HDPE': sample_groups['HDPE'], **{k: v for k, v in sample_groups.items() if k != 'HDPE'}}

    print(f"Sample groups: {dict(sample_groups)}")

    # Create subplots - 2x2 grid for 4 samples
    fig, axes = plt.subplots(2, 2, figsize=(width, height), constrained_layout=True)
    axes = axes.flatten()  # Flatten to make indexing easier

    # Set titles for each subplot e.g. (a) HDPE, (b) PEEKa, etc.
    titles = [f'({letter}) {sample_ids[sample_group]}' for letter, sample_group in zip(['a', 'b', 'c', 'd'], sample_groups.keys())]

    # Plot each sample group in its own subplot
    for idx, (sample_name, sheets) in enumerate(sample_groups.items()):
        ax = axes[idx]    

        # Plot each spectrum
        for i, sheet_name in enumerate(sheets):
            try:
                # Read spectrum data
                spectrum_data = pd.read_excel(file_path, sheet_name=sheet_name)
                
                # Assuming the first column is 2-theta (angle) and second column is intensity
                x_data = spectrum_data['T / °C']
                y_data = spectrum_data['q / W g^-1']
                
                # Get description from overview if available
                # description = sheet_name
                ax.plot(x_data, y_data, label=f'Repetion {i+1}', color=colours[i], marker=symbol, linestyle=linestyle, linewidth=linewidth)
                    
            except Exception as e:
                print(f"Error reading sheet {sheet_name}: {e}")

        # Set up individual subplot
        # with plt.rc_context({'text.usetex': False}):
        if idx in [2,3 ]:
            ax.set_xlabel('Temperature / °C')
        if idx in [0, 2]:
            ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
        # Set xlimit for each polyme class
        if sample_name == 'HDPE':
            ax.set_xlim(0, 250)
        # else:
        #     ax.set_xlim(20, 300)
            
        # Add title        
        ax.set_title(titles[idx])
        
        if display_legend:
            ax.legend(loc='lower right')
            
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_specturm_2nd_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()

def plot_DSC_spectrum_roomTemp_3rd_cycle(
    file_path, 
    width=6., height=6.,
    colours=['C0', 'C1', 'C2', 'C3'], symbol='None', linestyle='solid', linewidth=1,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    


    # Read the overview sheet to get spectrum descriptions
    overview = pd.read_excel(file_path, sheet_name='Overview')
    print("Overview data:")
    print(overview.head())

    # Get all sheet names to identify spectrum sheets
    xl_file = pd.ExcelFile(file_path)
    sheet_names = xl_file.sheet_names
    print(f"\nAvailable sheets: {sheet_names}")

    # Filter out the Overview sheet to get spectrum sheet names
    spectrum_sheets = [sheet for sheet in sheet_names if sheet != 'Overview']

    # Filter out the 3rd cycle sheets
    spectrum_sheets_3rd_cycle = [sheet for sheet in spectrum_sheets if '_cycle3' in sheet]

    # Group sheets by sample name (everything before the first underscore)
    sample_groups = defaultdict(list)
    for sheet in spectrum_sheets_3rd_cycle:
        if '_' in sheet:
            sample_name = sheet.split('_')[0]
        else:
            sample_name = sheet
        sample_groups[sample_name].append(sheet)

    # Match sample groups to sample IDs
    sample_groups = {sample_id: sheets for sample_id, sheets in sample_groups.items() if sample_id in sample_ids}

    # Order sample_groups to start with HDPE
    if 'HDPE' in sample_groups:
        sample_groups = {'HDPE': sample_groups['HDPE'], **{k: v for k, v in sample_groups.items() if k != 'HDPE'}}

    print(f"Sample groups: {dict(sample_groups)}")

    # Create subplots - 2x2 grid for 4 samples
    fig, axes = plt.subplots(2, 2, figsize=(width, height), constrained_layout=True)
    axes = axes.flatten()  # Flatten to make indexing easier

    # Set titles for each subplot e.g. (a) HDPE, (b) PEEKa, etc.
    titles = [f'({letter}) {sample_ids[sample_group]}' for letter, sample_group in zip(['a', 'b', 'c', 'd'], sample_groups.keys())]

    # Plot each sample group in its own subplot
    for idx, (sample_name, sheets) in enumerate(sample_groups.items()):
        ax = axes[idx]    

        # Plot each spectrum
        for i, sheet_name in enumerate(sheets):
            try:
                # Read spectrum data
                spectrum_data = pd.read_excel(file_path, sheet_name=sheet_name)
                
                # Assuming the first column is 2-theta (angle) and second column is intensity
                x_data = spectrum_data['T / °C']
                y_data = spectrum_data['q / W g^-1']
                
                # Get description from overview if available
                # description = sheet_name
                ax.plot(x_data, y_data, label=f'Repetion {i+1}', color=colours[i], marker=symbol, linestyle=linestyle, linewidth=linewidth)
                    
            except Exception as e:
                print(f"Error reading sheet {sheet_name}: {e}")

        # Set up individual subplot
        # with plt.rc_context({'text.usetex': False}):
        if idx in [2,3 ]:
            ax.set_xlabel('Temperature / °C')
        if idx in [0, 2]:
            ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
        # Set xlimit for each polyme class
        if sample_name == 'HDPE':
            ax.set_xlim(0, 250)
        # else:
        #     ax.set_xlim(20, 300)
            
        # Add title        
        ax.set_title(titles[idx])
        
        if display_legend:
            ax.legend(loc='lower right')
            
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_specturm_3rd_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()
