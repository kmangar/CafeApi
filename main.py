from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from random import randint

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


## Café TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

with app.app_context():

    # cafe1 = Cafe(name='Cafe 1', map_url='https://google.com/maps', img_url='https://example.com/image',
    #              location='New York', seats='10', has_toilet=True, has_wifi=True, has_sockets=True, can_take_calls=True,
    #              coffee_price='2.00')
    # cafe2 = Cafe(name='Cafe 2', map_url='https://google.com/maps', img_url='https://example.com/image',
    #              location='Los Angeles', seats='20', has_toilet=True, has_wifi=True, has_sockets=True,
    #              can_take_calls=True, coffee_price='2.50')
    # db.session.add_all([cafe1, cafe2])

    db.create_all()


## END DB SETUP


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def random():
    # The following code will return a random cafe.
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()

    print(random_cafe)
    return render_template("random.html", cafe=random_cafe)

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
