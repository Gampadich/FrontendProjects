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

## Project Structure

```text
User-Manager/
├── scripts/
│   ├── api.js
│   ├── addUser.js
│   └── renderUsers.js
├── index.html
├── style.css
└── main.js
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

## Author

Created as a personal frontend development project to practice JavaScript modules, asynchronous programming, REST API integration, and DOM manipulation.