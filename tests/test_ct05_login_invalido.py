import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT05:
    def test_ct05_login_invalido(self):

        # Cenário 5 
        # Login com senha inválida

        login_page = LoginPage()
        login_page.fazer_login('standard_user', 'xxxxx')
        login_page.verificar_mensagem_de_erro()
        #browser.find_element(By.CSS_SELECTOR, '[class="error-message-container error"]').is_displayed()
        #assert browser.find_element(By.CSS_SELECTOR, '[class="error-message-container error"]').text == "Epic sadface: Username and password do not match any user in this service"



