from selenium import webdriver
from selenium.webdriver.common.by import By


# Quando você tem um iframe, ele da início a um novo html dentro do html. 
# Isso faz com que o elemento que busca dentro de um iframe não seja encontrado fora dele. 
# Para conseguir localizar o elemento, é necessário setar o iframe em que o localizador se encontra.


browser = webdriver.Chrome()
url = 'https://leogcarvalho.github.io/test-automation-practice/#option3'

iframe = browser.find_element(By.ID, 'test-iframe') #pegar o localizador do iframe todo e salvar

browser.switch_to.frame(iframe) #trocar para o frame...

title_iframe = browser.find_element(By.CSS_SELECTOR, 'body>div>h1')

print(title_iframe.text)