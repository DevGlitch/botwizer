from final_project.actions.login import driver
from time import sleep
import os


class Pages:
    @staticmethod
    def account_page(account: str):
        # Opens account page - yours or someones else's account page
        driver.get("https://www.instagram.com/" + account + "/")  # POTENTIAL TO IMPROVE !!!!!!!!!!!!!!
        print("Loading", account, "'s page...")
        # Maybe instead try to click on first result?
        # Might not always work which could be an issue but this would look more human like
        sleep(2)

    @staticmethod
    def your_account_page(account: str):
        # Open your own account page using the drop down menu - more human-like
        your_acct = driver.find_element_by_xpath(
            "//a[contains(@href,'/{}')]".format(os.environ.get("username"))
        )
        your_acct.click()
        print("Opening your account page...")
        sleep(2)

    @staticmethod
    def inbox():  # pragma: no cover
        # Your inbox
        inbox_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a'
        )
        inbox_icon.click()
        print("Loading inbox page...")
        sleep(2)

    @staticmethod
    def new_message():  # pragma: no cover
        # To send a new DM
        new_dm_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button'
        )
        new_dm_icon.click()
        print("Creating new message...")
        sleep(2)

    @staticmethod
    def hashtag_page(hashtag: str):  # pragma: no cover
        # Page of a specific tag
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        print("Loading", hashtag, "hashtag page...")
        sleep(2)

    @staticmethod
    def home_page():  # pragma: no cover
        # Instagram Home Page - no real need at this time to use
        home_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a'
        )
        home_icon.click()
        print("Loading home page...")
        sleep(2)

    @staticmethod
    def explore_page():  # pragma: no cover
        # Leads to explore page - no real need at this time to use
        explore_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a'
        )
        explore_icon.click()
        print("Loading explore page...")
        # This page take longer to load
        sleep(4)

    @staticmethod
    def saved_pictures_page():  # pragma: no cover
        # Your Saved Pictures - no real need at this time to use
        driver.get("https://www.instagram.com/jacksoncav/saved/")
        sleep(2)

    @staticmethod
    def tagged_pictures_page():  # pragma: no cover
        # Pictures you are tagged - no real need at this time to use
        driver.get("https://www.instagram.com/jacksoncav/tagged/")
        sleep(2)

    @staticmethod
    def profile_edit():  # pragma: no cover
        # Your profile Edit - no real need at this time to use
        driver.get("https://www.instagram.com/accounts/edit/")
        sleep(2)

    @staticmethod
    def countries_list(country: str):  # pragma: no cover
        # Leads to countries list page - no real need at this time to use
        driver.get("https://www.instagram.com/explore/locations/" + country + "/")
        sleep(2)
        # To save list would need to click "see more" until no longer available
        # Then save all countries name with their respective link

    @staticmethod
    def country_cities_page(country_code: str, country: str):  # pragma: no cover
        # Leads to page listing cities of a specific country - no real need at this time to use
        driver.get(
            "https://www.instagram.com/explore/locations/"
            + country_code  # Country_code is 2 letters
            + "/"
            + country
            + "/"
        )
        sleep(2)
