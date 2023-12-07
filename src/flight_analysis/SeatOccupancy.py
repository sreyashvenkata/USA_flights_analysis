import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

class SeatOccupancy:
    def __init__(self):
        self.df = None  # Initialize df as None

    def set_data(self, data_processor):
        self.df = data_processor.df

    def seat_occupancy_year(self):
        """
        Seat occupancy trends over the years.

        Returns
        -------
        None
        """
        if self.df is None:
            print("DataFrame is not set. Please set the DataFrame using set_data method.")
            return
        self.df['Seat_Occupancy'] = self.df['Passengers'] / self.df['Seats']
        seat_occupancy_over_time = self.df.groupby('Year')['Seat_Occupancy'].mean()
        seat_occupancy_over_time.plot(kind='line')
        plt.title('Seat Occupancy Trends Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Average Seat Occupancy')
        plt.show()        

    def seat_occupancy_month(self):
        """
        Seat occupancy by month.

        Returns
        -------
        None
        """
        seat_occupancy_by_month = self.df.groupby('Month')['Seat_Occupancy'].mean()
        seat_occupancy_by_month.plot(kind='bar')
        plt.title('Seat Occupancy by Month')
        plt.xlabel('Month')
        plt.ylabel('Average Seat Occupancy')
        plt.show()        
        
    def route_seat_occupancy(self):
        """
        Average seat occupancy by route.

        Returns
        -------
        None
        """
        route_seat_occupancy = self.df.groupby('Route')['Seat_Occupancy'].mean().sort_values(ascending=False)
        print("Average Seat Occupancy by Route:")
        print(route_seat_occupancy)
        
    def Seat_Occupancy(self):
        """
        Sort rows by seat occupancy.

        Returns
        -------
        None
        """
        sorted_by_seat_occupancy = self.df.sort_values(by='Seat_Occupancy', ascending=False)
        print("Rows Sorted by Seat Occupancy:")
        print(sorted_by_seat_occupancy)
        
    def Examine_Seat_Occupancy(self):
        """
        Examine seat occupancy of a specific row and find rows with zero seats.

        Returns
        -------
        None
        """
        row_2801180 = self.df.loc[2801180]
        print("Details of Row 2801180:")
        print(row_2801180) 

        num_rows_with_zero_seats = len(self.df[self.df['Seats'] == 0])
        print("Number of Rows with Zero Seats:", num_rows_with_zero_seats)
        
    def Modify_Seat_Occupancy(self):
        """
        Replace zero seats with corresponding passengers in the DataFrame.

        Returns
        -------
        None
        """
        # Replace zero Seats with corresponding Passengers
        self.df['Seats'] = np.where(self.df['Seats'] == 0, self.df['Passengers'], self.df['Seats'])
        row_2801180 = self.df.loc[2801180]
        print("Details of Row 2801180 after Modification:")
        print(row_2801180)
        
    def Seat_Occupancy_new(self):
        """
        Calculate and display seat occupancy as a new column.

        Returns
        -------
        None
        """
        self.df['Seat_Occupancy_new'] = self.df['Passengers'] / self.df['Seats']
        sorted_by_seat_occupancy_new = self.df.sort_values(by='Seat_Occupancy_new', ascending=False)
        print("Rows Sorted by Seat Occupancy (New Column):")
        print(sorted_by_seat_occupancy_new)
        
    def Seat_Occupancy_new_year(self):
        """
        Seat occupancy trends with the new column over the years.

        Returns
        -------
        None
        """
        seat_occupancy_over_time = self.df.groupby('Year')['Seat_Occupancy_new'].mean()
        seat_occupancy_over_time.plot(kind='line')
        plt.title('Seat Occupancy Trends Over the Years (New Column)')
        plt.xlabel('Year')
        plt.ylabel('Average Seat Occupancy')
        plt.show()

    def Seat_Occupancy_new_month(self):
        """
        Seat occupancy by month using the new column.

        Returns
        -------
        None
        """
        seat_occupancy_by_month = self.df.groupby('Month')['Seat_Occupancy_new'].mean()
        seat_occupancy_by_month.plot(kind='bar')
        plt.title('Seat Occupancy by Month (New Column)')
        plt.xlabel('Month')
        plt.ylabel('Average Seat Occupancy')
        plt.show()