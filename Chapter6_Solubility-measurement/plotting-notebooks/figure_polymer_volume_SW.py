import pandas as pd
import matplotlib.pyplot as plt

def plot_polymer_volume_SW_vertical(
        data_path,
        width=5., height=3.5,
        linecolour='black', linestyle='None', symbol='o', markerfacecolor='None',
        display_fig=True, save_fig=False, folder_to_save ='../figures', save_format='pdf', dpi=400):
    
    T_celsius_values=[25, 35, 50]
    
    barToMPa = 1e-1
    m3ToCm3 = 1e6

    df_main = pd.read_excel(data_path, sheet_name='SW')
    
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
        ax.plot(df[T]['p / bar']*barToMPa, df[T]['Vp / m3/g'] * m3ToCm3, 
                color = linecolour, marker=symbol, linestyle=linestyle, markerfacecolor=markerfacecolor)
    
        # Configuring the plots
        ax.set_xlim(left=0)
        ax.set_title(title + f' {T:.0f} °C')
    
    #------------------------------- 
    # CONFIGURING THE PLOTS
    #-------------------------------
    # Labels
    ax1.set_ylabel(r'$\hat{V}_{\mathrm{p,am}}$ / $\mathrm{cm^3 \, g^{-1}}$')
    ax2.set_ylabel(r'$\hat{V}_{\mathrm{p,am}}$ / $\mathrm{cm^3 \, g^{-1}}$')
    ax3.set_ylabel(r'$\hat{V}_{\mathrm{p,am}}$ / $\mathrm{cm^3 \, g^{-1}}$')
    ax3.set_xlabel(r'$p$ / MPa')
    
    # Save figure
    if save_fig == True:
        save_fig_path = folder_to_save + f"/fig_polymer_volume_SW.{save_format}"
        plt.savefig(save_fig_path, dpi=dpi, bbox_inches='tight')
        print(f"Plot successfully exported to {save_fig_path}.")
    
    # Display figure
    if display_fig == True:
        plt.show()