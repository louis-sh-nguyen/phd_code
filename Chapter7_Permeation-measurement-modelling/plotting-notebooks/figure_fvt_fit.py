import os
import pandas as pd
import matplotlib.pyplot as plt
from utils import exp_dict

def plot_fvt_flux_fit_hdpe(
    data_folder_path,
    width=6., height=4.0,
    x_lo=0., y_lo=0.,
    model_colour='C2',
    exp_colour='black',
    symbol='None',
    markersize=2,
    linestyle='solid',
    linewidth=1,
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    ordered_hdpe_files = [
        'RUN_H_25C-50bar', 'RUN_H_25C-100bar_7', 'RUN_H_25C-100bar_8', 'RUN_H_25C-100bar_9',
        'RUN_H_25C-200bar_2', 'RUN_H_50C-50bar', 'RUN_H_50C-100bar_2', 'RUN_H_50C-200bar',
        'RUN_H_75C-50bar', 'RUN_H_75C-100bar',
    ]

    all_exp_data = {}
    all_fit_data = {}

    # Load data
    for file in ordered_hdpe_files:
        if file not in all_exp_data:
            all_exp_data[file] = {}
        data_dir = f'{data_folder_path}/{file}'
        # Load exp data
        exp_files = [f for f in os.listdir(data_dir) if f.startswith('experimental_data') and f.endswith(('.csv'))]    
        exp_data = pd.read_csv(f'{data_dir}/{exp_files[0]}')
        all_exp_data[file] = exp_data
        
        # Load fit data
        fit_files = [f for f in os.listdir(data_dir) if f.startswith('flux_evolution') and f.endswith(('.csv'))]
        fit_data = pd.read_csv(f'{data_dir}/{fit_files[0]}')
        all_fit_data[file] = fit_data

    # Calculate subplot grid dimensions
    n_plots = len(all_exp_data)
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

    title_letters = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)', '(j)', '(k)', '(l)', '(m)', '(n)', '(o)', '(p)']

    # Plot each sample group in its own subplot
    for i, exp_name in enumerate(ordered_hdpe_files):
        ax = axes[i]    
        
        exp_data = all_exp_data[exp_name]
        fit_data = all_fit_data[exp_name]
        
        # Plot exp data
        ax.plot(exp_data['time'], exp_data['normalised_flux'], color=exp_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Exp.')
        
        # Plot fit data
        ax.plot(fit_data['time'], fit_data['normalised_flux'], color=model_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Model')
        
        # Set axis limits
        if x_lo is not None:
            ax.set_xlim(left=x_lo)
        if y_lo is not None:
            ax.set_ylim(bottom=y_lo)
        ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
        ax.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
        
        # Set y-axis limits
        ax.set_ylim(top=1.25)
        
        # Set y-axis ticks
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0, 1.25])
        
        # Set custom x-axis limits for tau
        # if exp_name in ['RUN_H_25C-100bar_9', 'RUN_H_25C-200bar_2', 'RUN_H_50C-200bar', 'RUN_H_75C-50bar' ]:
        #     ax.set_xlim(right=0.8)
        
        # Set title
        ax.set_title(f'{title_letters[i]} {exp_dict[exp_name]}')
        
        # Set legend
        ax.legend(loc='lower right')

    # Set common labels
    for i in [0, 2, 4, 6, 8]:
        axes[i].set_ylabel(r'Norm. Flux')

    for i in [8, 9]:
        axes[i].set_xlabel('Time / s')

    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_fvt_flux_fit_hdpe.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()

def plot_fvt_flux_fit_peeka(
    data_folder_path,
    width=6., height=4.0,
    x_lo=0., y_lo=0.,
    model_colour='C2',
    exp_colour='black',
    symbol='None',
    markersize=2,
    linestyle='solid',
    linewidth=1,
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400,
):
    ordered_peeka_files = [
        'S4R3', 'S4R4', 'S4R6', 'S4R5',
    ]

    all_exp_data = {}
    all_fit_data = {}
    
    # Load data
    for file in ordered_peeka_files:
        if file not in all_exp_data:
            all_exp_data[file] = {}
        data_dir = f'{data_folder_path}/{file}'
        
        # Load exp data
        exp_files = [f for f in os.listdir(data_dir) if f.startswith('experimental_data') and f.endswith(('.csv'))]    
        exp_data = pd.read_csv(f'{data_dir}/{exp_files[0]}')
        all_exp_data[file] = exp_data
        
        # Load fit data
        fit_files = [f for f in os.listdir(data_dir) if f.startswith('flux_evolution') and f.endswith(('.csv'))]
        fit_data = pd.read_csv(f'{data_dir}/{fit_files[0]}')
        all_fit_data[file] = fit_data

    # Calculate subplot grid dimensions
    n_plots = len(all_exp_data)
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

    title_letters = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)', '(g)', '(h)', '(i)', '(j)', '(k)', '(l)', '(m)', '(n)', '(o)', '(p)']

    # Plot each sample group in its own subplot
    for i, exp_name in enumerate(ordered_peeka_files):
        ax = axes[i]    
        
        # Get data
        exp_data = all_exp_data[exp_name]
        fit_data = all_fit_data[exp_name]
        
        # Plot exp data
        ax.plot(exp_data['time'], exp_data['normalised_flux'], color=exp_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Exp.')
        
        # Plot fit data
        ax.plot(fit_data['time'], fit_data['normalised_flux'], color=model_colour, marker=symbol, markersize=markersize, linestyle=linestyle, linewidth=linewidth, label='Model')
        
        # Set axis limits
        if x_lo is not None:
            ax.set_xlim(left=x_lo)
        if y_lo is not None:
            ax.set_ylim(bottom=y_lo)
        ax.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
        ax.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))

        # Set y-axis limits
        ax.set_ylim(top=1.25)
        
        # Set y-axis ticks
        ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0, 1.25])
        
        # Set custom x-axis limits 
        if exp_name == 'S4R4':
            ax.set_xlim(right=80e3)
        
        # Set title
        ax.set_title(f'{title_letters[i]} {exp_dict[exp_name]}')
        
        # Set legend
        ax.legend(loc='lower right')

    # Set common labels
    for i in [0, 2]:
        axes[i].set_ylabel('Norm. Flux')

    for i in [2, 3]:
        axes[i].set_xlabel('Time / s')

    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_fvt_flux_fit_peeka.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()