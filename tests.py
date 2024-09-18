from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get('https://google.com')
print('Opening <google.com>')

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf')))

input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
input_element.send_keys('github gblw1' + Keys.ENTER)
print('Searching for <github gblw1>')

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.PARTIAL_LINK_TEXT, 'Gabriel gbLw1 - GitHub'))
)

driver.find_element(By.PARTIAL_LINK_TEXT, 'Gabriel gbLw1 - GitHub').click()
print('Opening <github gblw1> link')

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Repositories'))
)

driver.find_element(By.PARTIAL_LINK_TEXT, 'Repositories').click()
print('Opening <Repositories> tab')

search_input_id = 'your-repos-filter'

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, search_input_id))
)

search_input = driver.find_element(By.ID, search_input_id)
search_input.send_keys('python' + Keys.ENTER)
print('Searching for <python> repositories')

print('Rickrolling...')
time.sleep(1)
driver.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

time.sleep(10)
driver.quit()
