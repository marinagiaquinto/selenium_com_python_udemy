import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.browser = conftest.browser
        self.titulo_pagina = (By.CSS_SELECTOR, 'span[data-test="title"]')
        self.item_inventario = (By.XPATH, '(//div[@data-test="inventory-item-name"])[{}]')
        self.button_adicinar_carrinho = (By.ID, 'add-to-cart')

    def verificar_login_com_sucesso(self):

        self.verificar_se_elemento_existe(self.titulo_pagina)
        self.verificar_texto_esperado(self.titulo_pagina, 'Products')

    def adicionar_ao_carrinho(self, posicao_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(posicao_item))
        self.clicar(item)
        self.verificar_texto_esperado(self.button_adicinar_carrinho, 'Add to cart')
        self.clicar(self.button_adicinar_carrinho)