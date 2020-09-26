import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/contact_trace', methods=['POST'])
def main():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    s = data.get("shapeCoordinates")
    l = data.get("lineCoordinates")
    findSlope
    result = {"result" : search(n, s)}
    logging.info("result : {}".format(result))
    return jsonify(result)


def result():


def findSlope(n,s):
    s_slope = []
    for i in range(len(s)-1):
        temp = (s[i-1][]-s[i][1])/(s[i][1])
    