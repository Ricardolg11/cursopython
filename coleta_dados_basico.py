import requests
from bs4 import BeautifulSoup
import pandas

#web scraping

print('Request:')
responsa = requests.get('https://br.financas.yahoo.com/quote/%5EBVSP/history/')
print(responsa.text[:500])

print('BeautifulSoup:')
soup = BeautifulSoup(responsa.text, 'html.parser') #parser = analise
print(soup.prettify()[:1000]) #prettify melhora estrutura

print('Pandas: ')
url_dados = pandas.read_html('https://br.financas.yahoo.com/quote/%5EBVSP/history/') #lista de tabela
print(url_dados[0].head(10))
