import wx
import subprocess
import os

class HomePage(wx.Frame):
    def __init__(self, parent, title):
        super(HomePage, self).__init__(parent, title=title, size=(434, 287))
        panel = wx.Panel(self)
        buttonSuburbSearch = wx.Button(panel, label="Search for Listings by Suburb")
        buttonPriceDistribution = wx.Button(panel, label="Generate a Price Distribution Graph")
        buttonKeywordSearch = wx.Button(panel, label="Search for Listings by Keywords")
        buttonCleanlinessSearch = wx.Button(panel, label="Search for Comments on Cleanliness for Listings")
        buttonOccupancyTrends = wx.Button(panel, label="Generate an Occupancy Rate Trends Graph")

        buttonSuburbSearch.Bind(wx.EVT_BUTTON, lambda event, file="SuburbListingSearch.py": self.buttonClick(event, file))
        buttonPriceDistribution.Bind(wx.EVT_BUTTON, lambda event, file="PriceDistribution.py": self.buttonClick(event, file))
        buttonKeywordSearch.Bind(wx.EVT_BUTTON, lambda event, file="KeywordSearch.py": self.buttonClick(event, file))
        buttonCleanlinessSearch.Bind(wx.EVT_BUTTON, lambda event, file="CleanlinessSearch.py": self.buttonClick(event, file))
        buttonOccupancyTrends.Bind(wx.EVT_BUTTON, lambda event, file="OccupancyRateTrends.py": self.buttonClick(event, file))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(buttonSuburbSearch, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(buttonPriceDistribution, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(buttonKeywordSearch, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(buttonCleanlinessSearch, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(buttonOccupancyTrends, 0, wx.ALL | wx.CENTER, 10)
        panel.SetSizer(sizer)
        self.Center()

    def buttonClick(self, event, filename):
        currentDirectory = os.getcwd()
        filePath = os.path.join(currentDirectory, './', filename)
        subprocess.Popen(["python", filePath])

def main():
    app = wx.App(False)
    frame = HomePage(None, "Sydney Airbnb Data Analysis Tool")
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
