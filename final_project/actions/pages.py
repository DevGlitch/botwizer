from final_project.actions.login import driver
from time import sleep
import os


class Pages:
    @staticmethod
    def home_page():
        # Instagram Home Page
        home_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a'
        )
        home_icon.click()
        sleep(2)

    @staticmethod
    def explore_page():
        # Leads to explore page - no real need at this time to use
        explore_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a'
        )
        explore_icon.click()
        # This page take longer to load
        sleep(4)

    @staticmethod
    def account_page(account: str):
        # Opens account page - yours or someones else's account page
        driver.get("https://www.instagram.com/" + account + "/")
        sleep(2)

    @staticmethod
    def inbox():
        # Your inbox
        inbox_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a'
        )
        inbox_icon.click()
        sleep(2)

    @staticmethod
    def new_message():
        # To send a new DM
        # should add requirement to have inbox() ran before if not then should run it   !!!!!!!!!!!!!!
        new_dm_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button'
        )
        new_dm_icon.click()
        sleep(2)

    @staticmethod
    def tag_page(keyword: str):
        # Page of a specific tag
        driver.get("https://www.instagram.com/explore/tags/" + keyword + "/")
        sleep(2)

    @staticmethod
    def saved_pictures_page():
        # Your Saved Pictures
        driver.get("https://www.instagram.com/jacksoncav/saved/")
        sleep(2)

    @staticmethod
    def tagged_pictures_page():
        # Pictures you are tagged
        driver.get("https://www.instagram.com/jacksoncav/tagged/")
        sleep(2)

    @staticmethod
    def profile_edit():
        # Your profile Edit
        driver.get("https://www.instagram.com/accounts/edit/")
        sleep(2)

    @staticmethod
    def countries_list(country: str):
        driver.get("https://www.instagram.com/explore/locations/" + country + "/")
        sleep(2)
        # Lead the list of countries
        # click see more until no longer available
        # then save all countries name with their respective link

    @staticmethod
    def country_cities_page(country_code: str, country: str):
        driver.get(
            "https://www.instagram.com/explore/locations/"
            + country_code
            + "/"
            + country
            + "/"
        )
        sleep(2)
        # This will lead to the cities of that country
        # Should retrieve full list of countries
        # Save list a file to print/retrieve
        # Country_code is 2 letters
        # Should save all codes and countries in a file to be able to print/retrieve
