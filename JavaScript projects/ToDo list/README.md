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

## Project Structure

```text
TODO-List/
├── images/
│   └── 1560.png
├── index.html
├── style.css
├── main.js
└── README.md
```

## Getting Started

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Open the project folder.

3. Open `index.html` in your browser.

No additional dependencies or installation are required.

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

Created as a personal frontend development project to practice JavaScript, DOM manipulation, and browser storage.