import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

class PassengersDistance:
    def __init__(self):
        self.df = None  # Initialize df as None

    def set_data(self, data_processor):
        self.df = data_processor.df

    def distance_vs_passengers(self):
        """
        Create a scatter plot of distance vs. passengers.

        Returns
        -------
        None
        """
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df['Distance'], self.df['Passengers'], alpha=0.5)
        plt.title('Distance vs. Passengers Scatter Plot')
        plt.xlabel('Distance')
        plt.ylabel('Passengers')
        plt.show()

    def distance_vs_passengers_seaborn(self):
        """
        Create a Seaborn scatter plot of distance vs. passengers.

        Returns
        -------
        None
        """
        sns.set(style='whitegrid', context='notebook', palette='dark')
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df, x='Distance', y='Passengers', alpha=0.5)
        plt.xlabel('Distance')
        plt.ylabel('Passengers')
        plt.title('Distance vs. Passengers Scatter Plot')
        sns.regplot(data=self.df, x='Distance', y='Passengers', scatter=False, color='red')
        plt.show()
    
    def passengers_distance_matplotlib(self):
        """
        Create a scatter plot of seat occupancy vs. flight distance using Matplotlib.

        Returns
        -------
        None
        """
        plt.scatter(self.df['Distance'], self.df['Seat_Occupancy_new'], alpha=0.5)
        plt.title('Seat Occupancy vs. Flight Distance')
        plt.xlabel('Distance (Miles)')
        plt.ylabel('Seat Occupancy')
        plt.ylim(0, 2)  # Set the y-axis range to be between 0 and 2
        plt.show()

    def passengers_distance_seaborn(self):
        """
        Create a scatter plot of seat occupancy vs. flight distance using Seaborn.

        Returns
        -------
        None
        """
        # Set a professional style for the plot
        sns.set(style='whitegrid', context='notebook', palette='dark')

        # Create the scatter plot
        plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
        sns.scatterplot(data=self.df, x='Distance', y='Seat_Occupancy_new', alpha=0.5)

        # Set labels and title
        plt.xlabel('Distance (Miles)')
        plt.ylabel('Seat Occupancy')
        plt.title('Seat Occupancy vs. Flight Distance')

        # Set the y-axis range to be between 0 and 2
        plt.ylim(0, 2)

        plt.show()
