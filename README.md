# GitHub User Activity CLI

This project is a simple command-line interface (CLI) application that fetches and displays the recent activity of a specified GitHub user. It demonstrates working with APIs, handling JSON data, and building a CLI application using Python.

This is one of roadmap.sh [backend project.](https://roadmap.sh/projects/github-user-activity).

## Features

- Fetches recent GitHub activity for any given username
- Displays events in a user-friendly format in the terminal
- Provides descriptive output for various event types, such as push events, issues, comments, stars, and pull requests
- Includes basic error handling for invalid usernames or API failures

## Example Output

```bash
- Created a new branch (main) in hakeemyusuff/Task_tracker
- Created a new repository (repository) in hakeemyusuff/Task_tracker
- Created a new branch (main) in hakeemyusuff/bookmarks
- Created a new repository (repository) in hakeemyusuff/bookmarks
- Created a new branch (main) in hakeemyusuff/blog_application
- Created a new repository (repository) in hakeemyusuff/blog_application
- Pushed 1 commits to hakeemyusuff/Simple_TODO
- Created a new repository (repository) in hakeemyusuff/authentication-and-authorisation-with-expressjs.
```


## Requirements

- Python 3.x
- `requests` library (install with `pip install requests`)
- Internet connection to access the GitHub API

## Installation

1. Clone this repository:
    ```bash
    git clone <repository-url>
    cd github-user-activity-cli
    ```

2. Install the required dependencies:
    ```bash
    pip install requests
    ```

## Usage

Run the script from the command line, passing a GitHub username as an argument:
```bash
./github_activity.py <username>
```

Replace <username> with any valid GitHub username. For example:

```bash
./github_activity.py hakeemyusuff
```

## project structure

github_activity.py: Main script containing the CLI logic and functions for API requests and event processing
get_activities(): Fetches the user’s activity from the GitHub API and returns it as JSON data.
print_events(): Processes and displays each event in a user-friendly format based on event type (e.g., PushEvent, WatchEvent, etc.).

## Error Handling

Invalid Username: If an invalid username is provided, the CLI will display an error message.
API Errors: Errors such as a 404 (Not Found) or other status codes are handled gracefully with relevant messages.

