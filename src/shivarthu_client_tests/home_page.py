
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import csv
from datetime import datetime, timedelta
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import os
import unittest
from utils.config import Config



options = Options()
options.page_load_strategy = 'normal'
options.add_argument("-profile")
options.add_argument("/home/amiya/snap/firefox/common/.mozilla/firefox/0m6bcq5b.shivarthu")

class HomePageTest(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver (in this case, Chrome)
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
        self.driver.maximize_window()

    def test_google_search(self):
        # Load the Google homepage
        self.driver.get(Config.BASE_URL)
        time.sleep(10)


        # # Find the search input element by name
        # search_box = self.driver.find_element("name", "q")

        # # Type a search query
        # search_box.send_keys("Selenium with Python")

        # # Press Enter to perform the search
        # search_box.send_keys(Keys.RETURN)

        # # Verify that the search results page is displayed
        # self.assertIn("Selenium with Python", self.driver.title)

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

