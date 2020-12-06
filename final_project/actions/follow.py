from final_project.actions.login import driver
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


def follow():
    """ To follow an account while on their profile"""
    # Click follow button on profile page
    # Only works if you are not following the profile already
    follow_button = driver.find_element_by_xpath("//button[contains(text(), 'Follow')]")
    follow_button.click()
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


def get_followers():
    """ To get the full list of your followers """
    view_followers = driver.find_element_by_xpath("//a[contains(@href,'/followers')]")
    view_followers.click()
    print("Opening your followers list...")
    sleep(2)

    # p.scroll_down()
    # driver._make_driver_wait("/html/body/div[4]/div/div/div[2]")

    # Follower popup
    # I noticed that the xpath sometimes fluctuates which broke the code so had to consider that
    try:
        follower_popup = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
    except NoSuchElementException:
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
        except StaleElementReferenceException:
            continue

    # Find all username elements
    ele_user = follower_popup.find_elements_by_tag_name('a')
    usernames = [username.text for username in ele_user if username.text != '']

    return usernames
