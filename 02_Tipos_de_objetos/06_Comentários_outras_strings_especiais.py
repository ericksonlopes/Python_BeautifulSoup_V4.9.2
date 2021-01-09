from bs4 import BeautifulSoup

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"

soup = BeautifulSoup(markup, 'html.parser')

comment = soup.b.string

print(type(comment))

print(comment)

print(soup.b.prettify())


# Beautiful Soup também define classes chamadas Stylesheet, Scripte TemplateString, para folhas de estilo CSS
# incorporadas (quaisquer strings encontradas dentro de uma <style>tag), Javascript incorporado (quaisquer strings
# encontradas em uma <script>tag) e modelos HTML (quaisquer strings dentro de uma <template>tag). Essas classes
# funcionam exatamente da mesma maneira que NavigableString; seu único propósito é facilitar a seleção do corpo
# principal da página, ignorando strings que representam outra coisa. (Essas classes são novas no Beautiful Soup
# 4.9.0 e o analisador html5lib não as usa.)

from bs4 import CData
cdata = CData("A CDATA block")
comment.replace_with(cdata)

print(soup.b.prettify())