#!/usr/bin/env/ python

import os
from flask import Flask, jsonify, abort, make_response
import random

words_file = "/usr/share/dict/words"
words = open(words_file).read().splitlines()

app = Flask(__name__)

@app.route('/')
def index():
	return "Blue-Cow-Moon"

@app.route('/generate')
def generate_bcm():
	domain = []
	for i in range(0,3):
		domain.append(words[random.randrange(len(words))])
	dstring = "-".join(domain)
	return jsonify({'domain': dstring.replace("'","")})

@app.route('/plain')
def generate_plain():
	domain = []
	for i in range(0,3):
		domain.append(words[random.randrange(len(words))])
	dstring = "-".join(domain)
	return dstring.replace("'","")

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')