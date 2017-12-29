Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> res = urllib.request.urlopen('192.168.1.101:8080/insert/14').read()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    res = urllib.request.urlopen('192.168.1.101:8080/insert/14').read()
AttributeError: module 'urllib' has no attribute 'request'
>>> res = urllib.urlopen('192.168.1.101:8080/insert/14').read()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    res = urllib.urlopen('192.168.1.101:8080/insert/14').read()
AttributeError: module 'urllib' has no attribute 'urlopen'
>>> import urllib3
>>> res = urllib3.urlopen('192.168.1.101:8080/insert/14').read()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    res = urllib3.urlopen('192.168.1.101:8080/insert/14').read()
AttributeError: module 'urllib3' has no attribute 'urlopen'
>>> 
=============================== RESTART: Shell ===============================
>>> import urllib3
>>> http = urllib3.PoolManager()
>>> res = http.request('GET','192.168.1.101:8080/insert/14')
>>> res.status
200
>>> res.data
b'{"ok":1,"nModified":1,"n":1}'
>>> 
