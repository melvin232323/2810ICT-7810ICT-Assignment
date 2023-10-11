from buttonTest import HomePage
import pytest
import wx

app = wx.App(False)

def test_buttonClick():
    frame = HomePage(None, "Test Frame")
    with pytest.raises(FileNotFoundError):
        frame.buttonClick(None, 'NonExistentFile.py')