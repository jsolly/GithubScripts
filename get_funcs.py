import json
import re

import requests
import urllib3

from other.my_secrets import MySecrets

urllib3.disable_warnings()

ZENTOPIA_DICT = MySecrets.ZENTOPIA_DICT
ZENTOPIA_API_URL = ZENTOPIA_DICT["API_URL"]
ZENTOPIA_REPO_ID = ZENTOPIA_DICT["REPO_ID"]
ZENTOPIA_TOKEN = ZENTOPIA_DICT["TOKEN"]
ZENTOPIA_RELEASE_ID = "5f51cd7001486a33612a9f87"
DEVTOPIA_REPO_OBJECT = MySecrets.get_devtopia_api_obj()


pattern = re.compile(r"https://.*/issues/\d*")


def get_issue_numbers_from_issue_body(issue_number: int):
    issue_body = DEVTOPIA_REPO_OBJECT.get_issue(issue_number).body

    issue_links = pattern.findall(issue_body)
    issue_numbers = [int(issue_link.split("/")[-1]) for issue_link in issue_links]
    return issue_numbers


def get_epic_issue_numbers(epic_issue_number: int):
    epic_issues_request_url = f"{ZENTOPIA_API_URL}/p1/repositories/{ZENTOPIA_REPO_ID}/epics/{epic_issue_number}"

    head = {"X-Authentication-Token": ZENTOPIA_TOKEN}
    epic_json_data = requests.request(
        method="GET", url=epic_issues_request_url, headers=head, verify=False
    )
    epic_issues = json.loads(epic_json_data.content)["issues"]

    epic_issue_numbers = [issue["issue_number"] for issue in epic_issues]
    return epic_issue_numbers


def get_issues_to_verify_after_release(release_id: str, repo_id: int):
    release_issues_url = f"{ZENTOPIA_API_URL}/p1/reports/release/{release_id}/issues"
    head = {"X-Authentication-Token": ZENTOPIA_TOKEN}
    release_issues = requests.request(
        method="GET", url=release_issues_url, headers=head, verify=False
    ).json()

    issue_numbers = [issue_dict["issue_number"] for issue_dict in release_issues]

    for issue_number in issue_numbers:
        issue_data_url = (
            f"{ZENTOPIA_API_URL}/p1/repositories/{repo_id}/issues/{issue_number}/events"
        )

        issue_data = requests.request(
            method="GET", url=issue_data_url, headers=head, verify=False
        ).json()
        try:
            print(f"{issue_number}, {issue_data[0]['created_at'].split('T')[0]}")
        except:
            print(issue_number)


if __name__ == "__main__":
    get_issues_to_verify_after_release(ZENTOPIA_RELEASE_ID, ZENTOPIA_REPO_ID)
