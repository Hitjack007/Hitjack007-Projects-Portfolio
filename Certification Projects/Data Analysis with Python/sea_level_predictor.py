import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read the data from CSV
    df = pd.read_csv("epa-sea-level.csv")

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Original Data", alpha=0.6)

    # Perform linear regression on all data
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_all = pd.Series(range(1880, 2051))
    y_pred_all = res_all.intercept + res_all.slope * x_pred_all
    plt.plot(x_pred_all, y_pred_all, 'r', label='Fit: 1880–2050')

    # Perform linear regression on data from year 2000 onward
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, 'green', label='Fit: 2000–2050')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True)

    # Save the plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()
