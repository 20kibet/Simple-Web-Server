import os

class StaticFileHandler:
    def __init__(self, static_dir="."):
        """
        Static file handler.

        Default `static_dir` is the project root (".") so files like
        `index.html`, `style.css` and `script.js` placed in the repository
        root are served without moving them into a `static/` folder.
        """
        self.static_dir = static_dir
        
    def handle_request(self, path):
        """
        Handle static file requests
        Returns (data, content_type) if file exists, None otherwise
        """
        # Clean the path
        if path == "/":
            path = "/index.html"
        
        # Remove leading slash and build full path
        file_path = path.lstrip('/')
        full_path = os.path.join(self.static_dir, file_path)
        
        # Security check - prevent directory traversal
        if not self._is_safe_path(full_path):
            return None
        
        # Check if file exists and is a file
        if not os.path.exists(full_path) or not os.path.isfile(full_path):
            return None
        
        try:
            # Read file as binary
            with open(full_path, 'rb') as f:
                data = f.read()
            
            # Get content type
            content_type = self._get_content_type(full_path)
            
            return data, content_type
            
        except Exception as e:
            print(f"Error reading static file {path}: {e}")
            return None
    
    def _is_safe_path(self, path):
        """Prevent directory traversal attacks"""
        base_dir = os.path.abspath(self.static_dir)
        requested_path = os.path.abspath(path)
        return requested_path.startswith(base_dir)
    
    def _get_content_type(self, filename):
        """Determine content type from file extension"""
        content_types = {
            '.html': 'text/html',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.svg': 'image/svg+xml',
            '.json': 'application/json',
            '.txt': 'text/plain',
            '.ico': 'image/x-icon'
        }
        
        _, ext = os.path.splitext(filename.lower())
        return content_types.get(ext, 'application/octet-stream')