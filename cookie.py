#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import httplib
 
for i in range(0,1000):
    url = "/challenge/web/web-37/"
    cookie = {'Cookie':'PHPSESSID=abcd'}
 
    conn = httplib.HTTPConnection('webhacking.kr')
    conn.request('GET',url,'',cookie)
    data = conn.getresponse().read()
    conn.close()
 
    print data
