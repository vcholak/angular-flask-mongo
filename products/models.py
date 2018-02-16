__author__ = 'vcholak'

from pymongo import MongoClient
from bson.objectid import ObjectId
from json import dumps
import crypt
from hmac import compare_digest
from datetime import datetime
from .encoder import json_dict


class Product:
    """ Product document"""
    def __init__(self, name, description, category, price):
        self.name = name
        self.description = description
        self.category = category
        self.price = price

    @classmethod
    def all(cls):
        """
        :return: all products
        """
        return [json_dict(prod) for prod in db.products.find()]

    @classmethod
    def get(cls, prod_id):
        """Fetches a product by its string ID"""
        pid = ObjectId(prod_id)  # convert from string to ObjectId
        return db.products.find_one({'_id': pid})

    @classmethod
    def delete(cls, prod_id):
        """Removes from database a product by its string ID"""
        pid = ObjectId(prod_id)  # convert from string to ObjectId
        db.products.remove({"_id": pid})

    @classmethod
    def delete_all(cls):
        """Removes from database all products """
        db.products.remove()

    def __repr__(self):
        return dumps(self.to_dict())

    def to_dict(self):
        """ Dictionary representation """
        return {'name': self.name, 'description': self.description, 'category': self.category, 'price': self.price}

    def create(self):
        product_id = db.products.insert(self.to_dict())
        self._id = product_id
        return str(product_id)

    def update(self, product):
        """Updates whole document."""
        db.products.update({"_id": self._id}, product)


class OrderItem:
    """ Order Item """
    def __init__(self, product, count):
        self.product = product
        self.count = count

    def __repr__(self):
        return dumps(self.to_dict())

    def to_dict(self):
        """ Dictionary representation """
        return {'count': self.count, 'name': self.product['name'], 'price': self.product['price']}


class Order:
    """ Order document """
    def __init__(self, name, street, city, state, postal, country, giftwrap):
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.postal = postal
        self.country = country
        self.giftwrap = giftwrap
        self.items = []  # list of OrderItem

    @classmethod
    def all(cls):
        return [json_dict(order) for order in db.orders.find()]

    def __repr__(self):
        return dumps(self.to_dict())

    def to_dict(self):
        """ Dictionary representation """
        return {'name': self.name, 'street': self.street, 'city': self.city, 'state': self.state,
               'postal': self.postal, 'country': self.country, 'giftwrap': self.giftwrap, 'products': self.items}

    def create(self):
        order_id = db.orders.insert(self.to_dict())
        self._id = order_id
        return str(order_id)

    def add_product(self, product_id, count):
        """
        Adds a product to the order
        :param product_id: string
        :param count: number of products to order
        """
        product = Product.get(product_id)
        item = OrderItem(json_dict(product), count)
        self.items.append(item.to_dict())

    def update_items(self):
        db.orders.update({"_id": self._id}, {'items': self.items})

salt = '$6$dJY0RkstVvQetd6T'  # got it by calling crypt.mksalt()


class User:
    """ User of the app """
    def __init__(self, username, password, email, user_id=None):
        self.username = username
        hashed = crypt.crypt(password, salt)
        self.password = hashed
        self.email = email
        self.registered = datetime.utcnow()
        self.user_id = user_id

    @classmethod
    def all(cls):
        return db.users.find()

    @classmethod
    def load(cls, username, password):
        # first load user by username as User.username is unique
        user = db.users.find_one({'username': username})
        if user is None:
            return None
        hashed = crypt.crypt(password, salt)
        password_ok = compare_digest(user['password'], hashed)
        if not password_ok:
            return None
        return User(username, password, user['email'], str(user['_id']))

    @classmethod
    def get(cls, user_id):
        uid = ObjectId(user_id)  # convert from string to ObjectId
        user = db.users.find_one({'_id': uid})
        return user

    def __repr__(self):
        return dumps(self.to_dict())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    def to_dict(self):
        """ Dictionary representation """
        return {'username': self.username, 'email': self.email, 'registered': self.registered.isoformat()}

    def create(self):
        user_id = db.users.insert(self.to_dict())
        self._id = user_id
        return str(user_id)


def init_db(testing=False):
    """
    :param testing: set to 'True' to connect to a test database; set to 'False' to connect to a production / development database.
    :return: a database reference
    """
    client = MongoClient()  # connect on the default host and port
    if not testing:
        database = client['products']
    else:
        database = client['products-test']
    return database


def create_admin():
    """ Creates Admin user """
    users = db.users
    admin = users.find_one({'username': 'admin'})
    user_id = None
    if admin is None:
        admin = User('admin', 'Zaq!23', 'volchok60@yahoo.com')
        user_id = admin.create()
    return user_id

db = init_db()

create_admin()
