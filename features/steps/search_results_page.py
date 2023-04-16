from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


ITEM=(By.XPATH, '//img[@src="https://m.media-amazon.com/images/I/71ueEz22+KL._AC_UL320_.jpg"]')
CART=(By.ID, "add-to-cart-button")


@then ('click on first product')
def click_first_product(context):
    context.driver.wait.until(EC.element_to_be_clickable(ITEM))
    context.driver.find_element(*ITEM).click()
    #sleep(2)


@then ('add to cart')
def add_to_cart(context):
    context.driver.find_element(*CART).click()



