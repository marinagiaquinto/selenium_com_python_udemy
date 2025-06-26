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

    def verificar_se_elemento_esta_visivel(self, locator):
        assert self.encontrar_elemento(self.titulo_pagina).text == 'Products', 'Título da pág diferente de "Products"'