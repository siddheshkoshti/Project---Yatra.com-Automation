import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
options = webdriver.ChromeOptions()

def capture_screenshot(d,path):
    file_name = path + "screenshot" + ".png"
    d.save_screenshot(file_name)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
original_window = driver.current_window_handle
wait = WebDriverWait(driver, 10)

search = driver.find_element(By.XPATH,"//input[@placeholder='Search for Products, Brands and More']").send_keys("iphone 15 pro max")
driver.find_element(By.CSS_SELECTOR,"#container > div > div.q8WwEU > div > div > div > div > div.css-1dbjc4n.r-13awgt0 > div > div.css-1dbjc4n.r-13awgt0.r-1iqfa7g.r-60vfwk > div > div._2nl6Ch > div._2NhoPJ > header > div._3ZqtNW > div._3NorZ0._3jeYYh > form > div > button > svg").click()
driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)").click()

wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

driver.find_element(By.CSS_SELECTOR,"._2KpZ6l._2U9uOA._3v1-ww").click()
time.sleep(10)

# adding product to cart
checkout = driver.find_element(By.XPATH, "//button[normalize-space()='GO TO CART']")

capture_screenshot(driver,'"./screenshot/')
driver.quit()