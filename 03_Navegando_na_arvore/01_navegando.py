html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

# Navegando usando nomes de tags

# A maneira mais simples de navegar na árvore de análise é dizer o nome da tag desejada.
# Se você quiser a tag <head>, basta dizer soup.head:
print(soup.head, '\n')

print(soup.title, '\n')

print(soup.body.b, '\n')

# Usar um nome de tag como atributo fornecerá apenas a primeira tag com esse nome:
print(soup.a, '\n')

# Se você precisar obter todas as tags <a>, ou algo mais complicado do que a primeira tag com um determinado
# nome, você precisará usar um dos métodos descritos em Pesquisando a árvore , como find_all () :
print(soup.find_all('a'))
