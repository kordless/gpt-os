import datetime
import logging
import os
import json

import requests

from flask import Flask
from flask import session, request, redirect
from flask import render_template, make_response
from flask import url_for

# app up
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# image a page
@app.route('/grub')
def grub():
	document = {"response": "not implemented"}

	return make_response(document)

	
@app.route('/foo')
def foo():
	return None

if __name__ == '__main__':
	# This is used when running locally.
	# app.run(host='127.0.0.1', port=8000, debug=True)
	app.run(host='0.0.0.0', port=8000, debug=True)
	dev = True