import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_XRD_spectrum_heated_hdpe(
    file_path, 
    width=6., height=6.,
    x_lo=10, x_up=40, y_lo=0, y_up=None,
    colours=['black'], symbol='None', linestyle='solid', linewidth=1,
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    hdpe_ordered_sheets = [
        'HDPE_29C_1', 'HDPE_50C_1', 'HDPE_75C_1', 'HDPE_100C_1', 'HDPE_110C_1', 'HDPE_120C_1', 'HDPE_31C_after_1', 
    ]
    # Read data (your existing code)
    xl_file = pd.ExcelFile(file_path)
    sheet_names = xl_file.sheet_names
    spectrum_sheets = [sheet for sheet in sheet_names if sheet != 'Overview']

    # Filter HDPE data
    hdpe_sheets = [sheet for sheet in spectrum_sheets if 'HDPE' in sheet]
    
    hdpe_data = {}
    for sheet in hdpe_sheets:
        data = pd.read_excel(file_path, sheet_name=sheet)
        hdpe_data[sheet] = data
    
    # rearrange data according to the specified order
    hdpe_data = {sheet: hdpe_data[sheet] for sheet in hdpe_ordered_sheets if sheet in hdpe_data}
    
    # Legend dict (your existing code)
    hdpe_legend = {
        'HDPE_29C_1': '29 °C (heating)',
        'HDPE_50C_1': '50 °C (heating)',
        'HDPE_75C_1': '75 °C (heating)',
        'HDPE_100C_1': '100 °C (heating)',
        'HDPE_110C_1': '110 °C (heating)',
        'HDPE_120C_1': '120 °C (heating)',
        'HDPE_31C_after_1': '31 °C (cooling)',
    }
    
    title_letters = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)']
    
    # Calculate subplot grid dimensions
    n_plots = len(hdpe_data)
    n_cols = 3  # You can adjust this
    # n_rows = (n_plots + n_cols - 1) // n_cols  # Ceiling division
    n_rows = (n_plots // n_cols) + 1  # Ceiling division
    
    # Create subplots - one for each temperature
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(width, height), constrained_layout=True)
    
    # Flatten axes array for easy indexing
    if n_plots == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = axes
    else:
        axes = axes.flatten()
    
    # Plot each temperature on separate subplot
    for i, (sheet, spectrum_data) in enumerate(hdpe_data.items()):
        try:
            x_data = spectrum_data['2Theta_deg']
            y_data = spectrum_data['Original_Intensity_normalized']
            
            # Plot on individual subplot
            axes[i].plot(x_data, y_data, color=colours[i % len(colours)], 
                        marker=symbol, linestyle=linestyle, linewidth=linewidth)
            
            # Set title for each subplot
            axes[i].set_title(f'{title_letters[i]} {hdpe_legend[sheet]}')
            
            # Set axis limits
            if x_lo is not None:
                axes[i].set_xlim(left=x_lo)
            if x_up is not None:
                axes[i].set_xlim(right=x_up)
            if y_lo is not None:
                axes[i].set_ylim(bottom=y_lo)
            if y_up is not None:
                axes[i].set_ylim(top=y_up)
                
        except Exception as e:
            print(f"Error reading sheet {sheet}: {e}")
    
    # Label x axis the last 3 plots
    for i in [4, 5, 6]:
        with plt.rc_context({'text.usetex': False}):
            axes[i].set_xlabel(r'$2\theta$ / °')            
    
    # Label y axis
    for i in [0, 3, 6]:
        with plt.rc_context({'text.usetex': False}):            
            axes[i].set_ylabel('Norm. Intensity / A. U.')
    
    # Hide unused subplots
    for j in range(n_plots, len(axes)):
        axes[j].set_visible(False)
    
    # Save and display (your existing code)
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_XRD_heated_HDPE.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    if display_fig:
        plt.show()

def plot_XRD_spectrum_heated_peek(
    file_path, 
    width=6., height=6.,
    x_lo=10, x_up=40, y_lo=0, y_up=None,
    colours=['black'], symbol='None', linestyle='solid', linewidth=1,
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    peek_ordered_sheets = [
        'PEEK500907_26C_1', 
        'PEEK500907_50C_1', 
        'PEEK500907_100C_1', 
        'PEEK500907_150C_1', 
        'PEEK500907_200C_1', 
        'PEEK500907_250C_1', 
        'PEEK500907_300C_1', 
        'PEEK500907_30C_after_1', 
    ]
    # Read data (your existing code)
    xl_file = pd.ExcelFile(file_path)
    sheet_names = xl_file.sheet_names
    spectrum_sheets = [sheet for sheet in sheet_names if sheet != 'Overview']

    # Filter PEEK data
    peek_sheets = [sheet for sheet in spectrum_sheets if 'PEEK' in sheet]
    
    peek_data = {}
    for sheet in peek_sheets:
        data = pd.read_excel(file_path, sheet_name=sheet)
        peek_data[sheet] = data
    
    # rearrange data according to the specified order
    peek_data = {sheet: peek_data[sheet] for sheet in peek_ordered_sheets if sheet in peek_data}
    
    # Legend dict
    peek_legend = {
        'PEEK500907_26C_1': '26 °C (heating)',
        'PEEK500907_50C_1': '50 °C (heating)',
        'PEEK500907_100C_1': '100 °C (heating)',
        'PEEK500907_150C_1': '150 °C (heating)',
        'PEEK500907_200C_1': '200 °C (heating)',
        'PEEK500907_250C_1': '250 °C (heating)',
        'PEEK500907_300C_1': '300 °C (heating)',
        'PEEK500907_30C_after_1': '30 °C (cooling)',
    }
    
    title_letters = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)']
    
    # Calculate subplot grid dimensions
    n_plots = len(peek_data)
    n_cols = 3 
    n_rows = (n_plots // n_cols) + 1  # Ceiling division
    
    # Create subplots - one for each temperature
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(width, height), constrained_layout=True)
    
    # Flatten axes array for easy indexing
    if n_plots == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = axes
    else:
        axes = axes.flatten()
    
    # Plot each temperature on separate subplot
    for i, (sheet, spectrum_data) in enumerate(peek_data.items()):
        try:
            x_data = spectrum_data['2Theta_deg']
            y_data = spectrum_data['Original_Intensity_normalized']
            
            # Plot on individual subplot
            axes[i].plot(x_data, y_data, color=colours[i % len(colours)], 
                        marker=symbol, linestyle=linestyle, linewidth=linewidth)
            
            # Set title for each subplot
            axes[i].set_title(f'{title_letters[i]} {peek_legend[sheet]}')
            
            # Set axis limits
            if x_lo is not None:
                axes[i].set_xlim(left=x_lo)
            if x_up is not None:
                axes[i].set_xlim(right=x_up)
            if y_lo is not None:
                axes[i].set_ylim(bottom=y_lo)
            if y_up is not None:
                axes[i].set_ylim(top=y_up)
                
        except Exception as e:
            print(f"Error reading sheet {sheet}: {e}")
    
    # Label x axis
    for i in [5, 6, 7]:
        with plt.rc_context({'text.usetex': False}):
            axes[i].set_xlabel(r'$2\theta$ / °')
    
    # Label y axis
    for i in [0, 3, 6]:
        with plt.rc_context({'text.usetex': False}):            
            axes[i].set_ylabel('Norm. Intensity / A. U.')
    
    # Hide unused subplots
    for j in range(n_plots, len(axes)):
        axes[j].set_visible(False)
    
    # Save and display (your existing code)
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_XRD_heated_PEEKa.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    if display_fig:
        plt.show()

