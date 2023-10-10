import pandas as pd
import wx
import wx.grid as gridlib

class SuburbSearch(wx.Frame):
    def __init__(self, parent, title):
        super(SuburbSearch, self).__init__(parent, title=title, size=(835, 235))
        panel = wx.Panel(self)
        neighbourhoodLabel = wx.StaticText(panel, label="Enter Suburb to search:")
        self.neighbourhoodText = wx.TextCtrl(panel)
        uploadButton = wx.Button(panel, label="Upload CSV File")
        uploadButton.Bind(wx.EVT_BUTTON, self.onUploadButtonClick)
        searchButton = wx.Button(panel, label="Search")
        searchButton.Bind(wx.EVT_BUTTON, self.onSearchButtonClick)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(neighbourhoodLabel, 0, wx.ALL, 10)
        sizer.Add(self.neighbourhoodText, 0, wx.ALL | wx.EXPAND, 10)
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
                df = df.dropna(subset=['neighbourhood'])
                neighbourhood = self.neighbourhoodText.GetValue()
                filteredDf = df[df['neighbourhood'].str.lower().str.contains(neighbourhood.lower())]
                resultFrame = wx.Frame(None, title=f"Listings in the Suburb of '{neighbourhood}'", size=(800, 600))
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

def main():
    app = wx.App(False)
    frame = SuburbSearch(None, "Suburb Search")
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
