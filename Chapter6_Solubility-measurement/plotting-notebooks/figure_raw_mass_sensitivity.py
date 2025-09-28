from matplotlib import pyplot as plt
import pandas as pd
import os

def plot_raw_mass_sensitivity(
    file_path, 
    width=6., height=6.,
    x_lo=None, 
    colour='black', symbol='o', linestyle='None', markerfacecolor='None',
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400):
    """
    Plot sensitivity analysis data from an Excel file with multiple tabs for different conditions.
    
    Parameters:
    -----------
    file_path : str
        Path to the Excel file containing sensitivity data in multiple tabs
    width, height : float
        Figure dimensions in inches
    x_lo, y_lo : float or None
        Lower limits for x and y axes
    colour, symbol, linestyle, markerfacecolor : str
        Style specifications for plot
    display_legend : bool
        Whether to show legends
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
        Figure containing the sensitivity plots
    """
    import os
    
    # Expected sheet names for different conditions
    sheet_names = ['35C_10MPa', '35C_20MPa', '50C_10MPa', '50C_20MPa']

    # Load data from Excel tabs
    data = {}
    for sheet_name in sheet_names:
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            data[sheet_name] = df
        except Exception as e:
            print(f"Error reading sheet {sheet_name}: {e}")
            data[sheet_name] = None
    
    # Create figure with 2x2 grid
    fig, axs = plt.subplots(2, 2, figsize=(width, height), constrained_layout=True)
    axs = axs.flatten()  # Flatten for easier indexing

    title_letters = ['(a)', '(b)', '(c)', '(d)']  # Subplot labels for titles
    # Prepare subplot titles and map to proper position
    titles = []
    for i, sheet_name in enumerate(sheet_names):
        # Extract temperature and pressure from sheet name
        # Example: "35C_100bar"
        parts = sheet_name.split('_')
        temp = parts[0].replace('C', ' °C')  # Format as "35 °C"
        pressure = parts[1].replace('MPa', ' MPa')  # Format as "10.0 MPa"

        subplot_letter = title_letters[i]  # Get subplot letter
        titles.append(f'{subplot_letter} {temp}, {pressure}')    # Plot each dataset in its respective subplot
    for i, (sheet_name, title) in enumerate(zip(sheet_names, titles)):
        df = data[sheet_name]
        if df is not None and not df.empty:
            # Get all raw mass values
            m_raw_values = df['m_raw (g)']
            solubility_values = df['Solubility (g/g)']
            
            # Separate data points into those with and without solutions
            valid_mask = solubility_values.notnull()
            valid_m_raw = m_raw_values[valid_mask]
            valid_solubility = solubility_values[valid_mask]
            
            # Mark points with no solution found
            if not valid_mask.all():
                no_solution_m_raw = m_raw_values[~valid_mask]
                
                # Add vertical dashed lines for points without solutions
                has_marked_nosolution = False
                for m_raw_no_sol in no_solution_m_raw:
                    if not has_marked_nosolution:
                        # First line gets a label for the legend
                        axs[i].axvline(x=m_raw_no_sol, color='C2', linestyle=':', 
                                     alpha=0.7, linewidth=1.0, label='No solution')
                        has_marked_nosolution = True
                    else:
                        # Subsequent lines don't need labels
                        axs[i].axvline(x=m_raw_no_sol, color='C2', linestyle=':', 
                                     alpha=0.7, linewidth=1.0)
                
            # Find baseline (closest to zero percent change)
            if 'm_raw change (%)' in df.columns:
                baseline_idx = (df['m_raw change (%)'].abs()).idxmin()
                baseline_m_raw = df.loc[baseline_idx, 'm_raw (g)']
                
                # Add vertical line at baseline
                axs[i].axvline(x=baseline_m_raw, color='grey', linestyle='--', 
                              label='Baseline')
            
            # Plot points with valid solutions
            axs[i].plot(valid_m_raw, valid_solubility,
                      color=colour, marker=symbol, linestyle=linestyle, 
                      markerfacecolor=markerfacecolor, label='Solution')
            
            # Ensure the entire range of m_raw is shown
            axs[i].set_xlim(m_raw_values.min() * 0.99, m_raw_values.max() * 1.01)
      # Configure all subplots
    for i, ax in enumerate(axs):
        # Add title
        ax.set_title(titles[i])
        
        # Set axis limits if provided
        if x_lo is not None:
            ax.set_xlim(left=x_lo)
        
        # Add twin x-axis for percent change if baseline was found
        # if data[sheet_names[i]] is not None and 'm_raw change (%)' in data[sheet_names[i]].columns:
        #     ax2 = ax.twiny()
            
        #     # Find baseline m_raw
        #     baseline_idx = (data[sheet_names[i]]['m_raw change (%)'].abs()).idxmin()
        #     baseline_m_raw = data[sheet_names[i]].loc[baseline_idx, 'm_raw (g)']
            
        #     # Get current x limits (which should cover all m_raw values)
        #     x_limits = ax.get_xlim()
            
        #     # Calculate percentage changes relative to baseline
        #     percent_min = 100 * (x_limits[0] - baseline_m_raw) / baseline_m_raw
        #     percent_max = 100 * (x_limits[1] - baseline_m_raw) / baseline_m_raw
            
        #     # Set the twin axis limits to show percentage change
        #     ax2.set_xlim([percent_min, percent_max])
            
        #     # Only add label to top row
        #     if i < 2:
        #         ax2.set_xlabel('Change in raw mass (%)')
        
    # Set labels
    for i in [0, 2]:
        axs[i].set_ylabel(r'$q_{\mathrm{sc}}$ / $\mathrm{g \, g^{-1}}$')
    
    for i in [2, 3]:
        axs[i].set_xlabel(r'$m_\mathrm{raw}$ / g')
    
    # Add manual x-limits for each subplot
    xlimits_dict = {
        '35C_10MPa': (-1.12, -1.06),
        '35C_20MPa': (-1.38, -1.30),
        '50C_10MPa': ( -0.60, -0.560),
        '50C_20MPa': (-1.24, -1.18)
    }
    for i, ax in enumerate(axs):
        limits = xlimits_dict.get(sheet_names[i], (-1.5, 0.5))
        # Set x-limits based on the dictionary
        ax.set_xlim(limits[0], limits[1])

    # Add legend if required
    legend_loc_dict = {
        '35C_10MPa': 'upper left',
        '35C_20MPa': 'upper left',
        '50C_10MPa': 'upper left',
        '50C_20MPa': 'upper left'
    }    
    for i, ax in enumerate(axs):
        if display_legend:
            legend_loc = legend_loc_dict.get(sheet_names[i], 'upper right')
            ax.legend(loc=legend_loc)
    
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_raw_mass_sensitivity.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()
    
if __name__ == "__main__":
    # Example usage    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Set matplotlib style (optional)
    plt.style.use('seaborn-v0_8-colorblind')
    plt.style.use('../../../../thesis.mplstyle')
    
    # Figure sizes
    cmToInch = 1/2.54
    text_width = 14.2  # cm
    base_height = 5.  # cm
    dpi = 400
    format = 'pdf'
    
    width = text_width * cmToInch
    height = 2.3* base_height * cmToInch
    
    # Path to sensitivity data Excel file with multiple tabs
    file_path = '../data/raw_mass_sensitivity.xlsx'
    
    # Plot the sensitivity comparison
    plot_raw_mass_sensitivity(
        file_path=file_path,
        width=width, 
        height=height,
        # colour='black',
        # symbol='o',
        # linestyle='-',
        markerfacecolor='None',
        display_legend=True, 
        display_fig=True, 
        save_fig=False,
        # save_format=format,
        # dpi=dpi
    )