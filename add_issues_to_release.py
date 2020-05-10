import json
import requests
from other.my_secrets import DEVTOPIA_REPO_OBJECT as REPO
from other.my_secrets import ZENTOPIA_REPO_ID as REPO_ID
from other.my_secrets import ZENTOPIA_TOKEN, ZENTOPIA_API_URL

if __name__ == "__main__":
    issues = list(REPO.get_issues(state="open"))
    release_id = "5b560460f538700745b06be1"
    """
    if you go into the release reports in a browser, you will see the release id in the url...like
    {DEVTOPIA_BASE_URL}/{DEVTOPIA_DASHBOARD_REPO_URL}/issues#workspaces/{DEVTOPIA_DASHBOARD_WORKSPACE}/reports/release?release=5b560460f538700745b06be1
    """
    json_data = {
        "add_issues": [
            {"repo_id": REPO_ID, "issue_number": issue.number}
            for issue in issues
            if "[Ported to 4x]" in issue.title
        ],
        "remove_issues": [],
    }

    request_url = f"{ZENTOPIA_API_URL}/p1/reports/release/{release_id}/issues"
    head = {"X-Authentication-Token": ZENTOPIA_TOKEN}
    response = requests.request(
        method="PATCH", url=request_url, headers=head, json=json_data, verify=False
    )
    print(json.loads(response.text))
