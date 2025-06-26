from selenium  import webdriver
import time

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/')
time.sleep(2)

# title - nome da página na aba do navegador

title = browser.title
print(title)
assert 'Swag Labs' == title , 'Nome da pág diferente do esperado'

# current_url - url da pág

url = browser.current_url
print(url)
assert url == 'https://www.saucedemo.com/', 'Valor de URL diferente do esperado'

# page_source - retorna todo o cód fonte da pág

print(browser.page_source)