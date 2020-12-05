from final_project.actions.login import driver
from time import sleep


class Pages:
    @staticmethod
    def home_page():  # Pragma: no cover
        # Instagram Home Page
        home_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a'
        )
        home_icon.click()
        print("Loading home page...")
        sleep(2)

    @staticmethod
    def explore_page():  # Pragma: no cover
        # Leads to explore page - no real need at this time to use
        explore_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a'
        )
        explore_icon.click()
        print("Loading explore page...")
        # This page take longer to load
        sleep(4)

    @staticmethod
    def account_page(account: str):
        # Opens account page - yours or someones else's account page
        driver.get("https://www.instagram.com/" + account + "/")  # POTENTIAL TO IMPROVE !!!!!!!!!!!!!!
        print("Loading", account, "'s page...")
        # Maybe instead try to click on first result?
        # Might not always work which could be an issue but this would look more human like
        sleep(2)

    @staticmethod
    def inbox():  # Pragma: no cover
        # Your inbox
        inbox_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a'
        )
        inbox_icon.click()
        print("Loading inbox page...")
        sleep(2)

    @staticmethod
    def new_message():  # Pragma: no cover
        # To send a new DM
        # should add requirement to have inbox() ran before if not then should run it   !!!!!!!!!!!!!!
        new_dm_icon = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button'
        )
        new_dm_icon.click()
        print("Creating new message...")
        sleep(2)

    @staticmethod
    def hashtag_page(hashtag: str):  # Pragma: no cover
        # Page of a specific tag
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        print("Loading", hashtag, " hashtag page...")
        sleep(2)

    @staticmethod
    def saved_pictures_page():  # Pragma: no cover
        # Your Saved Pictures
        driver.get("https://www.instagram.com/jacksoncav/saved/")
        sleep(2)

    @staticmethod
    def tagged_pictures_page():  # Pragma: no cover
        # Pictures you are tagged
        driver.get("https://www.instagram.com/jacksoncav/tagged/")
        sleep(2)

    @staticmethod
    def profile_edit():  # Pragma: no cover
        # Your profile Edit
        driver.get("https://www.instagram.com/accounts/edit/")
        sleep(2)

    @staticmethod
    def countries_list(country: str):  # Pragma: no cover
        driver.get("https://www.instagram.com/explore/locations/" + country + "/")
        sleep(2)
        # Lead the list of countries
        # click see more until no longer available
        # then save all countries name with their respective link

    @staticmethod
    def country_cities_page(country_code: str, country: str):  # Pragma: no cover
        driver.get(
            "https://www.instagram.com/explore/locations/"
            + country_code
            + "/"
            + country
            + "/"
        )
        sleep(2)
        # This will lead to the cities of that country
        # Country_code is 2 letters
