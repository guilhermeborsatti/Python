from selenium import webdriver
from selenium.webdriver.common.by import By
import time

usuario = "guilhermeb"
senha = "Gui@140308"

driver = webdriver.Chrome()
driver.maximize_window()


try:
    driver.get("https://ead.ifc.edu.br/login/index.php")

    driver.find_element(By.ID, "username").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(senha)
    driver.find_element(By.ID, "loginbtn").click()

    driver.find_element(By.CLASS_NAME, "multiline").click()

    driver.find_element(By.LINK_TEXT, "aqui").click()

    driver.find_element(By.CSS_SELECTOR, ".ndfHFb-c4YZDc-Bz112c.ndfHFb-c4YZDc-C7uZwb-LgbsSe-Bz112c.ndfHFb-c4YZDc-nupQLb-Bz112c").click()
    time.sleep(20)

finally:
    driver.quit()
