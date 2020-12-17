from selenium.webdriver.common.keys import Keys
from time import sleep
from final_project.actions.driver import set_driver_firefox
from selenium.common.exceptions import NoSuchElementException

driver = set_driver_firefox()


def login(username: str, password: str):

    # Launch Instagram Page
    driver.get("https://www.instagram.com")
    print("Loading Instagram page...")
    # Using sleep to ensure the page has the time to load
    # This will be used multiple times throughout the code
    sleep(2)

    # On December 7th Insta added a new popup regarding cookies...
    # So another step in login is necessary
    # This popup is present everytime as selenium uses Firefox with private sessions

    # Click accept on cookie popup
    try:  # pragma no cover
        accept_button = driver.find_element_by_xpath(
            "//button[contains(text(), 'Accept')]"
        )
        accept_button.click()
        sleep(3)
    except NoSuchElementException:  # pragma no cover
        pass

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
        )
        not_now_button.click()
    except NoSuchElementException:  # pragma: no cover
        pass

    print("Successfully connected :)")
    sleep(2)


def close_browser():
    print("Closing browser...")
    driver.quit()  # Close browser and driver. For closing just the tab .close()
    print("Browser session successfully closed.")
