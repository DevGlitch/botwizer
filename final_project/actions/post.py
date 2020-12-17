from final_project.actions.login import driver
from time import sleep
from urllib.parse import urlparse
from urllib.request import urlretrieve
import requests
from csci_utils.io.io import atomic_write
import os
from selenium.common.exceptions import NoSuchElementException


def open_first_post():
    # Open the first post/picture available on the page
    # This is following human behaviors instead of opening by getting the url
    # pic = driver.find_element_by_class_name("kIKUG")  # If you click follow before this it doesn't work
    pic = driver.find_element_by_class_name("eLAPa")
    print("Opening first post...")
    pic.click()
    sleep(2)


def is_post_a_video():
    # Checking if the post is a video or not
    try:
        # Trying to find element that is a post with a video
        driver.find_element_by_class_name("tWeCl")
        return True
    except NoSuchElementException:
        return False


def get_img():
    # Find all elements containing img
    page_images = driver.find_elements_by_xpath("//img")

    # Check all images and getting their attribute sizes
    for img in page_images:
        sizes = img.get_attribute("sizes")

        # To find the post's image
        if sizes > "293px":
            # 293px is the size of the post preview
            # Any picture bigger than 293px is a post picture
            # So this will gives you only one url
            url = img.get_attribute("src")

            # Parsing the URL in order to get the filename path
            get_filename = urlparse(url).path

            # Image filename
            img_name = os.path.basename(get_filename)

            # Create folders to store the image
            os.makedirs("data/images", exist_ok=True)

            # Path where the image will be saved
            path = os.path.join(os.path.abspath("data"), "images/", img_name)

            # Making sure the file doesn't exist already
            if not os.path.exists(path):

                # Using package requests to check for any http issue like 4XX or 5XX errors
                headers = {}

                with requests.get(url, stream=True, headers=headers) as req:
                    # Checking if request is successful (None = no error)
                    if req.raise_for_status() is not None:  # pragma: no cover
                        print("Error: URL of picture is incorrect...")
                        pass

                    # Writing file atomically locally
                    with atomic_write(path, as_file=False) as f:
                        print("Saving image...")
                        urlretrieve(url, filename=f)
                        print("Image saved :)")

            else:
                # Pass if the picture is already present in the folder
                print("Picture already exists :(")

            # Returning path of the picture
            return path

        else:  # pragma: no cover
            pass


def get_vid():
    # Find the first element containing video
    # The first element will always be the post's video
    page_video = driver.find_element_by_xpath("//video")

    # Getting the URL of the video
    # url = page_video.get_attribute("src")
    # On December 8th Instagram changed something here which affected src that we were getting
    # Due to this and for now we will only save the first frame of the video as jpg - speed up bot
    url = page_video.get_attribute("poster")

    # Parsing the URL in order to get the filename path
    get_filename = urlparse(url).path

    # Video filename
    filename = os.path.basename(get_filename)

    # Create folders to store the video
    os.makedirs("data/videos", exist_ok=True)

    # Path where the video will be saved
    path = os.path.join("data/videos/", filename)

    # Making sure the video doesn't exist already
    if not os.path.exists(path):

        # Using package requests to check for any http issue like 4XX or 5XX errors
        with requests.get(url, stream=True) as req:
            # Checking if request is successful (None = no error)
            if req.raise_for_status() is not None:  # pragma: no cover
                print("Error: URL of video is incorrect :(")
                pass

            # Writing file atomically locally
            with atomic_write(path, as_file=False) as f:
                urlretrieve(url, filename=f)
                print("Video saved :)")

        # Returning the video path in order to use with other functions
        return path

    else:
        # Pass if the video is already present in the folder
        print("Video already exists :(")
        return path


def next_post():
    # Click on the right arrow to go to next post/picture
    next_button = driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
    print("Opening next post...")
    next_button.click()
    sleep(2)


def close_post():  # pragma: no cover
    # Click on the cross to close the post/picture
    # close_button = driver.find_element_by_class_name("wpO6b") # Error with the class
    try:
        close_button = driver.find_element_by_xpath("/html/body/div[5]/div[3]/button")
        print("Closing post...")
        close_button.click()
        sleep(2)
    except NoSuchElementException:
        pass
