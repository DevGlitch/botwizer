from final_project.actions.login import driver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
import os


def search_general(keyword: str):
    search_field = driver.find_element_by_xpath('//input[@placeholder="Search"]')
    search_field.clear()
    search_field.send_keys(keyword)
    sleep(2)
    try:
        search_field.send_keys(Keys.RETURN)
        sleep(2)
        search_field.send_keys(Keys.RETURN)
        sleep(2)
    except StaleElementReferenceException:
        pass


def search_account(account: str):
    search_field = driver.find_element_by_xpath('//input[@placeholder="Search"]')
    search_field.clear()
    search_field.send_keys(os.path.join("@"), account)
    sleep(2)
    try:
        search_field.send_keys(Keys.RETURN)
        sleep(2)
        search_field.send_keys(Keys.RETURN)
        sleep(2)
    except StaleElementReferenceException:
        pass


def search_hashtag(hashtag: str):
    search_field = driver.find_element_by_xpath('//input[@placeholder="Search"]')
    search_field.clear()
    search_field.send_keys(os.path.join("#"), hashtag)
    sleep(2)
    try:
        search_field.send_keys(Keys.RETURN)
        sleep(2)
        search_field.send_keys(Keys.RETURN)
        sleep(2)
    except StaleElementReferenceException:
        pass
