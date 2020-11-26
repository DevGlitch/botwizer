from final_project.actions.login import driver
from time import sleep
from urllib.parse import urlparse
from urllib.request import urlretrieve
import requests
from final_project.csci_utils.io.io import atomic_write
import os


def open_first_pic():
    # Open the first post/picture available on the page
    # This is following human behaviors instead of opening by getting the url
    pic = driver.find_element_by_class_name("kIKUG")
    pic.click()
    sleep(2)


'''def get_src_img():
    # Get the src link of the image opened
    img = driver.find_element_by_xpath("//img")
    return img.get_attribute("src")  # ISSUE it includes in url ?.... after img extension - need to clean url'''


def get_src_video():
    # Get the src link of the image opened
    img = driver.find_element_by_xpath("//video")
    return img.get_attribute("src")


def get_img():
    # Find all elements containing img
    page_images = driver.find_elements_by_xpath("//img")

    # Check all images and getting their attribute sizes
    for img in page_images:
        sizes = img.get_attribute("sizes")

        # To find the post image
        if sizes > "293px":
            # 293px is the size of the post preview
            # Any picture bigger than 293px is a post picture
            # So this will gives you only one url
            url = img.get_attribute("src")

            # Parsing the URL in order to get the filename path
            get_filename = urlparse(url).path

            # Image filename
            filename = os.path.basename(get_filename)

            # Path were images will be saved
            path = os.path.join("data/images/", filename)
            print("Path = ", path)

            # Making sure file doesn't exist already
            if not os.path.exists(filename):

                # Using package requests to check for any http issue like 4XX or 5XX errors
                with requests.get(url, stream=True) as req:
                    # Checking if request is successful (None = no error)
                    if req.raise_for_status() is not None:
                        print("Error: URL of picture is incorrect.")
                        pass

                    # Writing file atomically locally
                    with atomic_write(filename, as_file=False) as f:
                        print("going to save")

                        urlretrieve(url, filename=f)

                        print("saved the image")

                # Returning the image location in order to use with other functions
                return filename  # or file path ???

            else:
                print("Picture already exists.")
                pass

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
