
from lxml import html
import requests

page = requests.get('https://www.investing.com/currencies/btc-usd-historical-data')
tree = html.fromstring(page.content)

#buyers = tree.xpath('/html/body/div[5]/span/text()')
buyers = tree.xpath('//*[@id="last_last"]')
print 'Buyers: ', buyers

