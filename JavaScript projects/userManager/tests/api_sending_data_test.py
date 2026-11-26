import allure
from playwright.sync_api import Page

@allure.epic('Test api sending data')
@allure.feature('POST method')
@allure.story('It must return correct data after post')
def test_post_user(page: Page, website_url):
    with allure.step('Going to webpage'):
        page.goto(website_url)

    with allure.step('Excepting API request'):
        with page.expect_request(
                lambda request: request.method == "POST"
                    and request.url.endswith("/users")
        ) as request_info:
            with allure.step('Clicking add user button'):
                page.wait_for_selector('li')
                addUser = page.locator('#addBtn')
                addUser.click()
            with allure.step('Filling inputs'):
                page.wait_for_selector('input[placeholder="Name..."]')
                page.locator('input[placeholder="Name..."]').fill('New user')
                page.locator('input[placeholder="Email..."]').fill('user@example.com')
                page.locator('input[placeholder="City..."]').fill('Chadlington')
            with allure.step('Clicking save button'):
                page.locator('.saveBtn').click()

    with allure.step('Getting except value'):
        request = request_info.value

    with allure.step('Checking request method'):
        assert request.method == "POST"

    with allure.step('Getting content type'):
        assert request.headers["content-type"] == "application/json"

    with allure.step('Getting request data'):
        data = request.post_data_json

    with allure.step('Checking request data'):
        assert data["name"] == "New user"
        assert data["email"] == "user@example.com"
        assert data["address"]["city"] == "Chadlington"


@allure.epic('Test api sending data')
@allure.feature('PATCH method')
@allure.story('It must return correct data after patch')
def test_patch_user(page: Page, website_url):
    with allure.step('Going to webpage'):
        page.goto(website_url)

    with allure.step('Excepting API request'):
        with page.expect_request(
                lambda request: request.method == "PATCH"
                    and request.url.endswith("/users/1")
        ) as request_info:
            with allure.step('Clicking edit user button'):
                page.wait_for_selector('li')
                firstUser = page.locator('li').first
                editUser = firstUser.locator('.edit')
                editUser.click()
            with allure.step('Changing data'):
                page.wait_for_selector('input[placeholder="Email..."]')
                page.locator('input[placeholder="Name..."]').fill('Roman')
                page.wait_for_selector('input[placeholder="Email..."]')
                page.locator('input[placeholder="Email..."]').fill('user@example.com')
                page.wait_for_selector('input[placeholder="Email..."]')
                page.locator('input[placeholder="City..."]').fill('Kropyvnytskiy')
            with allure.step('Clicking save button'):
                page.locator('.saveBtn').click()

    with allure.step('Getting except value'):
        request = request_info.value

    with allure.step('Checking request method'):
        assert request.method == "PATCH"

    with allure.step('Getting content type'):
        assert request.headers["content-type"] == "application/json"

    with allure.step('Getting request data'):
        data = request.post_data_json

    with allure.step('Checking request data'):
        assert data["name"] == "Roman"
        assert data["email"] == "user@example.com"
        assert data["address"]["city"] == "Kropyvnytskiy"
