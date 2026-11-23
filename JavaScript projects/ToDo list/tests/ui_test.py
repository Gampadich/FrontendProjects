import allure
from playwright.sync_api import Page, expect

@allure.epic('Adding tasks test')
@allure.feature('Add new simple task')
@allure.story('Successfully adding new task')
def test_add_task(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.query_selector('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Check the appearing task'):
        task = page.query_selector('li')
    assert task.is_visible(), 'Task not found'

@allure.epic('Adding tasks test')
@allure.feature('Add new task with space at the start and at the end')
@allure.story('Successfully adding new task without spaces')
def test_add_task_with_spaces(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.query_selector('#taskInp')
        inputElem.fill(' New task ')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Check the task title without spaces'):
        taskTitle = page.query_selector('li span').inner_text()
    assert taskTitle != ' New task ', 'Task have spaces at start and end'

@allure.epic('Adding tasks test')
@allure.feature('Add new spaces task')
@allure.story("Successfully didn't appeared task")
def test_add_task_with_all_text_spaces(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.query_selector('#taskInp')
        inputElem.fill('    ')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step("Check the task didn't appeared"):
        task = page.locator('li')
    expect(task).not_to_be_visible(), 'Task found'

@allure.epic('Adding tasks test')
@allure.feature('Add new task without text')
@allure.story('Successfully appearing error')
def test_error(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.query_selector('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Check the error message'):
        error = page.query_selector('#error').inner_text()
    assert error == 'Please enter a task', "Error didn't appeared"

@allure.epic('Adding tasks test')
@allure.feature('Add new simple task and check input field')
@allure.story('Successfully clearing input field')
def test_add_task_and_check_input(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Check the empty input field'):
        expect(inputElem).to_have_value(''), "Input field isn't empty"

