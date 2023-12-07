import numpy as np
import pandas as pd

class DataProcessing:
    def __init__(self, data_path):
        """
        Initialize the M6Project instance.

        Read the data file and convert it to a DataFrame.

        Parameters
        ----------
        data_path (str): Path to the data file.
        """
        self.df = pd.read_csv(data_path, delimiter=',', names=["Origin", "Destination", "Origin City","Destination City","Passengers","Seats","Flights","Distance","Fly Date","Origin Population","Destination Population"])
        print(self.df)

    def data_wrangling(self):
        """
        Perform data wrangling operations on the DataFrame.

        This method modifies the DataFrame in place.

        Returns
        -------
        Top 5 rows data
        """
        # Split the 'Origin' column into 'Origin City' and 'Origin State' columns
        self.df[['Origin_City', 'Origin_State']] = self.df['Origin City'].str.split(', ', expand=True)

        # Drop the original "Origin City" column if you no longer need it
        self.df = self.df.drop(columns=['Origin City'])
        
        # Split the 'Destination' column into 'Destination City' and 'Destination State' columns
        self.df[['Destination_City', 'Destination_State']] = self.df['Destination City'].str.split(', ', expand=True)

        # Drop the original 'Destination City' column if needed
        self.df = self.df.drop(columns=['Destination City'])
        
        # Convert the "Fly Date" column to a string
        self.df['Fly Date'] = self.df['Fly Date'].astype(str)

        # Extract year and month using string slicing
        self.df['Year'] = self.df['Fly Date'].str[:4]
        self.df['Month'] = self.df['Fly Date'].str[4:]

        # Convert the new columns to integers if needed
        self.df['Year'] = self.df['Year'].astype(int)
        self.df['Month'] = self.df['Month'].astype(int)

        # Drop the 'Fly Date' column
        self.df = self.df.drop(columns=['Fly Date'])
        print(self.df.head())

    def desired_order(self):
        """
        Rearrange DataFrame columns based on a desired order.

        Returns
        -------
        None
            This method reorders DataFrame columns based on a specified order.
        """
        # Define the desired column order
        desired_order = [
            'Origin', 'Origin_City', 'Origin_State',
            'Destination', 'Destination_City', 'Destination_State',
            'Year', 'Month',
            'Passengers', 'Seats', 'Flights', 'Distance',
            'Origin Population', 'Destination Population'
        ]

        # Reorder the DataFrame columns
        self.df = self.df[desired_order]
        print(self.df.head())

    def shape(self):
        """
        Get the shape and column data types of the DataFrame.

        Returns
        -------
        None
            This method prints the number of rows, columns, and data types of the DataFrame.
        """
        # Get the number of rows and columns in the dataset
        num_rows, num_columns = self.df.shape
        print(f"Number of Rows: {num_rows}")
        print(f"Number of Columns: {num_columns}")

        # List the column names and their data types
        column_data_types = self.df.dtypes
        print("Column Data Types:")
        print(column_data_types)

    def summary(self):
        """
        Display summary statistics for the DataFrame.

        Returns
        -------
        None
            This method prints summary statistics for the DataFrame.
        """
        # Set the float format for display
        pd.set_option('display.float_format', '{:.1f}'.format)

        # Get summary statistics
        summary_stats = self.df.describe()
        print(summary_stats)

    def unique_values(self):
        """
        Find unique values in categorical columns.

        This method identifies and prints unique values in non-numeric (categorical) columns of the DataFrame.

        Returns
        -------
        None
            This method prints unique values for each categorical column.
        """
        categorical_columns = self.df.select_dtypes(include=['object']).columns
        for column in categorical_columns:
            unique_values = self.df[column].unique()
            print(f"Unique values in '{column}': {unique_values}")