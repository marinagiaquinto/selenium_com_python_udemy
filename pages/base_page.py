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
        return self.encontrar_elemento(locator).click()