#!/usr/bin/env python
"""
HTTP Protocol Handler - Member 2
Handles HTTP request parsing and response formatting
"""
import os
import time

class HTTPRequest:
    """Parses and stores HTTP request information"""
    
    def __init__(self, handler):
        self.method = handler.command  # GET, POST, etc.
        self.path = handler.path       # Requested path like "/index.html"
        self.headers = dict(handler.headers)  # All HTTP headers
        self.client_address = handler.client_address  # Client IP and port
        
        # Parse query parameters if present in URL
        self.query_params = {}
        if '?' in self.path:
            path_part, query_part = self.path.split('?', 1)
            self.path = path_part
            self._parse_query_string(query_part)
    
    def _parse_query_string(self, query_string):
        """Parse URL query parameters like ?name=value&age=25"""
        pairs = query_string.split('&')
        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                self.query_params[key] = value
    
    def get_header(self, name):
        """Get a specific header value"""
        return self.headers.get(name)
    
    def __str__(self):
        return f"{self.method} {self.path} from {self.client_address[0]}"

class HTTPResponse:
    """Builds and sends HTTP responses"""
    
    def __init__(self, handler):
        self.handler = handler
        self.status_code = 200
        self.headers = {}
        self.content = b""
    
    def set_status(self, code):
        """Set HTTP status code"""
        self.status_code = code
        return self
    
    def set_content(self, content, content_type="text/html"):
        """Set response content and type"""
        if isinstance(content, str):
            self.content = content.encode('utf-8')
        else:
            self.content = content
        
        self.set_header("Content-Type", content_type)
        return self
    
    def set_header(self, name, value):
        """Set a custom header"""
        self.headers[name] = value
        return self
    
    def send(self):
        """Send the complete HTTP response"""
        # Send status code
        self.handler.send_response(self.status_code)
        
        # Set content length
        self.set_header("Content-Length", str(len(self.content)))
        
        # Set default headers if not provided
        if "Content-Type" not in self.headers:
            self.set_header("Content-Type", "text/html")
        
        if "Server" not in self.headers:
            self.set_header("Server", "PythonWebServer/1.0")
        
        # Send all headers
        for name, value in self.headers.items():
            self.handler.send_header(name, value)
        self.handler.end_headers()
        
        # Send content
        self.handler.wfile.write(self.content)

def create_request(handler):
    """Create HTTPRequest object from handler"""
    return HTTPRequest(handler)

def create_response(handler):
    """Create HTTPResponse object from handler"""
    return HTTPResponse(handler)

def send_error(handler, status_code, message):
    """Send standardized error response"""
    error_html = f"""
    <html>
    <head><title>Error {status_code}</title></head>
    <body>
    <h1>Error {status_code}</h1>
    <p>{message}</p>
    <hr>
    <p><em>Python Web Server</em></p>
    </body>
    </html>
    """
    
    response = HTTPResponse(handler)
    response.set_status(status_code)
    response.set_content(error_html)
    response.send()