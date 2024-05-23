from jproperties import Properties
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append("E:\github\Selenium_Python\project1")
from pages.Home.home_page import click_downloads , search , search_by_looping, click_donate , click_download_python_docs_throuth_learnmore ,click_download_python_docs_throuth_learnmore_test2
from pages.Downloads.downloads_page import click_download_python



properties = Properties()

with open('testcase.properties', 'rb') as f:
    properties.load(f, 'utf-8')

test_url = properties.get('test_url','pythondocs_url')[0]
print(test_url)
pythondocs_url = properties.get('pythondocs_url')[0]
print(pythondocs_url)

def open_browser():
    service = webdriver.ChromeService(executable_path = 'E:\github\Selenium_Python\project1\drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(test_url)
    return driver


def check_latest_python_version():
    python_version_text = "Download Python 3.12.3"
    driver = open_browser()
    driver = click_downloads(driver)
    driver = click_download_python(driver,python_version_text)
    driver.close()
    

def search_for_python_realses():
    search_text = "Python 2.5 Release"
    driver = open_browser()
    driver = search_by_looping(driver,search_text)
    driver.close()
##---------------------------My test cases-------------------------
def click_donate_button():
    expected_url = "https://psfmember.org/civicrm/contribute/transact/?reset=1&id=2"
    driver = open_browser()
    driver = click_donate(driver,expected_url)
    driver.close()


def download_pythondocs():
    driver = open_browser()
    url = driver.get(pythondocs_url)
    driver = click_download_python_docs_throuth_learnmore(driver,url)

def download_pythondocs_test2():
    expected_url_learnmore ='https://www.python.org/doc/'
    expected_url_pythondocs ='https://docs.python.org/3/'
    driver = open_browser()
    driver = click_download_python_docs_throuth_learnmore_test2(driver,expected_url_learnmore,expected_url_pythondocs)  
    driver.close()