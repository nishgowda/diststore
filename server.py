#!/usr/bin/env python3

from diststore import DistStore
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)
dstore = DistStore()

@app.route('/master')
def create_master():
    ret = dstore.create_master()
    dstore.add_vol()
    return jsonify(str(ret))
@app.route('/put/<val>')
def put_req(val):
    if dstore.content_idx != 0 and dstore.content_idx % 5 == 0:
        dstore.add_vol_to_master()
        dstore.add_vol()
        #dstore.print_master()
    ret = dstore.put(val)
    return jsonify(ret)

@app.route('/get/<key>')
def get_req(key):
    ret = dstore.get(int(key))
    return jsonify(str(ret.decode('utf-8')))
@app.route('/clear')
def clear():
    dstore.close_master()
    return jsonify('Cleared')


if __name__ == "__main__":
    app.run()
