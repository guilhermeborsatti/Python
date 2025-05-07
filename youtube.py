from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# inicializando o driver do Chrome
driver = webdriver.Firefox()

# acessar o YouTube
driver.get('https://www.youtube.com')

# aguardar a página carregar
time.sleep(2)

# encontrar a barra de pesquisa do YouTube
search_box = driver.find_element(By.NAME, 'search_query')

# termo da pesquisa
termo_de_pesquisa = 'python tutorial'

# Digitar o termo de pesquisa na barra de pesquisa e pressionar Enter
search_box.send_keys(termo_de_pesquisa)
search_box.send_keys(Keys.RETURN)

# aguarda os resultados carregarem
time.sleep(3)

# mostra os títulos dos vídeos encontrados
videos = driver.find_elements(By.ID, 'video-title')

for video in videos[:5]:  # Mostrar apenas os 5 primeiros vídeos
    print(video.get_attribute('title'))