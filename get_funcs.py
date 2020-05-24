import requests
import json
import re
from other.my_secrets import get_devtopia_api_obj, ZENTOPIA_DICT

ZENTOPIA_API_URL = ZENTOPIA_DICT["ZENTOPIA_DICT"]
ZENTOPIA_REPO_ID = ZENTOPIA_DICT["ZENTOPIA_REPO_ID"]
ZENTOPIA_TOKEN = ZENTOPIA_DICT["ZENTOPIA_TOKEN"]
DEVTOPIA_REPO_OBJECT = get_devtopia_api_obj()


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


def get_issues_to_verify_after_release():
    time_in_datetime = datetime.strptime("07-02-2019", "%d-%m-%Y")

    issues = list(REPO.get_issues(state="closed", since=time_in_datetime))
    print(len(issues))
    for issue in issues:
        if "pull" in issue.html_url:
            continue
        print(issue.title)
        print(f"- [ ] {issue.html_url}")
        print(f"created by {issue.user.name}. Closed on {issue.closed_at}")
        print("\n")


if __name__ == "__main__":
    get_epic_issue_numbers(3591)
