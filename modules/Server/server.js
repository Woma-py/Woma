// This file is that at which will be responsible for development server algorithm
const fs = require("fs").promises;
const path = require("path");
const http = require("http");
const dotenv = require("dotenv");

// .ENV
dotenv.config();

// PORT
const PORT = process.env.SERVER__PORT || 5000;

// PUBLIC PATH
const public_path = path.resolve("../../public");

http
  .createServer(function (req, res) {
    res.setHeader("Content-Type", "text/html");
    res.writeHead(200, { "Content-Type": "text/html" });
    fs.readFile(public_path + "/index.html")
      .then((page) => {
        res.end(page);
      })
      .catch((err) => {
        res.writeHead(500);
        res.end(err);
        return;
      });
  })
  .listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  });
