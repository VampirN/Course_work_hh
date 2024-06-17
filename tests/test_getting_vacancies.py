from unittest.mock import patch
import pytest
from src.getting_vacancies import HeadHunterAPI


@pytest.fixture
def api():
    return HeadHunterAPI()


def test_get_vacancies(api):
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'items': ['vacancy1', 'vacancy2', 'vacancy3']}


name_job = 'python developer'
pages = 2

vacancies = api.get_vacancies(name_job, pages)

assert len(vacancies) == 6
assert vacancies == ['vacancy1', 'vacancy2', 'vacancy3', 'vacancy1', 'vacancy2', 'vacancy3']