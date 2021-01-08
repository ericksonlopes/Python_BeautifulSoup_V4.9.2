import requests
from bs4 import BeautifulSoup

html = requests.get('https://pt.wikipedia.org/wiki/Linguagem_de_programação')

# Executar o documento das "três irmãs" por meio da Beautiful Soup nos dá um
# BeautifulSoup objeto, que representa o documento como uma estrutura de dados aninhada:
soup = BeautifulSoup(html.text, 'html.parser')

print(soup.prettify(), '\n')

# Aqui estão algumas maneiras simples de navegar nessa estrutura de dados:


print(soup.title, '\n')  # titulo da pagina

print(soup.title.name, '\n')  # title

print(soup.title.string, '\n')  # Apenas o conteudo do titulo

print(soup.title.parent.name, '\n')  # parente que esteja o titulo

print(soup.p, '\n')  # exibe a primeira tag p encontrada

# print(soup.p['class'])

print(soup.a, '\n')  # exibe a primeira tag a encontrada

print(soup.find_all('a'), '\n')  # encontra todas as tag a e retorna uma lista
# for item in soup.find_all('a'):
#     print(item)


print(soup.find(title='Software'))  # procura diretamente title com Software como arqumento

# Uma tarefa comum é extrair todos os URLs encontrados nas tags <a> de uma página:
# for link in soup.find_all('a'):
#     print(link.get('href'))

# Outra tarefa comum é extrair todo o texto de uma página:
print(soup.getText())