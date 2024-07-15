import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

from register_test import test_valid_registration
from login_test import test_valid_login
from add_to_cart_test import test_add_product_to_cart
from checkout_test import test_checkout

import random
number = random.randint(1, 99)

EDGE_DRIVER_PATH = r"msedgedriver.exe"  

def setup_driver():
    edge_options = Options()
    edge_options.use_chromium = True
    service = Service(EDGE_DRIVER_PATH)
    return webdriver.Edge(service=service, options=edge_options)

def run_test(test_func, driver, *args):
    start_time = time.time()
    status = test_func(driver, *args)
    end_time = time.time()
    return {
        "Status": status,
        "Time": round(end_time - start_time, 2)
    }

def main():
    driver = setup_driver()
    driver.maximize_window()
    # driver.get('https://www.google.com')
    # driver.quit()
    # exit()

    rand_number = random.randint(1000, 9999)
    
    register_result = run_test(test_valid_registration, driver, rand_number)
    login_result = run_test(test_valid_login, driver, rand_number)
    add_to_cart_result = run_test(test_add_product_to_cart, driver, 3)
    checkout_result = run_test(test_checkout, driver)
    
    driver.quit()
    
    test_results = {
        "Test Name": "Demoblaze E-commerce Test Suite",
        "Test Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Test Author": "Dava Aditya Jauhar",
        "Test Result": {
            "Register": {
                "Test Scenario": "Register with valid credentials",
                "Test Case": "Register with VALID username and VALID password",
                "Status": register_result["Status"],
                "Time": register_result["Time"]
            },
            "Login": {
                "Test Scenario": "Login with valid credentials",
                "Test Case": "Login with VALID (registered) username and password",
                "Status": login_result["Status"],
                "Time": login_result["Time"]
            },
            "Add to Cart": {
                "Test Scenario": "Add a product to cart",
                "Test Case": "Add Samsung galaxy s6 to cart",
                "Status": add_to_cart_result["Status"],
                "Time": add_to_cart_result["Time"]
            },
            "Checkout": {
                "Test Scenario": "Complete checkout process",
                "Test Case": "User able to check out",
                "Status": checkout_result["Status"],
                "Time": checkout_result["Time"]
            }
        }
    }
    
    successful_tests = sum(1 for test in test_results["Test Result"].values() if test["Status"])
    total_tests = len(test_results["Test Result"])
    test_results["Overall Result"] = f"{successful_tests}/{total_tests}"
    
    return test_results

if __name__ == "__main__":
    results = main()
    print(results)
    exit()