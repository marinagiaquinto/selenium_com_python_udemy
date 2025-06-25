from selenium.webdriver.common.by import By
import conftest
import pytest

@pytest.mark.usefixtures("setup_teardown")
class TestCT05:
    def test_ct05_login_invalido(self):

        browser = conftest.browser

        # Cenário 5 
        # Login com senha inválida

        browser.find_element(By.ID, 'user-name').send_keys('standard_user')
        browser.find_element(By.ID, 'password').send_keys('xxx')
        browser.find_element(By.ID, 'login-button').click()

        browser.find_element(By.CSS_SELECTOR, '[class="error-message-container error"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[class="error-message-container error"]').text == "Epic sadface: Username and password do not match any user in this service"



