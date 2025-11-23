# server.py (The Aligned Version)

from http.server import SimpleHTTPRequestHandler, HTTPServer
from functools import partial
import os

# Import custom components
from router import route
from static_handler import StaticFileHandler
from protocal import create_request, send_error, HTTPResponse # Import necessary protocol tools

HOST = "127.0.0.1"
PORT = 8080
STATIC_DIR = "." # Set to '.' to serve from project root

# Initialize the static file handler globally
static_handler = StaticFileHandler(static_dir=STATIC_DIR)


class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        # 1. Create Request Object (using protocal.py)
        req = create_request(self)
        path = req.path
        
        # print(f"Handling GET request for: {path}") # Uncomment for debugging

        # 2. Try Custom Routing
        router_content = route(path)
        if router_content is not None:
            # If the router finds a match (e.g., /about), serve dynamic content
            response = HTTPResponse(self)
            response.set_content(router_content, content_type="text/html")
            response.send()
            return

        # 3. Try Static File Serving
        # This handles '/', which is now 'index.html', and all CSS/JS/images
        static_result = static_handler.handle_request(path)
        if static_result is not None:
            # If the static handler finds a file
            data, content_type = static_result
            
            # Send the binary file data
            response = HTTPResponse(self)
            response.set_content(data, content_type=content_type)
            response.send()
            return

        # 4. Fallback: 404 Not Found
        send_error(self, 404, f"The requested URL '{path}' was not found on this server.")
        

def run_server(host=HOST, port=PORT):
    with HTTPServer((host, port), MyHandler) as server:
        print(f"Server running at http://{host}:{port}")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server")


if __name__ == "__main__":
    run_server()