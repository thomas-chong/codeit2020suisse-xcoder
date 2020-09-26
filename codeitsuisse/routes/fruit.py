import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def main():
    data = request.get_json()
    #logging.info("data sent for evaluation {}".format(data))
    apple = data.get("maApple")
    watermelon = data.get("maWatermelon")
    banana = data.get("maBanana")

    guess = apple * 50 + watermelon * 50 + banana * 50
    result = "{}".format(guess)

    #logging.info("answer : {}".format(answer))
    return jsonify(guess)