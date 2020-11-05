from final_project.actions.login import Login
import os


def main():

    username = os.environ.get("username")
    password = os.environ.get("password")
    insta = Login(username, password)
    insta.login()
    insta.close_browser()
    #
    # Check Chrome installed
    # Get Chrome Version
    # Install chromedriver based on Chrome version
    #
