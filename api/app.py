from flask import Flask, request, jsonify
from flask import make_response
from flask import redirect
from flask_cors import CORS, cross_origin
# import storage
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, sys

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

# look for db.sqlite file in the current folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
# to avoid complains on the console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init sqlalchemy db
db = SQLAlchemy(app)

# init marshmallow (ma)
ma = Marshmallow(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

# init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/html')
def html():
    return '<h1>HOOOOOLLLLaaaaa</h1>'

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg' : 'Hello World'})

@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)
    db.session.add(new_product)
    db.session.commit()

    # we use marshmallow to Serialize an object to native Python data types according to this Schema’s fields.
    product_dict = product_schema.dump(new_product)
    # we jsonify a python dict
    return jsonify(product_dict)

    # this is a shorter form
    # return product_schema.jsonify(new_product)

# get all products
@app.route('/products', methods=["GET"])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

# get single product
@app.route('/product/<id>', methods=["GET"])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)
    # result = product_schema.dump(product)
    # return jsonify(result)

@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    req = request.json['name']
    # print('///////////////')
    # print(req, file=sys.stderr)
    
    if 'name' in request.json:
        print('got new name', file=sys.stderr)
        product.name = request.json['name']
    if 'description' in request.json:
        print('theres a new description', file=sys.stderr)
        product.description = request.json['description']
    if 'price' in request.json:
        print('theres a new price', file=sys.stderr)
        product.price = request.json['price']
    if 'qty' in request.json:
        print('theres a new qty', file=sys.stderr)
        product.qty = request.json['qty']
    
    # product.description = request.json['description']
    # product.price = request.json['price']
    # product.qty = request.json['qty']

    db.session.commit()

    # we use marshmallow to Serialize an object to native Python data types according to this Schema’s fields.

    # we jsonify a python dict
    return product_schema.jsonify(product)

# @app.route('/booklist/v1/', methods=['GET'])
# def GetAll():
#     if request.method == "GET":
#         result = storage.GetBookList()
#         return result

# @app.route('/booklist/v1/', methods=['POST'])
# def Insert():
#     if request.method == "POST":
#         book = request.args
#         result = storage.InsertBook(book)
#         return result

# @app.route('/booklist/v1/', methods=['PUT'])
# def Update():
#     if request.method == "PUT":
#         book = request.args
#         result = storage.UpdateBook(book)
#         return result

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")