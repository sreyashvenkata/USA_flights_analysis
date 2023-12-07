import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

class Visualization:
    def __init__(self):
        self.df = None  # Initialize df as None

    def set_data(self, data_processor):
        self.df = data_processor.df

    def passenger_trends(self):
        if self.df is None:
            print("DataFrame is not set. Please set the DataFrame using set_data method.")
            return

        # Use self.df to create visualizations
        passenger_trends = self.df.groupby('Year')['Passengers'].sum()
        passenger_trends.plot(kind='line')
        plt.title('Trends in Passenger Numbers Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Total Passengers')
        plt.xticks(range(2000, 2005, 1))
        formatter = mtick.FuncFormatter(lambda x, _: f'{int(x / 1e6):,}M')
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.show()

    def passenger_trends_seaborn(self):
        """
        Plot trends in passenger numbers over the years using Seaborn.

        This method visualizes the trends in passenger numbers over the years using a Seaborn line plot.

        Returns
        -------
        None
        """
        plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
        sns.set(style="whitegrid", font_scale=1.2, palette="Set1")
        passenger_trends = self.df.groupby('Year')['Passengers'].sum().reset_index()
        plot = sns.lineplot(data=passenger_trends, x='Year', y='Passengers', marker='o')
        plt.title('Trends in Passenger Numbers Over the Years', fontsize=16)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Total Passengers (in millions)', fontsize=12)
        plt.xticks(range(2000, 2005, 1))
        formatter = mtick.FuncFormatter(lambda x, _: f'{int(x / 1e6):,}M')
        plot.yaxis.set_major_formatter(formatter)
        plt.show()

    def monthly_passengers_plot(self):
        """
        Create a line plot of monthly passenger trends.

        Returns
        -------
        None
        """
        monthly_passengers = self.df.groupby(['Year', 'Month'])['Passengers'].mean().unstack().T
        # Create the plot
        fig, ax = plt.subplots(figsize=(12, 6))

        # Plot the data for all years
        for year in range(2000, 2005):
            plt.plot(monthly_passengers.index, monthly_passengers[year], label=str(year))

        # Set plot labels and legend
        plt.title('Monthly Passenger Trends (2000-2005)')
        plt.xlabel('Month')
        plt.ylabel('Average Passengers')
        plt.xticks(monthly_passengers.index)
        plt.legend(title='Year', loc='upper right')

        # Show the plot
        plt.show()

    def monthly_passengers_seaborn(self):
        """
        Create a Seaborn line plot of monthly passenger trends.

        Returns
        -------
        None
        """
        # Calculate and compare monthly passenger trends for all years
        monthly_passengers = self.df.groupby(['Year', 'Month'])['Passengers'].mean().unstack().T

        # Set the Seaborn style
        sns.set(style='whitegrid')

        # Create the plot
        fig, ax = plt.subplots(figsize=(12, 6))

        # Plot the data for all years using Seaborn
        for year in range(2000, 2005):
            sns.lineplot(data=monthly_passengers, x=monthly_passengers.index, y=year, label=str(year))

        # Set plot labels and legend
        plt.title('Monthly Passenger Trends (2000-2005)')
        plt.xlabel('Month')
        plt.ylabel('Average Passengers')

        # Create a legend outside of the plot
        ax.legend(title='Year', loc='center left', bbox_to_anchor=(1, 0.5))

        # Show the plot
        plt.show()