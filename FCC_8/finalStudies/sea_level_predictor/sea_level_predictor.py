import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_data = pd.read_csv('C:/Users/catte/Dropbox/Tech Learning/GitHub/FreeCodeCamp/FCC_8/finalStudies/sea_level_predictor/epa-sea-level.csv')

    # Create scatter plot


    # Create first line of best fit


    # Create second line of best P


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()
