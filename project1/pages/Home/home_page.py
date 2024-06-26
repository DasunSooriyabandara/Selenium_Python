from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_downloads(driver):
    wait = WebDriverWait(driver, 30)
    downloads_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    downloads_link.click()
    print('~~~~~~ Downloads link Clicked')
    print(str(driver.current_url))
    return driver


def click_all_releases(driver):
    wait = WebDriverWait(driver, 30)
    downloads_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    actions = ActionChains(driver)
    actions.move_to_element(downloads_link).perform()
    all_relases_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]/ul/li[1]/a")))
    all_relases_link.click()
    print('~~~~~~ All releases link Clicked')
    print(str(driver.current_url))
    return driver

def click_source_code(driver):
    wait = WebDriverWait(driver, 30)
    downloads_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    actions = ActionChains(driver)
    actions.move_to_element(downloads_link).perform()
    source_code_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]/ul/li[2]/a")))
    source_code_link.click()
    print('~~~~~~ Source Code link Clicked')
    print(str(driver.current_url))
    return driver

def click_windows(driver):
    wait = WebDriverWait(driver, 30)
    downloads_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]")))
    actions = ActionChains(driver)
    actions.move_to_element(downloads_link).perform()
    windows_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"downloads\"]/ul/li[3]/a")))
    windows_link.click()
    print('~~~~~~ Windows link Clicked')
    print(str(driver.current_url))
    return driver



def search(driver,search_text):
    wait = WebDriverWait(driver, 30)
    search_feild = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"id-search-field\"]")))
    search_feild.send_keys(search_text)
    print('~~~~~~ Searching for Text')
    GO_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"submit\"]")))
    GO_button.click()
    third_result = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"content\"]/div/section/form/ul/li[3]/h3/a")))  
    if search_text == third_result.text :
        print('Test Case Passed')
    else:
        print('Test Case Failed. The Searched result is'+ third_result.text)
    print(str(driver.current_url))
    return driver

def search_by_looping(driver,search_text):
    wait = WebDriverWait(driver, 30)
    search_feild = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"id-search-field\"]")))
    search_feild.send_keys(search_text)
    print('~~~~~~ Searching for Text')
    GO_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"submit\"]")))
    GO_button.click()
    for i in range(1, 21):
        print(i)
        try:
            serch_xpath = "//*[@id=\"content\"]/div/section/form/ul/li["+str(i)+"]/h3/a"
            search_result = wait.until(EC.element_to_be_clickable((By.XPATH,serch_xpath)))
            print(search_result.text)
            if search_text == search_result.text :
                print('Match')
                break
            else:
                print('No Math')
        except:
            print()
    return driver

# ------------------My test case-----------
def click_donate(driver, expected_url):
    wait = WebDriverWait(driver, 20)
    donate_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[1]/a')))
    donate_link.click()
    print('~~~~~~~~~~Donate link clicked')
    actual_url = driver.current_url
    if expected_url == actual_url:
        print('Test Case Passed')
    else:
        print('Test Case Failed. Current URL is different from expected')
    print(f'Current URL: {actual_url}')
    return driver

def click_download_python_docs_throuth_learnmore(driver,url):
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    python_docs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[2]/div/p[3]/a')))
    python_docs.click()
    print('successfully click the button')
    print('current url of the page'+driver.current_url)
    return driver

def click_download_python_docs_throuth_learnmore_test2(driver,expected_url_learnmore,expected_url_pythondocs):
    wait = WebDriverWait(driver,5)
    learn_more = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[3]/p/a')))
    learn_more.click()
    if expected_url_learnmore == driver.get.actual_url:
        print('Test pass: successfully direct to puthon docs page')
    else:
        print('Test fail: expected and actual url are different')
    python_docs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[2]/div/p[3]/a')))
    python_docs.click()
    if expected_url_pythondocs == driver.get.actual_url:
        print('Test pass: successfully click to puthon docs button')
    else:
        print('Test fail: \twrong button click : expected and actual url are different')

    return driver

def click_socialize_button(driver,expected_url):
    wait = WebDriverWait(driver, 30)
    socialize_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='touchnav-wrapper']/header/div/div[1]/div/div[2]/ul/li/a")))
    socialize_button.click()
    print("~~~~~~~Click Socialize button and menu opens")
    linkedin_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='touchnav-wrapper']/header/div/div[1]/div/div[2]/ul/li/ul/li[1]")))
    linkedin_option.click()
    actual_url = driver.current_url
    if expected_url == actual_url:
        print("Test Passed: successfly Click Likedine button")
    else:
        print("Test Failed: wrong socialmedia selected")
    return driver
    
def click_become_member_button(driver):
    become_member_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/section/div[5]/p[2]/a[1]')))
    print("~~~~ Found Become a Member button text" + become_member_button.text)
    become_member_button.click()
    print(str(driver.currnt_url))
    print("~~~~ Found Become a Member button and clicked")
    return driver

