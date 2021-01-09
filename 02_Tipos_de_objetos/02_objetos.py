from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')

tag = soup.b

print(type(tag))

tag.name = "blockquote"

print(tag)

