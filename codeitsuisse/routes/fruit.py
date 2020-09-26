import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def main():
    raw = request.get_data()
    data = json.loads(raw.decode('utf-8'))
    print(data)
    #logging.info("data sent for evaluation {}".format(data))
    # apple = data.get("maApple")
    # watermelon = data.get("maWatermelon")
    # banana = data.get("maBanana")
    total = 0
    for key, value in data.items():
        total += value * 80


    # guess = apple * 50 + watermelon * 50 + banana * 50
    result = "{}".format(total)

    #logging.info("answer : {}".format(answer))
    return jsonify(result)