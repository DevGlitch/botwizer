from final_project.actions.login import driver
from time import sleep
import os


class Pages:

    @staticmethod
    def home_page():
        # Launch Instagram Home Page
        driver.get("https://www.instagram.com")
        sleep(2)

    @staticmethod
    def account_page(account: str):
        # Opens account page - yours or someones else's account page
        driver.get(os.path.join("https://www.instagram.com/", account, "/"))
        sleep(2)

    @staticmethod
    def inbox():
        # Inbox
        driver.get("https://www.instagram.com/direct/inbox/")
        sleep(2)

    @staticmethod
    def new_message():
        # To send a new DM
        driver.get("https://www.instagram.com/direct/new/")
        sleep(2)

    @staticmethod
    def explore_page():
        # Leads to explore page - no real need at this time to use
        driver.get("https://www.instagram.com/explore/")
        sleep(2)

    @staticmethod
    def tag_page(keyword: str):
        # Page of a specific tag
        tag_page = os.path.join("https://www.instagram.com/explore/tags/#", keyword, "/")
        return tag_page

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
        driver.get(os.path.join("https://www.instagram.com/explore/locations/", country, "/"))
        sleep(2)
        # Lead the list of countries
        # click see more until no longer available
        # then save all countries name with their respective link

    @staticmethod
    def country_cities_page(country_code: str, country: str):
        driver.get(os.path.join("https://www.instagram.com/explore/locations/", country_code, "/", country, "/"))
        sleep(2)
        # This will lead to the cities of that country
        # Should retrieve full list of countries
        # Save list a file to print/retrieve
        # Country_code is 2 letters
        # Should save all codes and countries in a file to be able to print/retrieve