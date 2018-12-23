from bs4 import BeautifulSoup
import urllib3
import re

url = 'https://www.learncpp.com'

http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data.decode('utf-8'))
# print(soup)
for link in soup.findAll('a', attrs={'href': re.compile('^https://www.learncpp.com/cpp-tutorial$')}):
	print(link.get('href'))


