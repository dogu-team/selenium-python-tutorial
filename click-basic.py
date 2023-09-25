from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
element = driver.find_element(By.XPATH, "/html/body/div/main/section[2]/div/div/div[1]/div/div[2]/div/a")
element.click()
driver.quit()