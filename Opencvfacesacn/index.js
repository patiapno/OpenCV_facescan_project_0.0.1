var app = require('express')();
var mongojs = require('./db');
var db = mongojs.connect;
var port =process.env.PORT || 8080


app.get('/insert/:face',function(req,res){
    var data = req.params.face;
    db.userface.find({faceid:data},function(err,docs){
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
        if(json_data.status != "1") //0
        {
            console.log("Singin");
            users = {
                "id": json_data.id,
                "name":json_data.name,
                "surname":json_data.surname
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
        else{   //1
            console.log("Singout");
            users = {
                "id": json_data.id,
                "name":json_data.name,
                "surname":json_data.surname
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

    })
})
app.listen(port,function(){
    console.log('run at '+ port)
})
