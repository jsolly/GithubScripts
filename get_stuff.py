from other.my_secrets import (
    DEVTOPIA_REPO_OBJECT,
    ZENTOPIA_API_URL,
    ZENTOPIA_TOKEN,
    ZENTOPIA_REPO_ID,
)
import re
import json
import requests

pattern = re.compile(r"https://.*/issues/\d*")


def get_issue_numbers_from_issue_body(issue_number):
    issue_body = DEVTOPIA_REPO_OBJECT.get_issue(issue_number).body

    issue_links = pattern.findall(issue_body)
    issue_numbers = [int(issue_link.split("/")[-1]) for issue_link in issue_links]
    return issue_numbers


def get_epic_issue_numbers(epic_issue_number):
    epic_issues_request_url = f"{ZENTOPIA_API_URL}/p1/repositories/{ZENTOPIA_REPO_ID}/epics/{epic_issue_number}"

    head = {"X-Authentication-Token": ZENTOPIA_TOKEN}
    epic_json_data = requests.request(
        method="GET", url=epic_issues_request_url, headers=head, verify=False
    )
    epic_issues = json.loads(epic_json_data.content)["issues"]

    epic_issue_numbers = [issue["issue_number"] for issue in epic_issues]
    return epic_issue_numbers


if __name__ == "__main__":
    get_epic_issue_numbers(3591)
