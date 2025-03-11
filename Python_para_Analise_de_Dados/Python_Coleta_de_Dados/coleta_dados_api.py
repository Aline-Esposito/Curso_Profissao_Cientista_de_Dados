import requests

def enviar_arquivo():
    # Caminho do arquivo para upload
    caminho = 'C:/Users/User/FastBio Dropbox/Aline Esposito/PC/Desktop/EBAC/produtos_informatica (1).xlsx'

    # Enviar arquivo
    requisicao = requests.post('https://file.io/', files={'file': open(caminho, 'rb')})
    saida_requizicao = requisicao.json()

    print(saida_requizicao)
    url = saida_requizicao['link']
    print('Arquivo enviado: link de acesso:', url)


enviar_arquivo()

def receber_arquivo(file_url):

    requisicao =  requests.get(file_url)
    if requisicao.ok:
        with open ('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
            print('Arquivo baixado com sucesso')
    else:
        print('Erro ao baixar o arquivo:' requisicao.json())
receber_arquivo()



def enviar_arquivo_chave():
    caminho =
    chave_acesso =  #API Key

    requisicao = requests.post(
        'https://file.io/'
        files={'file': open(caminho, 'rb')},
        headers={'Authorization': chave_acesso})
    saida_requisicao = requisicao.json()
    print(saida_requisicao)
    url = saida_requisicao['link']
    print('Arquivo enviado com chave. Link de  acesso:', url )

enviar_arquivo_chave()









