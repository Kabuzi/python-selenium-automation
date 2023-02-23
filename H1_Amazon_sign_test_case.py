Create a test case for the Sign In page using python & selenium script.

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH,'//a[@href="/gp/css/order-history?ref_=nav_orders_first"]').click()

expected_result= "Sign in"
actual_result= driver.find_element(By.XPATH,'//h1[@class="a-spacing-small"]').text
print(actual_result)

assert expected_result == actual_result, f'expected{expected_result} but got {actual_result}'

