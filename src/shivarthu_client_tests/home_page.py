
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

    def test_sign_in(self):
        # Load the Google homepage
        self.driver.get(Config.BASE_URL)
        time.sleep(2)
        # Find the button by its ID
        sign_in_button_id = "sign-in-button"
        button = self.driver.find_element(By.ID, sign_in_button_id)
        # Click the button
        button.click()
        time.sleep(3)  
        seed_input = self.driver.find_element(By.XPATH, "//*[contains(@name, 'seed')]")     
        seed = "//Alice"
        seed_input.send_keys(seed)
        seed_input.send_keys(Keys.RETURN)
        password_input = self.driver.find_element(By.XPATH, "//*[contains(@name, 'password')]")
        password = "12345"
        password_input.send_keys(password) 
        password_input.send_keys(Keys.RETURN)
        time.sleep(3)  
        seed_submit_button =  self.driver.find_element(By.ID, "seed-submit-button")
        print(seed_submit_button)
        seed_submit_button.submit()
        time.sleep(50)

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

