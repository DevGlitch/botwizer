import unittest
from unittest import TestCase
from tempfile import mkdtemp, NamedTemporaryFile
# import os

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

from final_project.actions.comment import *
from final_project.actions.data_folder import *
from final_project.actions.decision import *
from final_project.actions.follow import *
from final_project.actions.like import *
from final_project.actions.login import *
from final_project.actions.pages import Pages as p
from final_project.actions.picture import *
from final_project.actions.search import *
from final_project.yolo.img_objects import *
# from final_project.yolo.vid_objects import *


class ActionsWithLogin(TestCase):
    def setUp(self):
        """ Setting up Chrome """
        # opts = Options()
        # opts.add_argument("--headless")
        # opts.add_argument("no-sandbox")

        # For running test locally add executable_path="drivers/chrome/chromedriver" options=opts
        # Make sure the chromedriver version matches your local Chrome version
        # DevGlitch local version: 86.0.4240.22
        self.driver = webdriver.Chrome()

    def test_basic(self):
        """ Basic test to ensure selenium is working correctly """
        self.driver.get("http://google.com")
        self.assertIn("Google", self.driver.title)

    def test_actions(self):
        """ Testing multiple actions that require being logged in """
        username = os.environ.get("test_username")
        password = os.environ.get("test_password")
        login(username, password)
        p.account_page("devglitchtest")
        open_first_post()
        # Checking to ensure media is not a video
        self.assertEqual(is_post_a_video(), 0)
        # Checking to ensure picture was not already liked
        lk = like()
        self.assertEqual(lk, 1)
        # Checking to ensure picture was liked already
        lk = like()
        self.assertEqual(lk, 0)
        next_post()
        post_comment("Hey!")
        p.account_page("jacksoncav")
        follow()
        unfollow()

    def tearDown(self):
        """ Tearing down Chrome """
        close_browser()


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
        self.assertEqual(detection, ['dog', 'car', 'car', 'motorbike'])

    # def test_vid(self):
    #
    #     vid = "test_files/test.mp4"
    #     detection = vid


if __name__ == "__main__":
    unittest.main()
