#-*-coding:utf-8 -*-
import urllib2
def web_spider(url,host):
	headers = {
				"GET":url,
				"Host":host,
#				"Referer":"",
				"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36"
				}
	request = urllib2.Request(url)
	for key in headers:
		request.add_header(key,headers[key])
	html = urllib2.urlopen(request,timeout=3000).read()
	return html
	
