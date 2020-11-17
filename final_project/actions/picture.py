from final_project.actions.login import driver
from time import sleep
from urllib.parse import urlparse
import requests
# from csci_utils.io.io import atomicwrite
import os


def open_first_pic():
    # Open the first post/picture available on the page
    # This is following human behaviors instead of opening by getting the url
    pic = driver.find_element_by_class_name("kIKUG")
    pic.click()
    sleep(2)


def get_src_img():
    # Get the src link of the image opened
    img = driver.find_element_by_xpath("//img")
    return img.get_attribute("src")  # ISSUE it includes in url ?.... after img extension - need to clean url


def get_src_video():
    # Get the src link of the image opened
    img = driver.find_element_by_xpath("//video")
    return img.get_attribute("src")


def get_img():
    # Download image locally
    page_images = driver.find_elements_by_xpath("//img")

    for img in page_images:
        sizes = img.get_attribute("sizes")

        if sizes > "293px":
            # 293px is the size of the post preview
            # Any picture bigger than 293px are a post picture
            # So this will gives you only one url
            src = img.get_attribute("src")
            url = urlparse(src).path
            print(url)
            filename = os.path.basename(url)
            print(filename)

            with requests.get(url, stream=True) as req:
                req.raise_for_status()

        else:
            pass

    # filename = os.path.basename(url)  # not working due to ?.... in url after img extension


def get_vid():
    # Download video locally
    page_videos = driver.find_elements_by_xpath("//video")
    ...


def next_pic():
    # Click on the right arrow to go to next post/picture
    next_button = driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
    next_button.click()
    sleep(2)


def close_pic():
    # Click on the cross to close the post/picture
    close_button = driver.find_element_by_class_name("wpO6b")  # might need to use xpath here to prevent errors
    close_button.click()
    sleep(2)


# save picture link with pandas?

# temp save then use YOLO?

# if object detected then like...

# what about post that was posted before XXX date and want to ignore?
# find post created after XXX date probably better idea
# date would be based on the last date we run the program?
