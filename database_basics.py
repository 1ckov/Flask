# Importing Database
from db_app import db

# Importing specific model(Table) from database
from db_app import BlogPost

# If not created run this
# db.create_all() ==> ./<db_name>.db

# Querying DB data
print (BlogPost.query.all()) # => [<Blog Post <id>>, <Blog Post <id>>]

# Adding data to DB
db.session.add(BlogPost(title='Blog Post 1', content='Imagine this is a Blog Post', author= 'sa6o'))
db.session.add(BlogPost(title='Blog Post 2',
content='Imagine this is a better  Blog Post'))

print (BlogPost.query.all()) # => [Blog post1, Blog post2][Blog Post]

# Quering a singe cell from a column
print (BlogPost.query.all()[0].title)       # => 'Blog Post 1'
print (BlogPost.query.all()[0].content)     # => 'Imagine this is a Blog Post'
print (BlogPost.query.all()[0].author)      # => 'sa6o
print (BlogPost.query.all()[0].date_posted) # =>  datetime.datetime(2021, 5, 6, 15, 41, 26, 863588)

print (BlogPost.query.all()[1].title)       # => 'Blog Post 2'
print (BlogPost.query.all()[1].content)     # => 'Imagine this is a better Blog Post'
print (BlogPost.query.all()[1].author)      # => 'N/A'
print (BlogPost.query.all()[1].date_posted) # =>  datetime.datetime(2021, 5, 6, 15, 41, 26, 863588)
