__author__ = 'vcholak'

from flask import request, session, redirect, url_for, flash, abort, render_template, g, jsonify
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from products import app
from .models import User, Product, Order

login_manager = LoginManager()
login_manager.init_app(app)

# redirect users to the login view whenever they are required to be logged in
login_manager.login_view = 'login'

# loads the user from the database by its ID
@login_manager.user_loader
def load(user_id):
    return User.get(user_id)

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/product', methods=['GET', 'POST'])
def products():
    # create a product
    if request.method == 'POST':
        name = request.json['name']
        description = request.json['description']
        category = request.json['category']
        price = request.json['price']
        prod = Product(name, description, category, price)
        prod.create()
        response = prod.to_dict()
        return jsonify(response)

    # fetch all products
    products = Product.all()
    return jsonify(products=products)


@app.route('/product/<product_id>', methods=['GET', 'POST', 'DELETE'])
def product(product_id):
    # delete a product
    if request.method == 'DELETE':
        Product.delete(product_id)
        return jsonify({'success': True})

    # update a product
    if request.method == 'POST':
        name = request.json['name']
        description = request.json['description']
        category = request.json['category']
        price = request.json['price']
        prod = Product(name, description, category, price)
        prod.id = product_id
        Product.get(product_id).update(prod)
        return jsonify({'success': True})

    # fetch a product
    prod = Product.get(product_id)
    return jsonify(prod.to_dict())


@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        #name = request.form['name'] - do not use this because you'll get 400 Bad Request
        name = request.json['name']
        street = request.json['street']
        city = request.json['city']
        state = request.json['state']
        postal = request.json['zip']
        country = request.json['country']
        giftwrap = 'giftwrap' in request.json
        items = request.json['products']
        order = Order(name, street, city, state, postal, country, giftwrap)

        #order_id = order.create()
        #print("New Order ID: " + order_id)
        for item in items:
            order.add_product(count=item['count'], product_id=item['id'])
        #order.update_items()
        order_id = order.create()

        data = order.to_dict()
        data['orderId'] = order_id
        return jsonify(data)
    else:
        orders = Order.all()
        return jsonify(orders=orders)

@app.route('/login', methods=['POST'])
def login():
    #username = request.form['username'] - do not use this because you'll get 400 Bad Request
    username = request.json['username']
    password = request.json['password']
    user = User.load(username, password)
    if user is None:
        flash('Username or password is invalid', 'error')
        response = {'success': False, 'status': 401}  # Not Authenticated
        return jsonify(response)

    print(user)
    login_user(user)
    flash('Logged in successfully')
    return jsonify({'success': True})

@app.route('/logout')
def logout():
    logout_user()
    return jsonify({'success': True})