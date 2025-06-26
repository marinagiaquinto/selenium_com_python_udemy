from selenium.webdriver.common.by import By
import conftest
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_login_valido(self):

        # Cenário 1 
        # Login com usuário e senha válidos
        # Verificar se foi para a pág de Products

        browser = conftest.browser


        #instanciar a LoginPage criando um objeto dela. Como uma cópia dela pra ser utilizada aqui.
        login_page = LoginPage()
        login_page.fazer_login('standard_user', 'secret_sauce')

        browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]').text == 'Products', 'Título da pág diferente de "Products"'

