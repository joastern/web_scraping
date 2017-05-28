
from lxml import html
import requests

page = requests.get('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')
tree = html.fromstring(page.content)

#price = tree.xpath('//*[@id="quote-leaf-comp"]/section/div[2]/table/tbody/tr/td[1]/span/text()')
price = tree.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div/h1/text()')
print 'Price: ', price

