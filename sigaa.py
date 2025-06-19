from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


usuario = "#usuario"
senha = "senha#"


driver = webdriver.Chrome()


try:
   driver.maximize_window()
   driver.get("https://sig.ifc.edu.br/sigaa/verTelaLogin.do")
   

   # logar
   botao_sigaa = driver.find_element(By.CLASS_NAME, "btn-primary")
   botao_sigaa.click()


   user_input = driver.find_element(By.NAME, "user.login")
   user_input.send_keys(usuario)


   password_input = driver.find_element(By.NAME, "user.senha")
   password_input.send_keys(senha)


   password_input.send_keys(Keys.RETURN)


   # buscar notas
   botao_materia = driver.find_element(By.XPATH, "//a[text()='DESENVOLVIMENTO DE PROJETOS EM INFORMÁTICA']")
   botao_materia.click()


   wait = WebDriverWait(driver, 15)
   botao_aluno = driver.find_element(By.XPATH, "//div[contains(@class, 'itemMenuHeaderAlunos')]")
   botao_aluno.click()


   botao_ver_notas = driver.find_element(By.XPATH, "//div[@class='itemMenu' and text()='Ver Notas']")
   botao_ver_notas.click()


   #imprime notas
   linhas_notas = driver.find_elements(By.CLASS_NAME, "linhaPar")


   print("Notas encontradas:")
   for linha in linhas_notas:
       print(linha.text)


   # para nao fechar sozinho
   input("Pressione Enter para encerrar...")


finally:
   driver.quit()



