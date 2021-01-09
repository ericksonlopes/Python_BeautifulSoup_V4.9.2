from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html_doc, 'html.parser')

# Os filhos de uma tag estão disponíveis em uma lista chamada .contents:
head_tag = soup.head

# Os atributos .contentse .childrenconsideram apenas os filhos diretos de uma tag . Por exemplo,
# a tag <head> tem um único filho direto - a tag <title>:
print(head_tag.contents, '\n')

# Mas a própria tag <title> tem um filho: a string “The Dormouse's story”.
# Em certo sentido, essa string também é filha da tag <head>. O .descendantsatributo permite que você
# itere sobre todos os filhos de uma tag, recursivamente: seus filhos diretos, os filhos de seus filhos
# diretos e assim por diante:
for child in head_tag.descendants:
    print(child)

# A tag <head> tem apenas um filho, mas tem dois descendentes: a tag <title> e a criança da tag <title>.
# O BeautifulSoupobjeto tem apenas um filho direto (a tag <html>), mas tem muitos descendentes:
print(len(list(soup.children)))
print(len(list(soup.descendants)))
