from selenium  import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://www.hyrtutorials.com/p/waits-demo.html'

browser.implicitly_wait(30) # Não necessita de importação.
# O sleep aguarda o tempo TOTAL setado e o faz apenas uma vez, no momento em que for setado no código.
# O implicity_wait define uma espera global e aguarda ATÉ o tempo limite em todas as buscas por elementos.
  # Porém, se antes desse tempo o elemento esperado for renderizado, ele segue com o teste.
  # Se o tempo limite for atingido e elemento não for encontrado, o teste quebra.


browser.get(url)

button_1 = browser.find_element(By.ID, 'btn1')
button_2 = browser.find_element(By.ID, 'btn2')

button_1.is_displayed()
button_2.is_displayed()

button_1.click()
campo_text_1 = browser.find_element(By.XPATH, '(//input[@id="txt1"])[1]')
button_1.is_displayed()
