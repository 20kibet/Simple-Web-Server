from http.server import SimpleHTTPRequestHandler, HTTPServer

# Server configuration
HOST = "127.0.0.1"  # Localhost
PORT = 8080         # Port to listen on

class MyHandler(SimpleHTTPRequestHandler):
    """
    Custom request handler to serve files.
    Overrides do_GET to handle root requests specifically.
    """
    def do_GET(self):
        """
        Handle GET requests.
        If the path is '/' or '/index.html', serve index.html
        Otherwise, let the default handler handle it.
        """
        if self.path == "/" or self.path == "/index.html":
            self.path = "index.html"  # Serve the index.html file
        # Call the parent class's do_GET method to handle the response
        return super().do_GET()

# Using 'with' ensures the server socket is properly closed when done
with HTTPServer((HOST, PORT), MyHandler) as server:
    print(f"Server running at http://{HOST}:{PORT}")
    # Start the server and keep it running indefinitely
    server.serve_forever()
