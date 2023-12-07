"""
Importing required libraries
"""
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

"""
Creating a class named analysis to define all the functions
"""
class Analysis:
    def __init__(self):
        self.df = None  # Initialize df as None

    def set_data(self, data_processor):
        self.df = data_processor.df

    def top_routes(self):
        """
        Find and print the top routes by total passengers.

        This method identifies and prints the top routes based on the total number of passengers.
        """
        # Combining Origin and Destination columns to create a 'Route' column
        self.df['Route'] = self.df['Origin'] + ' to ' + self.df['Destination']
        top_routes = self.df.groupby('Route')['Passengers'].sum().sort_values(ascending=False)
        print(top_routes)
    
    def top_city_routes(self):
        """
        Find and print the top city-to-city routes by total passengers.

        This method identifies and prints the top city-to-city routes based on the total number of passengers.
        """
        # Combining Origin City and Destination City columns to create a 'City_Route' column
        self.df['City_Route'] = self.df['Origin_City'] + ' to ' + self.df['Destination_City']
        top_city_routes = self.df.groupby('City_Route')['Passengers'].sum().sort_values(ascending=False)
        print(top_city_routes)
        
    def top_state_routes(self):
        """
        Find and print the top state-to-state routes by total passengers.

        This method identifies and prints the top state-to-state routes based on the total number of passengers.
        """
        # Combining Origin State and Destination State columns to create a 'State_Route' column
        self.df['State_Route'] = self.df['Origin_State'] + ' to ' + self.df['Destination_State']
        top_state_routes = self.df.groupby('State_Route')['Passengers'].sum().sort_values(ascending=False)
        print(top_state_routes)

    def monthly_passengers(self):
        """
        Calculate and return the monthly passenger trends.

        Returns
        -------
        pandas.Series
            Monthly passenger trends.
        """
        monthly_passengers = self.df.groupby('Month')['Passengers'].mean().sort_values(ascending=False)
        return monthly_passengers

    def flights_per_route(self):
        """
        Calculate and return the number of flights per route.

        Returns
        -------
        pandas.Series
            Number of flights per route.
        """
        flights_per_route = self.df['Route'].value_counts()
        return flights_per_route

    def airports(self):
        """
        Top and bottom airports by passenger count.
        """
        # Combine Origin and Destination columns to create an 'Airport' column
        self.df['Airport'] = self.df['Origin']
        top_airports = self.df.groupby('Airport')['Passengers'].sum().sort_values(ascending=False).head(10)
        bottom_airports = self.df.groupby('Airport')['Passengers'].sum().sort_values().head(10)
        print("Top Airports:")
        print(top_airports)
        print("\nBottom Airports:")
        print(bottom_airports)
        
    def state_passenger_data(self):
        """
        Top states by passenger count.
        """
        state_passenger_data = self.df.groupby('Origin_State')['Passengers'].sum().sort_values(ascending=False)
        print("Top States by Passenger Count:")
        print(state_passenger_data)