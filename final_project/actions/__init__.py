from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def set_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # Selenium webdriver to control Chrome
    driver = webdriver.Chrome(
        executable_path="drivers/travis/chromedriver", options=chrome_options
    )
    print("Launching Chrome...")
    return driver
