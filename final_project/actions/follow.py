from final_project.actions.login import driver
from time import sleep


def follow():
    # Click follow button on profile page
    # Only works if you are not following the profile already
    follow_button = driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
    follow_button.click()
    sleep(2)


def unfollow():
    # Click on icon with icon user and check mark
    following_icon = driver.find_element_by_class_name("yZn4P")
    following_icon.click()
    sleep(2)
    # Popup opens and click unfollow
    unfollow_button = driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]")
    unfollow_button.click()
    sleep(2)
