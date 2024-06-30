from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from behave import given, when, then
import allure

@given('we go to Google and search for eLearning.lk')
def open_browser(context):
    # Change this path to the actual location of your ChromeDriver
    driver_path = r'E:\\github\Selenium_Python\\Project5\driver\\chromedriver.exe'
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.get('https://www.google.com')
    search_box = context.driver.find_element(By.XPATH, '//*[@id="input"]')
    search_box.send_keys('eLearning.lk')
    search_box.submit()

@when('we click the eLearning.lk link from Google')
def click_elearning_link(context):
    context.wait = WebDriverWait(context.driver, 30)
    elearning_link = context.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'eLearning.lk')))
    elearning_link.click()

@when('we search for the Python course in the eLearning.lk search bar')
def search_python_course(context):
    search_box = context.wait.until(EC.element_to_be_clickable((By.NAME, 'q')))
    search_box.send_keys('Python')
    search_box.submit()

@when('we click on the Python course')
def click_python_course(context):
    python_course_link = context.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Python')))
    python_course_link.click()

@then('we check the course content')
def check_course_content(context):
    context.wait = WebDriverWait(context.driver, 30)
    course_content = context.wait.until(EC.presence_of_element_located((By.ID, 'course-content')))
    with allure.step('Course content found'):
        assert course_content is not None
        allure.attach(context.driver.page_source, name="Page Source", attachment_type=allure.attachment_type.HTML)

    context.driver.quit()
