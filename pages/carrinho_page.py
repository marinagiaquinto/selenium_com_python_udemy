import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CarrinhoPage(BasePage):

    def __init__(self):
        self.browser = conftest.browser
        self.titulo_pagina_carrinho = (By.CSS_SELECTOR, 'span[data-test="title"]')
        self.item_pag_carrinho = (By.XPATH, '//div[@data-test="inventory-item-name" and text()="{}"]')
        self.button_remover_item_inventario_pag_carrinho = (By.XPATH, '//button[@id="remove-{}"]')
        self.button_voltar_pag_principal = (By.CSS_SELECTOR, '[data-test="continue-shopping"]')

    def verificar_compra_no_carrinho(self, nome_item):
        self.verificar_texto_esperado(self.titulo_pagina_carrinho, 'Your Cart')
        item = (self.item_pag_carrinho[0], self.item_pag_carrinho[1].format(nome_item))
        self.verificar_se_elemento_existe(item)


    def verificar_estado_botao_remover_pag_carrinho(self, id_item):
        item = (self.button_remover_item_inventario_pag_carrinho[0], self.button_remover_item_inventario_pag_carrinho[1].format(id_item))
        self.verificar_texto_esperado(item, 'Remove')

    def voltar_para_pag_principal(self):
        self.clicar(self.button_voltar_pag_principal)