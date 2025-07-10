import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.browser = conftest.browser
        self.titulo_pagina = (By.CSS_SELECTOR, 'span[data-test="title"]')
        self.item_inventario_pag_principal = (By.XPATH, '//div[@data-test="inventory-item-name" and text()="{}"]')
        self.button_adicinar_carrinho_pag_item = (By.ID, 'add-to-cart')
        self.itens_carrinho = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        self.button_remover_item_inventario_pag_principal = (By.XPATH, '//button[@id="remove-{}"]')
        self.button_retorno_pag_principal = (By.ID, 'back-to-products')

    def verificar_login_com_sucesso(self):

        self.verificar_se_elemento_existe(self.titulo_pagina)
        self.verificar_texto_esperado(self.titulo_pagina, 'Products')

    def adicionar_ao_carrinho_pag_item(self, nome_item):
        #criar o mesmo localizador correspondente ao "item_inventario" só que de forma dinâmica
        #self.item_inventario[0] -> corresponde ao primeiro item da tupla => By.XPATH
        #self.item_inventario[1] -> corresponde ao segundo item da tupla -> locator
        # .format -> para manipular a string preenchendo o valor faltante
        item = (self.item_inventario_pag_principal[0], self.item_inventario_pag_principal[1].format(nome_item))
        self.clicar(item)
        self.verificar_texto_esperado(self.button_adicinar_carrinho_pag_item, 'Add to cart')
        self.clicar(self.button_adicinar_carrinho_pag_item)

    def qtd_itens_carrinho(self, qtd):
        self.verificar_texto_esperado(self.itens_carrinho, qtd)

    def retornar_tela_principal(self):
        self.clicar(self.button_retorno_pag_principal)

    def verificar_estado_botao_remover_pag_principal(self, id_item):
        item = (self.button_remover_item_inventario_pag_principal[0], self.button_remover_item_inventario_pag_principal[1].format(id_item))
        self.verificar_texto_esperado(item, 'Remove')