import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

def plot_solubility_literature_comparison(    
    data_path,
    width=5., height=3.5,
    y_up=None,
    colours=['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'], symbols=['o', 'D', 'P', '*', '^', 'H', '8', '4'], linestyle='None', markerfacecolor='None',
    alpha_zoom=0.8,
    display_legend=True, display_fig=True, save_fig=False, folder_to_save ='../figures', save_format='pdf', dpi=400):
    
    barToMPa = 1e-1

    # Get symbols
    model_symbol = symbols[0]   # first symbol is for model data
    lit_symbols = symbols[1:]
    
    # Read data
    df_model = pd.read_excel(data_path, sheet_name='SW_results')
    df_lit_all = pd.read_excel(data_path, sheet_name='literature')
    
    # Filter literature data
    df_lit = {}
    
    lit_types = df_lit_all['Type'].unique().tolist()
    for lit_type in lit_types:
        df_lit[lit_type] = df_lit_all.loc[df_lit_all['Type'] == lit_type].copy()

    # Get all types, starting with model
    all_types = ['Current work (SW)'] + lit_types
    # Get common list of temperatures in df_model and df_lit, starting with T values from models ([25, 35, 50])
    T_values_model_unique = df_model['T / °C'].unique()
    T_values_lit_unique = df_lit_all['T / °C'].unique()
    
    # Get the extra values other than 25, 35, 50 C
    T_values_diff = np.setdiff1d(T_values_lit_unique, T_values_model_unique)
    
    # Sort the extra values
    T_values_diff = np.sort(T_values_diff)

    # Get unique temperatures from both sets, starting with 25, 35, 50 C
    T_values_unique = np.concatenate((T_values_model_unique, T_values_diff))
    
    # Plotting
    fig = plt.figure(figsize=(width, height))
    n_col=1
    n_row=1
    ax = fig.add_subplot(n_row, n_col, 1)
    
    for i, T in enumerate(T_values_unique):
        # Plot model data from current work if temp available
        df_model_T = df_model.loc[df_model['T / °C'].astype(int) == T].copy()
        
        if T in T_values_model_unique:  # only plot if T is in model data
            ax.plot(df_model_T['f / bar'] * barToMPa, df_model_T['S_am / g/g_am'], color=colours[i], marker=model_symbol, markerfacecolor=markerfacecolor, linestyle=linestyle)

        # Plot literature data
        for j, lit_type in enumerate(lit_types):
            df_lit_T = df_lit[lit_type].loc[df_lit[lit_type]['T / °C'].astype(int) == T].copy()
            ax.plot(df_lit_T['f / bar'] * barToMPa, df_lit_T['S_am / g/g_am'], color=colours[i], marker=lit_symbols[j], markerfacecolor=markerfacecolor, linestyle=linestyle)

    # Add legend by colours and symbols
    if display_legend == True:
        # Use colours for temperature
        colour_legend = [matplotlib.lines.Line2D([], [], color=colours[i], marker='None', linestyle='solid', linewidth=5, label=f'{T} °C') for i, T in enumerate(T_values_unique)]
        # Use symbols for type 
        marker_legend = [matplotlib.lines.Line2D([], [], color='black', marker=symbols[i], markersize=6, markerfacecolor='None', linestyle='None', label=f'{type}') for i, type in enumerate(all_types)]
        custom_legend = colour_legend + marker_legend
        ax.legend(handles=custom_legend, bbox_to_anchor=(1.05, 1), loc='upper left').set_visible(True)
    
    # Configuring the plots
    ax.set_xlabel(r'$f$ / MPa')
    ax.set_ylabel(r'$q_{\mathrm{am}}$ / $\mathrm{g \, g^{-1}}$')
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)
    if y_up is not None:
        ax.set_ylim(top=y_up)
    
    #-------------------------------
    # PLOT INSET
    #-------------------------------
    # Create an inset axes
    axins = ax.inset_axes([0.55, 0.15, 0.4, 0.4])  # [x, y, width, height]
    
    # Plot the same data in the inset
    for i, T in enumerate(T_values_unique):
        # Plot model data from current work if temp available
        df_model_T = df_model.loc[df_model['T / °C'].astype(int) == T].copy()
        
        if T in T_values_model_unique:  # only plot if T is in model data
            axins.plot(df_model_T['f / bar'] * barToMPa, df_model_T['S_am / g/g_am'], color=colours[i], marker=model_symbol, markerfacecolor=markerfacecolor, linestyle=linestyle)

        # Plot literature data
        for j, lit_type in enumerate(lit_types):
            df_lit_T = df_lit[lit_type].loc[df_lit[lit_type]['T / °C'].astype(int) == T].copy()
            axins.plot(df_lit_T['f / bar'] * barToMPa, df_lit_T['S_am / g/g_am'], color=colours[i], marker=lit_symbols[j], markerfacecolor=markerfacecolor, linestyle=linestyle)

    # Specify the limits for the inset
    x1, x2, y1, y2 = 0, 5.0, 0, 0.075
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, y2)
    # axins.set_xticklabels('')
    # axins.set_yticklabels('')

    # Draw a rectangle to highlight the zoomed region
    ax.indicate_inset_zoom(axins, alpha=alpha_zoom)
    
    # Save figure
    if save_fig == True:
        save_fig_path = folder_to_save + f"/fig_literature_comparison.{save_format}"
        plt.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {save_fig_path}.")
    
    # Display figure
    if display_fig == True:
        plt.show()
        
if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # figure style
    plt.style.use('seaborn-v0_8-colorblind')
    plt.style.use('../../../../thesis.mplstyle')

    # Figure sizes
    cmToInch = 1/2.54
    text_width = 14.2  # cm
    base_height = 5.  # cm
    # Define the path to the data file
    wh_ratio = 4/3
    width = 0.70 * text_width * cmToInch
    height = width / wh_ratio
    plot_solubility_literature_comparison(
        data_path = '../data/literature_comparison_data.xlsx', width=width, height=height, 
        alpha_zoom=0.0,
        display_legend=True, display_fig=True, save_fig=False)
    