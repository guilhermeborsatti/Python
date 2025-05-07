from selenium import webdriver
import time

# Abre o navegador
navegador = webdriver.Firefox()

# Acessa um site
navegador.get("https://www.hashtagtreinamentos.com/")

#coloca em tela cheia
navegador.maximize_window()

#selecionar elemento na tela
botao_verde = navegador.find_element("class name", "botao-verde")

#clicar
botao_verde.click()

# Aguarda 10 segundos
time.sleep(10)
