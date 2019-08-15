import requests

url = 'http://www.samyukthawordbay.com/andros-treasure/'
res = requests.get(url)
html_page = res.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_page, 'html.parser')


text = soup.find_all(text=True)

"""for i in range(len(text)):
	if "Sandra" in text:
		print(i)
"""

text = text[75:]
t = []

for i in range(len(text)):
	x = text[i].split()
#	print(x)
#	x[i] = x.split()

	
#	for j in range(len(x)):
#		x = x[i].split(' ')
	n = len(x)

	for j in range(n):
		l = list(x[j])
#		print(l[23])
#		list2 = [x for x in l if x != []]

#			t.append(l)
		if len(l)==6:
			if l[0]=='b':
				print(l)

