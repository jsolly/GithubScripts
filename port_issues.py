import re
from other.my_secrets import get_devtopia_api_obj

REPO = get_devtopia_api_obj()

if __name__ == "__main__":
    try:
        porting_issue = REPO.get_issue(3294)
        # issue_content = porting_issue.body
        pattern = re.compile(r"https://.*/issues/\d*")

        issue_content = ""

        issue_links = pattern.findall(issue_content)

        for issue_link in issue_links[1:]:
            issue_number = int(issue_link.split("/")[-1])
            issue_obj = REPO.get_issue(issue_number)
            REPO.create_issue(
                title=f"[Ported to 4x] {issue_obj.title}",
                body=f"Initial implementation in the 3x version of dashboard here -> {issue_link}",
                assignee="",
            )
    except Exception as e:
        print(e)
