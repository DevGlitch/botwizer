from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def set_driver():
    """ Setting up Chrome with specific options and chromedriver
    :return: chrome webdriver
    """

    opts = Options()
    opts.add_experimental_option("detach", True)

    # To avoid seeing and interfering with what the bot is doing
    # Also note that this helps running the script slightly faster
    # opts.add_argument("--headless")
    opts.add_argument("no-sandbox")

    # Selenium webdriver to control Chrome
    driver = webdriver.Chrome(options=opts)
    print("Launching Chrome...")
    return driver
