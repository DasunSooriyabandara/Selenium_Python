import os
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@given('we go to Google and search for eLearning.lk')
def open_browser(context):
    driver_path = r'E:\\github\\Selenium_Python\\Project5\\driver\\chromedriver.exe'
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.get('https://www.google.com')
    search_box = context.driver.find_element(By.NAME, 'q')
    search_box.send_keys('eLearning.lk')
    search_box.send_keys(Keys.ENTER)

@when('we click the eLearning.lk link from Google')
def click_elearning_link(context):
    context.wait = WebDriverWait(context.driver, 30)
    elearning_link = context.wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'eLearning.lk')))
    elearning_link.click()

@then('we should be on the eLearning.lk website')
def verify_elearning_website(context):
    context.wait.until(EC.url_contains('elearning.lk'))
    assert 'The Premier Online Learning' in context.driver.title

@when('the user searches for the Python course in the eLearning.lk search bar')
def search_python_course(context):
    context.wait = WebDriverWait(context.driver, 30)
    search_bar = context.wait.until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/form[1]/input[1]')))
    search_bar.send_keys('Python')
    search_button = context.driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/form[1]/button[1]/h6[1]')
    context.wait.until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[1]/div[2]/form[1]/button[1]/h6[1]')))
    search_button.click()

@when('the user clicks on the Python course')
def click_python_course(context):
    python_course_link = context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="course-menu"]/div/div/div[2]/div[1]/div[4]')))
    python_course_link.click()

@then('the user should be on the Python course page')
def verify_python_course_page(context):
    context.wait.until(EC.url_contains('https://elearning.lk/course/python-basic-to-intermediate-online-sinhala-medium-certificate-course-class-in-sri-lanka-by-nimesha-jinarajadasa-with-elearning.lk'))

@when('the user checks the course content')
def check_course_content(context):
    context.wait = WebDriverWait(context.driver, 50)
    try:
        content_section = context.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="course-title-section"]')))
        context.course_content = content_section.text
        print(f"Course content found: {context.course_content}")
    except Exception as e:
        print(f"An error occurred while checking course content: {e}")
        context.course_content = None

@when('generates a report containing the course content')
def generate_report(context):
    report_file_path = os.path.join(os.path.expanduser('~'), 'course_report.txt')
    try:
        with open(report_file_path, 'w', encoding='utf-8') as file:
            file.write('Course Content Report\n')
            file.write('----------------------\n')
            if context.course_content:
                file.write(context.course_content)
            else:
                file.write("No course content found.")
        print(f'Report generated successfully at: {report_file_path}')
    except Exception as e:
        print(f"An error occurred while generating the report: {e}")
        
         

@then('the report should be generated successfully')
def verify_report_generated(context):
    report_file_path = os.path.join(os.path.expanduser('~'), 'course_report.txt')
    assert os.path.exists(report_file_path), "Report file was not generated"
    with open(report_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    assert 'Course Content Report' in content, "Report content is incorrect"
    print(f'Report content verified successfully from: {report_file_path}')
    
    print('Navigate to C:\\Users\\<YourUsername>\\ and look for course_report.txt.')  
    context.driver.quit()
