#import requests # Exercíco 01
#from bs4 import BeautifulSoup
#import pandas as pd
#requests.packages.urllib3.disable_warnings()

#url = 'https://books.toscrape.com/'
#requisicao = requests.get(url)
#extracao = BeautifulSoup(requisicao.text, 'html.parser')
#print(extracao.prettify()[:2000])

import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}
    titulo = artigo.h3.a.text.strip()
    livro['Título'] = titulo

    preco_tag = artigo.find('p', class_='price_color')
    if preco_tag:
        preco = preco_tag.text.strip()
        livro['Preço'] = preco



    catalogo.append(livro)

contar_livros = len(extracao.find_all('article', class_='product_pod'))
df = pd.DataFrame(catalogo)

print("Títulos dos livros:", [livro['Título'] for livro in catalogo])
print("Preços dos livros:", [livro['Preço'] for livro in catalogo])
print('Total livros:', contar_livros)
