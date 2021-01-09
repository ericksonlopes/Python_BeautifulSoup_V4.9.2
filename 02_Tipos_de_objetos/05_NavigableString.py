# Uma string corresponde a um pedaço de texto dentro de uma tag.
# Beautiful Soup usa a NavigableStringclasse para conter estes pedaços de texto:
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')

tag = soup.b
# extrair uma string
print(tag.string)
print(type(tag.string))

# A NavigableStringé como uma string Python Unicode, exceto que também suporta alguns dos recursos descritos
# em Navegando na árvore e Pesquisando na árvore . Você pode converter uma NavigableStringstring em Unicode
# com unicode()(no Python 2) ou str(no Python 3):

unicode_string = str(tag.string)
print(unicode_string)
print(type(unicode_string))

# Você não pode editar uma string no local, mas pode substituir uma string por outra, usando replace_with () :
print(tag.string.replace_with('Outro nome'))
print(tag)