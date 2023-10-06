import wx
from Feature1 import data_processing
import pandas as pd
import wx.grid as gridlib
from PriceDistribution import PriceDistribution

class DataEntryWindow(wx.Frame):
    def __init__(self, parent, title, selected_file_path):
        super(DataEntryWindow, self).__init__(parent, title=title, size=(800, 600))
        self.selected_file_path = selected_file_path

        # Create a panel to hold the widgets
        panel = wx.Panel(self)

        # Create labels and text boxes for data entry
        neighborhood_label = wx.StaticText(panel, label="Enter the neighborhood name:")
        self.neighborhood_text = wx.TextCtrl(panel)

        start_date_label = wx.StaticText(panel, label="Enter the start date (YYYY-MM-DD):")
        self.start_date_text = wx.TextCtrl(panel)

        end_date_label = wx.StaticText(panel, label="Enter the end date (YYYY-MM-DD):")
        self.end_date_text = wx.TextCtrl(panel)

        # Create an error message label
        self.error_label = wx.StaticText(panel, label="", style=wx.ALIGN_CENTER)
        self.error_label.SetForegroundColour(wx.Colour(255, 0, 0))  # Set text color to red
        self.error_label.Hide()  # Initially hide the error label

        # Create a result grid for displaying the report as a table
        self.result_grid = gridlib.Grid(panel)
        self.result_grid.Hide()  # Initially hide the grid

        # Create a button to submit the data
        submit_button = wx.Button(panel, label="Submit")
        submit_button.Bind(wx.EVT_BUTTON, self.on_submit_button_click)

        # Create a vertical sizer to organize the widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(neighborhood_label, 0, wx.ALL, 10)
        sizer.Add(self.neighborhood_text, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(start_date_label, 0, wx.ALL, 10)
        sizer.Add(self.start_date_text, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(end_date_label, 0, wx.ALL, 10)
        sizer.Add(self.end_date_text, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(self.error_label, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(self.result_grid, 1, wx.ALL | wx.EXPAND, 10)
        sizer.Add(submit_button, 0, wx.ALL | wx.CENTER, 10)

        # Set the sizer for the panel
        panel.SetSizer(sizer)

    def on_submit_button_click(self, event):
        target_neighborhood = self.neighborhood_text.GetValue()
        start_date = self.start_date_text.GetValue()
        end_date = self.end_date_text.GetValue()

        # Check if the entered dates are valid
        try:
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)

            if start_date > end_date:
                raise ValueError("Start date cannot be greater than end date.")

            # Call the data processing function from the data_processing module
            report = data_processing(self.selected_file_path, target_neighborhood, start_date, end_date)
            
            # Check if the report is a string (indicating an error)
            if isinstance(report, str):
                self.error_label.SetLabel(f"Error: {report}")
                self.error_label.Show()
                self.result_grid.Hide()
                self.Layout()
            else:
                # Display the report as a table in the grid
                self.result_grid.CreateGrid(len(report), len(report.columns))
                for i, col in enumerate(report.columns):
                    self.result_grid.SetColLabelValue(i, col)
                    for j, value in enumerate(report[col]):
                        self.result_grid.SetCellValue(j, i, str(value))
                self.result_grid.AutoSizeColumns()
                self.error_label.Hide()
                self.result_grid.Show()
                self.Layout()  # Update the layout to show the labels or grid

        except ValueError as input_error:
            self.error_label.SetLabel(f"Input Error: {input_error}")
            self.error_label.Show()
            self.result_label.Hide()
            self.result_grid.Hide()
            self.Layout()  # Update the layout to show the labels


class HomePage(wx.Frame):
    def __init__(self, parent, title):
        super(HomePage, self).__init__(parent, title=title, size=(400, 300))

        # Create a panel to hold the widgets
        panel = wx.Panel(self)

        # Create four buttons
        button1 = wx.Button(panel, label="Feature 1")
        button2 = wx.Button(panel, label="Feature 2")
        button3 = wx.Button(panel, label="Feature 3")
        button4 = wx.Button(panel, label="Feature 4")

        # Bind the "Feature 1" button to a function
        button1.Bind(wx.EVT_BUTTON, self.on_feature1_button_click)

        # Bind the "Feature 2" button to a function
        button2.Bind(wx.EVT_BUTTON, self.on_feature2_button_click)

        # Create a vertical sizer to organize the widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button1, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(button2, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(button3, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(button4, 0, wx.ALL | wx.CENTER, 10)

        # Set the sizer for the panel
        panel.SetSizer(sizer)

        # Center the frame on the screen
        self.Center()

    def on_feature1_button_click(self, event):
        # Create a file dialog to select a CSV file
        wildcard = "CSV files (*.csv)|*.csv"
        dialog = wx.FileDialog(self, "Select a CSV file", wildcard=wildcard, style=wx.FD_OPEN)

        if dialog.ShowModal() == wx.ID_OK:
            # Get the selected file path
            selected_file_path = dialog.GetPath()

            # Create and show the data entry window
            data_entry_window = DataEntryWindow(self, "Data Entry", selected_file_path)
            data_entry_window.Show()

        dialog.Destroy()
    
    def on_feature2_button_click(self, event):
        # Create a file dialog to select a CSV file
        wildcard = "CSV files (*.csv)|*.csv"
        dialog = wx.FileDialog(self, "Select a CSV file", wildcard=wildcard, style=wx.FD_OPEN)

        if dialog.ShowModal() == wx.ID_OK:
            # Get the selected file path
            selected_file_path = dialog.GetPath()

            # Create and show the PriceDistribution window
            price_distribution_window = PriceDistribution(self, "Price Distribution", selected_file_path)
            price_distribution_window.Show()

        dialog.Destroy()

def main():
    app = wx.App(False)
    frame = HomePage(None, "Home Page")
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
