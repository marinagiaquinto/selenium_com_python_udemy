import pytest
from selenium import webdriver

#definir a variável drive de forma global no arquivo e atribuir a ela o webdriver.remote
browser: webdriver.Remote

@pytest.fixture
def setup_teardown():

    # setup
    global browser
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get('https://www.saucedemo.com/')
    
    # run test - como um return. Para de executar esse código, vai pra execução do teste e depois retorna
    yield browser

    # teardown
    browser.quit()