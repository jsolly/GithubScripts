import os
import re
from selenium import webdriver
from other.my_secrets import DEVTOPIA_DICT, get_devtopia_api_obj

DEVTOPIA_REPO_OBJECT = get_devtopia_api_obj()

if __name__ == "__main__":
    opts = webdriver.ChromeOptions()
    driver = webdriver.Chrome()

    try:
        issues = list(DEVTOPIA_REPO_OBJECT.get_issues(state="open"))

        driver.get(f"{DEVTOPIA_DICT['DEVTOPIA_BASE_URL']}/login")
        driver.find_element_by_id("login_field").send_keys(
            DEVTOPIA_DICT["DEVTOPIA_USERNAME"]
        )
        driver.find_element_by_id("password").send_keys(
            DEVTOPIA_DICT["DEVTOPIA_PASSWORD"]
        )
        driver.find_element_by_name("commit").click()

        for issue in issues:
            if "right" not in issue.title.lower():
                continue
            else:
                title = issue.title
                clean_issue_title = re.sub(
                    "[^A-Za-z0-9]+", "_", title
                )  # Remove any weird punctuation
                driver.get(issue._html_url.value)
                driver.implicitly_wait(3)
                body_element = driver.find_element_by_tag_name(
                    "body"
                )  # avoids scrollbar
                body_element.screenshot(f"{clean_issue_title}.png")
                os.system(f"convert {clean_issue_title}.png {clean_issue_title}.pdf")
                os.remove(f"{clean_issue_title}.png")

        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()
