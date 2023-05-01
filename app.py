from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



navegador = webdriver.Firefox()

navegador.get("https://www.moodle.fsa.br/login/index.php")

navegador.find_elements(By.XPATH,'//*[@id="username"]')



navegador.quit()