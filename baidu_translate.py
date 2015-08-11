#-*-coding:utf-8 -*-
import urllib,web_spider,re,json

def baidu_translate(daifanyi):
	host = "openapi.baidu.com"
	YourApiKey = "CpEdx1EKHKw5SF32G93dxPxg"
	url = "http://openapi.baidu.com/public/2.0/bmt/translate?client_id={0}&q={1}&from=auto&to=auto"  .format(YourApiKey,daifanyi)

	request = web_spider.web_spider(url,host)
	request1 = json.loads(request)
	request2 = request1["trans_result"][0]
	request3 = request2["dst"]
	return request3