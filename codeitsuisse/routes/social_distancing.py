import logging
import json

from flask import request, jsonify;

from codeitsuisse import app
from itertools import permutations 

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def soc_dis_main():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    n = data.get("tests")
    ans = []
    for i in range(len(n)):
        seats = n[i].get("seats")
        people = n[i].get("people")
        spaces = n[i].get("spaces")
        ans.append({}, "i", ":", combinations(seats, people, spaces))
    
    result = {"answers" : ans}
    logging.info("result : {}".format(result))
    return jsonify(result)

def combinations(seats, people, spaces):
    comb = combinations([1, 2, 3], 2) 
