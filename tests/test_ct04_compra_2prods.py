from selenium.webdriver.common.by import By
import conftest
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
class TestCT04:
    def test_ct04_compra_2_produtos_carrinho(self):

        # Cenário 4
        # Fazer uma compra com 2 produtos no carrinho 
        # Verificar que a compra foi feita com sucesso

        browser = conftest.browser

        # Login
        login_page = LoginPage()
        login_page.fazer_login('standard_user', 'secret_sauce')
        name_title = browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]')
        name_title.is_displayed()

        # Adicionando produto 1 e produto 2
        browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        browser.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()

        # Entrando no carrinho
        browser.find_element(By.ID, 'shopping_cart_container').click()

        # Verificando a compra
        assert browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]').text == 'Your Cart', 'Título diferente de "Your Cart"'

        browser.find_element(By.XPATH, '(//div[@data-test="inventory-item-name"])[1]').is_displayed()
        browser.find_element(By.ID, 'remove-sauce-labs-backpack').is_displayed()
        assert browser.find_element(By.ID, 'remove-sauce-labs-backpack').text == 'Remove' , 'Texto do botão prod 1 diferente de "Remover"'

        browser.find_element(By.XPATH, '(//div[@data-test="inventory-item-name"])[2]').is_displayed()
        browser.find_element(By.ID, 'remove-sauce-labs-bike-light').is_displayed()
        assert browser.find_element(By.ID, 'remove-sauce-labs-bike-light').text == 'Remove' , 'Texto do botão prod 1 diferente de "Remover"'

        # Indo para o checkout
        browser.find_element(By.ID, 'checkout').click()
        assert browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]').text == 'Checkout: Your Information', 'Título diferente de "Checkout: Your Information"'

        #Preenchendo formulário
        browser.find_element(By.ID, 'first-name').send_keys('Marina')
        browser.find_element(By.ID, 'last-name').send_keys('Ferreira')
        browser.find_element(By.ID, 'postal-code').send_keys('13276154')
        browser.find_element(By.ID, 'continue').click()


        #Checando pedido de compra
        assert browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]').text == 'Checkout: Overview', 'Título diferente de "Checkout: Overview"'

        assert browser.find_element(By.XPATH, '(//div[@data-test="inventory-item-name"])[1]').is_displayed()
        assert browser.find_element(By.XPATH, '(//div[@data-test="inventory-item-price"])[1]').is_displayed()

        assert browser.find_element(By.XPATH, '(//div[@data-test="inventory-item-name"])[2]').is_displayed()
        assert browser.find_element(By.XPATH, '(//div[@data-test="inventory-item-price"])[2]').is_displayed()

        assert browser.find_element(By.CSS_SELECTOR, '[data-test="payment-info-label"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[data-test="payment-info-value"]').is_displayed()

        assert browser.find_element(By.CSS_SELECTOR, '[data-test="shipping-info-label"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[data-test="shipping-info-value"]').is_displayed()

        assert browser.find_element(By.CSS_SELECTOR, '[data-test="total-info-label"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[data-test="subtotal-label"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[data-test="tax-label"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').is_displayed()

        assert browser.find_element(By.CSS_SELECTOR, '[data-test="cancel"]').is_displayed()
        assert browser.find_element(By.ID, 'finish').is_displayed()
        browser.find_element(By.ID, 'finish').click()

        #Finalização do pedido
        assert browser.find_element(By.CSS_SELECTOR, '[data-test="complete-header"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, '[data-test="back-to-products"]').is_displayed()
        browser.find_element(By.CSS_SELECTOR, '[data-test="back-to-products"]').click()

        browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]').is_displayed()
        assert browser.find_element(By.CSS_SELECTOR, 'span[data-test="title"]').text == 'Products', 'Título da pág diferente de "Products"'