import time
from utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os


def add_balance_tranfer(self, to_account , amount):
    self.driver.get(Config.BASE_URL + "/transfer-balance")
    time.sleep(5)
    stake_input = self.driver.find_element(By.XPATH, "//*[contains(@name, 'destination_account')]")  
    stake_input.send_keys(to_account['public_key'])
    stake_input.send_keys(Keys.RETURN)
    stake_input = self.driver.find_element(By.XPATH, "//*[contains(@name, 'tranfer_balance')]")  
    stake_input.send_keys(amount)
    stake_input.send_keys(Keys.RETURN)
    time.sleep(5)
    submit_button = self.driver.find_element(By.XPATH, "//*[contains(@type, 'submit')]")  
    submit_button.submit() 
    time.sleep(5)