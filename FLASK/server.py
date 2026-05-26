from  selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Path = "/Users/dheerajsrivastava/Downloads/chromedriver-mac-arm64"
service = Service(Path)
driver = webdriver.Chrome()
driver.get("http://google.com")
Input =driver.find_element(By.CLASS_NAME,"gLFyf")
Input.send_keys("unep"+ Keys.ENTER)


time.sleep(100)
driver.quit()