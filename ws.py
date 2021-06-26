from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content
# objeto site está recebendo o conteudo da requisição http do site...
soup = BeautifulSoup(site, 'html.parser')
# objeto soup está baixando do site o html desse site.
print(soup.prettify())
# transforma a estrutura html em string



