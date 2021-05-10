from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# !NB '///' - relative path, '////' - absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'

# Links the DB to the Flask app
db = SQLAlchemy(app)

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
    return render_template('index.html')

@app.route('/posts', methods=["GET", "POST"])
def posts():
    if request.method == 'POST':
        #Filling database with the data from the Forms
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)

        # Onyl added to current session
        db.session.add(new_post)

        # Saves to db file
        db.session.commit()
        return redirect('/posts')
        
    else:
        # We call our databse table BlogPost
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts_db.html', posts = all_posts)

# We havethe id we want to delete in the 
@app.route('/posts/delete/<int:id>')
def delete(id):
    # 
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts') 

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post)

    


if __name__ == "__main__":
    app.run(debug=True)
