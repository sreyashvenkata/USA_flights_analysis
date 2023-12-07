import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

class GeoPlot:
    def __init__(self):
        self.df = None  # Initialize df as None
        self.df_airports = None  # Initialize df_airports as None

    def set_data(self, data_processor):
        self.df = data_processor.df

    def set_airport_data(self, df_airports):
        self.df_airports = df_airports

    def plot_airports_on_map(self):
        """
        Plot airport locations on a world map.

        Returns
        -------
        None
        """
        if self.df is None or self.df_airports is None:
            print("DataFrame or airport data is not set. Please set the dataframes using set_data and set_airport_data methods.")
            return

        # Merge self.df with self.df_airports based on relevant columns
        merged_df = pd.merge(self.df, self.df_airports, left_on='Origin', right_on='IATA Code', how='left')

        # Create a GeoDataFrame from the merged DataFrame
        geometry = [Point(xy) for xy in zip(merged_df['Longitude Decimal Degrees'], merged_df['Latitude Decimal Degrees'])]
        gdf = gpd.GeoDataFrame(merged_df, geometry=geometry, crs="EPSG:4326")

        # Get world map data
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

        # Plot the world map
        ax = world.plot(figsize=(10, 6), color='lightgrey')

        # Plot the airport locations
        gdf.plot(ax=ax, color='red', markersize=10)

        # Add labels
        for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf['IATA Code']):
            ax.text(x, y, label, fontsize=8)

        # Show the map
        plt.show()
