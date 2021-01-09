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
titel_tag = soup.title
head_tag = soup.head

# Se uma tag tiver apenas um filho e esse filho for um NavigableString, o filho será disponibilizado como .string:
print(titel_tag.string)

# Se o único filho de uma tag for outra tag, e essa tag tiver um .string, a tag pai será considerada igual a
# .stringsua filha:
print(head_tag.contents)
# [<title>The Dormouse's story</title>]

print(head_tag.string)
# 'The Dormouse's story'


# Se uma tag contém mais de uma coisa, não está claro a que .stringse refere, então .stringé definido como None:

print(soup.html.string)