from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

LINKS=(By.CSS_SELECTOR, "#zg_header a")

@Then ('verify 5 links')
def verify_link_count(context):
    best_seller_links=context.driver.find_elements(*LINKS)
    print(best_seller_links)
    assert len(best_seller_links)==5, f'Expected 5 links, but got {best_seller_links} links'
