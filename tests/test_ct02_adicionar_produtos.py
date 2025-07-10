from selenium.webdriver.common.by import By
import conftest
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.base_page import BasePage

@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_adicionar_produto(self):

        # Cenário 2
        # Adição de produtos ao carrinho
        # Adicionar um produto ao carrinho e verificar que foi adicionado corretamente. 
        # Voltar e adicionar mais um produto

        browser = conftest.browser
        login_page = LoginPage()
        home_page = HomePage()
        base_pag = BasePage()

        browser.implicitly_wait(30)

        # Login
        login_page.fazer_login('standard_user', 'secret_sauce')


        # Add produto 1 no carrinho
        home_page.adicionar_ao_carrinho_pag_item('Sauce Labs Backpack')
        base_pag.verificar_texto_esperado((By.ID, 'remove'), 'Remove')
        home_page.qtd_itens_carrinho('1')

        #retornando a tela principal
        home_page.retornar_tela_principal()
        home_page.verificar_estado_botao_remover_pag_principal('sauce-labs-backpack')

        # adicionando o produto 2
        home_page.adicionar_ao_carrinho_pag_item('Sauce Labs Bike Light')     
        base_pag.verificar_texto_esperado((By.ID, 'remove'), 'Remove')
        home_page.qtd_itens_carrinho('2')

        #retornando a tela principal
        home_page.retornar_tela_principal()
        home_page.verificar_estado_botao_remover_pag_principal('sauce-labs-backpack')
        home_page.verificar_estado_botao_remover_pag_principal('sauce-labs-bike-light')

