from final_project.actions.login import driver
from selenium.webdriver.common.keys import Keys
from time import sleep


def input_and_post_comment(your_comment: str):
    # Click on the text area to add a comment
    add_comment = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'Add a comment')]")
    add_comment.click()

    # Type your comment
    add_comment = driver.find_element_by_xpath("//textarea[contains(@placeholder, 'Add a comment')]")
    add_comment.send_keys(your_comment)
    sleep(1)

    # Press enter in order to submit comment
    add_comment.send_keys(Keys.RETURN)
    sleep(2)
