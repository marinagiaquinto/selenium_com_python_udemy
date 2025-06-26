import conftest
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self): #construtor da classe
        self.browser = conftest.browser #importa o browser setado no conftest (pra funcionar, precisa setar self.browser nas funções)
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')


    def fazer_login(self, usuario, senha): #por a função estar dentro da classe, ela precisa do self, por padrão do python.
        self.browser.find_element(*self.username_field).send_keys(usuario) # * para desempacotar a tupla
        self.browser.find_element(*self.password_field).send_keys(senha)
        self.browser.find_element(*self.login_button).click()