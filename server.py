from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080    #this is the port in which the server will listen or run

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.path = "index.html"    #serve the index.html file when the root URL is accessed
        return super().do_GET()

with HTTPServer(("127.0.0.1", PORT), MyHandler) as server:

    print(f"Server running at http://127.0.0.1:{PORT}")    #print the server address and port
    server.serve_forever()    #start the server and keep it running indefinitely    

