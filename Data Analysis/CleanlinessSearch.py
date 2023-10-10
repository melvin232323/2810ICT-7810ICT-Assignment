import wx
import pandas as pd
import matplotlib.pyplot as plt

class CleanlinessSearch(wx.Frame):
    def __init__(self, parent, title):
        super(CleanlinessSearch, self).__init__(parent, title=title, size=(631, 280))

        panel = wx.Panel(self)
        self.wordLabel = wx.StaticText(panel, label="Enter a Word to Search:")
        self.wordText = wx.TextCtrl(panel)
        uploadButton = wx.Button(panel, label="Upload CSV File")
        uploadButton.Bind(wx.EVT_BUTTON, self.onUploadButtonClick)
        searchButton = wx.Button(panel, label="Search")
        searchButton.Bind(wx.EVT_BUTTON, self.onSearchButtonClick)

        self.allowedWords = ['clean', 'tidy', 'hygienic', 'sanitary', 'spotless', 'neat', 'well-maintained', 'pristine', 'flawless']

        self.wordsLabel = wx.StaticText(panel, label=f"Allowed words are: Clean, Tidy, Hygienic, Sanitary, Spotless, Neat, Well-Maintained, Pristine, Flawless")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.wordLabel, 0, wx.ALL, 10)
        sizer.Add(self.wordText, 0, wx.ALL | wx.EXPAND, 10)
        sizer.Add(uploadButton, 0, wx.ALL, 10)
        sizer.Add(searchButton, 0, wx.ALL | wx.CENTER, 10)
        sizer.Add(self.wordsLabel, 0, wx.ALL, 10)
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
                searchWord = self.wordText.GetValue().lower()

                if searchWord in self.allowedWords:
                    df = pd.read_csv(self.data_file)
                    wordCounts = df['comments'].str.lower().str.count(searchWord).sum()

                    plt.figure(figsize=(5, 6))
                    plt.bar(searchWord, wordCounts, color='skyblue')
                    plt.xlabel('Word')
                    plt.ylabel('Frequency')
                    plt.title(f'Frequency of "{searchWord}" in Customer Comments')
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()
                else:
                    self.showErrorMessageBox(f"Error: '{searchWord}' is not a valid search word.")
            else:
                self.showErrorMessageBox("Error: Please upload a CSV file before searching.")

        except FileNotFoundError:
            self.showErrorMessageBox("Error: The specified file was not found.")

    def showErrorMessageBox(self, message):
        wx.LogError(message)

def main():
    app = wx.App(False)
    frame = CleanlinessSearch(None, "Cleanliness Comment Search")
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()
