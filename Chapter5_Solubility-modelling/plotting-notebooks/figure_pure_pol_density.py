import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from colour import Color
from pathlib import Path
import os

def plot_pure_pol_density_default_params(
    data_folder_path,
    width=6., height=4.1, 
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):

    def process_data(df):
        df = df.copy()
        df.columns = df.columns.str.strip()  # Remove leading/trailing whitespace from column names
        
        # Convert columns to numeric and handle errors
        df['Pressure (Pa)'] = pd.to_numeric(df['Pressure (Pa)'], errors='coerce')
        df['Temperature (K)'] = pd.to_numeric(df['Temperature (K)'], errors='coerce')
        df['Density EQ (g/cm^3)'] = pd.to_numeric(df['Density EQ (g/cm^3)'], errors='coerce')
        df['Density Exp (g/cm^3)'] = pd.to_numeric(df['Density Exp (g/cm^3)'], errors='coerce')
        
        # Add convenience columns
        df['Temperature (°C)'] = df['Temperature (K)'] - 273.15
        df['Pressure (MPa)'] = df['Pressure (Pa)'] * 1e-6
        return df
    
    # Read the CSV file
    df_PS = pd.read_csv(f'{data_folder_path}/PS_rubbery_PVT_data_default_params.csv')
    df_PMMA = pd.read_csv(f'{data_folder_path}/PMMA_rubbery_PVT_data_default_params.csv')
    
    # Process the data
    df_PS = process_data(df_PS)
    df_PMMA = process_data(df_PMMA)
    
    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(width, height), constrained_layout=True)
    ax1, ax2 = axes.flatten()  # Flatten for easy iteration
    
    # Plot (a) PS
    # Get unique pressure levels and organize data
    p_unq_list = sorted(df_PS['Pressure (Pa)'].unique())
    # Create color gradient
    colours = list(Color("silver").range_to(Color("maroon"), len(p_unq_list)))
    
    # Plot data for each pressure level
    for i, p in enumerate(p_unq_list):
        # Filter data for this pressure
        pressure_data = df_PS[df_PS['Pressure (Pa)'] == p]        
        # Sort by temperature for proper line plotting
        pressure_data = pressure_data.sort_values('Temperature (°C)')        
        # Plot EQ model data (lines)
        ax1.plot(
            pressure_data['Temperature (°C)'],
            pressure_data['Density EQ (g/cm^3)'],
            color=str(colours[i]),
            marker='None',
            linestyle='dashdot',
            label=f'{p * 1e-6:.0f} MPa' if i == 0 else ""  # Only label first line for legend
        )    
        # Plot experimental data (markers)
        ax1.plot(
            pressure_data['Temperature (°C)'],
            pressure_data['Density Exp (g/cm^3)'],
            color=str(colours[i]),
            marker='x',
            markersize=5,
            linestyle='None'
        )        
        # Set limits and ticks
        ax1.set_xlim(100, 275)
        ax1.set_xticks(np.linspace(100, 275, 8))
        ax1.set_ylim(0.9, 1.15)
        ax1.set_yticks(np.linspace(0.9, 1.15, 6))
        # Set labels
        ax1.set_xlabel('Temperature / °C')
        ax1.set_ylabel(r'$\rho_\mathrm{pol}^{0}$ / $\mathrm{g \, cm^{-3}}$')
        # Set title
        ax1.set_title('(a) PS')
    
    # Plot (b) PMMA data
    # Get unique pressure levels and organize data
    p_unq_list = sorted(df_PMMA['Pressure (Pa)'].unique())
    # Create color gradient
    colours = list(Color("silver").range_to(Color("maroon"), len(p_unq_list)))    
    # Plot data for each pressure level
    for i, p in enumerate(p_unq_list):
        # Filter data for this pressure
        pressure_data = df_PMMA[df_PMMA['Pressure (Pa)'] == p]        
        # Sort by temperature for proper line plotting
        pressure_data = pressure_data.sort_values('Temperature (°C)')        
        # Plot EQ model data (lines)
        ax2.plot(
            pressure_data['Temperature (°C)'],
            pressure_data['Density EQ (g/cm^3)'],
            color=str(colours[i]),
            marker='None',
            linestyle='dashdot',
            label=f'{p * 1e-6:.0f} MPa' if i == 0 else ""  # Only label first line for legend
        )    
        # Plot experimental data (markers)
        ax2.plot(
            pressure_data['Temperature (°C)'],
            pressure_data['Density Exp (g/cm^3)'],
            color=str(colours[i]),
            marker='x',
            markersize=5,
            linestyle='None'
        )
        # Set limits and ticks
        ax2.set_xlim(100, 250)
        ax2.set_xticks(np.linspace(100, 250, 7))
        ax2.set_ylim(0.8, 1.3)
        ax2.set_yticks(np.linspace(0.8, 1.3, 6))
        # Set labels
        ax2.set_xlabel('Temperature / °C')
        # ax2.set_ylabel(r'$\rho_\mathrm{pol}^{0}$ / $g \, cm^{-3}$')
        # Set title
        ax2.set_title('(b) PMMA')
    
    # Save plot
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)                
        filename = f"fig_pure_pol_density_default_params.{save_format}"
        save_plot_path = Path(folder_to_save) / filename                
        plt.savefig(save_plot_path, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot saved: {save_plot_path}")
    
    # Display plot
    if display_fig:
        plt.show()

def plot_pure_pol_density_fitted_params(
    data_folder_path,
    width=6., height=4.1, 
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):

    def process_data(df):
        df = df.copy()
        df.columns = df.columns.str.strip()  # Remove leading/trailing whitespace from column names
        
        # Convert columns to numeric and handle errors
        df['Pressure (Pa)'] = pd.to_numeric(df['Pressure (Pa)'], errors='coerce')
        df['Temperature (K)'] = pd.to_numeric(df['Temperature (K)'], errors='coerce')
        df['Density EQ (g/cm^3)'] = pd.to_numeric(df['Density EQ (g/cm^3)'], errors='coerce')
        df['Density Exp (g/cm^3)'] = pd.to_numeric(df['Density Exp (g/cm^3)'], errors='coerce')
        
        # Add convenience columns
        df['Temperature (°C)'] = df['Temperature (K)'] - 273.15
        df['Pressure (MPa)'] = df['Pressure (Pa)'] * 1e-6
        return df
    
    # Read the CSV file
    df_PS = pd.read_csv(f'{data_folder_path}/PS_rubbery_PVT_data_fitted_params.csv')
    df_PMMA = pd.read_csv(f'{data_folder_path}/PMMA_rubbery_PVT_data_fitted_params.csv')
    
    # Process the data
    df_PS = process_data(df_PS)
    df_PMMA = process_data(df_PMMA)
    
    # Plotting
    fig, axes = plt.subplots(1, 2, figsize=(width, height), constrained_layout=True)
    ax1, ax2 = axes.flatten()  # Flatten for easy iteration
    
    # Plot (a) PS
    # Get unique pressure levels and organize data
    p_unq_list = sorted(df_PS['Pressure (Pa)'].unique())
    # Create color gradient
    colours = list(Color("silver").range_to(Color("maroon"), len(p_unq_list)))
    
    # Plot data for each pressure level
    for i, p in enumerate(p_unq_list):
        # Filter data for this pressure
        pressure_data = df_PS[df_PS['Pressure (Pa)'] == p]        
        # Sort by temperature for proper line plotting
        pressure_data = pressure_data.sort_values('Temperature (°C)')        
        # Plot EQ model data (lines)
        ax1.plot(
            pressure_data['Temperature (°C)'],
            pressure_data['Density EQ (g/cm^3)'],
            color=str(colours[i]),
            marker='None',
            linestyle='solid',
            label=f'{p * 1e-6:.0f} MPa' if i == 0 else ""  # Only label first line for legend
        )    
        # Plot experimental data (markers)
        ax1.plot(
            pressure_data['Temperature (°C)'],
            pressure_data['Density Exp (g/cm^3)'],
            color=str(colours[i]),
            marker='x',
            markersize=5,
            linestyle='None'
        )        
        # Set limits and ticks
        ax1.set_xlim(100, 275)
        ax1.set_xticks(np.linspace(100, 275, 8))
        ax1.set_ylim(0.9, 1.10)
        ax1.set_yticks(np.linspace(0.9, 1.10, 5))
        # Set labels
        ax1.set_xlabel('Temperature / °C')
        ax1.set_ylabel(r'$\rho_\mathrm{pol}^{0}$ / $\mathrm{g \, cm^{-3}}$')
        # Set title
        ax1.set_title('(a) PS')
    
    # Plot (b) PMMA data
    # Get unique pressure levels and organize data
    p_unq_list = sorted(df_PMMA['Pressure (Pa)'].unique())
    # Create color gradient
    colours = list(Color("silver").range_to(Color("maroon"), len(p_unq_list)))    
    # Plot data for each pressure level
    for i, p in enumerate(p_unq_list):
        # Filter data for this pressure
        pressure_data = df_PMMA[df_PMMA['Pressure (Pa)'] == p]        
        # Sort by temperature for proper line plotting
        pressure_data = pressure_data.sort_values('Temperature (°C)')        
        # Plot EQ model data (lines)
        ax2.plot(
            pressure_data['Temperature (°C)'],
            pressure_data['Density EQ (g/cm^3)'],
            color=str(colours[i]),
            marker='None',
            linestyle='solid',
            label=f'{p * 1e-6:.0f} MPa' if i == 0 else ""  # Only label first line for legend
        )    
        # Plot experimental data (markers)
        ax2.plot(
            pressure_data['Temperature (°C)'],
            pressure_data['Density Exp (g/cm^3)'],
            color=str(colours[i]),
            marker='x',
            markersize=5,
            linestyle='None'
        )
        # Set limits and ticks
        ax2.set_xlim(100, 250)
        ax2.set_xticks(np.linspace(100, 250, 7))
        ax2.set_ylim(1.05, 1.25)
        ax2.set_yticks(np.linspace(1.05, 1.25, 5))
        # Set labels
        ax2.set_xlabel('Temperature / °C')
        # ax2.set_ylabel(r'$\rho_\mathrm{pol}^{0}$ / $g \, cm^{-3}$')
        # Set title
        ax2.set_title('(b) PMMA')
    
    # Save plot
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)                
        filename = f"fig_pure_pol_density_fitted_params.{save_format}"
        save_plot_path = Path(folder_to_save) / filename                
        plt.savefig(save_plot_path, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot saved: {save_plot_path}")
    
    # Display plot
    if display_fig:
        plt.show()
