from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from behave import *
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

@given(u'the user is at the login page')
def step_impl(context):
    driver.get("https://demo.realworld.io/#/login")


@when(u'the email and the password are filled correctly')
def step_impl(context):
    email = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/fieldset/fieldset[2]/input")
    email.send_keys("airotiv@gmail.com")
    password = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/form/fieldset/fieldset[3]/input")
    password.send_keys("testes123@")


@when(u'the Sign in button is clicked')
def step_impl(context):
    buttonIn = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/form/fieldset/button")
    buttonIn.click()


@then(u'then home page should be presented')
def step_impl(context):
    link_atual = driver.current_url
    assert link_atual == "https://demo.realworld.io/#/"