# TODO List

A simple TODO List web application built with **HTML, CSS, and JavaScript**. It allows users to manage their tasks, track progress, and save tasks locally in the browser.

## Features

- **Add tasks** — create new tasks.
- **Edit tasks** — change task titles.
- **Complete tasks** — mark tasks as completed.
- **Delete tasks** — remove tasks from the list.
- **Task statistics** — track total, completed, and remaining tasks.
- **Local Storage** — tasks are saved in the browser and restored after reloading the page.

## Technologies

- HTML5
- CSS3
- JavaScript (ES6+)
- DOM Manipulation
- Browser Local Storage
- JSON

## Automated Testing

The project includes UI automated tests written using **Python, Playwright, and pytest**.

### Testing Technologies

- Python
- pytest
- Playwright
- Allure Reports
- allure-pytest

### Test Coverage

Automated tests cover the following functionality:

- **Adding tasks** — adding new tasks and validating input.
- **Input validation** — handling empty input and whitespace.
- **Task completion** — marking tasks as completed.
- **Task editing** — changing task titles and validating edited values.
- **Task deletion** — removing tasks from the list.
- **Task statistics** — checking total, completed, and remaining tasks.
- **Local Storage** — verifying task persistence after page reload.

### Project Structure

```text
TODO-List/
├── images/
│   └── 1560.png
├── tests/
│   └── ui_test.py
├── conftest.py
├── index.html
├── main.js
├── README.md
├── requirements.txt
└── style.css
```

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd TODO-List
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install chromium
```

### 5. Run the application

Open `index.html` in your browser or use a local development server.

### 6. Run automated tests

Run all tests:

```bash
pytest -v
```

## Allure Reports

The project uses Allure to generate detailed test reports with execution statistics, test results, steps, and failure information.

### 1. Run tests and collect Allure results

```bash
pytest -v --alluredir=allure-results
```

### 2. Generate an Allure HTML report

```bash
allure generate allure-results -o allure-report --clean
```

### 3. Open the generated report

```bash
allure open allure-report
```

Alternatively, use:

```bash
allure serve allure-results
```

This command generates a temporary report and opens it in your browser automatically.

**Note:** Allure Commandline must be installed separately from the Python dependencies. Verify its installation with:

```bash
allure --version
```

### Allure Report Features

The generated report provides:

- **Overview Dashboard** — total tests, passed, failed, broken, and skipped tests.
- **Test Suites** — test organization by suites and features.
- **Behaviors** — test results grouped by epics, features, and stories.
- **Graphs** — visual statistics of test execution.
- **Test Details** — individual test steps, execution time, and failure information.

## Data Storage

The application uses the browser's `localStorage` to persist tasks.

Each task is stored as an object containing:

- `id` — unique task identifier.
- `title` — task description.
- `isDone` — completion status.

## Future Improvements

- Add task filtering (All / Active / Completed).
- Improve responsive design.
- Add keyboard support for task management.
- Add task deadlines.

## Author

Created as a personal frontend development project to practice JavaScript, DOM manipulation, browser storage, and UI test automation.