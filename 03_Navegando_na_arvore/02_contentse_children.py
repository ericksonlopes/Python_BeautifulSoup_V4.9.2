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

print(head_tag, '\n')

# colocando as tags em uma lista
print(head_tag.contents)

title_tag = head_tag.contents[0]
print(title_tag)

print(title_tag.contents, '\n')

# O BeautifulSouppróprio objeto tem filhos. Nesse caso, a tag <html> é filha do BeautifulSoupobjeto .
print(len(soup.contents))

print(soup.contents[0].name)

# Uma string não tem .contents, porque não pode conter nada:

