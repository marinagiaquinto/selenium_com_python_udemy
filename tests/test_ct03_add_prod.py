import conftest
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_compra_1_produto_carrinho(self):

        # Cenário 3 
        # Fazer uma compra com 1 produto no carrinho
        # Verificar se a compra foi feita com sucesso

        browser = conftest.browser
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_1_add_remover = 'sauce-labs-backpack'
        produto_2 = "Sauce Labs Fleece Jacket"
        produto_2_add_remover = 'sauce-labs-fleece-jacket'

        browser.implicitly_wait(30)
        # Login
        login_page.fazer_login('standard_user', 'secret_sauce')

        # Adicionando produto 1
        home_page.adicionar_ao_carrinho_pag_principal(produto_1_add_remover)
        time.sle
        # Entrando no carrinho
        home_page.entrar_no_carrinho()

        # Verificando a compra
        carrinho_page.verificar_compra_no_carrinho(produto_1)
        carrinho_page.verificar_estado_botao_remover_pag_carrinho(produto_1_add_remover)

        # Clicanco em voltar
        carrinho_page.voltar_para_pag_principal()

        # Adicionar produto 2
        home_page.adicionar_ao_carrinho_pag_principal(produto_2_add_remover)

        # Entrando no carrinho
        home_page.entrar_no_carrinho()

        # Verificando se os dois produtos estão no carrinho
        carrinho_page.verificar_compra_no_carrinho(produto_1)
        carrinho_page.verificar_estado_botao_remover_pag_carrinho(produto_1_add_remover)
        carrinho_page.verificar_compra_no_carrinho(produto_2)
        carrinho_page.verificar_estado_botao_remover_pag_carrinho(produto_2_add_remover)