# coding: UTF-8
'''
Created on 2017锟斤拷6锟斤拷23锟斤拷
@author: renshunyu
'''
#!/usr/bin/env python
import json
import re
import requests
import xmltodict

#import json

data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}

strs = 'ferf'
 
json_str = json.dumps(data)
jsr = json.dumps(strs)
print (json_str)
print (jsr)
print (strs)
print (data)


data1 = {"rating":{"max":10,"numRaters":79,"average":"9.1","min":0},"subtitle":"","author":["野夫"],"pubdate":"2013-9","tags":[{"count":313,"name":"野夫","title":"野夫"},{"count":151,"name":"散文随笔","title":"散文随笔"},{"count":83,"name":"身边的江湖","title":"身边的江湖"},{"count":82,"name":"土家野夫","title":"土家野夫"},{"count":70,"name":"散文","title":"散文"},{"count":44,"name":"中国文学","title":"中国文学"},{"count":43,"name":"随笔","title":"随笔"},{"count":38,"name":"中国现当代文学","title":"中国现当代文学"}],"origin_title":"","image":"http://img5.douban.com/mpic/s27008269.jpg","binding":"","translator":[],"catalog":"自序 让记忆抵抗n001 掌瓢黎爷n024 遗民老谭n039 乱世游击：表哥的故事n058 绑赴刑场的青春n076 风住尘香花已尽n083 “酷客”李斯n100 散材毛喻原n113 颓世华筵忆黄门n122 球球外传：n一个时代和一只小狗的际遇n141 童年的恐惧与仇恨n151 残忍教育n167 湖山一梦系平生n174 香格里拉散记n208 民国屐痕","pages":"256","images":{"small":"http://img5.douban.com/spic/s27008269.jpg","large":"http://img5.douban.com/lpic/s27008269.jpg","medium":"http://img5.douban.com/mpic/s27008269.jpg"},"alt":"http://book.douban.com/subject/25639223/","id":"25639223","publisher":"广东人民出版社","isbn10":"7218087353","isbn13":"9787218087351","title":"身边的江湖","url":"http://api.douban.com/v2/book/25639223","alt_title":"","author_intro":"郑世平，笔名野夫，网名土家野夫。毕业于武汉大学，曾当过警察、囚徒、书商。曾出版历史小说《父亲的战争》、散文集《江上的母亲》（获台北2010国际书展非虚构类图书大奖，是该奖项第一个大陆得主）、散文集《乡关何处》（被新浪网、凤凰网、新华网分别评为2012年年度好书）。","summary":"1.野夫书稿中被删减最少，最能体现作者观点、情感的作品。n2.文字凝练，具有极强的感染力。以一枝孤笔书写那些就在你我身边的大历史背景下普通人的生活变迁。n3. 柴静口中“一半像警察，一半像土匪”的野夫，以其特有的韵律表达世间的欢笑和悲苦。","price":"32元"}

data2 = json.loads(json.dumps(data1))



#html = urllib2.urlopen(r'http://api.douban.com/v2/book/isbn/9787218087351')
#hjson = json.loads(html.read())
print data2['rating']
print data2['images']['large']
print data2['summary']

assert {"max":10,"numRaters":79,"average":"9.1","min":0}==data2['rating']

#正则表达式测试
pattern = re.compile(r'(\w+) (\w+)')
match = pattern.match('hello word')
assert pattern.match('hello word')
if match:
    print match.group()
#m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print "m.groups():", m.group(2)
m = re.compile(r'[a-zA-Z]')
print m.findall('hello world!')

#接口测试
#r = requests.get('https://github.com/timeline.json')  
#r = requests.post("http://httpbin.org/post")  
#r = requests.put("http://httpbin.org/put")  
#r = requests.delete("http://httpbin.org/delete")  
#r = requests.head("http://httpbin.org/get")  
#r = requests.options("http://httpbin.org/get")
r = requests.get('https://github.com/timeline.json')  
print r.text
data2 = json.loads(r.text)
print data2['documentation_url']
assert "https://developer.github.com/v3/activity/events/#list-public-events" == data2['documentation_url']
print r.json()

#xml转换为json
xmlStr ='<root><log4a><id>wrw</id><name>jjhgj</name></log4a></root>'
convertedDict = xmltodict.parse(xmlStr)
jsonStr = json.dumps(convertedDict)
print "jsonStr=",jsonStr



