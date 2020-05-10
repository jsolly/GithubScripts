import json
import requests
from other.my_secrets import ZENTOPIA_REPO_ID as REPO
from other.my_secrets import ZENTOPIA_API_URL, ZENTOPIA_TOKEN


def add_issues_to_epic(issue_numbers, epic_issue_id):
    # issue_numbers = list(REPO.get_issues(state="closed", since=""))

    json_data = {
        "add_issues": [
            {"repo_id": REPO, "issue_number": issue.number} for issue in issue_numbers
        ],
        "remove_issues": [],
    }

    request_url = (
        f"{ZENTOPIA_API_URL}/p1/repositories/{REPO}/epics/{epic_issue_id}/update_issues"
    )
    head = {"X-Authentication-Token": ZENTOPIA_TOKEN}
    response = requests.request(
        method="POST", url=request_url, headers=head, json=json_data, verify=False
    )
    print(json.loads(response.text))


def add_labels_to_issues(issue_numbers, repo_obj):
    for issue_number in issue_numbers:
        try:
            issue = repo_obj.get_issue(issue_number)
            issue.add_to_labels("A-architecture")
            issue.remove_from_labels("A-bug")
        except:
            pass


if __name__ == "__main__":
    print("I was run from __main___")
