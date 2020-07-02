import sys
reload(sys)
sys.setdefaultencoding('utf8')

import markdown
from bs4 import BeautifulSoup
html = markdown.markdown(open("nlu.md").read())

print(type(html))

for i, entity in enumerate(html):
    print(i, entity)