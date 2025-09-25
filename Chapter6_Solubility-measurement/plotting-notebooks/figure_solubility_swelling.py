import pandas as pd
import os
import matplotlib.pyplot as plt

def plot_solubility_swelling_single_temp(
    data_path, T_celsius,
    types=['exp', 'SW', 'SAFT'],
    width=5., height=3.5,
    x_lo=0., y_lo=0., 
    colour='black', symbols=['s', 'o', 'v'], linestyle='None', markerfacecolor='None',
    alpha_zoom=0.,
    display_legend=True, display_fig=True, save_fig=True, folder_to_save ='../figures', save_format='pdf', dpi=400):

    # Check if the provided types are valid
    allowed_types = ['SAFT', 'exp', 'SW']
    if not all(t in allowed_types for t in types):
        raise ValueError(f"Invalid type(s) '{types}'. Allowed types are: {allowed_types}")
    
    # Check if the provided temperature is valid
    allowed_temps_celsius = [25, 35, 50]
    if T_celsius not in allowed_temps_celsius:
        raise ValueError(f"Invalid temperature '{T_celsius}'. Allowed temperatures are: {allowed_temps_celsius}")
    
    barToMPa = 1e-1

    df = {} # empty dict to store values
    
    # Reading data from Excel file
    for type in types:
        _df = pd.read_excel(data_path, sheet_name=f'{type}')
        df[type] = _df.loc[_df['T / °C'] == T_celsius].copy()    
    
    # Plotting
    fig = plt.figure(figsize=(width, height), constrained_layout=True)
    # Create subplots
    n_col=2
    n_row=1
    ax1 = fig.add_subplot(n_row, n_col, 1)
    ax2 = fig.add_subplot(n_row, n_col, 2)
    axs = [ax1, ax2]
    titles = ['(a)', '(b)']

    for i, type in enumerate(types):
        ax1.plot(df[type]['p / bar'] * barToMPa, df[type]['q_sc / g/g_overall'],
            color = colour, marker=symbols[i], linestyle=linestyle, markerfacecolor=markerfacecolor, label=type)
        ax2.plot(df[type]['p / bar'] * barToMPa, df[type]['SR / m3/m3'],
            color = colour, marker=symbols[i], linestyle=linestyle, markerfacecolor=markerfacecolor, label=type)

    
    # Configuring the plots
    for ax, title in zip(axs, titles):
        ax.set_title(title + f' {T_celsius:.0f} °C')
        if x_lo is not None:
            ax.set_xlim(left=x_lo)
        if y_lo is not None:
            ax.set_ylim(bottom=y_lo)
        
        if display_legend:
            ax.legend().set_visible(True)
    
    # Configure axis titles
    ax1.set_xlabel(r'$p$ / MPa')
    ax1.set_ylabel(r'$q_{\mathrm{sc}}$ / $\mathrm{g \, g^{-1}}$')
    ax2.set_xlabel(r'$p$ / MPa')
    ax2.set_ylabel(r'$SR$')

    # Save figure
    if save_fig == True:
        save_fig_path = folder_to_save + f"/fig_solubility_swelling_{T_celsius}.{save_format}"
        plt.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {save_fig_path}.")
    
    # Display figure
    if display_fig == True:
        plt.show()

def plot_solubility_swelling_all_temps(
    data_path, 
    types=['exp', 'SW', 'SAFT'],
    width=5., height=3.5,
    x_lo=0., y_lo=0., 
    colour='black', symbols=['s', 'o', 'v'], linestyle='None', markerfacecolor='None',
    alpha_zoom=0.,
    display_legend=True, display_fig=True, save_fig=True, folder_to_save ='../figures', save_format='pdf', dpi=400):
    
    # Check if the provided types are valid
    allowed_types = ['SAFT', 'exp', 'SW']
    if not all(t in allowed_types for t in types):
        raise ValueError(f"Invalid type(s) '{types}'. Allowed types are: {allowed_types}")
    
    T_celsius_values=[25, 35, 50]
    
    barToMPa = 1e-1

    df = {} # empty dict to store values
    
    # Reading data from Excel file
    for type in types:
        df[type] = pd.read_excel(data_path, sheet_name=f'{type}')
    
    # Plotting
    fig = plt.figure(figsize=(width, height), constrained_layout=True)
    # Create subplots
    n_col=2
    n_row=3
    ax1a = fig.add_subplot(n_row, n_col, 1)
    ax1b = fig.add_subplot(n_row, n_col, 2)
    ax2a = fig.add_subplot(n_row, n_col, 3)
    ax2b = fig.add_subplot(n_row, n_col, 4)
    ax3a = fig.add_subplot(n_row, n_col, 5)
    ax3b = fig.add_subplot(n_row, n_col, 6)
    axs = [ax1a, ax1b, ax2a, ax2b, ax3a, ax3b]
    axs_groups = [[ax1a, ax1b], [ax2a, ax2b], [ax3a, ax3b]]
    title_groups = [['(a)', '(b)'], ['(c)', '(d)'], ['(e)', '(f)']]
    titles = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']
    legend_dict={'SAFT':'SAFT', 'exp':'Exp.', 'SW':'SW'}

    for i, (T_celsius, ax_pair, title_pair) in enumerate(zip(T_celsius_values, axs_groups, title_groups)):
        axa, axb = ax_pair
        title_a, title_b = title_pair
        for j, type in enumerate(types):
            df_temp = df[type].loc[df[type]['T / °C'] == T_celsius].copy()
            
            # Plot solubility
            axa.plot(df_temp['p / bar'] * barToMPa, df_temp['q_sc / g/g_overall'],
                color = colour, marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor, label=legend_dict[type])
            # axa.errorbar(df_temp['p / bar'] * barToMPa, df_temp['q_sc / g/g_overall'],
            #              yerr=df_temp['u_c(q_sc) / g/g'],
            #     color = colour, marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor, label=legend_dict[type])
            
            # Plot swelling
            axb.plot(df_temp['p / bar'] * barToMPa, df_temp['SR / m3/m3'],
                color = colour, marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor, label=legend_dict[type])
            
            # Add title to the top plot
            axa.set_title(title_a + f' {T_celsius:.0f} °C')
            axb.set_title(title_b + f' {T_celsius:.0f} °C')
            
            # Configure axis limits
            if x_lo is not None:
                axa.set_xlim(left=x_lo)
                axb.set_xlim(left=x_lo)
                # axa.set_xlim(left=x_lo, right=25)
                # axb.set_xlim(left=x_lo, right=25)
            if y_lo is not None:
                axa.set_ylim(bottom=y_lo)
                axb.set_ylim(bottom=y_lo)
            
            # Display legend
            if display_legend:
                axa.legend().set_visible(True)
                axb.legend().set_visible(True)   
        
                # Add inset only for 35°C plots (ax2a and ax2b)
        if T_celsius == 35:
            # Create inset for ax2a (solubility)
            axins_a = axa.inset_axes([0.60, 0.25, 0.35, 0.35])  # [x, y, width, height]
            for j, type in enumerate(types):
                mask = df[type]['T / °C'] == T_celsius
                axins_a.plot(df[type][mask]['p / bar']*barToMPa, df[type][mask]['q_sc / g/g_overall'],
                      color=colour, marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor)
            
            x1, x2, y1, y2 = 0, 10.0, 0.0, 0.020
            axins_a.set_xlim(x1, x2)
            axins_a.set_ylim(y1, y2)
            axa.indicate_inset_zoom(axins_a, alpha=alpha_zoom)
            
            # Create inset for ax2b (swelling)
            axins_b = axb.inset_axes([0.60, 0.25, 0.35, 0.35])
            for j, type in enumerate(types):
                mask = df[type]['T / °C'] == T_celsius
                axins_b.plot(df[type][mask]['p / bar']*barToMPa, df[type][mask]['SR / m3/m3'],
                      color=colour, marker=symbols[j], linestyle=linestyle, markerfacecolor=markerfacecolor)

            x1, x2, y1, y2 = 0, 10.0, 0.0, 0.020
            axins_b.set_xlim(x1, x2)
            axins_b.set_ylim(y1, y2)
            axb.indicate_inset_zoom(axins_b, alpha=alpha_zoom)
    #------------------------------- 
    # INSET
    #-------------------------------
    # # ax2a
    # axins2a = ax2a.inset_axes([0.55, 0.15, 0.4, 0.4])  # [x, y, width, height]
    # for i, type in enumerate(types):
    #     mask = df[type]['T / °C'] == 35 
    #     axins2a.plot(df[type][mask]['p / bar']*barToMPa, df[type][mask]['q_sc / g/g_overall'],
    #             color = colour, marker=symbols[i], linestyle=linestyle, markerfacecolor=markerfacecolor)

    # x1, x2, y1, y2 = 0, 8.0, 0.0, 0.020
    # axins2a.set_xlim(x1, x2)
    # axins2a.set_ylim(y1, y2)
    # ax2a.indicate_inset_zoom(axins2a)
    
    # # ax2b
    # axins2b = ax2b.inset_axes([0.55, 0.15, 0.4, 0.4])  # [x, y, width, height]
    # for i, type in enumerate(types):
    #     mask = df[type]['T / °C'] == 35 
    #     axins2b.plot(df[type][mask]['p / bar']*barToMPa, df[type][mask]['SR / m3/m3'],
    #             color = colour, marker=symbols[i], linestyle=linestyle, markerfacecolor=markerfacecolor)

    # x1, x2, y1, y2 = 0, 8.0, 0.0, 0.015
    # axins2b.set_xlim(x1, x2)
    # axins2b.set_ylim(y1, y2)
    # ax2b.indicate_inset_zoom(axins2b)



    # Configuring the plots
    for ax_pair in zip([ax1a, ax2a, ax3a], [ax1b, ax2b, ax3b]):
        axa, axb = ax_pair
        axa.set_ylabel(r'$q_{\mathrm{sc}}$ / $\mathrm{g \, g^{-1}}$')
        axb.set_ylabel(r'$SR$')
    
    ax3a.set_xlabel(r'$p$ / MPa')
    ax3b.set_xlabel(r'$p$ / MPa')

    # Save figure
    if save_fig == True:
        save_fig_path = folder_to_save + f"/fig_solubility_swelling.{save_format}"
        plt.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {save_fig_path}.")
    
    # Display figure
    if display_fig == True:
        plt.show()

        

# def plot_solubility_swelling_all_temps(data_path, type='SAFT',
#                             width=5., height=3.5,                 
#                             linecolour='black', linestyle='None', symbol='o', markerfacecolor='None',
#                             alpha_zoom=0.8,
#                             display_fig=True, save_fig=False, folder_to_save ='../figures', save_format='pdf', dpi=1200):
    
#     allowed_types = ['SAFT', 'exp', 'SW']
#     if type not in allowed_types:
#         raise ValueError(f"Invalid type '{type}'. Allowed types are: {allowed_types}")
    
#     T_celsius_values=[25, 35, 50]
    
#     barToMPa = 1e-1

#     df_main = pd.read_excel(data_path, sheet_name='SAFT')
    
#     df = {} # empty dict to store values by temperature
#     for T in T_celsius_values:
#         df[T] = df_main.loc[df_main['T / °C'] == T].copy()
        
#     # Plotting
#     fig = plt.figure(figsize=(width, height), constrained_layout=True)
#     n_row=2
#     n_col=3
#     gs = gridspec.GridSpec(n_row, n_col, height_ratios=[1, 1], hspace=0, wspace=0.4) 
    
    
#     ax1a = fig.add_subplot(gs[0])
#     ax2a = fig.add_subplot(gs[1])
#     ax3a = fig.add_subplot(gs[2])
#     ax1b = fig.add_subplot(gs[3], sharex=ax1a)
#     ax2b = fig.add_subplot(gs[4], sharex=ax2a)
#     ax3b = fig.add_subplot(gs[5], sharex=ax3a)

#     axsa = [ax1a, ax2a, ax3a]  
#     axsb = [ax1b, ax2b, ax3b]  
#     titlesa = ['(a)', '(b)', '(c)']
#     titlesb = ['(d)', '(e)', '(f)']

#     for i, (T, axa, axb, titlea, titleb) in enumerate(zip(T_celsius_values, axsa, axsb, titlesa, titlesb)):
#         # Plotting the solubility and swelling data
#         axa.plot(df[T]['p / bar']*barToMPa, df[T]['q_sc / g/g_overall'],
#                    color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)
#         axb.plot(df[T]['p / bar']*barToMPa, df[T]['SR / m3/m3'],
#                    color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)

#         # Configuring the plots
#         axa.set_xlim(left=0)
#         axb.set_xlim(left=0)

#         # Add labels
#         # axa.set_ylabel(r'$q_{\mathrm{sc}}$ / $g \, g^{-1}$')
#         # axa.set_xlabel(r'$p$ / MPa')
#         # axb.set_ylabel(r'$SR$ / $\mathrm{cm^{-3} \, cm^{-3}}$')
#         # axb.set_xlabel(r'$p$ / MPa')

#         # Add title to the top plot
#         axa.set_title(titlea + f' {T:.0f} °C')
#         # axb.set_title(titleb + f' {T:.0f} °C')
        
#         # # Hide x-ticks for the top plot to prevent overlap
#         plt.setp(axa.get_xticklabels(), visible=False)
        
#         # Hide x-ticks for the top plot to prevent overlap
#         # axa.set_xticklabels([])

#         # Reduce number of vertical ticks
#         # axa.locator_params(axis='y', nbins=4)
#         # axb.locator_params(axis='y', nbins=4)
    
#     #------------------------------- 
#     # INSET
#     #-------------------------------
#     # ax2a
#     axins2a = ax2a.inset_axes([0.55, 0.55, 0.4, 0.4])  # [x, y, width, height]
#     axins2a.plot(df[35]['p / bar']*barToMPa, df[35]['q_sc / g/g_overall'],
#                 color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)

#     x1, x2, y1, y2 = 0, 2.0, 0.0, 0.02
#     axins2a.set_xlim(x1, x2)
#     axins2a.set_ylim(y1, y2)
#     axins2a.set_xticklabels('')
#     axins2a.set_yticklabels('')
#     ax2a.indicate_inset_zoom(axins2a, alpha=alpha_zoom)
    
#     # ax3a
#     axins3a = ax3a.inset_axes([0.55, 0.55, 0.4, 0.4])  # [x, y, width, height]
#     axins3a.plot(df[50]['p / bar']*barToMPa, df[50]['q_sc / g/g_overall'],
#                 color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)

#     x1, x2, y1, y2 = 0, 2.0, 0.0, 0.01
#     axins3a.set_xlim(x1, x2)
#     axins3a.set_ylim(y1, y2)
#     axins3a.set_xticklabels('')
#     axins3a.set_yticklabels('')
#     ax3a.indicate_inset_zoom(axins3a, alpha=alpha_zoom)
    
#     # ax2b
#     axins2b = ax2b.inset_axes([0.55, 0.55, 0.4, 0.4])  # [x, y, width, height]
#     axins2b.plot(df[35]['p / bar']*barToMPa, df[35]['SR / m3/m3'],
#                 color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)

#     x1, x2, y1, y2 = 0, 2.0, 0.0, 0.02
#     axins2b.set_xlim(x1, x2)
#     axins2b.set_ylim(y1, y2)
#     axins2b.set_xticklabels('')
#     axins2b.set_yticklabels('')
#     ax2b.indicate_inset_zoom(axins2b, alpha=alpha_zoom)

#     # ax3b
#     axins3b = ax3b.inset_axes([0.55, 0.55, 0.4, 0.4])  # [x, y, width, height]
#     axins3b.plot(df[50]['p / bar']*barToMPa, df[50]['SR / m3/m3'],
#                 color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)
    
#     x1, x2, y1, y2 = 0, 2.0, 0.0, 0.01
#     axins3b.set_xlim(x1, x2)
#     axins3b.set_ylim(y1, y2)
#     axins3b.set_xticklabels('')
#     axins3b.set_yticklabels('')
#     ax3b.indicate_inset_zoom(axins3b, alpha=alpha_zoom)

#     #-------------------------------
#     # CONFIGURING THE PLOTS
#     #-------------------------------
#     # Labels
#     ax1a.set_ylabel(r'$q_{\mathrm{sc}}$ / $\mathrm{g \, g^{-1}}$')    
#     ax1b.set_ylabel(r'$SR$ / $\mathrm{cm^{-3} \, cm^{-3}}$')
    
#     ax1b.set_xlabel(r'$p$ / MPa')
#     ax2b.set_xlabel(r'$p$ / MPa')
#     ax3b.set_xlabel(r'$p$ / MPa')

#     # Ticks
#     ax1a.set_xlim(left=0, right=6)
#     ax1b.set_xlim(left=0, right=6)
#     ax2a.set_xlim(left=0, right=30)
#     ax2b.set_xlim(left=0, right=30)
#     ax3a.set_xlim(left=0, right=30)
#     ax3b.set_xlim(left=0, right=30)
    
#     ax1a.set_ylim(0, 0.015)
#     ax2a.set_ylim(0, 0.3)  
#     ax3a.set_ylim(0, 0.08)
#     ax1b.set_ylim(0, 0.012)
#     ax2b.set_ylim(0, 0.35)
#     ax3b.set_ylim(0, 0.07)

#     # Format y-axis ticks to be more compact
#     # for ax in [ax1a, ax2a, ax3a, ax1b, ax2b, ax3b]:
#     #     ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    
#     # Save figure
#     if save_fig == True:
#         save_fig_path = folder_to_save + f"/fig_solubility_swelling.{save_format}"
#         plt.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
#         print(f"Plot successfully exported to {save_fig_path}.")
    
#     # Display figure
#     if display_fig == True:
#         plt.show()


if __name__ == "__main__":
    # Example usage
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # figure style
    plt.style.use('seaborn-v0_8-colorblind')
    plt.style.use('../../../../thesis.mplstyle')

    # Figure sizes
    cmToInch = 1/2.54
    text_width = 14.2  # cm
    base_height = 5.  # cm
    dpi = 400
    format = 'pdf'
    wh_ratio = 4/3
    width = text_width * cmToInch
    height = 3.3* base_height * cmToInch
    plot_solubility_swelling_all_temps(data_path='../data/sorption_isotherm_data.xlsx',
                                #    types=['exp', 'SW', 'SAFT'],
                                    types=['SW', 'SAFT', 'exp'],
                                   symbols=['o', 'v', 's'],
                                   width=width, height=height,
                                   display_legend=True, display_fig=True, save_fig=True)