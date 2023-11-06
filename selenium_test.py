import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='./chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("headless")
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://ifconfig.me/')
time.sleep(3)

ip_address = driver.find_element(By.XPATH,'//*[@id="ip_address"]')

print(ip_address.text)

driver.quit()
