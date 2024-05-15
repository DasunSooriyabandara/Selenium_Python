import time
from jproperties import Properties
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Create a Properties object
properties = Properties()
# Load properties from file
with open('testcase.properties', 'rb') as f:
    properties.load(f, 'utf-8')
# Access values
test_url = properties.get('test_url')[0]
print(test_url)
service = webdriver.ChromeService(executable_path = 'E:\github\Selenium_Python\project1\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(test_url)
driver.maximize_window()
time.sleep(5)
driver.close()