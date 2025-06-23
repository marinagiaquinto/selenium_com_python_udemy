from selenium import webdriver
import time
from selenium.webdriver.common. by import By


browser = webdriver.Chrome()
url = 'https://demo.applitools.com/'

browser.get(url)

# CONDICIONAIS RESPONDEM COM TRU OU FALSE

#is_displayed() - se o elemento está sendo mostrado em tela
username = browser.find_element(By.ID, 'username')
password = browser.find_element(By.ID, 'password')

assert username.is_displayed() == True , 'Campo user não apresentado em tela'
assert password.is_displayed() == True , 'Campo password não apresentado em tela'

#is_enabled() - se o elemento está habilitado
assert username.is_enabled() == True , 'Campo user não está habilitado'
assert password.is_enabled() == True , 'Campo password não está habilitado'

#is_selected() - se o elemento está selecionado

checkbox = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')

assert checkbox.is_selected() == False , 'Checkbox está selecionado'
#Ou assert not checkbox.is_selected()

checkbox.click()
assert checkbox.is_selected() == True , 'Checkbox não está selecionado'

time.sleep(2)