import pytest

@pytest.fixture(scope='session')
def api_url():
    return 'https://jsonplaceholder.typicode.com/users'

@pytest.fixture(scope='session')
def website_url():
    return 'https://gampadich.github.io/userManager/'