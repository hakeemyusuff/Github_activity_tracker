#!/usr/bin/env python3

# importing the required modules
import sys
import requests


def get_activities(url):
    """
    Fetches recent GitHub activity from the provided URL.

    Parameters:
    - url (str): The URL to fetch GitHub events.

    Returns:
    - list: JSON response containing user events if successful.
    """
    response = requests.get(url)
    status = response.status_code
    if status == 200:
        return response.json()
    elif status == 404:
        print("Ensure you input a valid github username")
        return
    else:
        print("Error: unable to fetch data (status code: {status})")


def print_events(url):
    data = get_activities(url)
    events = data

    if events:
        for event in events:
            event_type = event["type"]
            repo_name = event["repo"]["name"]

            if event_type == "PushEvent":
                commit_count = event["payload"]["size"]
                print(f"- Pushed {commit_count} commits to {repo_name}")

            elif event_type == "IssuesEvent":
                action = event["payload"]["action"]
                print(f"- {action.capitalize()} a new issue in {repo_name}")

            elif event_type == "IssueCommentEvent":
                action = event["payload"]["action"]
                print(f"- {action.capitalize()} a comment on an issue in {repo_name}")

            elif event_type == "WatchEvent":
                print(f"- Starred {repo_name}")

            elif event_type == "PullRequestEvent":
                action = event["payload"]["action"]
                print(f"- {action.capitalize()} a pull request in {repo_name}")

            elif event_type == "ForkEvent":
                print(f"- Forked {repo_name}")

            elif event_type == "CreateEvent":
                ref_type = event["payload"]["ref_type"]
                ref_name = event["payload"]["ref"] or "repository"
                print(f"- Created a new {ref_type} ({ref_name}) in {repo_name}")

            elif event_type == "DeleteEvent":
                ref_type = event["payload"]["ref_type"]
                ref_name = event["payload"]["ref"]
                print(f"- Deleted the {ref_type} ({ref_name}) in {repo_name}")

            elif event_type == "ReleaseEvent":
                release_name = event["payload"]["release"]["tag_name"]
                print(f"- Released {release_name} in {repo_name}")

            elif event_type == "GollumEvent":
                pages = event["payload"]["pages"]
                for page in pages:
                    action = page["action"]
                    page_name = page["page_name"]
                    print(
                        f"- {action.capitalize()} Wiki page '{page_name}' in {repo_name}"
                    )

            # Optionally handle other event types or unknown types
            else:
                print(f"- {event_type} occurred in {repo_name}")


def main():
    if len(sys.argv) > 1:
        username = sys.argv[1]
        url = f"https://api.github.com/users/{username}/events"
        print_events(url)
    else:
        print("Usage: github-activity <username>")


if __name__ == "__main__":
    main()
