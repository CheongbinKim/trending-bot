from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class KSelenium:
    def __init__(self):
        service = Service(executable_path='./chromedriver')
        options = webdriver.ChromeOptions()
        #options.add_argument("--start-maximized")
        options.add_argument("headless")
        options.add_argument("disable-gpu")
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36')
        self.__driver = webdriver.Chrome(service=service, options=options)
        self.__driver.set_window_size(1920, 1080)

    @property
    def driver(self):
        return self.__driver

    def get(self, xpath):
        return self.__driver.find_element(By.XPATH,xpath)

    def go(self,url):
        self.__driver.get(url)

    def close(self):
        self.__driver.quit()
