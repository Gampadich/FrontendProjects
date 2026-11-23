import pytest
import allure

@pytest.fixture
@allure.step('Getting URL address')
def url():
    return "https://gampadich.github.io/ToDo-list/"