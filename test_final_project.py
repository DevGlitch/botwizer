import unittest
from unittest import TestCase
from tempfile import TemporaryDirectory, TemporaryFile, NamedTemporaryFile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        opts = Options()
        opts.headless = True
        # Path of the webdriver might be an issue for running in Travis...
        # DevGlitch local version: 86.0.4240.22
        # For running test locally add executable_path="drivers/chrome/chromedriver"
        # make sure the chromedriver version matches your local Chrome version
        self.driver = webdriver.Chrome(options=opts)

    def test_title(self):
        self.driver.get("http://google.com")
        self.assertIn("Google", self.driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


# Random test to be removed. - Build your tests here.
# def test():
    # pass
