from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


COLOR_OPTIONS=(By.CSS_SELECTOR, 'span[id*="color_name_"][class*="a-button a-button-toggle"]')
FIRST_COLOR_OPTION = (By.CSS_SELECTOR, 'span[id*="color_name_"]')
COLOR_SELECTION=(By.ID, "inline-twister-expanded-dimension-text-color_name")


@given('Open Product {Product_ID} page')
def Open_product_page(context,Product_ID):
    context.driver.get(f'https://www.amazon.com/gp/product/{Product_ID}/')


@then('verify User clicks through the product types')
def verify_product_type_click(context):
    context.driver.find_element(*FIRST_COLOR_OPTION).click()
    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    print('All color options:', all_color_options)
    expected_colors = ['Light Wash', 'Black', 'Blue, Over Dye', 'Bright White', 'Dark Blue Vintage', 'Dark Indigo/Rinsed']

    actual_colors = []
    for color in all_color_options[:6]:
        color.click()
        current_color = context.driver.find_element(*COLOR_SELECTION).text
        print('current_color:', current_color)
        actual_colors += [current_color]
    assert expected_colors==actual_colors, f'Expected {expected_colors}, but got {actual_colors}'

