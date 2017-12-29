import urllib3
http = urllib3.PoolManager()

def insertData(faceid):
    res = http.request('GET','192.168.1.101:8080/insert/'+faceid)
    print(res.status)
    print(res.data)
    #print(res)
