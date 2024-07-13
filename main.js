
http = require('node:http');

listener = function (require,response){

    response.writeHead(200,{'Content-Type': 'text/html'});
    response.end(`
        <head>
            <h2>Hello World lmao</h2>
        </head>
        <body>
            <h3>This is the body</h3>
            <picture>
                <img src="img ip adress" style="width:auto;">
            </picture>
        </body>
        `);

}

server = http.createServer(listener);
server.listen(100);

console.log('Server running at "web ip adress"');
