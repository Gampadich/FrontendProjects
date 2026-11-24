import pytest, allure

@pytest.fixture(scope='session')
@allure.step('Get API URL')
def api_url():
    return 'https://jsonplaceholder.typicode.com/users'