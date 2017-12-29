var mongojs =require('mongojs')

var databaseUrl = 'mydb'
var collections = ['userface']
var connect = mongojs(databaseUrl,collections);

module.exports = {
    connect:connect
}