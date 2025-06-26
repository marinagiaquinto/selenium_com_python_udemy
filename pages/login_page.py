import conftest
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self): #construtor da classe
        self.browser = conftest.browser #importa o browser setado no conftest (pra funcionar, precisa setar self.browser nas funções)

    def fazer_login(self, usuario, senha): #por a função estar dentro da classe, ela precisa do self, por padrão do python.
        self.browser.find_element(By.ID, 'user-name').send_keys(usuario)
        self.browser.find_element(By.ID, 'password').send_keys(senha)
        self.browser.find_element(By.ID, 'login-button').click()