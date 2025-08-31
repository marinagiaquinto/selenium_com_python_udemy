import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

#abstrações, métodos/responsabilidades de ações específicas que se repetem no código e que servem para todas as pág

class BasePage:
    def __init__(self):
        self.browser = conftest.browser  #importar o browser

    def encontrar_elemento(self, locator):
        return self.browser.find_element(*locator)
    
    def escrever(self, locator, text):
        return self.encontrar_elemento(locator).send_keys(text)
    
    def clicar(self, locator):
        self.encontrar_elemento(locator).click()
    
    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f'O elemento {locator} não foi encontrado na tela'

    def verificar_texto_esperado(self, locator, texto_esperado):
        self.esperar_elemento_aparecer(locator)
        texto_encontrado = self.encontrar_elemento(locator).text
        assert texto_encontrado == texto_esperado, f'O texto esperado foi "{texto_esperado}", porém o texto apresentado foi "{texto_encontrado}"'

    def esperar_elemento_aparecer (self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(*locator))
    
    def verificar_se_elemento_nao_existe(self, locator):
        assert len(self.encontrar_elementos(locator)) == 0, f'Elemento "{locator}" existe, mas era esperado que não existisse.'

    def clique_duplo(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform()

    def clique_botao_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform()