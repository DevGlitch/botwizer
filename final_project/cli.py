import os
from final_project.actions.login import Login
from final_project.actions.search import Search
from final_project.actions.__init__ import close_browser


def main():

    # if first time and .env username/password don't exist
    # ask user to enter them
    # ask user to select a salt like a secure sentence that they will use to login

    username = os.environ.get("username")
    password = os.environ.get("password")

    # if .env are presents then ask user their secure salt
    # if incorrect return error
    # if correct decrypt variables for use in login

    insta = Login()
    insta.launch()
    insta.login(username, password)

    search = Search()
    search.search_field("cavalier")

    close_browser()

    # Check Chrome installed
    # Get Chrome Version
    # Install chromedriver based on Chrome version
