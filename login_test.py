from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.demoblaze.com/index.html"
USER_VALID_1 = "your_valid_username" 
PASS_VALID_1 = "your_valid_password" 
import time

def test_valid_login(driver, rand_number):
    try:
        driver.get(URL)
        driver.implicitly_wait(5)
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='login2']"))
        )
        login_button.click()
        
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='loginusername']"))
        )
        username_field.send_keys(USER_VALID_1 + str(rand_number))
        
        password_field = driver.find_element(By.XPATH, "//input[@id='loginpassword']")
        password_field.send_keys(PASS_VALID_1)
        
        login_submit_button = driver.find_element(By.XPATH, "//button[text()='Log in']")
        login_submit_button.click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(URL))
        assert driver.current_url == URL
        time.sleep(2)
        
        username_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@id='nameofuser']"))
        )
        print("USERNAME ", username_element.text)
        assert USER_VALID_1 + str(rand_number) in username_element.text
        
        return True
    
    except Exception as e:
        print(f"Login test failed: {str(e)}")
        return False