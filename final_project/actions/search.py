from final_project.actions.login import driver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


def search_general(keyword: str):
    search_field = driver.find_element_by_xpath('//input[@placeholder="Search"]')
    search_field.clear()
    search_field.send_keys(keyword)
    # search_field.send_keys(Keys.RETURN)  # CANNOT WORK
    # issue with search not giving your tag word first in list a lot of times
    # need a way to click on the correct option coming up...
    # probably too complicated to do
    # maybe use http address instead
    sleep(2)


def search_account(account: str):
    search_field = driver.find_element_by_xpath('//input[@placeholder="Search"]')
    search_field.clear()
    search_field.send_keys(os.path.join("@"), account)
    search_field.send_keys(Keys.RETURN)
    sleep(2)


def search_tag(tag: str):
    search_field = driver.find_element_by_xpath('//input[@placeholder="Search"]')
    search_field.clear()
    search_field.send_keys(os.path.join("#"), tag)
    search_field.send_keys(Keys.RETURN)
    sleep(2)
