from flask import Flask, render_template

app = Flask(__name__)
# Jinja work really well with dictionaries
# Here we make a list of dictionaries
all_posts = [
    {
        'title': 'post 1',
        'content': 'Imagine this is a post',
        'author':'sa6o'
    },
    {
        'title': 'post 2',
        'content': 'Imagine this is a post'
    }
]

@app.route('/')
def index():
    return "Home Page"

@app.route('/posts')
# We are gonna pass data to jinja thru this posts variable
def posts():
    return render_template('posts.html', posts = all_posts)

if __name__ == '__main__':
    app.run(debug=True)