import pytest
from loadDataTest import ButtonClick

@pytest.fixture
def csv_file():
    return 'valid_data.csv'

def test_loadData_valid_file(csv_file):
    data = loadData(csv_file)
    assert data is not None
    # Add more assertions to validate the loaded data if necessary
