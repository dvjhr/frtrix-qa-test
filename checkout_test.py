from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CART_URL = "https://www.demoblaze.com/cart.html"

def test_checkout(driver):
    try:
        driver.get(CART_URL)
        driver.implicitly_wait(5)
        time.sleep(1)
        
        place_order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]"))
        )
        place_order_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        )
        
        driver.find_element(By.ID, "name").send_keys("John Doe")
        driver.find_element(By.ID, "country").send_keys("United States")
        driver.find_element(By.ID, "city").send_keys("New York")
        driver.find_element(By.ID, "card").send_keys("1234567890123456")
        driver.find_element(By.ID, "month").send_keys("12")
        driver.find_element(By.ID, "year").send_keys("2025")
        
        purchase_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Purchase')]")
        purchase_button.click()
        
        thank_you_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Thank you for your purchase!')]"))
        )
        print("THANK YOU ", thank_you_message.text)
        assert "Thank you for your purchase!" in thank_you_message.text
        
        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'sa-button-container')]//div[contains(@class, 'sa-confirm-button-container')]//button"))
        )
        time.sleep(1)
        ok_button.click()
        
        return True
    
    except Exception as e:
        print(f"Checkout test failed: {str(e)}")
        return False