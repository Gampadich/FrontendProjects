# User Manager

A web application for managing user records using JavaScript and the JSONPlaceholder REST API. It allows users to view, add, edit, and delete user information through a dynamic interface.

## Features

- **Fetch Users** — retrieve user data from an external REST API.
- **Display Users** — dynamically render names, emails, and city information.
- **Add Users** — create new user records through an input form.
- **Edit Users** — update existing user information.
- **Delete Users** — remove user records from the interface and send DELETE requests.
- **Input Validation** — prevent submitting empty fields.
- **Responsive Layout** — adapt the user list for smaller screens.

## Technologies

- HTML5
- CSS3
- JavaScript (ES6+)
- Fetch API
- REST API
- Async/Await
- ES Modules
- DOM Manipulation
- JSON

## API

This project uses [JSONPlaceholder](https://jsonplaceholder.typicode.com/), a free fake REST API for testing and prototyping.

Available operations:

| Method | Endpoint | Description |
|---|---|---|
| GET | `/users` | Retrieve users |
| POST | `/users` | Create a user |
| PATCH | `/users/{id}` | Update a user |
| DELETE | `/users/{id}` | Delete a user |

**Note:** JSONPlaceholder simulates write operations. POST, PATCH, and DELETE requests return simulated responses, but changes are not permanently stored on the server.

## Automated Testing

The project includes an automated test suite built with Python and Playwright.

### Testing Stack

- **Python** — test scripting language.
- **Pytest** — test framework.
- **Playwright** — browser automation and API request interception.
- **Allure** — test reporting and visualization.

### Test Coverage

The test suite contains **24 automated tests**:

| Test Type | Number of Tests | Description |
|---|---:|---|
| UI Tests | 18 | Verify user interactions, interface behavior, and input validation. |
| API Tests | 4 | Verify API responses and HTTP operations independently of the UI. |
| UI/API Integration Tests | 2 | Verify that UI actions trigger the correct API requests and send the expected data. |
| **Total** | **24** | |

### Running Tests

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest -v
```

### Generating and Viewing Allure Reports

Allure provides an interactive HTML report containing test results, execution statuses, error details, and other test information.

**1. Run tests and collect Allure results:**

```bash
pytest -v --alluredir=allure-results
```

This creates the `allure-results/` directory containing raw test execution data.

**2. Generate the HTML report:**

```bash
allure generate allure-results -o allure-report --clean
```

This generates the report inside the `allure-report/` directory.

**3. Open the report in your browser:**

```bash
allure open allure-report
```

Allure starts a local server and opens the generated report in your default browser.

**Alternative — generate and open the report in one command:**

```bash
allure serve allure-results
```

This automatically generates a temporary report and opens it in the browser.

**Note:** The Allure Python adapter is installed through `requirements.txt`, but the Allure Commandline tool must be installed separately. You also need to have the required Java runtime available for your Allure CLI version.

### Important Directories

| Directory | Purpose |
|---|---|
| `allure-results/` | Raw test execution results. |
| `allure-report/` | Generated HTML report. |

To generate an updated report, run the tests again and use the `allure generate` command with `--clean` to replace the previous report.

## Project Structure

```text
User-Manager/
├── scripts/
│   ├── api.js
│   ├── addUser.js
│   └── renderUsers.js
├── tests/
│   ├── ui/
│   │   └── test_ui.py
│   ├── api/
│   │   └── test_api.py
│   └── integration/
│       └── test_ui_api.py
├── index.html
├── style.css
├── main.js
├── requirements.txt
└── README.md
```

## Getting Started

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Open the project folder.

3. Run the project using a local development server (for example, VS Code Live Server).

## Architecture

The application is organized into separate JavaScript modules:

- **main.js** — initializes the application and loads users.
- **api.js** — handles HTTP requests to the REST API.
- **renderUsers.js** — renders user records and handles editing and deletion.
- **addUser.js** — handles the creation of new users.

## Future Improvements

- Add more advanced input validation.
- Improve error handling and user feedback.
- Add search and filtering functionality.
- Improve accessibility and responsive design.
- Expand automated test coverage.
- Introduce CI/CD to automate test execution and report generation.

## Author

Created as a personal frontend development project to practice JavaScript modules, asynchronous programming, REST API integration, DOM manipulation, and automated testing with Python and Playwright.
