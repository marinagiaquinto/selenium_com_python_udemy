import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self): #construtor da classe. Self representa o contexto geral da classe. Quando a função sai do contexto específico e precisa do geral, é necessário usar self.
        self.browser = conftest.browser #importa o browser setado no conftest (pra funcionar, precisa setar self.browser nas funções)
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')


    def fazer_login(self, usuario, senha): #por a função estar dentro da classe, ela precisa do self, por padrão do python.
        self.escrever(self.username_field, usuario) # se não for usar essa abstração, direto com o find_element precisa usar o * para desempacotar a tupla do locator. ex: *self.username_field
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)