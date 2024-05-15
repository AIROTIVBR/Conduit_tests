from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demo.realworld.io/#/login")

email = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/fieldset/fieldset[2]/input")
email.send_keys("airotiv@gmail.com")

time.sleep(3)

password = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/form/fieldset/fieldset[3]/input")
password.send_keys("testes123@")

time.sleep(3)

buttonIn = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/fieldset/button")
buttonIn.click()

time.sleep(3)

driver.quit()