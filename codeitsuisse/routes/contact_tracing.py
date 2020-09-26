import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def main():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    n = data.get("number_of_salads");
    s = data.get("salad_prices_street_map")
    result = {"result" : search(n, s)}
    logging.info("result : {}".format(result))
    return jsonify(result)