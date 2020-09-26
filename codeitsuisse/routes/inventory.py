import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/inventory-management', methods=['POST'])
def main():
    data = request.get_data()
    for i in range(len(data))
        search = data[i].get("searchItemName")
        item = data[i].get("items")
        opearation(search,item)

    return jsonify(result)

def operation(search,item):
    