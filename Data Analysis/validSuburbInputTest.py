import wx
import wx.adv
import pandas as pd
import wx.grid as gridlib

class SuburbSearch(wx.Frame):
    def __init__(self, parent, title):
        super(SuburbSearch, self).__init__(parent, title=title, size=(835, 410))
        panel = wx.Panel(self)
        neighbourhoodLabel = wx.StaticText(panel, label="Enter Suburb to search:")
        self.neighbourhoodText = wx.TextCtrl(panel)
        dateLabelStart = wx.StaticText(panel, label="Start Date:")
        self.datePickerStart = wx.adv.DatePickerCtrl(panel, wx.ID_ANY, wx.DefaultDateTime)
        dateLabelEnd = wx.StaticText(panel, label="End Date:")
        self.datePickerEnd = wx.adv.DatePickerCtrl(panel, wx.ID_ANY, wx.DefaultDateTime)
        uploadButton = wx.Button(panel, label="Upload CSV File")
        uploadButton.Bind(wx.EVT_BUTTON, self.onUploadButtonClick)
        searchButton = wx.Button(panel, label="Search")
        searchButton.Bind(wx.EVT_BUTTON, self.onSearchButtonClick)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(neighbourhoodLabel, 0, wx.ALL, 10)
        sizer.Add(self.neighbourhoodText, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(dateLabelStart, 0, wx.ALL, 10)
        sizer.Add(self.datePickerStart, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(dateLabelEnd, 0, wx.ALL, 10)
        sizer.Add(self.datePickerEnd, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(uploadButton, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(searchButton, 0, wx.ALL | wx.CENTER, 10)

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

    def onSearchButtonClick(self, event):
        try:
            if self.data_file:
                selected_start_date = self.datePickerStart.GetValue().FormatISODate()
                selected_end_date = self.datePickerEnd.GetValue().FormatISODate()
                df = pd.read_csv(self.data_file, low_memory=False)
                df['first_review'] = pd.to_datetime(df['first_review'])
                df['last_review'] = pd.to_datetime(df['last_review'])

                # Handle NaN or NA values in the 'neighbourhood' column
                neighbourhood = self.neighbourhoodText.GetValue().strip()
                filteredDf = df.dropna(subset=['neighbourhood'])
                filteredDf = filteredDf[filteredDf['neighbourhood'].str.lower().str.contains(neighbourhood.lower())]

                # Perform date filtering
                filteredDf = filteredDf[
                    (filteredDf['first_review'] >= selected_start_date) & (
                                filteredDf['last_review'] <= selected_end_date)
                    ]

                resultFrame = wx.Frame(None, title=f"Listings in the Suburb of '{neighbourhood}'", size=(835, 600))
                grid = gridlib.Grid(resultFrame)
                grid.CreateGrid(len(filteredDf), len(filteredDf.columns))

                for i, col in enumerate(filteredDf.columns):
                    grid.SetColLabelValue(i, col)
                    for j, value in enumerate(filteredDf[col]):
                        grid.SetCellValue(j, i, str(value))
                grid.AutoSizeColumns()

                resultFrame.Show()
            else:
                self.showError("Error: Please upload a CSV file before searching.")

        except FileNotFoundError:
            self.showError("Error: The specified file was not found.")

    def showError(self, message):
        wx.LogError(message)

if __name__ == '__main__':
    app = wx.App(False)
    frame = SuburbSearch(None, "Suburb Search")
    frame.Show(True)
    app.MainLoop()
