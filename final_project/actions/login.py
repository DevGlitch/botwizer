from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


class Login:

    def __init__(self, username, password):
        # From environment variables - Might need to hash in the future
        self.username = username
        self.password = password

        # Option to prevent Chrome to close tab after task is done
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        # Selenium webdriver to control Chrome
        self.driver = webdriver.Chrome(
            executable_path="../drivers/chrome/chromedriver",
            options=chrome_options
        )
        # https://chromedriver.chromium.org/downloads
        # Cookiecutter option Chrome vs Firefox ??
        # self.driver = webdriver.Firefox()  #

    def close_browser(self):
        self.driver.close()  # Close only the tab not the browser. For closing browser .quit()

    def login(self):
        # Make it easier to call driver
        driver = self.driver
        # Launch Instagram Page
        driver.get("https://www.instagram.com")

        # Using sleep to ensure the page has the time to load
        # This will be used multiple times throughout the code
        sleep(2)

        # Find the page on the page to the username field
        # For more info about xpath: https://en.wikipedia.org/wiki/XPath
        username_field = driver.find_element_by_xpath("//input[@name=\"username\"]")
        # Clear field in case auto-filling is on
        username_field.clear()
        # Input my username in field
        username_field.send_keys(self.username)

        password_field = driver.find_element_by_xpath("//input[@name=\"password\"]")
        password_field.clear()
        password_field.send_keys(self.password)

        # Pressing Return/Enter is the equivalent to clicking the Submit button
        password_field.send_keys(Keys.RETURN)

        # If instead clicking is preferred - one can use the two lines below
        # submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
        # submit_button.click()

        sleep(4)

        # Click not now on "Save Info" popup
        not_now_button = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
        not_now_button.click()
        sleep(2)

        # Click not now on "Notification" popup
        # You Have to repeat the call to the driver element in order for it to work
        not_now_button = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")  # Needed as a recall
        not_now_button.click()
        sleep(10)
