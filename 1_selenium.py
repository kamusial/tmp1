from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')
time.sleep(1)
button1_accept = driver.find_element('id','L2AGLb')
button1_accept.click()
search_field = driver.find_element('name','q')
search_field.send_keys('Ile lat ma Mariusz Pudzianowski?')
search_button = driver.find_element('name','btnK')
search_button.submit()
driver.get_screenshot_as_file('screen.png')
time.sleep(3)
driver.quit()