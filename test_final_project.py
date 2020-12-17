import unittest
from pathlib import Path
from tempfile import NamedTemporaryFile, mkdtemp
from unittest import TestCase

from final_project.actions.comment import *
from final_project.actions.data_folder import *
from final_project.actions.decision import *
from final_project.actions.follow import *
from final_project.actions.like import *
from final_project.actions.login import *
from final_project.actions.pages import Pages as p
from final_project.actions.post import *
from final_project.actions.search import *
from final_project.yolo.img_objects import *

# from final_project.yolo.vid_objects import *


class ActionsWithLogin(TestCase):
    def setUp(self):
        """ Setting up Chrome and Logging-in"""
        username = os.environ.get("test_username")
        password = os.environ.get("test_password")
        login(username, password)

    def test_actions(self):
        """ Testing multiple actions that require being logged in. This is done in one session. """

        # Check to ensure it goes to the right account page
        p.your_account_page("devglitchtest")

        # Check to ensure it opened the first post
        open_first_post()
        self.assertEqual(
            driver.current_url,
            "https://www.instagram.com/p/CIZ74mIHLTMeVBcPFgK_-uZruD1iZb1PtnLI_Y0/",
        )

        # Check to ensure media is not a video
        vid_or_img = is_post_a_video()
        self.assertEqual(vid_or_img, 0)

        # Check to ensure we can get the image
        img = get_img()
        assert os.path.exists(img)

        # Check to ensure it detects the image already exist
        img = get_img()
        self.assertEqual(
            Path(img).name, "129722442_199445988466445_8180753295980843210_n.jpg"
        )

        # Check to ensure picture was not already liked
        # Running a second time pytest with this will throw an error unless
        # we use an unlike function or unlike directly on the post in question
        lk = like()
        self.assertEqual(lk, 1)

        # Check to ensure picture was liked already
        lk = like()
        self.assertEqual(lk, 0)

        # Check to ensure going to the next post is correct
        next_post()
        self.assertEqual(
            driver.current_url,
            "https://www.instagram.com/p/CIZ7vePHk6r7LMZToZX2Sg-vpk0Ynm4-XIUT2g0/",
        )

        # Check to ensure posting a comment is successful
        cmt = post_comment("Hey! 👍👍")
        self.assertEqual(cmt, 1)

        # Check to ensure it can close the post
        close_post()
        self.assertNotEqual(
            driver.current_url,
            "https://www.instagram.com/p/CIZ7vePHk6r7LMZToZX2Sg-vpk0Ynm4-XIUT2g0/",
        )
        self.assertEqual(driver.current_url, "https://www.instagram.com/devglitchtest/")

        # Check to ensure it can get a specific account page
        p.account_page("jacksoncav")
        self.assertEqual(driver.current_url, "https://www.instagram.com/jacksoncav/")

        # Ensuring it can follow and unfollow
        follow()
        unfollow()

        # Check to ensure it get followers and returns the correct list
        # Too tricky to test due to changes
        # followers = get_followers()
        # self.assertEqual(len(followers), 111)

        # Check to ensure search account works
        search_account("harvard")
        self.assertEqual(driver.current_url, "https://www.instagram.com/harvard/")

        # Check to ensure search hashtag works
        search_hashtag("dog")
        self.assertEqual(
            driver.current_url, "https://www.instagram.com/explore/tags/dog/"
        )

        # Check to ensure search general works
        search_general("motorcycleofin")
        self.assertEqual(
            driver.current_url,
            "https://www.instagram.com/explore/tags/motorcycleofinstagram/",
        )

        # Check to ensure video media are detected
        driver.get("https://www.instagram.com/p/CIOyhCSBFXs/")
        vid_or_img = is_post_a_video()
        self.assertEqual(vid_or_img, 1)

        # Check to ensure we can get the video
        vid = get_vid()
        sleep(5)
        assert os.path.exists(vid)

        # Check to ensure it get the first frame of the video
        vid = get_vid()
        self.assertEqual(
            Path(vid).name, "128383303_145819103956437_4362863989620933869_n.jpg"
        )

    def tearDown(self):
        """ Tearing down the setup """
        close_browser()
        delete_folder("images")
        delete_folder("videos")


class Decision(TestCase):
    def test_decision(self):
        """ Testing to ensure function return the correct bool """
        self.assertEqual(decision(1), True)
        self.assertEqual(decision(0), False)


class DataFolder(TestCase):
    @staticmethod
    def test_delete_dir():
        """ Testing to ensure it correctly delete directories """
        tmp_dir = mkdtemp()
        assert os.path.exists(tmp_dir)
        delete_folder(tmp_dir)
        assert not os.path.exists(tmp_dir)

    @staticmethod
    def test_delete_file():
        """ Testing to ensure it correctly delete files """
        tmp_file = NamedTemporaryFile()
        assert os.path.exists(tmp_file.name)
        delete_file(tmp_file.name)
        assert not os.path.exists(tmp_file.name)


class YOLOTesting(TestCase):
    def test_one_object(self):
        """ Ensuring that YOLO detects the correct object"""
        img = "test_files/test_one_obj.jpg"
        detection = img_object_detection(img)
        self.assertEqual(detection, ["dog"])

    def test_no_object(self):
        """ Ensuring that YOLO doesn't detect any object"""
        img = "test_files/test_no_obj.jpg"
        detection = img_object_detection(img)
        self.assertEqual(detection, None)

    def test_multi_objects(self):
        """ Ensuring that YOLO detects the correct number of object """
        img = "test_files/test_multi_obj.jpg"
        detection = img_object_detection(img)
        self.assertEqual(detection, ["dog", "car", "car", "motorbike"])

    # def test_vid(self):
    # """ Ensuring that YOLO detects objects in a video """
    #     vid = "test_files/test.mp4"
    #     detection = vid
    #     self.assertEqual(detection, [...", "...", "...", "..."])


if __name__ == "__main__":
    unittest.main()
