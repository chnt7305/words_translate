#-*-coding:utf-8 -*-
import re,baidu_translate,sys,sqlite3
type = sys.getfilesystemencoding()

with open('fanyi_wenjian.txt','r') as f:		#打开要翻译的纯文本文件
	daifanyi_wenjian = f.read()
	
daifanyi_danci = re.findall(r'[a-zA-Z]+',daifanyi_wenjian)		#用正则将单词提取出来
daifanyi_danci_pinlu ={}		#建立两个空的字典
daifanyi_danci_fanyi = {}

for i in daifanyi_danci:									#将单词统计 放入字典中 Key是单词本身 值是出现次数
	if daifanyi_danci.count(i) > 0:
		daifanyi_danci_pinlu[i] = daifanyi_danci.count(i)
		
for key in daifanyi_danci_pinlu:							#将单词通过百度翻译模块进行翻译 并放入字典中 Key是单词本身 值是单词释义
	request = baidu_translate.baidu_translate(key)
	daifanyi_danci_fanyi[key] = request
	
conn = sqlite3.connect('fanyi_wenben.db')					#创建数据库
cursor = conn.cursor()
sql = ''' create table words_translate (
		words text,
		words_frequency int,
		word_translate text ) '''
		
		
try:														#测试数据库是否已经存在
	cursor.execute(sql)
except:
	pass
cursor.close()

conn = sqlite3.connect('fanyi_wenben.db')					#在数据库中导入数据
cursor = conn.cursor()

for item in daifanyi_danci_fanyi:
	sql = ''' insert into words_translate
				(words,word_translate)
				values
					(:words_translate_words,:words_translate_word_translate) '''
	cursor.execute(sql,{'words_translate_words':item,'words_translate_word_translate':daifanyi_danci_fanyi[item]})
	conn.commit()

cursor.close()

conn = sqlite3.connect('fanyi_wenben.db')
cursor = conn.cursor()

for ii in daifanyi_danci_pinlu:								#在数据库中修改数据
	cursor.execute("UPDATE words_translate SET words_frequency = {0} WHERE words = '{1}'".format(daifanyi_danci_pinlu[ii],ii))	#WHERE 后面的字符串要加引号
	conn.commit()
cursor.close()
