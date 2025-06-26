
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_login_valido(self):

        # Cenário 1 
        # Login com usuário e senha válidos
        # Verificar se foi para a pág de Products

        #instanciar a LoginPage criando um objeto dela. Como uma cópia dela pra ser utilizada aqui.
        login_page = LoginPage()
        login_page.fazer_login('standard_user', 'secret_sauce')

        home_page = HomePage()
        home_page.verificar_login_com_sucesso()
        

