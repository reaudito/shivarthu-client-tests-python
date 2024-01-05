
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
from utils.profile_validation_functions import add_profile, view_profile_details
from utils.account_info import account_info
from utils.common_functions import sign_in, sign_in_contract



options = Options()
options.page_load_strategy = 'normal'
options.add_argument("-profile")
options.add_argument("/home/amiya/snap/firefox/common/.mozilla/firefox/0m6bcq5b.shivarthu")

class HomePageTest(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver (in this case, Chrome)
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
        self.driver.maximize_window()     

    # def test_sign_in(self):
    #     print("test sign in")
    #     sign_in(self, account_info['alice'])        
    #     time.sleep(10)
        
    def test_add_profile(self):
        print("test profile validation")
        sign_in(self, account_info['alice']) 
        add_profile(self)
        sign_in_contract(self, account_info['alice'])
        time.sleep(20)
        view_profile_details(self)
        
    
    # def test_add_profile_stake(self):
    #     print("test add profile stake")
    #     sign_in(self, account_info['bob'])
        
        

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

