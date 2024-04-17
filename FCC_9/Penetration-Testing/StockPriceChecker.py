


api.js>>>

  app.use(helmet({
    frameguard: {
      action: "deny"
    },
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'"],
        styleSrc: ["style.css"],
      }
    }
  }))
  
  
  
  '''

module.exports = function (app) {
// CSP to only allow scripts and CSS

app.use(helmt.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'"],
    styleSrc: ["'self'", "style.css"],
  }
}))


app.use(helmet({
  frameguard: {
    action: "deny"
  },
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'"],
      styleSrc: ["style.css"],
    }
  }
}))