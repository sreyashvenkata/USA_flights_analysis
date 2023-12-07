        # flight_model.py

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

class FlightModel:
    def __init__(self, data_processor):
        self.df = data_processor.df
        #self.model = None

    def preprocess_data(self):
        """
        Preprocess the data for the regression model.
        """
        # For simplicity, let's use only numerical features
        features = ['Distance', 'Seats', 'Flights', 'Origin Population', 'Destination Population']

        # Extract features and target variable
        X = self.df[features]
        y = self.df['Passengers']

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    def train_model(self):
        """
        Train a Linear Regression model.
        """
        X_train, X_test, y_train, y_test = self.preprocess_data()

        # Create and train the Linear Regression model
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

        # Predict on the test set
        y_pred = self.model.predict(X_test)

        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        print(f"Mean Squared Error: {mse}")

    def visualize_predictions(self):
        """
        Visualize the actual vs. predicted number of passengers.
        """
        if self.model is None:
            print("Model is not trained. Please train the model first.")
            return

        X_train, X_test, y_train, y_test = self.preprocess_data()

        # Predict on the test set
        y_pred = self.model.predict(X_test)

        # Visualize actual vs. predicted
        plt.scatter(y_test, y_pred)
        plt.xlabel("Actual Number of Passengers")
        plt.ylabel("Predicted Number of Passengers")
        plt.title("Actual vs. Predicted Number of Passengers")
        plt.show()

if __name__ == "__main__":
    from DataProcessing import DataProcessing  # Update with your actual import path

    # Example usage:
    data_processor = DataProcessing('https://raw.githubusercontent.com/sreyashvenkata/USA_flights_analysis/main/data/subset_data_2000_2005.csv')
    data_processor.data_wrangling()

    # Train and visualize the regression model
    model = FlightModel(data_processor)
    model.train_model()
    model.visualize_predictions()
