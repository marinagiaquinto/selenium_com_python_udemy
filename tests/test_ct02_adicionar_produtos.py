from selenium.webdriver.common.by import By
import conftest
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

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

        # Login
        login_page.fazer_login('standard_user', 'secret_sauce')


        # Add produto 1 no carrinho
        home_page.adicionar_ao_carrinho(1)

        browser.find_element(By.ID, 'remove').is_displayed()
        assert browser.find_element(By.ID, 'remove').text == 'Remove' , 'Texto do botão prod 1 diferente de "Remover"'

        qtd_itens_carrinho = browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        assert qtd_itens_carrinho.text == '1' , 'Qtd de itens no carrinho diferente de 1'

        #retornando a tela principal
        browser.find_element(By.ID, 'back-to-products').click()
        assert browser.find_element(By.ID, 'remove-sauce-labs-backpack').text == 'Remove' , 'Texto do botão prod 1 diferente de "Remover"'


        # adicionando o produto 2
        browser.find_element(By.XPATH, '(//div[@data-test="inventory-item-name"])[2]').click()
        browser.find_element(By.XPATH, '(//div[@data-test="inventory-item-name"])[1]').is_displayed()

        button_add_produto_2 = browser.find_element(By.ID, 'add-to-cart')
        button_add_produto_2.is_displayed()
        assert button_add_produto_2.text == 'Add to cart', 'Texto do botão prod 2 diferente de "Add to cart"'
        button_add_produto_2.click()

        browser.find_element(By.ID, 'remove').is_displayed()
        assert browser.find_element(By.ID, 'remove').text == 'Remove' , 'Texto do botão prod 2 diferente de "Remover"'

        qtd_itens_carrinho = browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        assert qtd_itens_carrinho.text == '2' , 'Qtd de itens no carrinho diferente de 2'

        #retornando a tela principal
        browser.find_element(By.ID, 'back-to-products').click()
        assert browser.find_element(By.ID, 'remove-sauce-labs-backpack').text == 'Remove' , 'Texto do botão prod 1 diferente de "Remover"'
        assert browser.find_element(By.ID, 'remove-sauce-labs-bike-light').text == 'Remove' , 'Texto do botão prod 2 diferente de "Remover"'

