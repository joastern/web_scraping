from lxml import html
import requests

page = requests.get('https://www.investing.com/commodities/gold-historical-data')
tree = html.fromstring(page.content)


date = tree.xpath('//*[@id="curr_table"]/tbody/tr/td[1]/text()')
price = tree.xpath('//*[@id="curr_table"]/tbody/tr/td[2]/text()')
test = tree.xpath('//*[@id="quotes_summary_current_data"]/div[1]/div[2]/div[1]/span[2]/text()')
test2 = tree.xpath('//*[@id="last_last"]')

print 'Date: ', date
print 'Price: ', price
print 'Test: ', test
print 'Test2: ', test2


