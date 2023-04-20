from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
print('Nazwa strony to ',driver.title)
time.sleep(1)

try:
    user = driver.find_element('xpath','//*[@id="user-name"]')
except NoSuchElementException:
    driver.get_screenshot_as_file('screen2')
else:
    user.send_keys('standard_user')

passwd = driver.find_element('xpath','/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input')
passwd.clear()
passwd.send_keys('secret_sauce')

login_button = driver.find_element('xpath','//*[@id="login-button"]')
login_button.click()

try:
    assert driver.current_url == 'https://www.saucedemo.com/inventory.hdtml'
except:
    driver.get_screenshot_as_file('scs.png')
finally:
    print('po asercji')
    driver.quit()



