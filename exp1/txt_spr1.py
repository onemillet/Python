#!/usr/bin/python
#coding=utf-8

import urllib,urllib2
import re

page=10
url='https://www.qiushibaike.com/8hr/page/'+str(page)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    html=response.read()
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

re_page=re.compile(r'<div class="author.*?>.*?<a.*?<img.*?alt="(.*?)">.*?<div class="content">(.*?)</div>.*?<div class="stats">.*?<i class="number">(\d+)</i>',re.S)
items=re_page.findall(html)
#print items
for item in items:
    for i in items:
        print i
