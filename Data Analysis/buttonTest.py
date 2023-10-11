import wx
import subprocess
import os

class HomePage(wx.Frame):
    def __init__(self, parent, title):
        super(HomePage, self).__init__(parent, title=title, size=(434, 287))
        panel = wx.Panel(self)

    def buttonClick(self, event, filename):
        currentDirectory = os.getcwd()
        filePath = os.path.join(currentDirectory, './', filename)
        if os.path.exists(filePath):
            subprocess.Popen(["python", filePath])
        else:
            raise FileNotFoundError(f"File '{filename}' not found.")
