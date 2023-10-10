import pandas as pd
import wx
import wx.adv
import matplotlib.pyplot as plt

class OccupancyRateTrends(wx.Frame):
    def __init__(self, parent, title):
        super(OccupancyRateTrends, self).__init__(parent, title=title, size=(435, 291))

        panel = wx.Panel(self)

        self.startDatePicker = wx.adv.DatePickerCtrl(panel, wx.ID_ANY, style=wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN)
        self.endDatePicker = wx.adv.DatePickerCtrl(panel, wx.ID_ANY, style=wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN)
        uploadButton = wx.Button(panel, label="Upload CSV File")
        uploadButton.Bind(wx.EVT_BUTTON, self.onUploadButtonClick)
        generateButton = wx.Button(panel, label="Generate Occupancy Rate Trends")
        generateButton.Bind(wx.EVT_BUTTON, self.onGenerateButtonClick)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(uploadButton, 0, wx.ALL, 10)
        sizer.Add(self.startDatePicker, 0, wx.ALL, 10)
        sizer.Add(self.endDatePicker, 0, wx.ALL, 10)
        sizer.Add(generateButton, 0, wx.ALL, 10)

        panel.SetSizer(sizer)
        self.Center()

        self.data_file = None

    def onUploadButtonClick(self, event):
        wildcard = "CSV files (*.csv)|*.csv"
        dialog = wx.FileDialog(self, "Choose a file", wildcard=wildcard, style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_CANCEL:
            return
        self.data_file = dialog.GetPath()
        dialog.Destroy()

    def calculateOccupancyRates(self, startDate, endDate):
        try:
            df = pd.read_csv(self.data_file)
            uniqueSuburbs = df.loc[(df['first_review'] >= startDate) & (df['last_review'] <= endDate), 'neighbourhood_cleansed'].unique()
            occupancyRates = []
            for suburb in uniqueSuburbs:
                totalNights = df.loc[df['neighbourhood_cleansed'] == suburb, ['availability_30', 'availability_60', 'availability_90', 'availability_365']].sum().sum()
                bookedNights = df.loc[df['neighbourhood_cleansed'] == suburb, 'reviews_per_month'].sum()
                occupancyRate = (bookedNights / totalNights) * 100
                occupancyRates.append(occupancyRate)
            return uniqueSuburbs, occupancyRates
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return [], []

    def onGenerateButtonClick(self, event):
        if self.data_file:
            startDate = self.startDatePicker.GetValue().FormatISODate()
            endDate = self.endDatePicker.GetValue().FormatISODate()
            suburbs, occupancyRates = self.calculateOccupancyRates(startDate, endDate)
            occupancyRatesPercentage = [rate * 100 for rate in occupancyRates]
            plt.figure(figsize=(12, 6))
            plt.bar(suburbs, occupancyRatesPercentage, color='skyblue')
            plt.xlabel('Suburb')
            plt.ylabel('Occupancy Rate (%)')
            plt.title('Occupancy Rate Trends for Different Suburbs')
            plt.ylim(0, 100)
            plt.tight_layout()
            plt.xticks(rotation=45)
            plt.show()
        else:
            self.showErrorMessageBox("Error: Please upload a CSV file.")

    def showErrorMessageBox(self, message):
        wx.LogError(message)

def main():
    app = wx.App(False)
    frame = OccupancyRateTrends(None, "Generate Occupancy Rate Trends Graph")
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
