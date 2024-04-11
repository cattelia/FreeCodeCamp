# YcOZPNhykQqAE2Kb DB password
# cattelia : YcOZPNhykQqAE2Kb
# URI Link: "mongodb+srv://cattelia:YcOZPNhykQqAE2Kb@cluster.xqwz3kx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
# mongodb+srv://cattelia:<password>@cluster.xqwz3kx.mongodb.net/
# mongodb+srv://cattelia:YcOZPNhykQqAE2Kb@cluster.xqwz3kx.mongodb.net/
# 24/04/10: 76.146.226.58/32

'''


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