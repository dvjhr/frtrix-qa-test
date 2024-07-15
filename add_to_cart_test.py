from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://www.demoblaze.com/"
CART_URL = "https://www.demoblaze.com/cart.html"

def test_add_product_to_cart(driver, amounts):
    added_items = {}
    try:
        for amount in range(1, amounts + 1):
            print(amount)
            driver.get(URL)
            time.sleep(1)
            driver.implicitly_wait(5)
        
            phones_category = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Phones')]"))
            )
            phones_category.click()
        
            prod_loc = f"(//div[@id='tbodyid']//a[@class='hrefch'])[{amount}]"
            product = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, prod_loc))
            )
            prod_href = driver.find_element(By.XPATH, prod_loc).get_attribute("href")
            product.click()
            
            WebDriverWait(driver, 10).until(EC.url_contains(prod_href))
            assert f"prod.html?idp_={amount}" in driver.current_url
            
            product_title = driver.find_element(By.XPATH, "//h2[@class='name']").text
            added_items[product_title] = added_items.get(product_title, 0) + 1
            
            add_to_cart_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Add to cart')]")
            add_to_cart_button.click()
            
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            assert "Product added" in alert.text
            alert.accept()
        
        driver.get(CART_URL)
        time.sleep(2)
        
        cart_items = {}
        rows = driver.find_elements(By.XPATH, "//table[@class='table table-bordered table-hover table-striped']//tr")
        for row in rows[1:]:
            title = row.find_element(By.XPATH, "./td[2]").text
            cart_items[title] = cart_items.get(title, 0) + 1
        
        assert added_items == cart_items
        return True
    
    except Exception as e:
        print(f"Add to cart test failed: {str(e)}")
        return False