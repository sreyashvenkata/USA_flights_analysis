import pandas as pd

class DataSubsetting:
    def __init__(self, data_path):
        """
        Initialize the DataProcessing instance.

        Parameters
        ----------
        data_path : str
            Path to the data file.
        """
        self.df = pd.read_csv(data_path, delimiter='\t', header=None)

    def data_subsetting(self, output_path='subset_data_2000_2005.csv'):
        """
        Perform data subsetting for the years 2000 to 2005 using column 9 (Fly_Date)
        and save the subset as a CSV file.

        Parameters
        ----------
        output_path : str, optional
            Path to save the subset data CSV file. Default is 'subset_data_2000_2005.csv'.

        Returns
        -------
        None
        """
        # Extract the first four digits of 'Fly Date' as integers
        self.df['Year'] = self.df.iloc[:, 8].astype(str).str[:4].astype(int)

        # Filter the DataFrame for the years 2000 to 2005
        subset_df = self.df[(self.df['Year'] >= 2000) & (self.df['Year'] <= 2005)]

        # Drop the temporary 'Year' column
        subset_df = subset_df.drop(columns=['Year'])

        # Save the subset DataFrame to a new CSV file
        subset_df.to_csv(output_path, index=False, header=False)
