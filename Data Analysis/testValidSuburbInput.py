import pytest
import wx
from validSuburbInputTest import SuburbSearch

@pytest.fixture
def app():
    return wx.App(False)

@pytest.fixture
def frame(app):
    return SuburbSearch(None, "Test Suburb Search")

def test_search_with_valid_input(frame):
    frame.neighbourhoodText.SetValue("Example Suburb")
    frame.datePickerStart.SetValue(wx.DateTime.Now())
    frame.datePickerEnd.SetValue(wx.DateTime.Now())
    frame.onSearchButtonClick(None)
    grid = frame.grid
    assert grid is not None
