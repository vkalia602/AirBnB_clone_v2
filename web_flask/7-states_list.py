#!/usr/bin/python3
"""
Module for flask web framework
"""

from flask import Flask
from flask import render_template
from models import storage, classes
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def render_states():
    state_list = []
    retrieved_dict = storage.all(classes["State"])
    for value in retrieved_dict.values():
        state_list.append(value)
    return render_template('7-states_list.html', state_list=state_list)


@app.teardown_appcontext
def close_dat_sess(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
