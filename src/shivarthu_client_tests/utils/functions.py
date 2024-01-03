import time
from utils.config import Config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import os



account_info = {
    'alice': {'seed': '//Alice', 'password': 'password123'},
    'bob': {'seed': '//Bob', 'password': 'securepass456'},
    'charlie': {'seed': '//Charlie', 'password': 'pass53453'},
    'dave': {'seed': '//Dave', 'password': 'peirujds88'},
    'eve': {'seed': '//Eve', 'password': '9353jdkeir'},
    'ferdie': {'seed': '//Ferdie', 'password': 'i9kd720834u'},
    'alice_stash': {'seed': '//Alice//stash', 'password': 'ierikd5732'},
    'bob_stash': {'seed': '//Bob//stash', 'password': 'passueris89348'},
    'charlie_stash': {'seed': '//Charlie//stash', 'password': 'cheeirus83483'},
    'dave_stash': {'seed': '//Dave//stash', 'password': 'dai93943hixd'},
    'eve_stash': {'seed': '//Eve//stash', 'password': 'ie9359EIIDwrir'},
    'ferdie_stash': {'seed': '//Ferdie//stash', 'password': "feeiiide8354"},    
}


# Accounts with initial balance

# ```
# alice
# alice_stash
# bob
# bob_stash
# ```

current_directory = os.path.dirname(os.path.realpath(__file__))


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

def add_profile(self, account):
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
 
    
    
    
       
    


