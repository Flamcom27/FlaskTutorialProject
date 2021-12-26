from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():  # put application's code here
    return render_template('home.html')


@app.route('/about/<username>')  # dynamic route
def about_page(username):
    return f'<h1>about page {username}</1>'


if __name__ == '__main__':
    app.run(debug=True)
