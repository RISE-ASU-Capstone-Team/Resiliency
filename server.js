var express = require('express');
var app = express();

var server = app.listen(8080, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Resiliency app listening at http://%s:%s', host, port);
});

//Default "/" address maps to index.html
app.get('/', function (req, res) {
	res.sendFile(__dirname + '/index.html');
});

//Recieve files from / directory.
app.get('/:name', function (req, res, next) {

  var options = {
    root: __dirname + '/',
    dotfiles: 'allow',
    headers: {
        'x-timestamp': Date.now(),
        'x-sent': true
    }
  };

  var fileName = req.params.name;
  res.sendFile(fileName, options, function (err) {
    if (err) {
      console.log(err);
      res.status(err.status).end();
    }
    else {
      console.log('Sent:', fileName);
    }
  });

});

//Recieve files from /lib/ directory.
app.get('/lib/:name', function (req, res, next) {

  var options = {
    root: __dirname + '/lib/',
    dotfiles: 'allow',
    headers: {
        'x-timestamp': Date.now(),
        'x-sent': true
    }
  };

  var fileName = req.params.name;
  res.sendFile(fileName, options, function (err) {
    if (err) {
      console.log(err);
      res.status(err.status).end();
    }
    else {
      console.log('Sent:', fileName);
    }
  });

});

//Recieve files from /layout/ directory.
app.get('/layout/:name', function (req, res, next) {

  var options = {
    root: __dirname + '/layout/',
    dotfiles: 'allow',
    headers: {
        'x-timestamp': Date.now(),
        'x-sent': true
    }
  };

  var fileName = req.params.name;
  res.sendFile(fileName, options, function (err) {
    if (err) {
      console.log(err);
      res.status(err.status).end();
    }
    else {
      console.log('Sent:', fileName);
    }
  });

});

//Recieve files from /css/ directory.
app.get('/css/:name', function (req, res, next) {

  var options = {
    root: __dirname + '/css/',
    dotfiles: 'allow',
    headers: {
        'x-timestamp': Date.now(),
        'x-sent': true
    }
  };

  var fileName = req.params.name;
  res.sendFile(fileName, options, function (err) {
    if (err) {
      console.log(err);
      res.status(err.status).end();
    }
    else {
      console.log('Sent:', fileName);
    }
  });

});

// accept POST request on the homepage
app.post('/', function (req, res) {
  res.send('Got a POST request');
});
