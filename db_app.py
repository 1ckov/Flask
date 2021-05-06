from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# !NB '///' - relative path, '////' - absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'

# Links the DB to the Flask app
db = SQLAlchemy(app)

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

# to interact with db we need to create a class, and inherit from db.Model
class BlogPost(db.Model):

    # Each column is a Holds the types of data that willber input into it
    # primary_key = True - sets this column as the primary
    id = db.Column(db.Integer, primary_key = True)

    # db.String(n) - Sets the column type as String, with a length of n
    # nullable = False - sets field as required
    title = db.Column(db.String(100), nullable = False)

    content = db.Column(db.Text, nullable = False)
    author = db.Column(db.String, nullable = False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    # Printing out Blog Posts (equvalent to the toString method from java)
    def __repr__(self) :
        return 'Blog Post ' + str(self.id)



@app.route('/')
def index():
    return "Hello World"

@app.route('/posts', methods=["GET", "POST"])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content, author='sa6o')
        # Onyl added to current session
        db.session.add(new_post)
        # Saves to db file
        db.session.commit()
        return redirect('/posts')
    else:
        # We call our databse table BlogPost
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts_db.html', posts = all_posts)

if __name__ == "__main__":
    app.run(debug=True)
