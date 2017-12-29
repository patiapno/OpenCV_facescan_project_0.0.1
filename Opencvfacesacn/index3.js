var app = require('express')();
var mongojs = require('./db');
var time =require('time')
var db = mongojs.connect;
var port =process.env.PORT || 8080

app.get('/insert/:face',function(req,res){
    var data = req.params.face;
    var now = time.localtime(Date.now()/1000)
    db.userface.find({faceid:data},function(err,docs){
        var mytime = "Day: "+now.dayOfMonth+":"+now.month;
        mytime += " Time: "+now.hours+":"+now.minutes+":"+now.seconds;
        var raw_data = JSON.stringify(docs)
        var json_data,cutString = ""
        for(var i=0;i<raw_data.length;i++)
        {
            if(raw_data[i] == "[" || raw_data[i] =="]")
            {
                continue;
            }
            else{
                cutString+= raw_data[i];
            }
        }
        json_data = JSON.parse(cutString);
        console.log(json_data.name);
        if(now.hours >= 8 && now.hours <=9)
        {
            console.log("Singin moring");
            if(json_data.status != "1") //0
            {
                console.log("Singin");
                users = {
                    "id": json_data.id,
                    "name":json_data.name,
                    "surname":json_data.surname,
                    "time":mytime
                }
                db.logfacein.insert(users);
                db.userface.update({id:json_data.id},{
                    "$set":{
                        "status":"1"
                    }
                },function(err,result){
                    res.send(result);
                })
            }
            else{  // 1
                res.send("Hasid:Signin")
            }

        }
        else if(now.hours >= 11 && now.hours <=23)
        {
            console.log("Sing out");
            if(json_data.status != "0"){   //0
                console.log("Singout");
                users = {
                    "id": json_data.id,
                    "name":json_data.name,
                    "surname":json_data.surname,
                    "time":mytime
                }
                db.logfaceout.insert(users);
                db.userface.update({id:json_data.id},{
                    "$set":{
                        "status":"0"
                    }
                },function(err,result){
                    res.send(result);
                })
            }
            else{
                res.send("Hasid:Singout")
            }
        }
        else{
            res.send("No service")
        }
    })
})
app.listen(port,function(){
    console.log('run at '+ port)
})
