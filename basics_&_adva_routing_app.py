####################### 1.Basics ##########################
# Importing the flask Library
from flask import Flask

#!NB
# __name__ is the name of our program file

# Creating a flask object to be our app
app = Flask(__name__)

# Base URL
@app.route('/')

# You can have multiple ulrs leading to the same function 
@app.route('/home')

# This function always gets run when you enter the URL
def hello():
    return "Hello World"


# Defining a route with a parameter  - <type:name> 
@app.route('/home/<string:name>')
def hello_name(name):
    #It can later be called by the argument name 
    return "Hello, " + name


# Possible use of URL parameters
#@app.route('/<string:country>', methods=['GET', 'POST'])

#def index(country):
#    if country == "Bulgaria":
#        language = "BG"
#        return 'Здравей българино'
#    elif language == '' :
#        return None

# Setting the "methods" variable will allow you to Specify 
# which HTTP methods are allowed to be called on your website.
@app.route('/onlyget', methods=['GET'])
def get_only():
    return 'You can only GET this webpage'

# @app.route('/onlyget', methods=['POST'])
# ==> "Method Not Allowed" error will be caused because unless Specified the Browser Always tries to use GET

# Debugging purposes
# !NB When running the app from a terminal the name == main
if __name__ == "__main__":
    app.run(debug=True)