from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

from final_project.actions.__init__ import set_driver

driver = set_driver()


class Login:

    '''def close_browser(self):
        driver.quit()  # Close browser and driver. For closing just the tab .close()'''

    @staticmethod
    def launch():
        # Launch Instagram Page
        driver.get("https://www.instagram.com")

        # Using sleep to ensure the page has the time to load
        # This will be used multiple times throughout the code
        sleep(2)

    @staticmethod
    def login(username: str, password: str):

        # build a wait time and check every two seconds (loop and/or if else statement)
        # maybe build its own function and call when needed?
        # or put it as a default?
        """if self.driver.find_element() is False:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "myDynamicElement"))
            )
        else:

        https://selenium-python.readthedocs.io/waits.html
        https://polling2.readthedocs.io/en/latest/examples.html#polling-for-selenium-webdriver-elements
        """

        # Find on the page to the username field
        # For more info about xpath: https://en.wikipedia.org/wiki/XPath
        username_field = driver.find_element_by_xpath('//input[@name="username"]')
        # Clear field in case auto-filling is on
        username_field.clear()
        # Input my username in field
        username_field.send_keys(username)

        # Same as what we did for username but here for password
        password_field = driver.find_element_by_xpath('//input[@name="password"]')
        password_field.clear()
        password_field.send_keys(password)

        # Pressing Return/Enter here is the equivalent to clicking the Submit button
        password_field.send_keys(Keys.RETURN)

        # If instead clicking is preferred - one can use the two lines below
        # submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
        # submit_button.click()

        sleep(4)

        # Click not now on "Save Info" popup
        not_now_button = driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]"
        )
        not_now_button.click()
        sleep(2)

        # Click not now on "Notification" popup
        # You Have to repeat the call to the driver element in order for it to work
        not_now_button = driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]"
        )  # Needed as recall
        not_now_button.click()
        sleep(2)
