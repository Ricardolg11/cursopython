import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'

requisicao = requests.get(url)

extracao = BeautifulSoup(requisicao.text, 'html.parser') #extraindo todo texto

# print(extracao.text.strip()) #strip tirando os espaços em branco

# for linha_texto in extracao.find_all('h2'):
#     titulo = linha_texto.text.strip()
#     print('Titulo:', titulo)


conta_p = 0
conta_h1 = 0

#contanto e exibindo nome dos titulos e paragrafos
for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'p':
        conta_p += 1
        paragrafo = linha_texto.text.strip()
        print('Paragrafo: ', paragrafo)

    elif linha_texto.name == 'h2':
        conta_h1 += 1
        titulo = linha_texto.text.strip()
        print('Titulo:', titulo)

print("Quantidade de titulo: ", conta_h1)
print("Quantidade de paragrafo: " , conta_p)

#exibindo tag aninhadas
for titulo in extracao.find_all('h2'):
    print('\n Titulo: ', titulo.text.strip())
    for link in titulo.find_next_siblings('p'): # find_next_siblings = pegando as proximas tag depois do H2, ate acha o p
            for a in link.find_all('a', href=True): #procurando um a com link verdadeiro
                print('Texto link: ', a.text.strip(), ' URL: ', a['href'])
