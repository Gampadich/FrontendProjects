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

@allure.epic('Test API')
@allure.feature('POST test')
@allure.story('It must return JSON with parameters id, name, email, address')
@allure.severity(allure.severity_level.CRITICAL)
def test_post(api_url):
    with allure.step('Making API request and checking the status'):
        postData = {
            "id": 1,
            "name": "New Name",
            "email": "new@example.com",
            "address": {
                "city": "Kyiv"
            }
        }
        response = requests.post(api_url, json=postData)
        assert response.status_code == 200 or response.status_code == 201
    with allure.step('Converting response to JSON form'):
        data = response.json()
    with allure.step('Checking if user exists'):
        assert 'id' in data, 'Data haven`t id but it is required'
        assert data['name'] == postData['name'], 'Data haven`t name but it is required or data do not equals'
        assert data['email'] == postData['email'], 'Data haven`t email but it is required or data do not equals'
        assert data['address']['city'] == postData['address']['city'] , 'Data haven`t city but it is required or data do not equals'

@allure.epic('Test API')
@allure.feature('PATCH test')
@allure.story('It must return JSON with parameters id, name, email, address')
@allure.severity(allure.severity_level.CRITICAL)
def test_patch(api_url):
    with allure.step('Making API request and checking the status'):
        postData = {
            "id": 1,
            "name": "New Name",
            "email": "new@example.com",
            "address": {
                "city": "Kyiv"
            }
        }
        response = requests.patch(f'{api_url}/1', json=postData)
        assert response.status_code == 200 or response.status_code == 201
    with allure.step('Converting response to JSON form'):
        data = response.json()
    with allure.step('Checking if user exists'):
        assert 'id' in data, 'Id is not equals'
        assert data['name'] == postData['name'], 'Name is not equals'
        assert data['email'] == postData['email'], 'Email is not equals'
        assert data['address']['city'] == postData['address']['city'] , 'City is not equals'

@allure.epic('Test API')
@allure.feature('DELETE test')
@allure.story('It must return JSON message or just return a status code 200 or 201')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete(api_url):
    with allure.step('Making API request and checking the status'):
        response = requests.delete(f'{api_url}/1')
    with allure.step('Checking status code'):
        assert response.status_code == 200 or response.status_code == 201, f'Status code: {response.status_code}'

