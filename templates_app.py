# The render_template function allows us to introduce html into our website 
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return "Home Page"


# One could directly paste HTML code
@app.route('/text')
def index_text():
   return '''
   <!DOCTYPE html><head><title>Home page</title></head><body><h1>Home Page 2</h1></body><html>
   '''
# But templates make for a cleener Program
@app.route('/template')
def index_template():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

