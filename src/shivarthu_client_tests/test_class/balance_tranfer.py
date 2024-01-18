
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
from utils.balance_tranfer_functions import add_balance_tranfer
from utils.account_info import account_info
from utils.common_functions import sign_in, sign_in_contract



options = Options()
options.page_load_strategy = 'normal'
options.add_argument("-profile")
options.add_argument("/home/amiya/snap/firefox/common/.mozilla/firefox/0m6bcq5b.shivarthu")

class BalanceTransfers(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver (in this case, Chrome)
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
        self.driver.maximize_window()     
        
    
    def test_balance_transfer(self):
        sign_in(self, account_info['bob'])
        add_balance_tranfer(self, account_info['charlie'], 1000000000000000)
        sign_in_contract(self, account_info['bob'])
        # sign_in(self, account_info['bob'])
        # add_balance_tranfer(self, account_info['dave'], 10000000)
        # sign_in_contract(self, account_info['bob'])
    def test_balance_transfer2(self):
        sign_in(self, account_info['bob'])
        add_balance_tranfer(self, account_info['dave'], 1000000000000000)
        sign_in_contract(self, account_info['bob'])
    def test_balance_transfer3(self):
        sign_in(self, account_info['bob'])
        add_balance_tranfer(self, account_info['eve'], 1000000000000000)
        sign_in_contract(self, account_info['bob'])
    def test_balance_transfer4(self):
        sign_in(self, account_info['bob'])
        add_balance_tranfer(self, account_info['ferdie'], 1000000000000000)
        sign_in_contract(self, account_info['bob'])
    def test_balance_transfer5(self):
        sign_in(self, account_info['bob'])
        add_balance_tranfer(self, account_info['charlie_stash'], 1000000000000000)
        sign_in_contract(self, account_info['bob'])
    def test_balance_transfer6(self):
        sign_in(self, account_info['bob'])
        add_balance_tranfer(self, account_info['dave_stash'], 1000000000000000)
        sign_in_contract(self, account_info['bob'])
    def test_balance_transfer7(self):
        sign_in(self, account_info['bob'])
        add_balance_tranfer(self, account_info['eve_stash'], 1000000000000000)
        sign_in_contract(self, account_info['bob'])
    def test_balance_transfer8(self):
        sign_in(self, account_info['bob'])
        add_balance_tranfer(self, account_info['ferdie_stash'], 1000000000000000)
        sign_in_contract(self, account_info['bob'])
        
        

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

