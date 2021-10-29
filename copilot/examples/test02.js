// Express server on port 3000

var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io').listen(server);

var port = process.env.PORT || 3000;

app.use(express.static(__dirname + '/public'));

app.get('/', function(req, res){
  res.sendfile(__dirname + '/index.html');
});

server.listen(port);
console.log('Server running on port ' + port);

// Socket.io

io.sockets.on('connection', function(socket) {
  socket.on('chat message', function(msg) {
    io.emit('chat message', msg);
  });
});

// Return the current time

var express = require('express');
var app = express();

app.get('/', function(req, res) {
  res.send(new Date());
});

app.listen(3000);