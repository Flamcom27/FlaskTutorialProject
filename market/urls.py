from flask import render_template
from market import app
from market.models import Product


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
    products = Product.query.all()
    return render_template('market.html', products=products)
