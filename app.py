from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
def home_page():  # put application's code here
    return render_template('home.html')


@app.route('/about')  # dynamic route
def about_page():
    return render_template('about.html')
    # return f'<h1>about page {username}</1>'


@app.route('/market')
def market_page():
    products = [
        {'id': 1, 'name': 'phone', 'barcode': '379463', 'price': '500$'},
        {'id': 2, 'name': 'laptop', 'barcode': '407852', 'price': '1000$'},
        {'id': 3, 'name': 'keyboard', 'barcode': '869306', 'price': '100$'}
    ]
    return render_template('market.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
