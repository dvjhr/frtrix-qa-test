from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.demoblaze.com/"
USER_VALID_1 = "your_valid_username" 
PASS_VALID_1 = "your_valid_password" 

def test_valid_registration(driver, rand_number):
    try:
        driver.get(URL)
        driver.implicitly_wait(5)
        
        signup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='signin2']"))
        )
        signup_button.click()
        
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='sign-username']"))
        )
        username_field.send_keys(USER_VALID_1 + str(rand_number))
        
        password_field = driver.find_element(By.XPATH, "//input[@id='sign-password']")
        password_field.send_keys(PASS_VALID_1)
        
        signup_submit_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")
        signup_submit_button.click()
        
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("ALERT 1", alert)
        print("ALERT 2", alert.text)
        assert "Sign up successful" in alert.text
        alert.accept()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(URL))
        assert driver.current_url == URL
        
        return True
    
    except Exception as e:
        print(f"Registration test failed: {str(e)}")
        return False