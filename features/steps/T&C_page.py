from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRIVACY_NOTICE=(By.XPATH, '//a[@href="https://www.amazon.com/privacy"]')

@given('Open Amazon T&C page')
def open_TandC_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_current_window(context):
    context.original_window=context.driver.current_window_handle
    #print('Original Window:', context.current_window)


@when('Click on Amazon Privacy Notice link')
def verify_privacy_page(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def verify_window_switch(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print('ALL WINDOWS:', windows)
    context.driver.switch_to.window(windows[1])

    context.current_window = context.driver.current_window_handle
    print('AFTER_SWITCH Window:', context.current_window)




@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))



@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
