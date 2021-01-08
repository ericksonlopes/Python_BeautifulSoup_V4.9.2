from bs4 import BeautifulSoup

tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser')

# Uma tag pode ter qualquer número de atributos. A tag possui um atributo “id” cujo valor é “boldest”.
# Você pode acessar os atributos de uma tag tratando a tag como um dicionário:<b id="boldest">
print(tag.b['id'], '\n')

# Você pode acessar esse dicionário diretamente como .attrs:
print(tag.b.attrs)
