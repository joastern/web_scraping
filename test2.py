
from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#buyers = tree.xpath('/html/body/div[5]/span/text()')
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
print 'Buyers: ', buyers

