import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

#print(extracao.text.strip())

for linha_texto in extracao.find_all('h2'):
    titulo = linha_texto.name
    print('Titulo:', titulo)

contar_titulos = 0
contar_paragrafos = 0

for linha_text in extracao.find_all(['h2' , 'p']):  #contar titulos == contar titulos +1
    if linha_text.name == 'h2':
        contar_titulos += 1
    elif linha_text.name == 'p':
        contar_paragrafos += 1
print('Numero de titulos=', contar_titulos)
print('Numero de paragrafos=', contar_paragrafos)

for linha_text in extracao.find_all(['h2' , 'p']):
    if linha_text.name == 'h2':
        titulo = linha_text.text.strip()
        print('Titulo: \n', titulo)
    elif linha_text.name == 'p':
        pagrafo = linha_text.text.strip()
        print('Paragrafos: \n' , pagrafo)
        
for titulo in extracao.find_all('h2'):
    print('\n Titulo:', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Texto Link:', a.text.strip(),' | URL:', a['href'])




