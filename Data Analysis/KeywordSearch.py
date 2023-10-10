import wx
import pandas as pd
import wx.adv
import wx.grid

class KeywordSearch(wx.Frame):
    def __init__(self, parent, title):
        super(KeywordSearch, self).__init__(parent, title=title, size=(500, 435))
        panel = wx.Panel(self)
        self.wordLabel = wx.StaticText(panel, label="Enter word to search:")
        self.wordText = wx.TextCtrl(panel)
        self.datePickerStart = wx.adv.DatePickerCtrl(panel, wx.ID_ANY, style=wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN)
        self.datePickerEnd = wx.adv.DatePickerCtrl(panel, wx.ID_ANY, style=wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN)
        uploadButton = wx.Button(panel, label="Upload CSV File")
        uploadButton.Bind(wx.EVT_BUTTON, self.onUploadButtonClick)
        searchButton = wx.Button(panel, label="Search")
        searchButton.Bind(wx.EVT_BUTTON, self.onSearchButtonClick)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.wordLabel, 0, wx.ALL, 10)
        sizer.Add(self.wordText, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(self.datePickerStart, 0, wx.ALL, 10)
        sizer.Add(self.datePickerEnd, 0, wx.ALL, 10)
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
                df = pd.read_csv(self.data_file, low_memory=False)
                searchWord = self.wordText.GetValue().lower()
                startDate = self.datePickerStart.GetValue().FormatISODate()
                endDate = self.datePickerEnd.GetValue().FormatISODate()
                filteredDf = df[(pd.to_datetime(df['last_review']) >= startDate) &
                                (pd.to_datetime(df['last_review']) <= endDate) &
                                (df['amenities'].str.lower().str.contains(searchWord))]

                self.showFilteredResults(filteredDf, searchWord)
            else:
                self.showErrorMessageBox("Error: Please upload a CSV file before searching.")

        except FileNotFoundError:
            self.showErrorMessageBox("Error: The specified file was not found.")

    def showFilteredResults(self, filteredDf, searchWord):
        resultFrame = wx.Frame(None, title=f'Listings with the keyword "{searchWord}"', size=(800, 600))
        grid = wx.grid.Grid(resultFrame)
        grid.CreateGrid(len(filteredDf), len(filteredDf.columns))

        for col, columnName in enumerate(filteredDf.columns):
            grid.SetColLabelValue(col, columnName)
        for i, row in enumerate(filteredDf.itertuples()):
            for j, value in enumerate(row[1:]):
                grid.SetCellValue(i, j, str(value))

        grid.AutoSizeColumns()
        resultFrame.Show(True)

    def showErrorMessageBox(self, message):
        wx.LogError(message)

def main():
    app = wx.App(False)
    frame = KeywordSearch(None, "Keyword Search")
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
