import logging
import json

from flask import request, jsonify;

from codeitsuisse import app
from itertools import combinations
import math 

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def soc_dis_main():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    n = data.get("tests")
    # logging.info("result : {}".format(result))
    ans = {}
    for i in range(1, len(n) + 1):
        seats = n[str(i)]["seats"]
        people = n[str(i)]["people"]
        spaces = n[str(i)]["spaces"]
        res = ways(seats, people, spaces)
        # res = ways(seats, people, spaces)
        ans[str(i)] = res
    
    result = {"answers" : ans}
    # logging.info("result : {}".format(result))
    return jsonify(result)

def ways(seats, people, spaces):
    l = []
    count = 0
    required = people + spaces * (people-1)
    if (required > seats):
        return count
    n = required + 1
    c = seats - required
    if (c > 0):
        count = int(math.factorial(n)/((math.factorial(c)*math.factorial(n-c))))
    return count
