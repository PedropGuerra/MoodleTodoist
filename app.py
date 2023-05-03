from time import sleep
from playwright.sync_api import sync_playwright

# Acesso Moodle
LNK_LOGIN_MOODLE = "https://www.moodle.fsa.br/login/index.php"
USERNAME = '751806'
PASSWORD = '45038361889'

# Base Links
CURSOS_BASELINK = "course"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Acesso ao Moodle
    page.goto(LNK_LOGIN_MOODLE)

    username_field = page.locator('//*[@id="username"]')
    username_field.type(USERNAME)

    password_field = page.locator('//*[@id="password"]')
    password_field.type(PASSWORD)
    password_field.press("Enter")

    # Validaçõa de Acesso
    if page.title() == "Painel":
        print("Login Efetuado com sucesso")

    else:
        print("Login Mal Sucedido")

    # Listar todos os cursos do Moodle
    cursos = page.locator('a')
    # set(cursos)

    print(cursos.get_attribute('name'))

    browser.close()
