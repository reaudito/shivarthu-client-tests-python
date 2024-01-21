
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
from utils.profile_validation_functions import add_profile, view_profile_details, add_profile_stake, add_challenge_evidence, add_juror_stake, change_period, draw_juror
from utils.account_info import account_info
from utils.common_functions import sign_in, sign_in_contract
# from utils.gecko_path import gecko_driver_path





options = Options()
options.page_load_strategy = 'normal'
options.add_argument("-profile")
options.add_argument("/home/amiya/snap/firefox/common/.mozilla/firefox/0m6bcq5b.shivarthu")

class ProfileValidationTests(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver (in this case, Chrome)
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
        self.driver.maximize_window()     

    # def test_sign_in(self):
    #     print("test sign in")
    #     sign_in(self, account_info['alice'])        
    #     time.sleep(10)
        
    def test_add_profile(self):
        print("test_add_profile")
        sign_in(self, account_info['alice']) 
        add_profile(self)
        sign_in_contract(self, account_info['alice'])
        view_profile_details(self)
        time.sleep(10)
        
    
    def test_add_profile_stake(self):
        print("test_add_profile_stake")
        sign_in(self, account_info['bob'])
        add_profile_stake(self, account_info['alice'], 500)
        sign_in_contract(self, account_info['bob'])
        time.sleep(10)
        sign_in(self, account_info['alice_stash'])
        add_profile_stake(self, account_info['alice'], 500)
        sign_in_contract(self, account_info['alice_stash'])
    
    def test_challenge_evidence(self):
        print("test_challenge_evidence")
        sign_in(self, account_info['bob_stash'])
        add_challenge_evidence(self, account_info['alice'], 60)
        sign_in_contract(self, account_info['bob_stash'])
    
    def test_juror_stake(self):
        print("test_juror_stake")
        sign_in(self, account_info['charlie'])
        add_juror_stake(self, account_info['alice'], 100)
        sign_in_contract(self, account_info['charlie'])
        sign_in(self, account_info['dave'])
        add_juror_stake(self, account_info['alice'], 500)
        sign_in_contract(self, account_info['dave'])
        sign_in(self, account_info['eve'])
        add_juror_stake(self, account_info['alice'], 1000)
        sign_in_contract(self, account_info['eve'])
        sign_in(self, account_info['ferdie'])
        add_juror_stake(self, account_info['alice'], 1500)
        sign_in_contract(self, account_info['ferdie'])
        sign_in(self, account_info['charlie_stash'])
        add_juror_stake(self, account_info['alice'], 2000)
        sign_in_contract(self, account_info['charlie_stash'])
    
    def test_change_period_from_evidence(self):
        print("test change period")
        sign_in(self, account_info['bob'])
        change_period(self, account_info['alice'], 10)
        sign_in_contract(self, account_info['bob'])
        sleep(60)
        
    def test_change_period_from_staking(self):
        print("test change period")
        sign_in(self, account_info['bob'])
        change_period(self, account_info['alice'], 600)
        sign_in_contract(self, account_info['bob'])
        sleep(60)
    
    def test_draw_juror(self):
        print("test juror stake")
        sign_in(self, account_info['bob'])
        draw_juror(self, account_info['alice'], 5)
        sign_in_contract(self, account_info['bob'])
        sleep(60)
        
        

        
              

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

