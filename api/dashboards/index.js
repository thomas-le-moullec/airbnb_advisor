console.log('PostgreSQL GET Function')
var pg = require('pg')

exports.handler = function(event, context) {
  const userName = process.env.DB_USERNAME;
  const passWord = process.env.DB_PASSWORD;
  const host = process.env.DB_HOST;
  const port = process.env.DB_PORT;
  const dbName = process.env.DB_NAME;
  var conn = 'postgres://'+userName+':'+passWord+'@'+host+':'+port+'/'+dbName
  var client = new pg.Client(conn)
  client.connect()
  //var id = event.id;
  var query = "";
  if (event.city == 'be') {
      query = client.query("SELECT * from processed_data where city = 'be'")
  } else if (event.city == 'pa') {
       query = client.query("SELECT * from processed_data where city = 'pa'")
  } else if (event.city == 'hk') {
       query = client.query("SELECT * from processed_data where city = 'hk'")
  }
  query.on('row', function(row, result) {
    result.addRow(row)
  })
  query.on('end', function(result) {
    var jsonString = JSON.stringify(result.rows)
    var jsonObj = JSON.parse(jsonString)
    console.log(jsonString)
    client.end()
    context.succeed(jsonObj)
  })
}