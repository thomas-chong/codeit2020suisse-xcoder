import logging
import json
import re 

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/intelligent-farming', methods=['POST'])
def main():
    data = request.get_json()
    #logging.info("data sent for evaluation {}".format(data))
    apple = data.get("maApple")
    watermelon = data.get("maWatermelon")
    banana = data.get("maBanana")

    guess = apple * 50 + watermelon * 50 + banana * 50
    result = "{}".format(guess)

    #logging.info("answer : {}".format(answer))
    return jsonify(result)


def reOrder(s):
    res = []
    freq["A"] = len(re.findall("A", s))
    freq["C"] = len(re.findall("C", s))
    freq["G"] = len(re.findall("G", s))
    freq["T"] = len(re.findall("T", s))
    
    i = 1
    while (freq["A"] != 0)
        res.append("A")
        freq["A"] -= 1
        if (i % 3 == 0):
            if (freq["G"] != 0):
                res.append("G")
                freq["G"] -= 1
            else if (freq["T"] != 0):
                res.append("T")
                freq["T"] -= 1
            else if (freq["A"] != 0):
                res.append("A")
                freq["A"] -= 1
                i += 1
        i += 1




    count_c = int(freq["C"]/2)
    for i in range(count_c - 1)
        res.append("CC")
        freq["C"] -= 2

    if 


