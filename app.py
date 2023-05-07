
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

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

    page.fill('//*[@id="username"]', USERNAME)
    # username_field = page.locator('//*[@id="username"]')
    # username_field.type(USERNAME)

    page.fill('//*[@id="password"]', PASSWORD)
    page.press(selector='//*[@id="password"]', key="Enter")
    # password_field.type(PASSWORD)

    # Validaçõa de Acesso
    if page.title() == "Painel":
        print("Login Efetuado com sucesso")

    else:
        print("Login Mal Sucedido")

    # Listar todos os cursos do Moodle
   # cursos = page.locator('a')
    # set(cursos)

    # preciso retirar o class "card-body p-3", uma div que está superior com todos os links
    html = page.inner_html("card-body p-3", timeout=0)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

    browser.close()
