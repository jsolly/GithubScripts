import json
import requests
from other.my_secrets import DEVTOPIA_TOKEN, ZENTOPIA_API_URL, ZENTOPIA_REPO_ID


def add_issues_to_epic_from_issue_body(issue_numbers, epic_issue_number):
    epic_issue_id = epic_issue_number

    json_data = {
        "add_issues": [
            {"repo_id": ZENTOPIA_REPO_ID, "issue_number": issue_number}
            for issue_number in issue_numbers
        ],
        "remove_issues": [],
    }

    request_url = f"{ZENTOPIA_API_URL}/p1/repositories/{ZENTOPIA_REPO_ID}/epics/{epic_issue_id}/update_issues"
    head = {"X-Authentication-Token": DEVTOPIA_TOKEN}
    response = requests.request(
        method="POST", url=request_url, headers=head, json=json_data, verify=False
    )
    print(json.loads(response.text))


if __name__ == "__main__":
    add_issues_to_epic_from_issue_body(3587, 3587)
