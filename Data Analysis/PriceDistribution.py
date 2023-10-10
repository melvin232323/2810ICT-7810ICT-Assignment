import wx
import wx.adv
import pandas as pd
import matplotlib.pyplot as plt

class PriceDistribution(wx.Frame):
    def __init__(self, parent, title):
        super(PriceDistribution, self).__init__(parent, title=title, size=(500, 289))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.datePickerStart = wx.adv.DatePickerCtrl(panel, wx.ID_ANY, style=wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN)
        self.datePickerEnd = wx.adv.DatePickerCtrl(panel, wx.ID_ANY, style=wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN)
        datePickerLabel = wx.StaticText(panel, label="Select Start and End Date:")
        uploadButton = wx.Button(panel, label="Upload CSV File")
        uploadButton.Bind(wx.EVT_BUTTON, self.onUploadButtonClick)
        generateButton = wx.Button(panel, label="Generate Price Distribution Graph")
        generateButton.Bind(wx.EVT_BUTTON, self.onGenerateButtonClick)

        sizer.Add(datePickerLabel, 0, wx.ALL, 10)
        sizer.Add(self.datePickerStart, 0, wx.ALL, 10)
        sizer.Add(self.datePickerEnd, 0, wx.ALL, 10)
        sizer.Add(uploadButton, 0, wx.ALL, 10)
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

    def cleanPriceColumn(self, df):
        df['price'] = df['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
        return df

    def onGenerateButtonClick(self, event):
        try:
            if self.data_file:
                startDate = self.datePickerStart.GetValue().FormatISODate()
                endDate = self.datePickerEnd.GetValue().FormatISODate()

                df = pd.read_csv(self.data_file, low_memory=False)
                df['last_review'] = pd.to_datetime(df['last_review'])
                df = self.cleanPriceColumn(df)
                filteredDf = df[(df['last_review'] >= startDate) & (df['last_review'] <= endDate)]
                groupedData = filteredDf.groupby('last_review')['price'].mean()

                plt.figure(figsize=(10, 6))
                plt.plot(groupedData.index, groupedData.values, marker='o', linestyle='-')
                plt.xlabel('Date(YYYY-MM-DD)')
                plt.ylabel('Average Price($)')
                plt.title('Price Distribution Over Time for Listings')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            else:
                self.showError("Error: Please upload a CSV file before generating the graph.")

        except FileNotFoundError:
            self.showError("Error: The specified file was not found.")

    def showError(self, message):
        wx.LogError(message)

def main():
    app = wx.App(False)
    frame = PriceDistribution(None, "Generate Price Distribution Graph for Listings")
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
