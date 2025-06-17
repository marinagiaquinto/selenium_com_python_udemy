## Selenium com Pyhton (udemy)

"O Selenium automatiza navegadores. O que você vai fazer com ele, você que decide." 
Ele pode ser usado tanto para automações de testes, quanto pra automação de atividades em geral que são repetitivas. 

https://www.selenium.dev/ 

**Selenium webdriver** : 
É uma biblioteca/módulo para interagir com navegadores. Também pode ser considerado uma API.
Usado para automatizar testes de GUI.

![webdriver](/imagens/webdriver.png)

O webdriver é que executa a ação no navegador.

## Instalação 

1. Instalar o python

2. Vscode > extensões > campo de busca -> python > instalar a extensão para habilitar o suporte pro pyhton.

3. Criar ambiente virtual, para instalar e isolar as dependências de cada projeto. Dentro do repositório do projeto:

    python -m venv venv

(o segundo venv é o nome dado ao ambiente virtual)

4. Ativar o ambiente virtual

    source venv/bin/activate

obs. No curso instalou o python 3.11 e a ativação do ambiente virtual foi com venv/Scripts/Activate.ps1, porém aqui não deu certo.

5. Instalar o selenium (com a VENV ATIVA) e verificar instalação

    pip install selenium

    pip show selenium

**NÃO FOI NECESSÁRIA A INSTALAÇÃO DO WEBDRIVER**