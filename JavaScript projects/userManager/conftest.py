import pytest, allure

@pytest.fixture(scope='session')
@allure.step('Get API URL')
def api_url():
    return 'https://jsonplaceholder.typicode.com/users'

@pytest.fixture(scope='session')
@allure.step('Get website URL')
def website_url():
    return 'https://gampadich.github.io/userManager/'