import wx
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class PriceDistribution(wx.Frame):
    def __init__(self, parent, title, selected_file_path):
        super(PriceDistribution, self).__init__(parent, title=title, size=(800, 600))
        self.selected_file_path = selected_file_path

        # Create a panel to hold the widgets
        panel = wx.Panel(self)

        # Create text controls for start date and end date
        price_start_date = wx.StaticText(panel, label="Enter the start date (YYYY-MM-DD):")
        self.price_start_date_text = wx.TextCtrl(panel)
        
        price_end_date = wx.StaticText(panel, label="Enter the end date (YYYY-MM-DD):")
        self.price_end_date_text = wx.TextCtrl(panel)

        # Create a button to calculate and display the price distribution
        calculate_button = wx.Button(panel, label="Show the Distribution")
        calculate_button.Bind(wx.EVT_BUTTON, self.calculate_and_display_distribution)

        # Create a vertical sizer to organize the widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(price_start_date, 0, wx.ALL, 10)
        sizer.Add(self.price_start_date_text, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(price_end_date, 0, wx.ALL, 10)
        sizer.Add(self.price_end_date_text, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(calculate_button, 0, wx.ALL | wx.CENTER, 10)

        # Set the sizer for the panel
        panel.SetSizer(sizer)

    def calculate_and_display_distribution(self, event):
        # Load the dataset
        data_df = self.load_dataset(self.selected_file_path)

        # Check if the dataset was loaded successfully
        if data_df is None:
            self.show_error_message("Error: Unable to load the dataset.")
            return

        # Preprocess the data
        data_df = self.preprocess_data(data_df)

        # Check if the data was preprocessed successfully
        if data_df is None:
            self.show_error_message("Error: Unable to preprocess the data.")
            return

        # Get start and end dates from text input fields
        start_date_str = self.price_start_date_text.GetValue()
        end_date_str = self.price_end_date_text.GetValue()

        # Validate and convert start and end dates to datetime
        try:
            start_date = pd.to_datetime(start_date_str)
            end_date = pd.to_datetime(end_date_str)
        except ValueError:
            self.show_error_message("Error: Invalid date format.")
            return

        # Check if start_date is before or equal to end_date
        if start_date > end_date:
            self.show_error_message("Error: Start date should be before or equal to end date.")
            return

        # Filter data by date range
        selected_data = self.filter_data_by_date(data_df, start_date, end_date)

        # Check if there's data in the selected range
        if selected_data is None or selected_data.empty:
            self.show_error_message("Error: No data available in the selected date range.")
            return

        # Calculate and display the histogram in a separate window
        self.display_histogram(selected_data, start_date, end_date)

    def load_dataset(self, file_path):
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            return None

    def preprocess_data(self, df):
        if df is None:
            return None

        # Remove rows with missing values in the 'price' column
        df = df.dropna(subset=['price'])

        # Convert the 'date' column to datetime
        df['date'] = pd.to_datetime(df['date'])

        # Clean the 'price' column by removing dollar signs and commas, then convert to float
        df['price'] = df['price'].str.replace('$', '').str.replace(',', '').astype(float)

        return df

    def filter_data_by_date(self, df, start_date, end_date):
        if df is None:
            return None
        return df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    def display_histogram(self, data, start_date, end_date):

        graph_frame = wx.Frame(None, title="Price Distribution Graph", size=(1000, 800))

        # Create a Matplotlib figure
        figure = Figure(figsize=(8, 6))
        ax = figure.add_subplot(111)

        # Create a Matplotlib canvas
        canvas = FigureCanvas(graph_frame, -1, figure)

        # Center the frame on the screen
        graph_frame.Center()

        # Plot the histogram on the Matplotlib figure
        ax.hist(data['price'], bins=30, color='blue', alpha=0.7)
        ax.set_xlabel('Property Price (in AUD)')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Distribution of Property Prices ({start_date} to {end_date})')
        ax.grid(True)

        # Add the Matplotlib canvas to the graph_frame
        graph_frame.SetSizerAndFit(wx.BoxSizer(wx.VERTICAL))
        graph_frame.GetSizer().Add(canvas, 1, wx.EXPAND)

        # Show the graph frame
        graph_frame.Show()


    def show_error_message(self, message):
        wx.LogError(message)

if __name__ == '__main__':
    app = wx.App(False)
    frame = PriceDistribution(None, "Price Distribution", "your_selected_file.csv")
    frame.Show(True)
    app.MainLoop()
