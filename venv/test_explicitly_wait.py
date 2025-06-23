from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #importe com o apelido de EC
# explicitly wait necessita das duas últimas importações.
# Com ele, a ferramenta aguardará encontrar um elemento em específico (não mais uma espera global), até o tempo determinado.
import time
browser = webdriver.Chrome()
url = 'https://www.hyrtutorials.com/p/waits-demo.html'
browser.get(url)

wait = WebDriverWait (browser, 30) #tempo de espera até dar erro, caso não encontre o elemento

browser.find_element(By.ID, 'btn1').click()
campo_text_1 = wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@id="txt1"])[1]'))) #espere ATÉ o elemento estar presente
campo_text_1.is_displayed()


browser.find_element(By.ID, 'btn2').click()
campo_text_2 = wait.until(EC.visibility_of_element_located((By.XPATH, '(//input[@id="txt2"])[1]')))
campo_text_2.is_displayed()

#Caso a espera seja por um texto:
#wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, '<locator>'), '<nome do texto esperado>'))

#Caso a espera seja por um botão que deve aparecer ou por um botão que deve habilitar
#wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '<locator>')))

#Caso a espera seja por um checkbox selecionado
#checkbox = browser.find_element(By.CLASS_NAME, '<locator>')
#wait.until(EC.element_to_be_selected(checkbox))