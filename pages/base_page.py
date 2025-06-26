import conftest

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
        texto_encontrado = self.encontrar_elemento(locator).text
        assert texto_encontrado == texto_esperado, f'O texto esperado foi "{texto_esperado}", porém o texto apresentado foi "{texto_encontrado}"'
