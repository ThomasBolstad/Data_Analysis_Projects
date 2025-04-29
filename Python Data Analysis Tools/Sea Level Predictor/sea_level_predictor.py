import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

    # Create first line of best fit (1880 to 2050)
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_full = pd.Series(range(1880, 2051))
    y_pred_full = res_full.intercept + res_full.slope * x_pred_full
    ax.plot(x_pred_full, y_pred_full, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit (2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    ax.plot(x_pred_recent, y_pred_recent, 'green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()