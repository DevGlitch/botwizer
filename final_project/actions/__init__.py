from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def set_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # Selenium webdriver to control Chrome
    driver = webdriver.Chrome(executable_path="../drivers/chrome/chromedriver", options=chrome_options)
    return driver


def close_browser():
    closing = set_driver().quit()  # Close browser and driver. For closing just the tab .close()
    return closing
