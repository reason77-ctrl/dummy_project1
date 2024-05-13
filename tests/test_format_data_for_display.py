import pytest
from package_reason.format_data import format_data_for_display, format_data_for_excel

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Reason",
            "family_name": "Regmi",
            "title": "Developer",
        },
        {
            "given_name": "Rahul",
            "family_name": "Karki",
            "title": "Designer",
        },
    ]

def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Reason Regmi: Developer",
        "Rahul Karki: Designer",
    ]