from final_project.actions.login import driver
from time import sleep


def like():
    """ Function to automatically like a picture
    :return: 0 or 1 where 1 = one picture liked
    :rtype: int
    """
    like_icons = driver.find_elements_by_xpath("//*[contains(@aria-label, 'Like')]")
    unlike_icons = driver.find_elements_by_xpath("//*[contains(@aria-label, 'Unlike')]")

    for icon in unlike_icons or like_icons:

        height = icon.get_attribute("height")
        fill_color = icon.get_attribute("fill")

        # Ensuring it is the correct icon and that it has not been liked before

        if height == "24" and fill_color == "#ed4956":
            # Fill color of a post already liked is #ed4956
            print("Picture already liked.")
            return 0

        elif height == "24" and fill_color == "#262626":
            # Fill color of post NOT liked is #262626
            # ('..') is used here to fetch the parent of icon using xpath
            like_button = icon.find_element_by_xpath('..')
            like_button.click()
            print("Picture liked :)")
            sleep(2)
            return 1

        else:  # pragma: no cover
            pass
