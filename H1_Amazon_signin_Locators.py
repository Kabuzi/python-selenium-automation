from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

#driver = webdriver.Chrome(executable_path='./chromedriver')

service = Service('/Users/kkabu/Documents/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')


#LOGO
driver.find_element(By.XPATH,'//i[@class="a-icon a-icon-logo"]''//i[@class="a-icon a-icon-logo"]')

#Continue Button
driver.find_element(By.XPATH,"//input[@class='a-button-input']").click()

#Need_help
driver.find_element(By.XPATH,'//span[@class="a-expander-prompt"]').click()

#Forget_Password
driver.find_element(By.ID, "auth-fpp-link-bottom").click()

# Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link").click()

# Create your Amazon account button
driver.find_element(By.ID,"createAccountSubmit").click()

# *Conditions of use link
driver.find_element(By.XPATH, '//a[contains(@href,"ap_signin_notification_condition_of_use")]').click()

# *Privacy Notice link
driver.find_element(By.XPATH,'//a[contains(@href, "ap_signin_notification_privacy_notice")]').click()


