import requests
from BeautifulSoup import BeautifulSoup as bs
import re
import settings

region = ["south","east","west","central"]




def controller(regionn,total_page):
	list = range(int(total_page))
	for j in list:
		crawler(regionn,j+1)



def crawler(reg,page_number):
	url = "http://www.zomato.com/chennai/restaurants/" + reg
	payload = { 'page' : page_number}
	r = requests.get(url,params = payload)
	s = bs(r.text)
	res = s.findAll('div',{'class':re.compile(r'\bsearch-name\b')})
	for w in res:
		hotels = {}
		name = w.find('h3',{'class':re.compile(r'\btop-res-box-name\b')}).a
		address = w.find('span',{'class':re.compile(r'\bsearch-result-address\b')})
		cuisine = w.find('div',{'class':re.compile(r'\bres-snippet-small-cuisine\b')})
		# print name.string
		# print address['title']
		# print cuisine['title']
		# print name['href']
		# print "-----------"
		hotels['name'] = name.string
		hotels['address'] = address['title']
		hotels['cuisine'] = cuisine['title']
		settings.db[reg].insert(hotels)
		print "database "+ reg + "side Chennai Hotels Created"

for i in region:
	url = "http://www.zomato.com/chennai/restaurants/" + i
	req = requests.get(url)
	soup = bs(req.text)
	page = soup.findAll('div',{'class':'pagination-meta'})
	total_page = page[0].string[-1]
	controller(i,total_page)


