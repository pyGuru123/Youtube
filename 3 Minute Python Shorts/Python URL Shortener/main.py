# url shortening with python

# required libraries
# requests : pip install requests

# http://tinyurl.com/api-create.php?url=

import requests  

def shorten_url(url):
	base_url = 'http://tinyurl.com/api-create.php?url='
	url = base_url + url
	print('Original URL', url)
	r = requests.get(url)
	print(r.text)

url = 'https://dwhistle.wordpress.com/2020/05/28/who-needed-to-be-saved-us-or-earth/'
shorten_url(url)