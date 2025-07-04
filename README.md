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

    Atualmente, bibliotecas como webdriver-manager (para Python, por exemplo) automatizam esse processo. Elas verificam a versão do seu navegador, baixam o webdriver compatível e o configuram para você, eliminando a necessidade de gerenciamento manual.

    ![primeiro_teste](/imagens/primeiro_teste.png)


## XPATH

Contains (contén parte do texto)

![contains](/imagens/contains.png)

And, or e | (ou)

![and](/imagens/and.png)

Text = (texto exato)

![text=](/imagens/text=.png)

O "irmão" seguinte (quando quiser ir para a próxima tag, "descendo" no mesmo nível em que já está)

![sibling1](/imagens/sibling1.png)
![sibling2](/imagens/sibling2.png)

Obs: "::" seguido pela tag que quer chegar

## Pytest

![pytest_beneficios](/imagens/pytest_beneficios.png)
![pytest_nomeacao](/imagens/pytest_nomeacao.png)


1. Com a VENV ATIVA, instalar o pytest
2. Criar um arquivo "conftest.py" na raíz do projeto
3. Preencher o arquivo com a configuração de base para execução dos testes: 
   - código comum anterior a execução do teste
   - return para execução do teste
   - fechar o navegador
   ![conftest](/imagens/conftest.png)
4. nos arquivos de teste
   - importar o drive do conftest
   - criar a classe definidora do teste e o método.
    ![confitest_arq_test](/imagens/confitest_arq_test.png)
5. importe o pytest e o uso da fixture
6. ATENÇÃO:
   - TODOS os arquivos de teste devem iniciar com "test_"
   - a pasta de teste deve se chamar "tests" ou "testes"
   - todas as pastas abertas devem conter um __init__.py vazio. Ele ajuda o Python a reconhecer a pasta como um módulo.
   - os testes "pytest" devem ser executados na RAIZ do projeto com a VENV ATIVA

## PageObeject

Padrão de projeto que visa separar o código por páginas criando funções para possibilitar a reutilização do código. 

![PageObeject](/imagens/pageObeject.png)

- Criar uma pasta "pages" aonde vai se concentrar as classes de cada pág
- Criar arquivos que ajudem na reutilização do código