import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# lista com materias
materias = [
   "BIOLOGIA",
   "DESENVOLVIMENTO DE PROJETOS EM INFORMÁTICA",
   "EDUCAÇÃO FÍSICA",
   "EMPREENDEDORISMO",
   "FÍSICA",
   "GEOGRAFIA",
   "HISTÓRIA",
   "LÍNGUA PORTUGUESA",
   "MATEMÁTICA",
   "PORTUGUÊS PARA O ENEM",
   "PROGRAMAÇÃO II",
   "PROGRAMAÇÃO MOBILE",
   "QUÍMICA",
   "SOCIOLOGIA"
]

def buscar_notas():
   usuario = entry_usuario.get()
   senha = entry_senha.get()
   materia = selected_materia.get()

   if not usuario or not senha:
       messagebox.showerror("Erro", "Usuário e senha são obrigatórios.")
       return

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

       # buscar matéria selecionada
       botao_materia = driver.find_element(By.XPATH, f"//a[text()='{materia.upper()}']")
       botao_materia.click()

       wait = WebDriverWait(driver, 15)
       botao_aluno = driver.find_element(By.XPATH, "//div[contains(@class, 'itemMenuHeaderAlunos')]")
       botao_aluno.click()

       botao_ver_notas = driver.find_element(By.XPATH, "//div[@class='itemMenu' and text()='Ver Notas']")
       botao_ver_notas.click()

       # imprime notas
       linhas_notas = driver.find_elements(By.CLASS_NAME, "linhaPar")
       notas = [linha.text for linha in linhas_notas]

       campo_resultado.delete("1.0", tk.END)  # limpa
       if notas:
           campo_resultado.insert(tk.END, "\n".join(notas))
       else:
           campo_resultado.insert(tk.END, "Nenhuma nota encontrada.")

   except Exception as e:
       messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

   finally:
       driver.quit()

# INTERFACE

def criar_interface():
   global entry_usuario, entry_senha, selected_materia, campo_resultado

   root = tk.Tk()
   root.title("Buscar Notas SIGAA")
   root.geometry("600x600")  # aumenta o tamanho da janela

   # Usuário
   tk.Label(root, text="Usuário:").pack(pady=5)
   entry_usuario = tk.Entry(root, width=40)
   entry_usuario.pack(pady=5)

   # Senha
   tk.Label(root, text="Senha:").pack(pady=5)
   entry_senha = tk.Entry(root, width=40, show="*")
   entry_senha.pack(pady=5)

   # Matéria
   tk.Label(root, text="Selecione a Matéria:").pack(pady=5)
   selected_materia = tk.StringVar(value=materias[0])
   tk.OptionMenu(root, selected_materia, *materias).pack(pady=5)

   # Botão buscar
   tk.Button(root, text="Buscar Notas", command=buscar_notas).pack(pady=20)

   # Resultado
   tk.Label(root, text="Notas Encontradas:").pack(pady=5)
   campo_resultado = tk.Text(root, width=70, height=20)
   campo_resultado.pack(pady=10)

   root.mainloop()

# Rodar
if __name__ == "__main__":
   criar_interface()
