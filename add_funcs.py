import json
import requests
from other.my_secrets import ZENTOPIA_DICT

ZENTOPIA_API_URL = ZENTOPIA_DICT["ZENTOPIA_API_URL"]
REPO = ZENTOPIA_DICT["REPO"]
ZENTOPIA_TOKEN = ZENTOPIA_DICT["REPO"]


def add_issues_to_release(issues: list, release_id: str):
    issues = list(REPO.get_issues(state="open"))
    release_id = "5b560460f538700745b06be1"
    """
    if you go into the release reports in a browser, you will see the release id in the url...like
    {DEVTOPIA_BASE_URL}/{DEVTOPIA_DASHBOARD_REPO_URL}/issues#workspaces/{DEVTOPIA_DASHBOARD_WORKSPACE}/reports/release?release=5b560460f538700745b06be1
    """
    json_data = {
        "add_issues": [
            {"repo_id": ZENTOPIA_DICT["REPO_ID"], "issue_number": issue.number}
            for issue in issues
            if "[Ported to 4x]" in issue.title
        ],
        "remove_issues": [],
    }

    request_url = (
        f"{ZENTOPIA_DICT['ZENTOPIA_API_URL']}/p1/reports/release/{release_id}/issues"
    )
    head = {"X-Authentication-Token": ZENTOPIA_DICT["ZENTOPIA_TOKEN"]}
    response = requests.request(
        method="PATCH", url=request_url, headers=head, json=json_data, verify=False
    )
    print(json.loads(response.text))


def add_issues_to_epic(issue_numbers: list, epic_issue_number: int):
    epic_issue_id = epic_issue_number

    json_data = {
        "add_issues": [
            {"repo_id": ZENTOPIA_DICT["ZENTOPIA_REPO_ID"], "issue_number": issue_number}
            for issue_number in issue_numbers
        ],
        "remove_issues": [],
    }

    request_url = f"{ZENTOPIA_API_URL}/p1/repositories/{ZENTOPIA_REPO_ID}/epics/{epic_issue_id}/update_issues"
    head = {"X-Authentication-Token": DEVTOPIA_DICT["DEVTOPIA_TOKEN"]}
    response = requests.request(
        method="POST", url=request_url, headers=head, json=json_data, verify=False
    )
    print(json.loads(response.text))


def add_labels_to_issues(issue_numbers: list, repo_obj):
    for issue_number in issue_numbers:
        issue = repo_obj.get_issue(issue_number)
        issue.add_to_labels("A-architecture")
        issue.remove_from_labels("A-bug")


if __name__ == "__main__":
    print("I was run from __main___")
