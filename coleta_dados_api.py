import requests

def enviar_arquivo ():
    # Caminho do aquivo
    caminho = 'C:/Users/ricar/Documents/Projetos/CursoPython/produtos_informatica.xlsx'

    # Enviando arquivo
    requisicao = requests.post('https://file.io', files={'file': open(caminho, 'rb')}) #rb = leitura/binario
    saida_requisicao = requisicao.json() #tranformando em json( chave: valor)

    print(saida_requisicao)
    url = saida_requisicao['link'] #usando atributo link
    print("Arquivo enviado com sucesso, Link de acesso: ", url)


def enviar_arquivo_chave():
    # Caminho do aquivo e chave para Upload
    caminho= 'C:/Users/ricar/Documents/Projetos/CursoPython/produtos_informatica.xlsx'
    chave_acesso = 'PBAMYJD.EM4W2JH-2MKM03J-QX6WZFX-RRMDFW9' # API KEY

    #Enviar o arquivo
    requisicao = requests.post('https://file.io',
                               files={'file': open(caminho, 'rb')},
                               headers={'Authorization': chave_acesso}
                               )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print('Arquivo enviado com sucesso com chave. Link de acesso: ', url)


def receber_arquivo(file_url):
    # Receber o arquivo
    requisicao = requests.get(file_url)

    #Salvando arquivo
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print('Arquivo baixado com sucesso')
    else:
        print("Erro ao baixar arquivo", requisicao.json())


# enviar_arquivo()
# enviar_arquivo_chave()
receber_arquivo('https://file.io/rMgMjhCAuwXu')