from pymongo import MongoClient
import json
import datetime

con=MongoClient("localhost",27017)
db=con.get_database("mydb")

myclass=db.userface
datain=db.logfacein
dataout=db.logfaceout

d=datetime.datetime.today()
def finddate():
    #d=datetime.datetime.today()
    mydayofweek=datetime.date.today().strftime("%A")
    myday=datetime.date.today().strftime("%d")
    mymonth=datetime.date.today().strftime("%B")
    myyear=datetime.date.today().strftime("%Y")
    myhour = d.hour
    myminute=d.minute
    mysec=d.second
    x="Singin at: "+" "+mydayofweek+" "+" "+myday+" "+mymonth+" "+str(myyear)+" Time: "+str(myhour)+":"+str(myminute)+":"+str(mysec)
    return x

def insertData(faceid):
    for f in myclass.find({"faceid":faceid}):
        g=f
    if(d.hour >= 8 and d.hour <=9):
        if(g['status'] != "1"):
            print("in")
            datain.insert({"id":g['id'],"name":g['name'],"surname":g['surname'],
                       "time":finddate()})
            myclass.update_one({"id":g['id']},
            {
               "$set":{
                   "status":"1"
               }
            })
            return "id: "+str(g['id'])+"\n name: "+str(g['name'])
        else:
            print("hasid")
            return "id: "+str(g['id'])+"\n name: "+str(g['name'])
    elif(d.hour>=15 and d.hour <= 23 ):
        if(g['status']!="0"):
            print("out")
            dataout.insert({"id":g['id'],"name":g['name'],"surname":g['surname'],
                       "time":finddate()})
            myclass.update_one({"id":g['id']},
            {
                "$set":{
                  "status":"0"
                }
            })
            return "id: "+str(g['id'])+"\n name: "+str(g['name'])
        else:
            print("hasID")
            return "id: "+str(g['id'])+"\n name: "+str(g['name'])
    else:
        print("No service")
        return "id: "+str(g['id'])+"\n name: "+str(g['name'])
        
