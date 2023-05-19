#!/usr/bin/python3
""" Script for starting a flask web application """
from flask import Flask, request, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    """ print out hbnb """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
