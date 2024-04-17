const express = require('express');

// My code
var timeInSeconds = 90*24*60*60;
const helmet = require("helmet")
// End My code

const app = express();

module.exports = app;
const api = require('./server.js');
app.use(express.static('public'));

// My code
app.use(helmet.hidePoweredBy());
app.use(helmet.frameguard({
  action: 'deny'
}));
app.use(helmet.xssFilter());
app.use(helmet.noSniff());
app.use(helmet.ieNoOpen());

app.use(helmet.hsts({
  maxAge: timeInSeconds, 
  force: true
}));
app.use(helmet.dnsPrefetchControl());
app.use(helmet.noCache());

//https://cybeready.com/content-security-policy/helmet-content-security-policy
app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", 'trusted-cdn.com'],
  }
}));
// End My code 

// My code : implement helmet Parent
app.use(helmet({
  frameguard: {         // configure
    action: 'deny'
  },
  contentSecurityPolicy: {    // enable and configure
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ['style.com'],
    }
  },
  dnsPrefetchControl: false     // disable
}))
// End My code


app.disable('strict-transport-security');
app.use('/_api', api);
app.get("/", function (request, response) {
  response.sendFile(__dirname + '/views/index.html');
});
let port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Your app is listening on port ${port}`);
});
