import time
from utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def sign_in(self, account):
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
    seed_input.send_keys(account["seed"])
    seed_input.send_keys(Keys.RETURN)
    password_input = self.driver.find_element(By.XPATH, "//*[contains(@name, 'password')]")
    password_input.send_keys(account["password"]) 
    password_input.send_keys(Keys.RETURN)
    time.sleep(3)  
    seed_submit_button =  self.driver.find_element(By.ID, "seed-submit-button")
    # print(seed_submit_button)
    seed_submit_button.submit() 
    

def sign_in_contract(self, account):
    WebDriverWait(self.driver, 50).until(
    ec.element_to_be_clickable((By.ID, "input-password"))
    )
    input_password = self.driver.find_element(By.ID, "input-password")
    input_password.send_keys(account["password"])
    input_password.send_keys(Keys.RETURN)
    submit_button = self.driver.find_element(By.XPATH, "//*[contains(@type, 'submit')]")  
    submit_button.submit()
     