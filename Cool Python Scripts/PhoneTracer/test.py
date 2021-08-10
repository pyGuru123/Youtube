import mechanize
from bs4 import BeautifulSoup

url = 'https://www.findandtrace.com/trace-mobile-number-location'

br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots.txt file
br.open(url)
br.select_form(name='trace')
br['mobilenumber'] = '8182830457'
res = br.submit()

soup = BeautifulSoup(res.read(),'html.parser')

tbl = soup.find_all('table',class_='shop_table')

data = tbl[0].find('tfoot')

count = 0
for tr in data:
	count += 1
	if count in (1,4,6,8):
		continue
	th = tr.find('th')
	td = tr.find('td')

	print(th.text,td.text)

data = tbl[1].find('tfoot')

count = 0
for tr in data:
	count += 1
	if count in (2,20,22,26):
		th = tr.find('th')
		td = tr.find('td')

		print(th.text,td.text)
