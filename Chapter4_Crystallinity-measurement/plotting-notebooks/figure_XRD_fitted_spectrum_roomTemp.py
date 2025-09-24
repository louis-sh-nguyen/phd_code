import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_XRD_fitted_spectrum_hdpe(
    file_path, 
    width=6., height=6.,
    x_lo=10, x_up=40, y_lo=0, y_up=None,
    colours=['black', 'C2', 'C0', 'C1'], symbol='None', raw_linestyle='solid', fit_linestyle='dashed', linewidth=1,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        'HDPE', 'HDPE_2', 'HDPE_3', 'HDPE_4'
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
        axes[i].set_title(f'{title_letters[i]} Repeat {i+1}')
        
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
        filename = f"fig_XRD_RT_fit_HDPE.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    if display_fig:
        plt.show()

def plot_XRD_fitted_spectrum_peeka(
    file_path, 
    width=6., height=6.,
    x_lo=10, x_up=40, y_lo=0, y_up=None,
    colours=['black', 'C2', 'C0', 'C1'], symbol='None', raw_linestyle='solid', fit_linestyle='dashed', linewidth=1,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '500907', '500907_2'
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
        axes[i].set_title(f'{title_letters[i]} Repeat {i+1}')
        
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
    
        # Label axis
        with plt.rc_context({'text.usetex': False}):
            axes[i].set_xlabel(r'$2\theta$ / °')    
            axes[i].set_ylabel('Norm. Intensity / A. U.')
    
    # Hide unused subplots
    for j in range(n_plots, len(axes)):
        axes[j].set_visible(False)
    
    # Save and display (your existing code)
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_XRD_RT_fit_PEEKa.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    if display_fig:
        plt.show()

def plot_XRD_fitted_spectrum_peekb(
    file_path, 
    width=6., height=6.,
    x_lo=10, x_up=40, y_lo=0, y_up=None,
    colours=['black', 'C2', 'C0', 'C1'], symbol='None', raw_linestyle='solid', fit_linestyle='dashed', linewidth=1,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '501023', '501023_2', '501023_3', '501023_4'
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
        axes[i].set_title(f'{title_letters[i]} Repeat {i+1}')
        
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
        filename = f"fig_XRD_RT_fit_PEEKb.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    if display_fig:
        plt.show()        

def plot_XRD_fitted_spectrum_peekc(
    file_path, 
    width=6., height=6.,
    x_lo=10, x_up=40, y_lo=0, y_up=None,
    colours=['black', 'C2', 'C0', 'C1'], symbol='None', raw_linestyle='solid', fit_linestyle='dashed', linewidth=1,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '501024', '501024_2'
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
        axes[i].set_title(f'{title_letters[i]} Repeat {i+1}')
        
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
    
        # Label axis
        with plt.rc_context({'text.usetex': False}):
            axes[i].set_xlabel(r'$2\theta$ / °')    
            axes[i].set_ylabel('Norm. Intensity / A. U.')
            
    # Hide unused subplots
    for j in range(n_plots, len(axes)):
        axes[j].set_visible(False)
    
    # Save and display (your existing code)
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_XRD_RT_fit_PEEKc.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    if display_fig:
        plt.show()        
