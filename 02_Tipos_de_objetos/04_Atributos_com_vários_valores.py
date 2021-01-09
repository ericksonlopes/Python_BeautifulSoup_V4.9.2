# HTML 4 define alguns atributos que podem ter vários valores. O HTML 5 remove alguns deles, mas define alguns mais.
# O atributo de valores múltiplos mais comum é class(ou seja, uma tag pode ter mais de uma classe CSS).
# Outros incluem rel, rev, accept-charset, headers, e accesskey. Beautiful Soup apresenta o (s) valor (es)
# de um atributo de vários valores como uma lista:
from bs4 import BeautifulSoup

css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')

print(css_soup.p['class'])

css_soup = BeautifulSoup('<p class="body stickeout"></p>', 'html.parser')

print(css_soup.p['class'], '\n')

# Se um atributo parece ter mais de um valor, mas não é um atributo com vários valores
# conforme definido por qualquer versão do padrão HTML, Beautiful Soup deixará o atributo sozinho:
id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
print(id_soup.p['id'], '\n')

# Quando você transforma uma tag de volta em uma string, vários valores de atributos são consolidado
rel_soup = BeautifulSoup('<p> Back to the <a rel="index">home page </a></p>', 'html.parser')

print(rel_soup.a['rel'])

# colocou dentro da tag
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p, '\n')

# Você pode desativar isso passando multi_valued_attributes=Nonecomo um argumento
# de palavra-chave para o BeautifulSoupconstrutor:
no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
print(no_list_soup.p['class'], '\n')

# Você pode usar `get_attribute_listpara obter um valor que é sempre uma lista, seja ou não um atributo de vários
# valores:
id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
print(id_soup.p.get_attribute_list('id'))