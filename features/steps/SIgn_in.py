from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when ('User Clicks Orders')
def click_orders(context):
    context.driver.find_element(By.XPATH, '//span[text()="& Orders"]').click()


@when('click on cart')
def user_clicks_on_cart(context):
    context.driver.find_element(By.XPATH, '//span[@class="nav-cart-icon nav-sprite"]').click()


@then('Verify Sign in page is shown')
def sign_in_page(context):
   expected_result= "Sign in"
   actual_result= context.driver.find_element(By.XPATH,'//h1[@class="a-spacing-small"]').text
   assert expected_result == actual_result, f'expected{expected_result} but got {actual_result}'


@then('Verify email input field is shown')
def verify_email_input(context):
    assert context.driver.find_element(By.ID, 'ap_email'), f'Email input field not found'


