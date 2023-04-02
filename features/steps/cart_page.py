from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART=(By.XPATH, '//span[@class="a-size-medium-plus a-color-base sw-atc-text a-text-bold"]')


@when('click on cart')
def user_clicks_on_cart(context):
    context.driver.find_element(By.XPATH, '//span[@class="nav-cart-icon nav-sprite"]').click()


@then('Verify cart is empty')
def Verify_cart(context):
    expected_result = "0"
    actual_result = context.driver.find_element(By.ID, "nav-cart-count").text
    assert expected_result == actual_result, f'expected{expected_result} but got {actual_result}'


@then('confirm item in cart')
def confirm_cart(context):
    expected_result = "Added to Cart"
    actual_result = context.driver.find_element(*CART).text
    assert expected_result == actual_result, f'expected{expected_result} but got {actual_result}'
