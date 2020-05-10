from datetime import datetime
from other.my_secrets import DEVTOPIA_REPO_OBJECT as REPO

if __name__ == "__main__":
    time_in_datetime = datetime.strptime("07-02-2019", "%d-%m-%Y")

    try:
        issues = list(REPO.get_issues(state="closed", since=time_in_datetime))
        print(len(issues))
        for issue in issues:
            if "pull" in issue.html_url:
                continue
            print(issue.title)
            print(f"- [ ] {issue.html_url}")
            print(f"created by {issue.user.name}. Closed on {issue.closed_at}")
            print("\n")

    except Exception as e:
        pass
