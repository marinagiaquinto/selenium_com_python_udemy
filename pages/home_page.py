import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.browser = conftest.browser
        self.titulo_pagina = (By.CSS_SELECTOR, 'span[data-test="title"]')

    def verificar_login_com_sucesso(self):

        self.verificar_se_elemento_existe(self.titulo_pagina)
        self.verificar_se_elemento_esta_visivel(self.titulo_pagina)