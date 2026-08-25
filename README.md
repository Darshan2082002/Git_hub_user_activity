# GitHub User Activity

A command-line tool built in Python to fetch and display recent activity for any GitHub user using the GitHub REST API.

This project is built as part of the roadmap.sh project challenge: [GitHub User Activity](https://roadmap.sh/projects/github-user-activity).

## Features

- Fetch recent public events for a specified GitHub username.
- Display activity neatly in the terminal (e.g., pushed commits, opened issues, created repositories).
- Simple caching mechanism to avoid hitting API rate limits.

## Requirements

- Python 3.x
- `requests` (or standard library modules depending on implementation)

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/Darshan2082002/Git_hub_user_activity.git](https://github.com/Darshan2082002/Git_hub_user_activity.git)
   cd Git_hub_user_activity


python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt

python Git_hub_user_activity.py <username>
