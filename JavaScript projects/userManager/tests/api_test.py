import allure, requests

@allure.epic('Test API')
@allure.feature('GET test')
@allure.story('It must return JSON with parameters id, name, email, address')
@allure.severity(allure.severity_level.CRITICAL)
def test_get(api_url):
    with allure.step('Making API request and checking the status'):
        response = requests.get(api_url)
        assert response.status_code == 200 or response.status_code == 201
    with allure.step('Converting response to JSON form'):
        data = response.json()
    with allure.step('Checking if user exists'):
        for user in data:
            assert 'id' in user, 'Data haven`t id but it is required'
            assert 'name' in user, 'Data haven`t name but it is required'
            assert 'email' in user, 'Data haven`t email but it is required'
            assert 'city' in user['address'], 'Data haven`t city but it is required'
