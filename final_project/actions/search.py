from final_project.actions.login import driver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


class Search:

    @staticmethod
    def search_field(keyword: str):
        search_field = driver.find_element_by_xpath('//input[@placeholder="Search"]')
        search_field.clear()
        search_field.send_keys(keyword)
        # search_field.send_keys(Keys.RETURN)  # CANNOT WORK
        # issue with search not giving your tag word first in list a lot of times
        # need a way to click on the correct option coming up...
        # probably too complicated to do
        # maybe use http address instead
        sleep(2)

    @staticmethod
    def search_tags(keyword: str):
        tag_page = os.path.join("https://www.instagram.com/explore/tags/#", keyword, "/")
        return tag_page

    @staticmethod
    def search_account(account: str):
        account_page = os.path.join("https://www.instagram.com/", account, "/")
        return account_page

    # OR

    @staticmethod
    def search_account_bis(account: str):
        search_field = driver.find_element_by_xpath('//input[@placeholder="Search"]')
        search_field.clear()
        search_field.send_keys(os.path.join("@"), account)
        search_field.send_keys(Keys.RETURN)
        sleep(2)
