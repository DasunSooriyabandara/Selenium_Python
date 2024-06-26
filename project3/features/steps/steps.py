from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
from behave import given , when , then



@given('we go to python.org site')
def open_browser(context):
    # context.driver = webdriver.chrome.webdriver.WebDriver(executable_path='E:\github\Selenium_Python\project3\driver\chromedriver.exe')
    context.service = webdriver.ChromeService(executable_path = 'E:\github\Selenium_Python\project3\driver\chromedriver.exe')
    context.driver = webdriver.Chrome(service=context.service)
    context.driver.maximize_window()
    context.driver.get('https://www.python.org/')

@when('we click downloads')
def click_downloads(context):
    context.wait = WebDriverWait(context.driver, 30)
    downloads_link = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    downloads_link.click()
    print('~~~~~~ Downloads link Clicked')
    print(str(context.driver.current_url))
    assert str(context.driver.current_url) == 'https://www.python.org/downloads/'

@then('we should download python 3.12.4')
#def click_download_python(driver , python_version):
def click_download_python(context):
    context.wait = WebDriverWait(context.driver, 30)
    download_python_button = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"touchnav-wrapper\"]/header/div/div[2]/div/div[2]/p/a")))
    print('~~~~~~~~~~~~~~~~')
    print(download_python_button.text)
    if 'Download Python 3.12.4' == download_python_button.text :
        print('Test Case Passed')
        assert True
    else:
        print('Test Case Failed. The version avaialable to download is'+ download_python_button.text)
        assert False


