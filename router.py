# router.py 
# Removed: add_route("/", home)

routes = {}

def route(path):
    if path in routes:
        return routes[path]()
    return None  # means: not found

def add_route(path, handler):
    routes[path] = handler


# Example routes
# The 'home' function is no longer needed/used because '/' is now a static file
def about():
    return "<h1>About Page</h1><a href='/'>Home</a>"

# We ONLY define the dynamic route here
add_route("/about", about)