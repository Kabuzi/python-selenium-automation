from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify cart is empty')
def Verify_cart(context):
    expected_result = "0"
    actual_result = context.driver.find_element(By.ID, "nav-cart-count").text
    assert expected_result == actual_result, f'expected{expected_result} but got {actual_result}'
