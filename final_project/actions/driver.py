from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options


def set_driver_firefox():
    """ Setting up Chrome with specific options and chromedriver
    :return: chrome webdriver
    """

    # Firefox Options
    opts = Options()

    # Headless mode to avoid seeing and interfering with what the bot is doing
    # Also note that this helps running the script slightly faster
    # Switch to False if you want to see the browser running
    opts.headless = True  # For Travis CI make sure it is set to True

    # Selenium webdriver to control Chrome
    driver = webdriver.Firefox(options=opts)

    # Timeout waiting time for pages to load
    driver.implicitly_wait(5)

    print("Launching Firefox...")
    return driver


# I had to unfortunately give up the chromedriver as I ran into the issue
# that it doesn't support unicode after FFFF which means no emojis...
# See here: https://bugs.chromium.org/p/chromedriver/issues/detail?id=2269
# This is the reason why I switched to Firefox and do not recommend using Chrome

# def set_driver_chrome():
#     """ Setting up Chrome with specific options and chromedriver
#     :return: chrome webdriver
#     """
#
#     opts = Options()
#     opts.add_experimental_option("detach", True)
#
#     # To avoid seeing and interfering with what the bot is doing
#     # Also note that this helps running the script slightly faster
#     opts.add_argument("--headless")
#     opts.add_argument("--incognito")
#     opts.add_argument("no-sandbox")
#
#     # Selenium webdriver to control Chrome
#     driver = webdriver.Chrome(options=opts)
#
#     # Timeout waiting time for pages to load
#     driver.implicitly_wait(15)
#
#     print("Launching Chrome...")
#     return driver


# For Chrome, add to travis.yml this:
# addons:
#     chrome: stable
# before_script:
#     - CHROME_MAIN_VERSION=`google-chrome-stable --version | sed -E 's/(^Google Chrome |\.[0-9]+ )//g'`
#     - CHROMEDRIVER_VERSION=`curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_MAIN_VERSION"`
#     - curl "https://chromedriver.storage.googleapis.com/${CHROMEDRIVER_VERSION}/chromedriver_linux64.zip" -O
#     - unzip chromedriver_linux64.zip -d ~/bin
