import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_DSC_spectrum_fit_roomTemp_1st_cycle_hdpe(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        'HDPE_1_cycle1', 'HDPE_2_cycle1',
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
        ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='lower right')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_HDPE_1st_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()

def plot_DSC_spectrum_fit_roomTemp_1st_cycle_peeka(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '500907_1_cycle1', '500907_2_cycle1',
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
            ax.fill_between(x_data, y_data, baseline_data,where=(y_data - baseline_data <= 0), 
                            color=colours[2], alpha=alpha, label='Crystallisation')
        
        # Plot baseline
        ax.plot(x_data, baseline_data, color=colours[1], marker=symbol, linestyle=linestyle, linewidth=linewidth, label='Baseline')
        
        # Plot spectrum data
        ax.plot(x_data, y_data, color=colours[0], marker=symbol, linestyle=linestyle, linewidth=linewidth, label='Raw')
        
        # Add title        
        ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='best')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_PEEKa_1st_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()

def plot_DSC_spectrum_fit_roomTemp_1st_cycle_peekb(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '501023_1_cycle1', '501023_2_cycle1',
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
        ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='best')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_PEEKb_1st_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()

def plot_DSC_spectrum_fit_roomTemp_1st_cycle_peekc(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '501024_1_cycle1'
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
        if n_plots > 1:
            ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='best')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Hide unused subplots
    for j in range(n_plots, len(axes)):
        axes[j].set_visible(False)
    
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_PEEKc_1st_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()


def plot_DSC_spectrum_fit_roomTemp_2nd_cycle_hdpe(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        'HDPE_1_cycle2', 'HDPE_2_cycle2',
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
        ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='lower right')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_HDPE_2nd_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()

def plot_DSC_spectrum_fit_roomTemp_2nd_cycle_peeka(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '500907_1_cycle2', '500907_2_cycle2',
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
            ax.fill_between(x_data, y_data, baseline_data,where=(y_data - baseline_data <= 0), 
                            color=colours[2], alpha=alpha, label='Crystallisation')
        
        # Plot baseline
        ax.plot(x_data, baseline_data, color=colours[1], marker=symbol, linestyle=linestyle, linewidth=linewidth, label='Baseline')
        
        # Plot spectrum data
        ax.plot(x_data, y_data, color=colours[0], marker=symbol, linestyle=linestyle, linewidth=linewidth, label='Raw')
        
        # Add title        
        ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='lower right')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_PEEKa_2nd_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()


def plot_DSC_spectrum_fit_roomTemp_2nd_cycle_peekb(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '501023_1_cycle2', '501023_2_cycle2',
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
        ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='lower right')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_PEEKb_2nd_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()

def plot_DSC_spectrum_fit_roomTemp_2nd_cycle_peekc(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '501024_1_cycle2'
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
        if n_plots > 1:
            ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='lower right')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Hide unused subplots
    for j in range(n_plots, len(axes)):
        axes[j].set_visible(False)
    
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_PEEKc_2nd_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()

def plot_DSC_spectrum_fit_roomTemp_3rd_cycle_hdpe(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        'HDPE_1_cycle3', 'HDPE_2_cycle3',
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
        ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='lower right')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_HDPE_3rd_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()


def plot_DSC_spectrum_fit_roomTemp_3rd_cycle_peeka(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '500907_1_cycle3', '500907_2_cycle3',
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
            ax.fill_between(x_data, y_data, baseline_data,where=(y_data - baseline_data <= 0), 
                            color=colours[2], alpha=alpha, label='Crystallisation')
        
        # Plot baseline
        ax.plot(x_data, baseline_data, color=colours[1], marker=symbol, linestyle=linestyle, linewidth=linewidth, label='Baseline')
        
        # Plot spectrum data
        ax.plot(x_data, y_data, color=colours[0], marker=symbol, linestyle=linestyle, linewidth=linewidth, label='Raw')
        
        # Add title        
        ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='lower right')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_PEEKa_3rd_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()

def plot_DSC_spectrum_fit_roomTemp_3rd_cycle_peekb(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '501023_1_cycle3', '501023_2_cycle3',
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
        ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='lower right')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_PEEKb_3rd_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()


def plot_DSC_spectrum_fit_roomTemp_3rd_cycle_peekc(
    file_path, 
    width=6., height=6.,
    colours=['black', 'grey', 'C0', 'C2',], symbol='None', linestyle='solid', linewidth=1, alpha=0.6,
    shade_melt=True, shade_crys=False,
    display_legend=True, display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400
    ):    

    ordered_sheets = [
        '501024_1_cycle3'
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
        if n_plots > 1:
            ax.set_title(f'{title_letters[i]} Repeat {i+1}')
        
        # Display legend
        if display_legend:
            ax.legend(loc='lower right')
    
        # Label axes        
        ax.set_xlabel('Temperature / °C')
        ax.set_ylabel(r'Heat Flow / $\mathrm{W \, g^{-1}}$')
        
    # Hide unused subplots
    for j in range(n_plots, len(axes)):
        axes[j].set_visible(False)
    
    # Save figure
    if save_fig:
        # Create directory if it doesn't exist
        os.makedirs(folder_to_save, exist_ok=True)
        
        # Create filename
        filename = f"fig_DSC_RT_spectrum_fit_PEEKc_3rd_cycle.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        
        # Save figure
        plt.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {filepath}")
    
    # Display figure
    if display_fig:
        plt.show()
