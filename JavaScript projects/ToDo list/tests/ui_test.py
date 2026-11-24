import allure, re
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
        task = page.locator('li')
    expect(task).to_be_visible(), 'Task not found'

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
        inputElem.fill('')
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

@allure.epic('Done tasks')
@allure.feature('Add new simple task and check edit and done button is disabled')
@allure.story('Successfully disabled edit and done')
def test_add_task_and_check_edit(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking done button'):
        doneButton = page.get_by_role(role='button', name='Done')
        doneButton.click()
    with allure.step('Check disabled done and edit button is disabled'):
        expect(doneButton).to_be_disabled(), 'Done button is enabled'
        editButton = page.get_by_role(role='button', name='Edit')
        expect(editButton).to_be_disabled(), 'Edit button is enabled'

@allure.epic('Done tasks')
@allure.feature('Add new simple task and click done button')
@allure.story('Successfully changing numbers at stats')
def test_add_task_and_check_stats(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking done button'):
        doneButton = page.get_by_role(role='button', name='Done')
        doneButton.click()
    with allure.step('Checking stats'):
        totalTasks = page.locator('#total').inner_text()
        remainingTasks = page.locator('#remaining').inner_text()
        completedTasks = page.locator('#completed').inner_text()
        totalMatch = re.search(r"\d+", totalTasks)
        remainingMatch = re.search(r'\d+', remainingTasks)
        totalTasksNum = int(totalMatch.group()) if totalMatch else None
        remainingTasksNum = int(remainingMatch.group()) if remainingMatch else None

        assert totalTasksNum == 1, f'Total tasks num is {totalTasksNum} but must be 1'
        assert remainingTasksNum == 0, f'Remaining tasks num is {remainingTasksNum} but must be 0'
        assert int(completedTasks) == 1, f'Completed tasks num is {completedTasks} but must be 1'

@allure.epic('Editing task')
@allure.feature('Look at the edit input')
@allure.story('Successfully appearing edit input')
def test_appearing_edit_input(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking done button'):
        doneButton = page.get_by_role(role='button', name='Edit')
        doneButton.click()
    with allure.step('Check disabled done and edit button is disabled'):
        editInput = page.locator('li span input')
        expect(editInput).to_be_visible(), 'Edit input is not visible'

@allure.epic('Editing task')
@allure.feature('Change the task title')
@allure.story('Successfully changing task title')
def test_changing_product_title(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking done button'):
        doneButton = page.get_by_role(role='button', name='Edit')
        doneButton.click()
    with allure.step('Check disabled done and edit button is disabled'):
        editInput = page.locator('li span input')
        editInput.fill('New task title')
    with allure.step('Clicking save button'):
        saveButton = page.get_by_role(role='button', name='Save')
        saveButton.click()
    with allure.step('Check changed title'):
        newTitle = page.locator('li span').inner_text()
        assert newTitle == 'New task title', 'Task title does not changing'

@allure.epic('Editing task')
@allure.feature('Do not change task title')
@allure.story('Title must be like previous title')
def test_changing_product_title_but_new_title_is_empty(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking done button'):
        doneButton = page.get_by_role(role='button', name='Edit')
        doneButton.click()
    with allure.step('Check disabled done and edit button is disabled'):
        editInput = page.locator('li span input')
        editInput.fill('')
    with allure.step('Clicking save button'):
        saveButton = page.get_by_role(role='button', name='Save')
        saveButton.click()
    with allure.step('Check not changed title'):
        newTitle = page.locator('li span').inner_text()
        assert newTitle == 'New task', 'Task title changed'

@allure.epic('Editing task')
@allure.feature('Change task title with spaces at start and end')
@allure.story('Title must be like previous title')
def test_changing_product_title_but_new_title_is_with_spaces(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking done button'):
        doneButton = page.get_by_role(role='button', name='Edit')
        doneButton.click()
    with allure.step('Check disabled done and edit button is disabled'):
        editInput = page.locator('li span input')
        editInput.fill(' New task ')
    with allure.step('Clicking save button'):
        saveButton = page.get_by_role(role='button', name='Save')
        saveButton.click()
    with allure.step('Check not changed title'):
        newTitle = page.locator('li span').inner_text()
        assert newTitle == 'New task', 'Task title changed'

@allure.epic('Delete task')
@allure.feature('Delete task without clicking done button')
@allure.story('Successfully deleting task')
def test_delete_task_and_checking_stats(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking delete button'):
        deleteButton = page.get_by_role(role='button', name='Delete')
        deleteButton.click()
    with allure.step('Check deleted task. It may not be visible'):
        expect(deleteButton).not_to_be_visible(), 'Task was not deleted'
    with allure.step('Checking stats'):
        totalTasks = page.locator('#total').inner_text()
        remainingTasks = page.locator('#remaining').inner_text()
        totalMatch = re.search(r"\d+", totalTasks)
        remainingMatch = re.search(r'\d+', remainingTasks)
        totalTasksNum = int(totalMatch.group()) if totalMatch else None
        remainingTasksNum = int(remainingMatch.group()) if remainingMatch else None

        assert totalTasksNum == 0, f'Total tasks num is {totalTasksNum} but must be 0'
        assert remainingTasksNum == 0, f'Remaining tasks num is {remainingTasksNum} but must be 0'

@allure.epic('Delete task')
@allure.feature('Delete done task')
@allure.story('Successfully deleting done task')
def test_delete_done_task_and_checking_stats(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking done button'):
        doneButton = page.get_by_role(role='button', name='Done')
        doneButton.click()
    with allure.step('Clicking delete button'):
        deleteButton = page.get_by_role(role='button', name='Delete')
        deleteButton.click()
    with allure.step('Check deleted task. It may not be visible'):
        expect(deleteButton).not_to_be_visible(), 'Task was not deleted'
    with allure.step('Checking stats'):
        totalTasks = page.locator('#total').inner_text()
        remainingTasks = page.locator('#remaining').inner_text()
        completedTasks = page.locator('#completed').inner_text()
        totalMatch = re.search(r"\d+", totalTasks)
        remainingMatch = re.search(r'\d+', remainingTasks)
        totalTasksNum = int(totalMatch.group()) if totalMatch else None
        remainingTasksNum = int(remainingMatch.group()) if remainingMatch else None

        assert totalTasksNum == 0, f'Total tasks num is {totalTasksNum} but must be 0'
        assert remainingTasksNum == 0, f'Remaining tasks num is {remainingTasksNum} but must be 0'
        assert int(completedTasks) == 0, f'Completed tasks num is {completedTasks} but must be 0'

@allure.epic('Local storage tests')
@allure.feature('Add new simple task and check it after page reload')
@allure.story('Successfully appearing task after reload')
def test_page_reload(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.query_selector('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Restarting page'):
        page.reload()
    with allure.step('Check the appearing task'):
        task = page.locator('li')
        expect(task).to_be_visible(), 'Task not found'

@allure.epic('Local storage tests')
@allure.feature('Add new simple task and check it after page reload')
@allure.story('Successfully appearing task after reload')
def test_page_reload(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.query_selector('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Reloading page'):
        page.reload()
    with allure.step('Check the appearing task'):
        task = page.locator('li')
        expect(task).to_be_visible(), 'Task not found'

@allure.epic('Local storage tests')
@allure.feature('Add new simple task, click done button and check it after page reload')
@allure.story('Successfully disabled edit and done after reload')
def test_reload_page_with_done_task(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking done button'):
        doneButton = page.get_by_role(role='button', name='Done')
        doneButton.click()
    with allure.step('Reloading page'):
        page.reload()
    with allure.step('Check disabled done and edit button is disabled'):
        expect(doneButton).to_be_disabled(), 'Done button is enabled'
        editButton = page.get_by_role(role='button', name='Edit')
        expect(editButton).to_be_disabled(), 'Edit button is enabled'

@allure.epic('Local storage tests')
@allure.feature('Add new simple task, change title and check it after page reload')
@allure.story('Successfully changing and saving task title after reloading')
def test_changing_product_title(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking done button'):
        doneButton = page.get_by_role(role='button', name='Edit')
        doneButton.click()
    with allure.step('Check disabled done and edit button is disabled'):
        editInput = page.locator('li span input')
        editInput.fill('New task title')
    with allure.step('Clicking save button'):
        saveButton = page.get_by_role(role='button', name='Save')
        saveButton.click()
    with allure.step('Reloading page'):
        page.reload()
    with allure.step('Check changed title'):
        newTitle = page.locator('li span').inner_text()
        assert newTitle == 'New task title', 'Task title does not changing or saving'

@allure.epic('Local storage tests')
@allure.feature('Delete task without clicking done button and reload page')
@allure.story('Successfully deleting task after reloading page it must not be visible')
def test_delete_task_and_check_it_after_reloading(page : Page, url):
    page.goto(url)
    with allure.step('Finding input and writing a task there'):
        inputElem = page.locator('#taskInp')
        inputElem.fill('New task')
    with allure.step('Clicking add task button'):
        addTaskButton = page.query_selector('#addTask')
        addTaskButton.click()
    with allure.step('Clicking delete button'):
        deleteButton = page.get_by_role(role='button', name='Delete')
        deleteButton.click()
    with allure.step('Reloading page'):
        page.reload()
    with allure.step('Check deleted task. It may not be visible'):
        expect(deleteButton).not_to_be_visible(), 'Task was not deleted'
    with allure.step('Checking stats'):
        totalTasks = page.locator('#total').inner_text()
        remainingTasks = page.locator('#remaining').inner_text()
        totalMatch = re.search(r"\d+", totalTasks)
        remainingMatch = re.search(r'\d+', remainingTasks)
        totalTasksNum = int(totalMatch.group()) if totalMatch else None
        remainingTasksNum = int(remainingMatch.group()) if remainingMatch else None
