__author__ = 'vcholak'

import os
from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='../static')
secret_key = os.urandom(24)  # generate based on a cryptographic random generator available in your OS
app.secret_key = secret_key

import products.views

#import logging
#logging.basicConfig(filename='products.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')