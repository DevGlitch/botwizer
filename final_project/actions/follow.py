import os
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from final_project.actions.login import driver
from final_project.actions.post import *from final_project.csci_utils.io.io import atomic_write
from csci_utils.io.io import atomic_write


def follow():
    """ To follow an account while on their profile"""
    # Click follow button on profile page
    # Only works if you are not following the profile already
    follow_button = driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
    follow_button.click()
    print("Started following account...")
    sleep(2)


def unfollow():
    """ To unfollow an account while on their profile"""
    # Click on icon with icon user and check mark
    following_icon = driver.find_element_by_class_name("yZn4P")
    following_icon.click()
    sleep(2)
    # Popup opens and click unfollow
    unfollow_button = driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]")
    unfollow_button.click()
    sleep(2)


def close_followers_window():  # pragma: no cover
    # Click on the cross to close the followers popup window
    try:
        close_button = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
        print("Closing followers popup...")
        close_button.click()
        sleep(2)
    except NoSuchElementException:
        pass


def get_followers():
    """ To get the full list of followers from an account """
    view_followers = driver.find_element_by_xpath("//a[contains(@href,'/followers')]")
    view_followers.click()
    print("Checking list of followers...")
    sleep(2)

    # Follower popup
    # I noticed that this xpath sometimes fluctuates which broke the code so had to consider that
    # This is not a normal behavior for an xpath... But this below fix the issue
    try:
        follower_popup = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    except NoSuchElementException:  # pragma: no cover
        follower_popup = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")

    # Scrolling until the end of the popup
    end, beginning = 0, 1
    while end != beginning:
        end = beginning
        sleep(1)
        try:
            beginning = driver.execute_script(
                "arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight;",
                follower_popup
            )
        except StaleElementReferenceException:  # pragma: no cover
            continue

    # Find all username elements
    ele_user = follower_popup.find_elements_by_tag_name('a')
    usernames = [username.text for username in ele_user if username.text != '']

    # Closing popup
    close_followers_window()

    return usernames


def save_followers(file: str, followers: list):  # pragma: no cover
    """ Saving followers list locally and counting new followers
    :param file: str filepath of the txt file
    :param followers: usernames list from get_followers
    :return: return the number of new followers
    :rtype: int
    """
    new_followers = 0

    if len(followers) == 0:
        print("No followers found.")
        return 0

    elif os.path.exists(file):
        print("Updating followers.txt ...")
        with open(file, "a+") as f:
            for username in followers:
                if username not in f.read().strip().split():
                    f.write("%s\n" % username)
                    new_followers += 1
            f.close()

    else:
        with atomic_write(file, mode="w", as_file=True) as f:
            print("Creating followers.txt ...")
            for username in followers:
                f.write("%s\n" % username)
                new_followers += 1

    return new_followers
