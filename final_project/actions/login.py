from selenium.webdriver.common.keys import Keys
from time import sleep
# from final_project.actions.__init__ import set_driver
from final_project.actions.driver import set_driver
from selenium.common.exceptions import NoSuchElementException

driver = set_driver()


def login(username: str, password: str):

    # Launch Instagram Page
    driver.get("https://www.instagram.com")
    print("Loading Instagram page...")
    # Using sleep to ensure the page has the time to load
    # This will be used multiple times throughout the code
    sleep(2)

    # Find on the page to the username field
    # For more info about xpath: https://en.wikipedia.org/wiki/XPath
    print("Entering credentials...")
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
    print("Connecting...")

    # If instead clicking is preferred - one can use the two lines below
    # submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
    # submit_button.click()

    sleep(4)

    # Click not now on "Save Info" popup
    not_now_button = driver.find_element_by_xpath(
        "//button[contains(text(), 'Not Now')]"
    )
    not_now_button.click()
    sleep(4)

    # Click not now on "Notification" popup
    # This popup is not always present
    try:
        not_now_button = driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]"
        )  # Needed as recall
        not_now_button.click()
    except NoSuchElementException:
        pass

    print("Successfully connected :)")
    sleep(2)


def close_browser():
    print("Closing Chrome...")
    driver.quit()  # Close browser and driver. For closing just the tab .close()
    print("Chrome session successfully closed.")
