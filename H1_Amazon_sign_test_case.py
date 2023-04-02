#Create a test case for the Sign In page using python & selenium script.
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

#driver = webdriver.Chrome(executable_path='./chromedriver')

service = Service('/Users/kkabu/Documents/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH,'//a[@href="/gp/css/order-history?ref_=nav_orders_first"]').click()


driver.find_element(By.XPATH,'//h1[@class="a-spacing-small"]')

expected_result= "Sign in"
actual_result= driver.find_element(By.XPATH,'//h1[@class="a-spacing-small"]').text
print(actual_result)

assert expected_result == actual_result, f'expected{expected_result} but got {actual_result}'


