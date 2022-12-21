# python3 -m pip install selenium


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome("/Users/muslimovramazan/skillfactoryGitHub/test_practice_sf/choredriver")
driver.get("http://130.193.37.179/app/pets")
(driver.find_element(By.XPATH, "//* [@id-\"image\"]/img"))[0].click()
sleep(3)
driver.save_screenshot("pet_home.png")
driver.quit()


