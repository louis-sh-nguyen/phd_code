import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def plot_polymer_compressibility_vertical(
        data_path,
        width=6.5, height=8.,
        colour='black',
        linestyle_saft='-', linestyle_tait='--',
        display_fig=True, save_fig=False, folder_to_save='../figures', save_format='pdf', dpi=400):
    """
    Plot polymer compressibility data from Excel file in a vertical layout for different temperatures.
    
    Parameters:
    -----------
    data_path : str
        Path to the Excel file containing polymer compressibility data
    width, height : float
        Figure dimensions in inches
    linecolour_saft, linecolour_tait : str
        Colors for SAFT and Tait equation lines
    linestyle_saft, linestyle_tait : str
        Line styles for SAFT and Tait equation lines
    display_fig : bool
        Whether to display the figure
    save_fig : bool
        Whether to save the figure
    folder_to_save : str
        Directory to save the figure
    save_format : str
        Format for saved figure ('pdf', 'png', etc.)
    dpi : int
        Resolution for saved figure
        
    Returns:
    --------
    fig : matplotlib figure
        Figure containing the compressibility plots
    """
    T_celsius_values = [25, 35, 50]
    barToMPa = 1e-1  # Conversion from bar to MPa
    
    # Read data from Excel sheets
    data_sheets = {}
    metadata_sheets = {}
    
    for T in T_celsius_values:
        sheet_name = f"{T}C_Compressibility Data"
        meta_sheet_name = f"{T}C_Metadata"
        
        try:
            data_sheets[T] = pd.read_excel(data_path, sheet_name=sheet_name)
            metadata_sheets[T] = pd.read_excel(data_path, sheet_name=meta_sheet_name)
        except Exception as e:
            print(f"Error reading sheet for {T}°C: {e}")
            # Create empty dataframe if sheet doesn't exist
            data_sheets[T] = pd.DataFrame({
                'Pressure (bar)': [],
                'V_p SAFT (cm³/g)': [],
                'V_p Tait (cm³/g)': []
            })
            metadata_sheets[T] = pd.DataFrame({
                'Parameter': [], 'Value': []
            })
      # Plotting
    fig = plt.figure(figsize=(width, height), constrained_layout=True)    
    n_row = 3
    n_col = 1
    ax1 = fig.add_subplot(n_row, n_col, 1)
    ax2 = fig.add_subplot(n_row, n_col, 2)
    ax3 = fig.add_subplot(n_row, n_col, 3)
    
    axs = [ax1, ax2, ax3]
    titles = ['(a)', '(b)', '(c)']
    
    for i, (T, ax, title) in enumerate(zip(T_celsius_values, axs, titles)):
        df = data_sheets[T]
        meta_df = metadata_sheets[T]
        if not df.empty:
            # Plot SAFT data
            ax.plot(df['Pressure (bar)']*barToMPa, df['V_p SAFT (cm³/g)'], 
                   color=colour, linestyle=linestyle_saft, label='SAFT')
            
            # Plot Tait equation data
            ax.plot(df['Pressure (bar)']*barToMPa, df['V_p Tait (cm³/g)'], 
                   color=colour, linestyle=linestyle_tait, label='Tait')
            
            # Add Widom line if available
            widom_param = meta_df[meta_df['Parameter'] == 'Widom Line Pressure (bar)']
            if not widom_param.empty:
                widom_p = float(widom_param['Value'].values[0])
                ax.axvline(x=widom_p*barToMPa, color='gray', linestyle=':', label='Widom Line')
        
        # Configuring the plots
        ax.set_xlim(left=0)
        ax.legend()
        ax.set_title(title + f' {T:.0f} °C')
    
    # Configuring the plots
    # Labels
    ax1.set_ylabel(r'$\hat{V}_{\mathrm{p,am}}$ / $\mathrm{cm^3 \, g^{-1}}$')
    ax2.set_ylabel(r'$\hat{V}_{\mathrm{p,am}}$ / $\mathrm{cm^3 \, g^{-1}}$')
    ax3.set_ylabel(r'$\hat{V}_{\mathrm{p,am}}$ / $\mathrm{cm^3 \, g^{-1}}$')
    ax3.set_xlabel(r'$p$ / MPa')
    
    # Get polymer type from metadata if available
    polymer_type = "HDPE"  # Default
    if metadata_sheets[T_celsius_values[0]].shape[0] > 0:
        polymer_param = metadata_sheets[T_celsius_values[0]][
            metadata_sheets[T_celsius_values[0]]['Parameter'] == 'Polymer']
        if not polymer_param.empty:
            polymer_type = polymer_param['Value'].values[0]
    
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        save_fig_path = os.path.join(folder_to_save, f"fig_polymer_compressibility_comparison.{save_format}")
        plt.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {save_fig_path}.")
    
    # Display figure
    if display_fig:
        plt.show()
        
if __name__ == "__main__":
    # Example usage
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # figure style
    plt.style.use('seaborn-v0_8-colorblind')
    plt.style.use('../../../../thesis.mplstyle')
    
    # Example usage
    data_path = "../data/polymer_compressibility.xlsx"  # Path to the Excel file
    
    # Figure sizes (based on journal requirements)
    cmToInch = 1/2.54
    text_width = 14.2  # cm
    height = 18.0  # cm
    
    width = text_width * cmToInch
    height = height * cmToInch
    
    plot_polymer_compressibility_vertical(
        data_path=data_path,
        width=width, 
        height=height,
        # linestyle_saft='-',  # Solid line for SAFT
        # linestyle_tait='--', # Dashed line for Tait
        save_fig=False, 
    )