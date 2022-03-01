from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://ke.qq.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id("js_login").click()
driver.

