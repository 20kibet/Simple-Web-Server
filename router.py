from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1><a href='/about'>About</a> | <a href='/students'>Students</a>"

@app.route("/about")
def about():
    return "<h1>About Page</h1><a href='/'>Home</a>"

@app.route("/students/")
def students_home():
    return "<h1>Students Home</h1><a href='/'>Home</a>"

@app.route("/students/<int:student_id>")
def student_profile(student_id):
    return f"<h1>Student ID: {student_id}</h1><a href='/students/'>Back to Students</a>"

if __name__ == "__main__":
    app.run(debug=True)
