from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
time.sleep(1)
#user = driver.find_element('id','user-name')
user = driver.find_element('xpath','//*[@id="user-name"]')
user.clear()
user.send_keys('standard_user')

passwd = driver.find_element('xpath','/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input')
passwd.clear()
passwd.send_keys('secret_sauce')
