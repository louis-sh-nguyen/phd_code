import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def plot_timelag_explanation(
    width=6., height=4.0,
    display_fig=True, save_fig=True, 
    folder_to_save='../figures', save_format='pdf', dpi=400):

    df = pd.read_csv('../data/timelag/RUN_H_25C-50bar/experimental_data_20250711-113053.csv')
    df = df.loc[df['time'] < 30e3].copy()

    fig=plt.figure(figsize=(width, height), constrained_layout=True)
    ax=fig.add_subplot(111)

    ax.plot(df['time'], df['cumulative_flux'], color='black', linestyle='solid', label='Exp.')

    # Fit linear line from last 5000 data points
    steady_data = df.tail(500)
    slope, intercept = np.polyfit(steady_data['time'], steady_data['cumulative_flux'], 1)
    steady_line = slope * steady_data['time'] + intercept

    # ax.plot(steady_data['time'], steady_line, color='grey', linestyle='dashed', alpha=0.7, )
    ax.set_xlabel('Time / s')
    ax.set_ylabel(r'Cumulative Flux / $\mathrm{cm^{3}(STP) \, cm^{-2}}$')
    # Find the x-intercept (time lag) by extending the steady-state line
    # y = mx + b, when y = 0: x = -b/m
    theta = -intercept / slope

    # Add vertical line at time lag
    # ax.axvline(x=theta, color='green', linestyle=':', linewidth=2)

    # Extend the steady-state line to show intersection with x-axis
    x_extended = np.linspace(theta, steady_data['time'].max(), 100)
    y_extended = slope * x_extended + intercept
    ax.plot(x_extended, y_extended, color='black', linestyle='dashed', label=f'Linear fit')

    # Add annotation for theta
    ax.annotate(r'$\theta$', xy=(theta, 0), xytext=(theta, -ax.get_ylim()[1]*0.1), 
                ha='center', va='bottom', fontsize=12, color='black')

    ax.set_xlim(0)
    ax.set_ylim(0)

    ax.set_xticks([])
    ax.set_yticks([])
    
    ax.legend(loc='upper left')
    
    if save_fig:
        os.makedirs(folder_to_save, exist_ok=True)
        filename = f"fig_timelag_explanation.{save_format}"
        filepath = os.path.join(folder_to_save, filename)
        fig.savefig(filepath, format=save_format, dpi=dpi, bbox_inches='tight')
        print(f"Figure saved to {filepath}")
    
    if display_fig:
        plt.show()
