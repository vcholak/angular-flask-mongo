__author__ = 'vcholak'

import unittest
from json import dumps
import products.models as models


class JsonTestCase(unittest.TestCase):

    def test_dict(self):
        obj = {"id": 1, "description": "A boat for one person", "name": "Kayak", "price": 275.0, "category": "Watersports"}
        st = dumps(obj)
        print(st)
        assert st is not None

    def test_list(self):
        lst = [{"id": 1, "description": "A boat for one person", "name": "Kayak", "price": 275.0, "category": "Watersports"}]
        st = dumps({'data': lst})
        print(st)
        assert st is not None


class ProductTestCase(unittest.TestCase):

    def setUp(self):
        models.init_db(True)

    def tearDown(self):
        models.Product.delete_all()

    def test_products(self):
        product = models.Product("Kayak", "A boat for one person", "Watersports", 275.0)
        pid = product.create()
        assert pid is not None

        st = dumps(product.to_dict())
        print(st)
        assert st is not None

        products = models.Product.all()
        assert len(products) == 1

        st = dumps({'products': products})
        print(st)
        assert st is not None