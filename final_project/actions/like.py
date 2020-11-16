from final_project.actions.login import driver
from time import sleep


def like():
    like_icons = driver.find_elements_by_xpath("//*[contains(@aria-label, 'Like')]")

    for icon in like_icons:

        fill_color = icon.__getattribute__("fill")
        height = icon.__getattribute__("height")

        # Ensuring it is the correct icon and that it has not been liked before
        if height == "24" and fill_color == "262626":
            # Fill color of post NOT liked is #262626
            like_button = icon.find_element_by_xpath('..')
            like_button.click()
            sleep(2)

        elif height == "24" and fill_color == "ed4956":
            # Fill color of a post liked is #ed4956
            print("Picture already liked.")
            pass

        else:
            print("Nothing to like")
            pass
