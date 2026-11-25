import allure
from playwright.sync_api import Page, expect

@allure.epic('UI tests')
@allure.feature('Loading users')
@allure.story('Users count must be 10 and they must load')
@allure.severity(allure.severity_level.NORMAL)
def test_loading_and_user_count(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Getting users'):
        page.wait_for_selector('li')
        users = page.query_selector_all('li')
    with allure.step('Checking user count'):
        assert len(users) == 10, 'User count should be 10'

@allure.epic('UI tests')
@allure.feature('Loading users')
@allure.story('First user must include data: Leanne Graham, Sincere@april.biz, Gwenborough')
@allure.severity(allure.severity_level.CRITICAL)
def test_user_data(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Getting first user data'):
        page.wait_for_selector('li')
        name = page.query_selector('span[data-test-id="name"]').inner_text()
        email = page.query_selector('span[data-test-id="email"]').inner_text()
        city = page.query_selector('span[data-test-id="city"]').inner_text()
    with allure.step('Checking user count'):
        assert name == 'Leanne Graham', 'Name do not equals'
        assert email == 'Sincere@april.biz', 'Email do not equals'
        assert city == 'Gwenborough', 'City do not equals'

@allure.epic('UI tests')
@allure.feature('Adding users')
@allure.story('Click add user button and inputs must appear')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_user_inputs_appearing(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking add user button'):
        page.wait_for_selector('li')
        addUser = page.locator('#addBtn')
        addUser.click()
    with allure.step('Checking inputs appearing'):
        page.wait_for_selector('input[placeholder="Email..."]')
        nameInput = page.locator('input[placeholder="Name..."]')
        emailInput = page.locator('input[placeholder="Email..."]')
        cityInput = page.locator('input[placeholder="City..."]')
        expect(nameInput).to_be_visible(), 'Name input do not appear'
        expect(emailInput).to_be_visible(), 'Email input do not appear'
        expect(cityInput).to_be_visible(), 'City input do not appear'

@allure.epic('UI tests')
@allure.feature('Adding users')
@allure.story('Click add user button add user. Check user appearing after it')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_user_and_check_appearing(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
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
    with allure.step('Checking user appearing'):
        page.wait_for_selector('span:has-text("New user")')
        lastUser = page.locator('li').last
        name = lastUser.locator('span[data-test-id="name"]')
        email = lastUser.locator('span[data-test-id="email"]')
        city = lastUser.locator('span[data-test-id="city"]')
        expect(name).to_be_visible(), 'Name is not visible'
        expect(email).to_be_visible(), 'Email is not visible'
        expect(city).to_be_visible(), ' City is not visible'
        assert name.inner_text() == 'New user', 'Name do not equals'
        assert email.inner_text() == 'user@example.com', 'Email do not equals'
        assert city.inner_text() == 'Chadlington', 'City do not equals'

@allure.epic('UI tests')
@allure.feature('Adding users')
@allure.story('Add empty user. Error must appear')
@allure.severity(allure.severity_level.NORMAL)
def test_check_error_on_void_user(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking add user button'):
        page.wait_for_selector('li')
        addUser = page.locator('#addBtn')
        addUser.click()
    with allure.step('Clicking save button'):
        page.locator('.saveBtn').click()
    with allure.step('Checking error appearing'):
        page.wait_for_selector('p:has-text("Please fill all fields...")')
        error = page.locator('p:has-text("Please fill all fields...")')
        expect(error).to_be_visible(), 'Error do not appear'

@allure.epic('UI tests')
@allure.feature('Adding users')
@allure.story('Add user but name is empty. Error must appear')
@allure.severity(allure.severity_level.NORMAL)
def test_add_user_but_name_is_empty(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking add user button'):
        page.wait_for_selector('li')
        addUser = page.locator('#addBtn')
        addUser.click()
    with allure.step('Filling inputs'):
        page.wait_for_selector('input[placeholder="Name..."]')
        page.locator('input[placeholder="Name..."]').fill('')
        page.locator('input[placeholder="Email..."]').fill('user@example.com')
        page.locator('input[placeholder="City..."]').fill('Chadlington')
    with allure.step('Clicking save button'):
        page.locator('.saveBtn').click()
    with allure.step('Checking error appearing'):
        page.wait_for_selector('p:has-text("Please fill all fields...")')
        error = page.locator('p:has-text("Please fill all fields...")')
        expect(error).to_be_visible(), 'Error do not appear'

@allure.epic('UI tests')
@allure.feature('Adding users')
@allure.story('Add user but email is empty. Error must appear')
@allure.severity(allure.severity_level.NORMAL)
def test_add_user_but_email_is_empty(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking add user button'):
        page.wait_for_selector('li')
        addUser = page.locator('#addBtn')
        addUser.click()
    with allure.step('Filling inputs'):
        page.wait_for_selector('input[placeholder="Name..."]')
        page.locator('input[placeholder="Name..."]').fill('New user')
        page.locator('input[placeholder="Email..."]').fill('')
        page.locator('input[placeholder="City..."]').fill('Chadlington')
    with allure.step('Clicking save button'):
        page.locator('.saveBtn').click()
    with allure.step('Checking error appearing'):
        page.wait_for_selector('p:has-text("Please fill all fields...")')
        error = page.locator('p:has-text("Please fill all fields...")')
        expect(error).to_be_visible(), 'Error do not appear'

@allure.epic('UI tests')
@allure.feature('Adding users')
@allure.story('Add user but email is empty. Error must appear')
@allure.severity(allure.severity_level.NORMAL)
def test_add_user_but_city_is_empty(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking add user button'):
        page.wait_for_selector('li')
        addUser = page.locator('#addBtn')
        addUser.click()
    with allure.step('Filling inputs'):
        page.wait_for_selector('input[placeholder="Name..."]')
        page.locator('input[placeholder="Name..."]').fill('New user')
        page.locator('input[placeholder="Email..."]').fill('user@example.com')
        page.locator('input[placeholder="City..."]').fill('')
    with allure.step('Clicking save button'):
        page.locator('.saveBtn').click()
    with allure.step('Checking error appearing'):
        page.wait_for_selector('p:has-text("Please fill all fields...")')
        error = page.locator('p:has-text("Please fill all fields...")')
        expect(error).to_be_visible(), 'Error do not appear'

@allure.epic('UI tests')
@allure.feature('Adding users')
@allure.story('Add user but user is spaces. Error must appear')
@allure.severity(allure.severity_level.NORMAL)
def test_add_user_but_user_is_spaces(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking add user button'):
        page.wait_for_selector('li')
        addUser = page.locator('#addBtn')
        addUser.click()
    with allure.step('Filling inputs'):
        page.wait_for_selector('input[placeholder="Name..."]')
        page.locator('input[placeholder="Name..."]').fill('   ')
        page.locator('input[placeholder="Email..."]').fill('   ')
        page.locator('input[placeholder="City..."]').fill('   ')
    with allure.step('Clicking save button'):
        page.locator('.saveBtn').click()
    with allure.step('Checking error appearing'):
        page.wait_for_selector('p:has-text("Please fill all fields...")')
        error = page.locator('p:has-text("Please fill all fields...")')
        expect(error).to_be_visible(), 'Error do not appear'

@allure.epic('UI tests')
@allure.feature('Adding users')
@allure.story('Click cancel button. Inputs must not to be visible')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_user_inputs_not_appearing(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking add user button'):
        page.wait_for_selector('li')
        addUser = page.locator('#addBtn')
        addUser.click()
    with allure.step('Clicking cancel button'):
        page.locator('button:has-text("Cancel")').click()
    with allure.step('Checking inputs appearing'):
        nameInput = page.locator('input[placeholder="Name..."]')
        emailInput = page.locator('input[placeholder="Email..."]')
        cityInput = page.locator('input[placeholder="City..."]')
        expect(nameInput).not_to_be_visible(), 'Name input do not appear'
        expect(emailInput).not_to_be_visible(), 'Email input do not appear'
        expect(cityInput).not_to_be_visible(), 'City input do not appear'

@allure.epic('UI tests')
@allure.feature('Delete user')
@allure.story('Users count must be 9 after deleting one')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_user(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking delete user button'):
        page.wait_for_selector('li')
        firstUser = page.locator('li').first
        firstUser.locator('.delete').click()
    with allure.step('Getting users'):
        users = page.query_selector_all('li')
    with allure.step('Checking user count'):
        assert len(users) == 9, 'User count should be 9'

@allure.epic('UI tests')
@allure.feature('Editing users')
@allure.story('Click edit user button and edit inputs must appear')
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_user(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking edit user button'):
        page.wait_for_selector('li')
        firstUser = page.locator('li').first
        editUser = firstUser.locator('.edit')
        editUser.click()
    with allure.step('Checking inputs appearing'):
        page.wait_for_selector('input[placeholder="Email..."]')
        nameInput = page.locator('input[placeholder="Name..."]')
        emailInput = page.locator('input[placeholder="Email..."]')
        cityInput = page.locator('input[placeholder="City..."]')
        expect(nameInput).to_be_visible(), 'Name input do not appear'
        expect(emailInput).to_be_visible(), 'Email input do not appear'
        expect(cityInput).to_be_visible(), 'City input do not appear'

@allure.epic('UI tests')
@allure.feature('Editing users')
@allure.story('Input values must equal user data')
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_input_equals(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking edit user button'):
        page.wait_for_selector('li')
        firstUser = page.locator('li').first
        editUser = firstUser.locator('.edit')
        editUser.click()
    with allure.step('Checking inputs appearing'):
        page.wait_for_selector('input[placeholder="Email..."]')
        nameInput = page.locator('input[placeholder="Name..."]').input_value()
        emailInput = page.locator('input[placeholder="Email..."]').input_value()
        cityInput = page.locator('input[placeholder="City..."]').input_value()
        assert nameInput == 'Leanne Graham', 'Name input do not equal'
        assert emailInput == 'Sincere@april.biz', 'Email input do not equal'
        assert cityInput == 'Gwenborough', 'City input do not equal'

@allure.epic('UI tests')
@allure.feature('Editing users')
@allure.story('Changing username')
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_username(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking edit user button'):
        page.wait_for_selector('li')
        firstUser = page.locator('li').first
        editUser = firstUser.locator('.edit')
        editUser.click()
    with allure.step('Changing username'):
        page.wait_for_selector('input[placeholder="Email..."]')
        page.locator('input[placeholder="Name..."]').fill('Roman')
    with allure.step('Clicking save button'):
        page.locator('.saveBtn').click()
    with allure.step('Checking data equals'):
        page.wait_for_timeout(500)
        username = firstUser.locator('span[data-test-id="name"]').inner_text()
        assert username == 'Roman', 'Name do not equal'

@allure.epic('UI tests')
@allure.feature('Editing users')
@allure.story('Changing email')
@allure.severity(allure.severity_level.CRITICAL)
def test_edit_email(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking edit user button'):
        page.wait_for_selector('li')
        firstUser = page.locator('li').first
        editUser = firstUser.locator('.edit')
        editUser.click()
    with allure.step('Changing username'):
        page.wait_for_selector('input[placeholder="Email..."]')
        page.locator('input[placeholder="Email..."]').fill('user@example.com')
    with allure.step('Clicking save button'):
        page.locator('.saveBtn').click()
    with allure.step('Checking data equals'):
        page.wait_for_timeout(500)
        email = firstUser.locator('span[data-test-id="email"]').inner_text()
        assert email == 'user@example.com', 'Email do not equal'

@allure.epic('UI tests')
@allure.feature('Editing users')
@allure.story('Changing city')
@allure.severity(allure.severity_level.CRITICAL)
def test_city(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking edit user button'):
        page.wait_for_selector('li')
        firstUser = page.locator('li').first
        editUser = firstUser.locator('.edit')
        editUser.click()
    with allure.step('Changing username'):
        page.wait_for_selector('input[placeholder="Email..."]')
        page.locator('input[placeholder="City..."]').fill('Kropyvnytskiy')
    with allure.step('Clicking save button'):
        page.locator('.saveBtn').click()
    with allure.step('Checking data equals'):
        page.wait_for_timeout(500)
        city = firstUser.locator('span[data-test-id="city"]').inner_text()
        assert city == 'Kropyvnytskiy', 'City do not equal'

@allure.epic('UI tests')
@allure.feature('Editing users')
@allure.story('Changing all user data')
@allure.severity(allure.severity_level.CRITICAL)
def test_changing_all_user_data(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
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
    with allure.step('Checking data equals'):
        firstUser = page.locator('li').first
        name = firstUser.locator('span[data-test-id="name"]')
        email = firstUser.locator('span[data-test-id="email"]')
        city = firstUser.locator('span[data-test-id="city"]')
        assert name.inner_text() == 'Roman', 'Name do not equals'
        assert email.inner_text() == 'user@example.com', 'Email do not equals'
        assert city.inner_text() == 'Kropyvnytskiy', 'City do not equals'

@allure.epic('UI tests')
@allure.feature('Editing users')
@allure.story('Do not change anything')
@allure.severity(allure.severity_level.CRITICAL)
def test_do_not_change_anything(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking edit user button'):
        page.wait_for_selector('li')
        firstUser = page.locator('li').first
        editUser = firstUser.locator('.edit')
        editUser.click()
    with allure.step('Clicking save button'):
        page.locator('.saveBtn').click()
    with allure.step('Checking data equals'):
        firstUser = page.locator('li').first
        name = firstUser.locator('span[data-test-id="name"]')
        email = firstUser.locator('span[data-test-id="email"]')
        city = firstUser.locator('span[data-test-id="city"]')
        assert name.inner_text() == 'Leanne Graham', 'Name do not equals'
        assert email.inner_text() == 'Sincere@april.biz', 'Email do not equals'
        assert city.inner_text() == 'Gwenborough', 'City do not equals'

@allure.epic('UI tests')
@allure.feature('Editing users')
@allure.story('Change all to spaces. Changings should not save')
@allure.severity(allure.severity_level.CRITICAL)
def test_do_not_change_anything(website_url, page : Page):
    with allure.step('Opening page'):
        page.goto(website_url)
    with allure.step('Clicking edit user button'):
        page.wait_for_selector('li')
        firstUser = page.locator('li').first
        editUser = firstUser.locator('.edit')
        editUser.click()
    with allure.step('Changing data'):
        page.wait_for_selector('input[placeholder="Email..."]')
        page.locator('input[placeholder="Name..."]').fill('   ')
        page.wait_for_selector('input[placeholder="Email..."]')
        page.locator('input[placeholder="Email..."]').fill('   ')
        page.wait_for_selector('input[placeholder="Email..."]')
        page.locator('input[placeholder="City..."]').fill('   ')
    with allure.step('Clicking save button'):
        page.locator('.saveBtn').click()
    with allure.step('Checking data equals'):
        firstUser = page.locator('li').first
        name = firstUser.locator('span[data-test-id="name"]')
        email = firstUser.locator('span[data-test-id="email"]')
        city = firstUser.locator('span[data-test-id="city"]')
        assert name.inner_text() == 'Leanne Graham', 'Name do not equals'
        assert email.inner_text() == 'Sincere@april.biz', 'Email do not equals'
        assert city.inner_text() == 'Gwenborough', 'City do not equals'
