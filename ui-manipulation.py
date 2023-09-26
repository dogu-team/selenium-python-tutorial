from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os;

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
text_input = driver.find_element(By.XPATH, '//input[@id="my-text-id"]')
text_input.send_keys("ABCD")
password_input = driver.find_element(By.XPATH, '//input[@name="my-password"]')
password_input.send_keys("mypassword!")
select_option_one = driver.find_element(By.XPATH, '//select[@name="my-select"]//option[@value="1"]')
select_option_one.click()
datalist_input = driver.find_element(By.XPATH, '//input[@name="my-datalist"]')
datalist_input.send_keys("Los Angeles")
file_input = driver.find_element(By.XPATH, "//input[@name='my-file']")
file_input.send_keys(os.getcwd() + "/click-basic.py")
default_radio = driver.find_element(By.XPATH, '//input[@id="my-radio-2"]')
default_radio.click()
color_input = driver.find_element(By.XPATH, '//input[@name="my-colors"]')
color_input.send_keys("#000000")
calendar_input = driver.find_element(By.XPATH, '//input[@name="my-date"]')
calendar_input.click()
driver.find_element(By.XPATH, '//td[@class="day" and text()="25"]').click()
range_input = driver.find_element(By.XPATH, '//input[@name="my-range"]')
for i in range(0, 4):
  range_input.send_keys(Keys.ARROW_LEFT)
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

SUCCESS_TEXT = "Received!"
result_text = driver.find_element(By.XPATH, '//p[@id="message"]').text
assert SUCCESS_TEXT == result_text

driver.quit()