from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://www.realestate.com.au/sold/in-wayville,+sa+5034%3b/list-1')

# wait for "video" to be present
video = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "page-wrapper")))

# get the src value
print(video.get_attribute("src"))

driver.close()