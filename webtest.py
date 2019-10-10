from selenium import webdriver
from time import sleep

driver = webdriver.Firefox(executable_path='C:/Users/Ranjitha/Downloads/geckodriver')
driver.get('http://www.demo.guru99.com/V4/')
user = driver.find_element_by_name('uid')
user.send_keys('mngr227751')
sleep(1)
pw = driver.find_element_by_name('password')
pw.send_keys('UjavEjE')
sleep(1)
login = driver.find_element_by_name('btnLogin')
login.click()
print("login successful")
driver.quit()

