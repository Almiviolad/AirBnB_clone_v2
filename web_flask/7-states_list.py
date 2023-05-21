#!/usr/bin/python3
""" script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)
from models import storage
from models.state import State

@app.teardown_appcontext
def teardown(exception):
    storage.close()
    
@app.route('/states_list', strict_slashes=False)
def all_state():
    states = storage.all(State)
    sorted_state = sorted(states)
    return render_template('7-states_list.html', states=sorted_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
