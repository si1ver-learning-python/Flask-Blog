# Blog Example
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

posts = {
    0: {
        'Title': 'First Blog',
        'Author': 'George',
        'Content': 'first post'
    },
    1: {
        'Title': 'Second Blog',
        'Author': 'Connor',
        'Content': 'second post'
    }
}


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>') # the url would be 'addr/post/0'. 0 would be the post_id and is passed to the function
def access_post(post_id):
    post = posts.get(post_id)
    if post:
        return render_template('post.html', post=post) # variables for the html are the default args
    else:
        return render_template('404.html', message=f'Not found - Post {post_id}')


@app.route('/post/create', methods=['GET', 'POST']) # called from create.html when user submits form
def recv_post():
    if request.method == 'POST':
        title = request.form.get('title') # gets title from submitted form
        author = request.form.get('author')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'Title': title, 'Author': author, 'Content': content}

        """
        'url_for' takes a function and its arguments, and returns the appropriate url
        redirect is used to redirect the user to the specified url
        """
        return redirect(url_for('access_post', post_id=post_id))
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True) # opening in debug mode to get more info for developing
