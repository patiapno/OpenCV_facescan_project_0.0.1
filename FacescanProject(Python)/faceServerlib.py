import urllib3
http = urllib3.PoolManager()

def insertData(faceid):
    res = http.request('GET','YOURIP/insert/'+faceid)
    print(res.status)
    print(res.data)
    #return res.data
    #print(res)
