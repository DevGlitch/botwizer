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
    print("Opening first picture/post...")
    pic.click()
    sleep(2)


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
                with requests.get(url, stream=True) as req:
                    # Checking if request is successful (None = no error)
                    if req.raise_for_status() is not None:
                        print("Error: URL of picture is incorrect...")
                        pass

                    # Writing file atomically locally
                    with atomic_write(path, as_file=False) as f:
                        print("Saving image...")
                        urlretrieve(url, filename=f)
                        print("Image saved :)")

                # Returning the image path in order to use with other functions

            else:
                # Pass if the picture is already present in the folder
                print("Picture already exists :(")

            # Returning path of the picture
            return path

        else:
            pass


def get_vid():
    # Find the first element containing video
    # The first element will always be the post's video
    page_video = driver.find_element_by_xpath("//video")

    # Getting the URL of the video
    url = page_video.get_attribute("src")

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
            if req.raise_for_status() is not None:
                print("Error: URL of video is incorrect :(")
                pass

            # Writing file atomically locally
            with atomic_write(path, as_file=False) as f:
                urlretrieve(url, filename=f)
                print("Video saved :)")

        # Returning the video path in order to use with other functions
        return f

    else:
        # Pass if the video is already present in the folder
        print("Video already exists :(")
        pass


def next_pic():
    # Click on the right arrow to go to next post/picture
    next_button = driver.find_element_by_class_name("coreSpriteRightPaginationArrow")
    print("Opening next picture/post...")
    next_button.click()
    sleep(2)


def close_pic():
    # Click on the cross to close the post/picture
    close_button = driver.find_element_by_class_name("wpO6b")  # might need to use xpath here to prevent errors
    print("Closing picture/post...")
    close_button.click()
    sleep(2)
