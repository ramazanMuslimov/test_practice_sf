# python3 -m pip install selenium

from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("/Users/muslimovramazan/skillfactoryGitHub/test_practice_sf/choredriver")
driver.get("https://google.com")
driver.find_element(By.XPATH, "//input[@title=\"Поиск\"]").send_keys('Skillfactory' + Keys.RETURN)
sleep(3)
driver.save_screenshot("sf.png")
driver.quit()
