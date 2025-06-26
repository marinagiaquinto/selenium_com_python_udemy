from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = 'https://www.saucedemo.com/'

browser.get(url)
browser.maximize_window()

#send_keys()
username = browser.find_element(By.ID, 'user-name')
password = browser.find_element(By.ID, 'password')
username.send_keys('standard_user')
password.send_keys('secret_sauce')

#click()
button = browser.find_element(By.ID, 'login-button')
button.click()

#text (pega o formato do texto apresentado em tela e não seu formato no HTML)
title_products = browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]')

assert title_products.text == 'Products', 'Título diferente de "Products"'


#get_attribute()

imagem = browser.find_element(By.XPATH, '(//img[@class="inventory_item_img"])[1]') # o primeiro dos 6 itens da classe

value_attr_alt_img = imagem.get_attribute('alt')

assert value_attr_alt_img == 'Sauce Labs Backpack', 'Atributo diferente de Sauce Labs Backpack'