from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/')

# find_element - retorna o primeiro locator encontrado. Quebra caso não encontre o elemento.

name = browser.find_element(By.ID, 'user-name')
password = browser.find_element(By.ID, 'password')

name.send_keys('standard_user'),
password.send_keys('secret_sauce')

# find_elements - retorna uma lista com os locators encontrados. Não quebra caso não encontre o elemento, retorna zero. 

lista_campos = browser.find_elements(By.CSS_SELECTOR, "input[class='input_error form_input']")

assert len(lista_campos) == 2, 'Número de elementos da lista está errado'