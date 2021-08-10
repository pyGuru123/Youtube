import mechanize
from bs4 import BeautifulSoup

url = "https://www.findandtrace.com/trace-mobile-number-location"

br = mechanize.Browser()
br.set_handle_robots(False) # ignore robots
br.open(url)
br.select_form(name="trace")
br["mobilenumber"] = "8896270660"
res = br.submit()

soup = BeautifulSoup(res.read(),'html.parser')

tbl = soup.find_all('table',class_='shop_table')

data = tbl[0].find('tfoot')



#8400374356
