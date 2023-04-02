from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


WELCOME_TITLE=(By.XPATH, '//h1[@class="fs-heading bolded"]')
CARD_CONTAINER=(By.CSS_SELECTOR,'.issue-card-container')
HELP_LIBRARY=(By.XPATH, '//h2[text()="Search our help library"]')
SEARCH_FIELD=(By.ID, 'hubHelpSearchInput')
HELP_TOPICS=(By.XPATH, '//h2[text()="All help topics"]')
RECOMMENDED_TOPICS=(By.CSS_SELECTOR, '.help-topics-list-wrapper')


@given('Open Amazon customer service page')
def open_customer_service_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('verify Welcome to customer service link')
def verify_customer_service_link(context):
     actual_result= context.driver.find_element(*WELCOME_TITLE).text
     expected_result="Welcome to Amazon Customer Service"
     assert actual_result==expected_result, f'expected{expected_result} but got actual{actual_result}'


@when('verify container')
def verify_container(context):
    assert context.driver.find_element(*CARD_CONTAINER), f'Container not found'


@when('verify search our help library')
def verify_library_search(context):
    actual_result = context.driver.find_element(*HELP_LIBRARY).text
    expected_result = "Search our help library"
    assert actual_result == expected_result, f'expected{expected_result} but got actual{actual_result}'

@when('search field')
def verify_search_field(context):
    assert context.driver.find_element(*SEARCH_FIELD), f'Search field field not found'


@when('all help topics')
def verify_all_help_topics(context):
    actual_result = context.driver.find_element(*HELP_TOPICS).text
    expected_result ="All help topics"
    assert actual_result == expected_result, f'expected{expected_result} but got actual{actual_result}'

@when('recommended topics')
def verify_recommended_topics(context):
    assert context.driver.find_element(*RECOMMENDED_TOPICS), f'recommended topics input field not found'

