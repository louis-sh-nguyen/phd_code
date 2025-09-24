import matplotlib.pyplot as plt
import pandas as pd
import os

from utils import sample_ids
def plot_XRD_fitted_spectrum_sample(
    file_path, 
    width=6., height=6.,
    x_lo=10, x_up=40, y_lo=0, y_up=None,
    colours=['black', 'C2', 'C0', 'C1'], symbol='None', raw_linestyle='solid', fit_linestyle='dashed', linewidth=1,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    
    
    ordered_sheets = [
        'HDPE', '500907', '501023', '501024',
    ]
    
    all_data = {}
    for sheet in ordered_sheets:
        data = pd.read_excel(file_path, sheet_name=sheet)
        all_data[sheet] = data
    
    # Calculate subplot grid dimensions
    n_plots = len(all_data)
    n_cols = 2  # Adjust this
    n_rows = (n_plots // n_cols) if (n_plots % n_cols == 0) else (n_plots // n_cols) + 1
    
    # Create subplots - one for each temperature
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(width, height), constrained_layout=True)
    
    # Flatten axes array for easy indexing
    if n_plots == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = axes
    else:
        axes = axes.flatten()
    
    title_letters = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)']
    
    # Plot each temperature on separate subplot
    for i, (sheet, spectrum_data) in enumerate(all_data.items()):
        x_data = spectrum_data['2Theta_deg']
        y_data_raw = spectrum_data['Original_Intensity_normalized']
        y_data_fit_total = spectrum_data['Total_Fit']
        y_data_fit_crys = spectrum_data['Crystalline_Fit']
        y_data_fit_amor = spectrum_data['Amorphous_Fit']
        
        # Plot raw spectrum
        axes[i].plot(x_data, y_data_raw, color=colours[0], 
                    marker=symbol, linestyle=raw_linestyle, linewidth=linewidth, label='Raw')
        
        # Plot amorphous fit
        axes[i].plot(x_data, y_data_fit_amor, color=colours[3], 
                    marker=symbol, linestyle=fit_linestyle, linewidth=linewidth, label='Amorphous Fit')
        
        # Plot crystalline fit
        axes[i].plot(x_data, y_data_fit_crys, color=colours[2], 
                    marker=symbol, linestyle=fit_linestyle, linewidth=linewidth, label='Crystalline Fit')
        
        # Plot total fit
        axes[i].plot(x_data, y_data_fit_total, color=colours[1], 
                    marker=symbol, linestyle=fit_linestyle, linewidth=linewidth, label='Total Fit')            

        # Set title for each subplot
        axes[i].set_title(f'{title_letters[i]} {sample_ids.get(sheet, sheet)}')
        
        # Set axis limits
        if x_lo is not None:
            axes[i].set_xlim(left=x_lo)
        if x_up is not None:
            axes[i].set_xlim(right=x_up)
        if y_lo is not None:
            axes[i].set_ylim(bottom=y_lo)
        if y_up is not None:
            axes[i].set_ylim(top=y_up)
                
        # Display legend
        if display_legend:
            axes[i].legend(loc='best')
    
    # Label x axis
    for i in [2, 3]:
        with plt.rc_context({'text.usetex': False}):
            axes[i].set_xlabel(r'$2\theta$ / °')            
    
    # Label y axis
    for i in [0, 2]:
        with plt.rc_context({'text.usetex': False}):            
            axes[i].set_ylabel('Norm. Intensity / A. U.')
    
    # Hide unused subplots
    for j in range(n_plots, len(axes)):
        axes[j].set_visible(False)
    
        
    # Save and display (your existing code)
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_XRD_RT_fit_samples.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    if display_fig:
        plt.show()

def plot_DSC_spectrum_fit_roomTemp_1st_cycle_sample(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        'HDPE_1_cycle1', '500907_1_cycle1', '501023_1_cycle1', '501024_1_cycle1'
    ]
    
    polymer_names = {
        'HDPE_1_cycle1': 'HDPE',
        '500907_1_cycle1': 'PEEKa',
        '501023_1_cycle1': 'PEEKb',
        '501024_1_cycle1': 'PEEKc',
    }
    
    all_data = {}
    for sheet in ordered_sheets:
        data = pd.read_excel(file_path, sheet_name=sheet)
        all_data[sheet] = data
    
    # Calculate subplot grid dimensions
    n_plots = len(all_data)
    n_cols = 2  # Adjust this
    n_rows = (n_plots // n_cols) if (n_plots % n_cols == 0) else (n_plots // n_cols) + 1
    
    # Create subplots - one for each temperature
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(width, height), constrained_layout=True)
    
    # Flatten axes array for easy indexing
    if n_plots == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = axes
    else:
        axes = axes.flatten()
    
    title_letters = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)']
    
    # Plot each sample group in its own subplot
    for i, (sheet, spectrum_data) in enumerate(all_data.items()):
        ax = axes[i]    
        
        # Assuming the first column is 2-theta (angle) and second column is intensity
        x_data = spectrum_data['T / °C']
        y_data = spectrum_data['q / W g^-1']
        baseline_data = spectrum_data['q_bl / W g^-1']
        
        # Shade the area between the spectrum and baseline
        if shade_melt:
            ax.fill_between(x_data, y_data, baseline_data, where=(y_data - baseline_data > 0), 
                            color=colours[3], alpha=alpha, label='Melting')
        if shade_crys:
            ax.fill_between(x_data, y_data, baseline_data, where=(y_data - baseline_data <= 0), 
                            color=colours[2], alpha=alpha, label='Crystallisation')
        
        # Plot baseline
        ax.plot(x_data, baseline_data, color=colours[1], marker=symbol, linestyle=linestyle, linewidth=linewidth, label='Baseline')
        
        # Plot spectrum data
        ax.plot(x_data, y_data, color=colours[0], marker=symbol, linestyle=linestyle, linewidth=linewidth, label='Raw')
        
        # Add title        
        ax.set_title(f'{title_letters[i]} {polymer_names.get(sheet, sheet)}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='best')
    
        # Label axes    
        if i in [2, 3]:    
            ax.set_xlabel('Temperature / °C')
        if i in [0, 2]:
            ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_samples_1st_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()
