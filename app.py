from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)

    def __repr__(self):
        return self.name


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


if __name__ == '__main__':
    app.run(debug=True)
