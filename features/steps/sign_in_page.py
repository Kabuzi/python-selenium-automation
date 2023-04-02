from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign in page is shown')
def sign_in_page(context):
   expected_result= "Sign in"
   actual_result= context.driver.find_element(By.XPATH,'//h1[@class="a-spacing-small"]').text
   assert expected_result == actual_result, f'expected{expected_result} but got {actual_result}'


@then('Verify email input field is shown')
def verify_email_input(context):
    assert context.driver.find_element(By.ID, 'ap_email'), f'Email input field not found'


