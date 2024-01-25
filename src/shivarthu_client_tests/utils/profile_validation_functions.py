import time
from utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os




current_directory = os.path.dirname(os.path.realpath(__file__))




def add_profile(self):
    self.driver.get(Config.BASE_URL + "/add-profile")
    time.sleep(2)
    name_input = self.driver.find_element(By.XPATH, "//*[contains(@name, 'name')]")  
    name_input.send_keys("Alice in Wonderland")
    name_input.send_keys(Keys.RETURN)   
    details_input = self.driver.find_element(By.XPATH, "//*[contains(@name, 'details')]")  
    details_data = """
    "Alice in Wonderland" is a timeless literary classic written by Lewis Carroll. 
    """
    details_input.send_keys(details_data)
    details_input.send_keys(Keys.RETURN)
    
    self.driver.execute_script("arguments[0].blur();", details_input)
    
    file_input = self.driver.find_element(By.ID, "file-upload")

    project_root = os.path.abspath(os.path.join(current_directory, '..', '..', '..'))

    file_data = os.path.join(project_root, 'files', 'movie.mp4')

    print("Project Root:", project_root)
    print("File Data:", file_data)
    file_input.send_keys(file_data)

    WebDriverWait(self.driver, 50).until(
    ec.element_to_be_clickable((By.ID, "profile-video-load"))
    )
    time.sleep(3) 
    
    submit_button = self.driver.find_element(By.XPATH, "//*[contains(@type, 'submit')]")  
    submit_button.submit()
    time.sleep(5)

def view_profile_details(self):
    view_profile_link = self.driver.find_element(By.CLASS_NAME, "view-profile-link")
    view_profile_link.click()
    time.sleep(5)

def add_profile_stake(self, for_account, stake):
    self.driver.get(Config.BASE_URL + "/add-profile-stake/" + for_account['public_key'])
    time.sleep(5)
    stake_input = self.driver.find_element(By.XPATH, "//*[contains(@name, 'profile-stake')]")  
    stake_input.send_keys(stake)
    stake_input.send_keys(Keys.RETURN)
    submit_button = self.driver.find_element(By.XPATH, "//*[contains(@type, 'submit')]")  
    submit_button.submit() 
    time.sleep(5)
      
def add_challenge_evidence(self, for_account):
    self.driver.get(Config.BASE_URL + "/schelling-game/" + for_account['public_key'])
    # Find the element by ID
    element = self.driver.find_element(By.ID, "end-period-time")

    # Get the initial value
    initial_value = element.get_attribute("innerHTML")
    print(f"Initial value: {initial_value}")

    # Check if the value changes to 0
    while True:
        current_value = element.get_attribute("innerHTML")
        if current_value == "0":
            print("Value changed to 0")
            break

        # Add a sleep or wait here to avoid continuous polling and CPU usage
        time.sleep(1)
    evidence_details = self.driver.find_element(By.XPATH, "//*[contains(@name, 'details')]")  
    evidence_details_data = """
    This is an invalid profile
    """
    evidence_details.send_keys(evidence_details_data)
    self.driver.execute_script("arguments[0].blur();", evidence_details)
    time.sleep(5) 
    submit_button = self.driver.find_element(By.XPATH, "//*[contains(@type, 'submit')]")  
    submit_button.submit() 
    time.sleep(5)

def add_juror_stake(self, for_account, stake):
    self.driver.get(Config.BASE_URL + "/schelling-game/" + for_account['public_key'])
    time.sleep(5)
    juror_stake_input = self.driver.find_element(By.XPATH, "//*[contains(@name, 'juror-stake')]")  
    juror_stake_input.send_keys(stake)
    juror_stake_input.send_keys(Keys.RETURN)
    time.sleep(5) 
    submit_button = self.driver.find_element(By.ID, "juror-stake") 
    submit_button.submit() 
    time.sleep(5)
    
def change_period(self, for_account):
    self.driver.get(Config.BASE_URL + "/schelling-game/" + for_account['public_key'])
    time.sleep(5) 
     # Find the element by ID
    element = self.driver.find_element(By.ID, "end-period-time")
     # Get the initial value
    initial_value = element.get_attribute("innerHTML")
    print(f"Initial value: {initial_value}")

    # Check if the value changes to 0
    while True:
        current_value = element.get_attribute("innerHTML")
        if current_value == "0":
            print("Value changed to 0")
            break

        # Add a sleep or wait here to avoid continuous polling and CPU usage
        time.sleep(1)  
    
    submit_button = self.driver.find_element(By.ID, "change-period")
    submit_button.submit()
    time.sleep(5)
    

def draw_juror(self, for_account, count):
    self.driver.get(Config.BASE_URL + "/schelling-game/" + for_account['public_key'])
    time.sleep(5)
    draw_juror = self.driver.find_element(By.ID, "iterations")
    draw_juror.send_keys(count)
    draw_juror.send_keys(Keys.RETURN)
    time.sleep(5)
    submit_button = self.driver.find_element(By.ID, "draw-jurors-submit")
    submit_button.submit()

def change_period_from_drawing(self, for_account):
    self.driver.get(Config.BASE_URL + "/schelling-game/" + for_account['public_key'])
    time.sleep(5) 
     # Find the element by ID
    element = self.driver.find_element(By.ID, "end-drawing-period-time")
     # Get the initial value
    initial_value = element.get_attribute("innerHTML")
    print(f"Initial value: {initial_value}")

    # Check if the value changes to 0
    while True:
        current_value = element.get_attribute("innerHTML")
        if current_value == "true":
            print("Value changed to true")
            break

        # Add a sleep or wait here to avoid continuous polling and CPU usage
        time.sleep(1)  
    
    submit_button = self.driver.find_element(By.ID, "change-period")
    submit_button.submit()
    time.sleep(5)

    

    


    
 
    
    
    
       
    


