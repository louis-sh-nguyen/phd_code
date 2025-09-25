import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def plot_raw_mass_horizontal(data_path,
                 width=5., height=3.5,
                 linecolour='black', linestyle='None', symbol='o', markerfacecolor='None',
                 alpha_zoom=0.8,
                 display_fig=True, save_fig=False, folder_to_save ='../figures', save_format='pdf', dpi=1200):
    
    T_celsius_values=[25, 35, 50]
    
    barToMPa = 1e-1

    df_main = pd.read_excel(data_path, sheet_name='raw')
    
    df = {} # empty dict to store values by temperature
    for T in T_celsius_values:
        df[T] = df_main.loc[df_main['T / °C'] == T].copy()
        
    # Plotting
    fig = plt.figure(figsize=(width, height), constrained_layout=True)
    n_row=1
    n_col=3
    ax1 = fig.add_subplot(n_row, n_col, 1)
    ax2 = fig.add_subplot(n_row, n_col, 2)
    ax3 = fig.add_subplot(n_row, n_col, 3)
    
    axs = [ax1, ax2, ax3]
    titles = ['(a)', '(b)', '(c)']
    
    for i, (T, ax, title) in enumerate(zip(T_celsius_values, axs, titles)):
        ax.plot(df[T]['p / bar']*barToMPa, df[T]['m_raw / g'], 
                color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)
    
        # Configuring the plots
        ax.set_xlim(left=0)
        ax.set_title(title + f' {T:.0f} °C')        
    
    #------------------------------- 
    # INSET
    #-------------------------------
    # ax2
    axins2 = ax2.inset_axes([0.55, 0.55, 0.4, 0.4])  # [x, y, width, height]
    axins2.plot(df[35]['p / bar']*barToMPa, df[35]['m_raw / g'],
                color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)

    x1, x2, y1, y2 = 0, 1.5, -0.2, 0.2
    axins2.set_xlim(x1, x2)
    axins2.set_ylim(y1, y2)
    axins2.set_xticklabels('')
    axins2.set_yticklabels('')
    
    ax2.indicate_inset_zoom(axins2, alpha=alpha_zoom)
    
    # ax3
    axins3 = ax3.inset_axes([0.55, 0.55, 0.4, 0.4])  # [x, y, width, height]
    axins3.plot(df[50]['p / bar']*barToMPa, df[50]['m_raw / g'],
                color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)
    
    x1, x2, y1, y2 = 0, 1.5, -0.2, 0.2
    axins3.set_xlim(x1, x2)
    axins3.set_ylim(y1, y2)
    axins3.set_xticklabels('')
    axins3.set_yticklabels('')
    
    ax3.indicate_inset_zoom(axins3, alpha=alpha_zoom)
    
    #------------------------------- 
    # CONFIGURING THE PLOTS
    #-------------------------------
    # Labels
    ax1.set_ylabel(r'$m_{\mathrm{raw}}$ / g')
    ax1.set_xlabel(r'$p$ / MPa')    
    ax2.set_xlabel(r'$p$ / MPa')    
    ax3.set_xlabel(r'$p$ / MPa')
    
    # Ticks
    ax1.set_xlim(left=0, right=6)
    ax1.set_ylim(top=0.1, bottom=-0.3)
    ax1.set_yticks(np.arange(-0.3, 0.11, 0.1))
    ax2.set_xlim(left=0, right=30)
    ax3.set_xlim(left=0, right=30)
    
    # Save figure
    if save_fig == True:
        save_fig_path = folder_to_save + f"/fig_raw_mass.{save_format}"
        plt.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {save_fig_path}.")
    
    # Display figure
    if display_fig == True:
        plt.show()

def plot_raw_mass_vertical(data_path,
                 width=5., height=3.5,
                 linecolour='black', linestyle='None', symbol='o', markerfacecolor='None',
                 alpha_zoom=0.8, error_capsize=3, error_capthick=1,
                 display_fig=True, save_fig=False, folder_to_save ='../figures', save_format='pdf', dpi=1200):
    
    T_celsius_values=[25, 35, 50]
    
    barToMPa = 1e-1

    df_main = pd.read_excel(data_path, sheet_name='raw')
    
    df = {} # empty dict to store values by temperature
    for T in T_celsius_values:
        df[T] = df_main.loc[df_main['T / °C'] == T].copy()
        
    # Plotting
    fig = plt.figure(figsize=(width, height), constrained_layout=True)
    n_row=3
    n_col=1
    ax1 = fig.add_subplot(n_row, n_col, 1)
    ax2 = fig.add_subplot(n_row, n_col, 2)
    ax3 = fig.add_subplot(n_row, n_col, 3)
    
    axs = [ax1, ax2, ax3]
    titles = ['(a)', '(b)', '(c)']
    
    for i, (T, ax, title) in enumerate(zip(T_celsius_values, axs, titles)):
        ax.plot(df[T]['p / bar']*barToMPa, df[T]['m_raw / g'], 
                color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)
        # ax.errorbar(df[T]['p / bar']*barToMPa, df[T]['m_raw / g'], 
        #             yerr=df[T]['u_c(m_raw) / g'],
        #             color=linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor,
        #             capsize=error_capsize, capthick=error_capthick)

        # Configuring the plots
        ax.set_xlim(left=0)
        ax.set_title(title + f' {T:.0f} °C')        
    
    #------------------------------- 
    # INSET
    #-------------------------------
    # # ax2
    # axins2 = ax2.inset_axes([0.55, 0.55, 0.4, 0.4])  # [x, y, width, height]
    # axins2.plot(df[35]['p / bar']*barToMPa, df[35]['m_raw / g'],
    #             color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)

    # x1, x2, y1, y2 = 0, 1.5, -0.2, 0.2
    # axins2.set_xlim(x1, x2)
    # axins2.set_ylim(y1, y2)
    # # axins2.set_xticklabels('')
    # # axins2.set_yticklabels('')
    
    # ax2.indicate_inset_zoom(axins2, alpha=alpha_zoom)
    
    # # ax3
    # axins3 = ax3.inset_axes([0.55, 0.55, 0.4, 0.4])  # [x, y, width, height]
    # axins3.plot(df[50]['p / bar']*barToMPa, df[50]['m_raw / g'],
    #             color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)
    
    # x1, x2, y1, y2 = 0, 1.5, -0.2, 0.2
    # axins3.set_xlim(x1, x2)
    # axins3.set_ylim(y1, y2)
    # # axins3.set_xticklabels('')
    # # axins3.set_yticklabels('')
    
    # ax3.indicate_inset_zoom(axins3, alpha=alpha_zoom)
    
    #------------------------------- 
    # CONFIGURING THE PLOTS
    #-------------------------------
    # Labels
    ax1.set_ylabel(r'$m_{\mathrm{raw}}$ / g')
    ax2.set_ylabel(r'$m_{\mathrm{raw}}$ / g')
    ax3.set_ylabel(r'$m_{\mathrm{raw}}$ / g')
    ax3.set_xlabel(r'$p$ / MPa')
    
    # Ticks
    # ax1.set_xlim(left=0, right=6)
    # ax1.set_ylim(top=0.1, bottom=-0.3)
    # ax1.set_yticks(np.arange(-0.3, 0.11, 0.1))
    # ax2.set_xlim(left=0, right=30)
    # ax3.set_xlim(left=0, right=30)
    
    # Save figure
    if save_fig == True:
        save_fig_path = folder_to_save + f"/fig_raw_mass.{save_format}"
        plt.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {save_fig_path}.")
    
    # Display figure
    if display_fig == True:
        plt.show()
        