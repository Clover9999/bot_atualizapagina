from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# Caminho para o ChromeDriver
driver_path = r'C:\Users\meige\Downloads\chromedriver-win64\chromedriver.exe'

# Verifica se o caminho do ChromeDriver está correto
if not os.path.exists(driver_path):
    print("Erro: O ChromeDriver não foi encontrado no caminho especificado!")
    exit()

# Inicializa o serviço com o caminho do ChromeDriver
service = Service(driver_path)

# Inicializa as opções do navegador
options = Options()
options.add_argument('--ignore-certificate-errors')  # Ignora erros de certificado SSL

# Inicializa o navegador com o serviço e as opções
driver = webdriver.Chrome(service=service, options=options)

# URL que será recarregada
url = "https://www.youtube.com/watch?v=GQrnbLUXToY"  # Altere para a página que deseja atualizar

# Abre a página no navegador
driver.get(url)

# Recarrega a página 30 vezes
for i in range(30):
    print(f"Recarregando página {i+1}/30...")
    driver.refresh()  # Atualiza a página
    time.sleep(2)  # Aguarda 2 segundos entre as recargas

# Fecha o navegador
driver.quit()
print("Processo concluído!")
