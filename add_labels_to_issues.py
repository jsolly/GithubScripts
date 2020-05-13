from other.my_secrets import get_devtopia_api_obj

DEVTOPIA_REPO_OBJECT = get_devtopia_api_obj()
issues = list(DEVTOPIA_REPO_OBJECT.get_issues(state="open"))
# issue = repo.get_issue(3736)

issues_filtered = [issue for issue in issues if "[Ported to 4x]" in issue.title]

for issue in issues_filtered:
    issue.add_to_labels("A-bug", "S-low")
