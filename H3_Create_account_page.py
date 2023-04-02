from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

#driver = webdriver.Chrome(executable_path='./chromedriver')

service = Service('/Users/kkabu/Documents/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//span[text()='& Orders']").click()

driver.find_element(By.ID, "createAccountSubmit").click()

#LOGO
driver.find_element(By.CSS_SELECTOR, 'i.a-icon a-icon-logo')

#CREATE ACCOUNT
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#YOUR NAME
driver.find_element(By.ID, 'ap_customer_name').send_keys('Khumbo Munthali')

#EMAIL
driver.find_element(By.ID, 'ap_email')

#PASSWORD
driver.find_element(By.ID, "ap_password").send_keys('Biri+265')

#PASSWORD INFO
driver.find_element(By.XPATH, "//a[text()='Passwords must be at least 6 characters.']")

#REENTER PASSWORD
driver.find_element(By.ID, "ap_password_check").send_keys('Biri+265')

#CREATE AMAZON ACCOUNT
driver.find_element(By.ID, "continue").click()

#CONDITIONS OF SERVICE
driver.find_element(By.CSS_SELECTOR, 'a[href*= "ap_register_notification_condition_of_use"]').click()

#PRIVACY
driver.find_element(By.CSS_SELECTOR, 'a[href*="display.html/ref=ap_register_notification_privacy_notice"]').click()

#SIGN IN
driver.find_element(By.CSS_SELECTOR, 'a[href*="/ap/signin?]').click()
