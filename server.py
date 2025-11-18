from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.path = "index.html"
        return super().do_GET()

with HTTPServer(("127.0.0.1", PORT), MyHandler) as server:
    print(f"Server running at http://127.0.0.1:{PORT}")
    server.serve_forever()
