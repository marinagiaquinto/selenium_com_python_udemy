from selenium.webdriver.common.by import By
import conftest
import pytest

@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_login_valido(self):

        # Cenário 1 
        # Login com usuário e senha válidos
        # Verificar se foi para a pág de Products

        browser.find_element(By.ID, 'user-name').send_keys('standard_user')
        browser.find_element(By.ID, 'password').send_keys('secret_sauce')
        browser.find_element(By.ID, 'login-button').click()

        browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]').text == 'Products', 'Título da pág diferente de "Products"'

