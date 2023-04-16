from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


SEARCH_INPUT=(By.ID, "twotabsearchtextbox")
SEARCH_BTN=(By.ID, "nav-search-submit-button")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when ('User Clicks Orders')
def click_orders(context):
    context.driver.find_element(By.XPATH, '//span[text()="& Orders"]').click()


@when ('click on best sellers')
def click_best_sellers(context):
    context.driver.find_element(By.XPATH, '//a[contains(@href, "nav_cs_bestsellers")]').click()


@When ('add {product} into search field')
def search_for_item(context, product):
    search_field = context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys(product)


@When ('Click on search')
def click_on_search(context):
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN))
    context.driver.find_element(*SEARCH_BTN).click()
 #   sleep(0)





