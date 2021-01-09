from bs4 import BeautifulSoup

# todo| Você pode adicionar, remover e modificar os atributos de uma tag. Novamente,
# todo| isso é feito tratando a tag como um dicionário:

tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b

print(tag['id'])

tag['id'] = 'verybold'

print(tag['id'])

tag['another-attribute'] = 1

print(tag)

del tag['id']
del tag['another-attribute']

print(tag)

print(tag['id'])
print(tag.get('id'))

