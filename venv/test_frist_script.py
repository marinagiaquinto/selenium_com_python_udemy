from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('https://google.com')
time.sleep(15)