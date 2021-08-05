import requests
from bs4 import BeautifulSoup

texto = input("Digite um site a ser verificado: ")
site = requests.get(texto).content
soup = BeautifulSoup(site, 'html.parser')

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
print(soup.find('temperatura'))
