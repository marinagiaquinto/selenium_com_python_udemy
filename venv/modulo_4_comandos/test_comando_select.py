from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select # IMPORTAR
import time

browser = webdriver.Chrome()
url = 'https://leogcarvalho.github.io/test-automation-practice/#option3'

browser.get(url)

dropdown = Select(browser.find_element(By.ID, 'dropdown')) # pegar o id do select e não da opção em específico. Com o select aqui e importado
dropdown.select_by_visible_text('Option 2') # ao colocar ".", abre uma opção de tipos de seleção
time.sleep(2)
dropdown.select_by_visible_text('Option 1')
time.sleep(2)