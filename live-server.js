const liveServer = require("live-server");

const params = {
  port: 8000,
  host: "0.0.0.0",
  root: ".",
  open: true,
  file: "index.html",
  wait: 1000,
  mount: [['/', './']],
  logLevel: 2,
  middleware: [function(req, res, next) { next(); }]
};

liveServer.start(params); 