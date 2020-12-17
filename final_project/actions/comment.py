# emojis: https://en.wikipedia.org/wiki/Emoji#Unicode_blocks
# chromedriver unicode after FFFF not supported: https://bugs.chromium.org/p/chromedriver/issues/detail?id=2269

from final_project.actions.login import driver
from selenium.webdriver.common.keys import Keys
from time import sleep


def post_comment(your_comment: str):
    """ Function that automatically add comments
    :param your_comment: str
    :return: 1 to use for counting posted comments
    :rtype: int
    """
    # Click on the text area to add a comment
    add_comment = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'Add a comment')]")
    add_comment.click()

    # Type your comment
    add_comment = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'Add a comment')]")
    print("Writing comment...")
    add_comment.send_keys(your_comment)
    sleep(1)

    # Press enter in order to submit comment
    add_comment.send_keys(Keys.RETURN)
    print("Comment posted :)")
    sleep(3)
    return 1
