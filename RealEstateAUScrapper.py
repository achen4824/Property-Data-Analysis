from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0")
driver = webdriver.Firefox(profile)
driver.get('https://www.realestate.com.au/sold')

driver.get_cookies()

search = driver.find_element(By.XPATH,'//*[@id="where"]')
search.send_keys("5062")

searchbutton = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/form/div/div[1]/div/div/button')
searchbutton.click()

# get the src value
# print(video.get_attribute("src"))

# driver.close()