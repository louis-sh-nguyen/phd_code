import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def plot_CO2_density(data_path, T_celsius_values=[25, 35, 50], types=['Exp.', 'SW', 'SAFT'],
                 width=5., height=3.5,
                 x_lo=0., x_up=None, y_lo=0., y_up=None,
                 colours=['C0', 'C1','C2'], symbols=['s', 'o', 'v'], linestyle='None', markerfacecolor='None',
                 error_capsize=3, error_capthick=1,
                 alpha_zoom=0.8,
                 display_legend=True, display_fig=True, save_fig=True, folder_to_save ='../figures', save_format='pdf', dpi=1200):
    
    barToMPa = 1e-1

    df = {} # empty dict to store values
    
    # Reading data from Excel file
    for T in T_celsius_values:
        df[T] = pd.read_excel(data_path, sheet_name=f'{T}C')
        
    # Plotting
    fig = plt.figure(figsize=(width, height))
    n_col=1
    n_row=1
    ax = fig.add_subplot(n_row, n_col, 1)

    for i, T in enumerate(T_celsius_values):
        if 'Exp.' in types:
            j = 0
            ax.plot(df[T]['p / bar'] * barToMPa, df[T]['ρexp / g/cc'],
                color = colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor)
            # ax.errorbar(df[T]['p / bar'] * barToMPa, df[T]['ρexp / g/cc'],
            #     yerr=df[T]['u_c (ρexp)'],
            #     color=colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor, capsize=error_capsize, capthick=error_capthick)

        if 'SW' in types:
            j = 1
            ax.plot(df[T]['p / bar'] * barToMPa, df[T]['ρSW / g/cc'],
                color = colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor)
            # ax.errorbar(df[T]['p / bar'] * barToMPa, df[T]['ρSW / g/cc'],
            #     yerr=df[T]['u_c (ρSW)'],
            #     color=colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor, capsize=error_capsize, capthick=error_capthick)
        if 'SW' in types:
            j = 2
            ax.plot(df[T]['p / bar'] * barToMPa, df[T]['ρSAFT / g/cc'],
                color = colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor)
            # ax.errorbar(df[T]['p / bar'] * barToMPa, df[T]['ρSAFT / g/cc'],
            #     yerr=df[T]['u_c (ρSAFT)'],
            #     color=colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor, capsize=error_capsize, capthick=error_capthick)

    # Create an inset axes
    axins = ax.inset_axes([0.55, 0.15, 0.4, 0.4])  # [x, y, width, height]

    for i, T in enumerate(T_celsius_values):
        if 'Exp.' in types:
            j = 0
            axins.plot(df[T]['p / bar'] * barToMPa, df[T]['ρexp / g/cc'],
                color = colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor)
            # axins.errorbar(df[T]['p / bar'] * barToMPa, df[T]['ρexp / g/cc'],
            #     yerr=df[T]['u_c (ρexp)'],
            #     color=colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor, capsize=error_capsize, capthick=error_capthick)
        if 'SW' in types:
            j = 1
            axins.plot(df[T]['p / bar'] * barToMPa, df[T]['ρSW / g/cc'],
                color = colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor)
            # axins.errorbar(df[T]['p / bar'] * barToMPa, df[T]['ρSW / g/cc'],
            #     yerr=df[T]['u_c (ρSW)'],
            #     color=colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor, capsize=error_capsize, capthick=error_capthick)
        if 'SW' in types:
            j = 2
            axins.plot(df[T]['p / bar'] * barToMPa, df[T]['ρSAFT / g/cc'],
                color = colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor)
            # axins.errorbar(df[T]['p / bar'] * barToMPa, df[T]['ρSAFT / g/cc'],
            #     yerr=df[T]['u_c (ρSAFT)'],
            #     color=colours[i], marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor, capsize=error_capsize, capthick=error_capthick)

    # Specify the limits for the inset
    x1, x2, y1, y2 = 0, 6.0, 0, 0.20
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, y2)
    axins.set_xticks([0, 2, 4, 6])
    # axins.set_xticklabels('')
    # axins.set_yticklabels('')

    # Draw a rectangle to highlight the zoomed region
    ax.indicate_inset_zoom(axins, alpha=alpha_zoom)
    
    ax.set_xlabel(r'$p$ / MPa')
    # ax.set_ylabel(r'$\rho_{\mathrm{CO}_2}$ / $\mathrm{g \, cm^{-3}}$')
    ax.set_ylabel(r'$\rho_{\mathrm{s,ext}}$ / $\mathrm{g \, cm^{-3}}$')
    
    if x_lo is not None:
        ax.set_xlim(left=x_lo)
    if x_up is not None:
        ax.set_xlim(right=x_up)
    if y_lo is not None:
        ax.set_ylim(bottom=y_lo)
    if y_up is not None:
        ax.set_ylim(top=y_up)
    
    # Add legend by colours and symbols
    if display_legend == True:
        colour_legend = [matplotlib.lines.Line2D([], [], color=colours[i], marker='None', linestyle='solid', linewidth=5, label=f'{T} °C') for i, T in enumerate(T_celsius_values)]
        marker_legend = [matplotlib.lines.Line2D([], [], color='black', marker=symbols[i], markerfacecolor='None', linestyle='None', label=f'{type}') for i, type in enumerate(types)]
        custom_legend = colour_legend + marker_legend
        ax.legend(handles=custom_legend).set_visible(True)  # inside
        # ax.legend(handles=custom_legend, bbox_to_anchor=(1.05, 1), loc='upper left').set_visible(True) # outside
    
    # Save figure
    if save_fig == True:
        save_fig_path = folder_to_save + f"/fig_CO2_density.{save_format}"
        plt.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {save_fig_path}.")
    
    # Display figure
    if display_fig == True:
        plt.show()
