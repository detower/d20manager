var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.end('<html><head><title>Hello World</title></head><body><h1>Hello World!!!</h1></body></html>');
}).listen(9001, '0.0.0.0');
console.log('Server running at http://127.0.0.1:1337/');

