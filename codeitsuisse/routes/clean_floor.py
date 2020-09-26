import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/clean_floor', methods=['POST'])
def clean_main():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))

    s = data.get("tests")
    for i in range(len(s)):
        floor = data.get()

    ans = {"answers" : ans(n, s)}

    logging.info("result : {}".format(result))
    return jsonify(result)


def ans(s):
    clean = false
    count = 1
    i = 1;
    while (clean == false):
        if (s[i] == 0):
            s[i] = s[i] + 1
        if (s[i] > 0):
            s[i] = s[i] - 1
        if (i != len(s)-1):
            i = i + 1
            count = count + 1
        else:
            

        
