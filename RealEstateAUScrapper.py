import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
print(driver.execute_script("return navigator.userAgent;"))

driver.get('https://www.realestate.com.au/sold')

search = driver.find_element(By.XPATH,'//*[@id="where"]')
search.send_keys("5062")

time.sleep(30)

searchbutton = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/form/div/div[1]/div/div/button')
searchbutton.click()
time.sleep(30)
# print(video.get_attribute("src"))

#driver.close()