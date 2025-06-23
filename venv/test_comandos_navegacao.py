from selenium import webdriver
import time

browser = webdriver.Chrome()

# get - entrar em uma página
browser.get('https://google.com')
time.sleep(2)

# maximize_window() - maximizar a tela

browser.maximize_window()
time.sleep(2)

# refresh() - atualizar a pág

browser.refresh()
time.sleep(2)

# back() - retornar na navegação

browser.get('https://www.saucedemo.com/')
browser.back()
time.sleep(2)

# forward() - ir pra frente na pág navegada

browser.forward()
time.sleep(2)

# close () - fechar uma aba

browser.switch_to.new_window("tab") #abre uma nova aba no navegador
browser.get('https://google.com')
browser.close()
time.sleep(5)

# quit () - fechar todas as abas do navegador

browser.switch_to.new_window("tab")
browser.get('https://google.com')
time.sleep(5)
browser.quit()