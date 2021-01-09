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

# Se houver mais de uma coisa dentro de uma tag, você ainda pode olhar apenas para as strings. Use o .stringsgerador:
for string in soup.strings:
    print(string)


# Essas strings tendem a ter muitos espaços em branco extras, que você pode remover usando o .stripped_stringsgerador
for string in soup.stripped_strings:
    print(repr(string))

