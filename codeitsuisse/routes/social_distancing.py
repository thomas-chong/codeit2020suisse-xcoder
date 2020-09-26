import logging
import json

from flask import request, jsonify;

from codeitsuisse import app
from itertools import combinations

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])
def soc_dis_main():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    n = data.get("tests")
    # logging.info("result : {}".format(result))
    ans = {}
    for i in range(1, len(n) + 1):
        # seats = n[str(i)]["seats"]
        # people = n[str(i)]["people"]
        # spaces = n[str(i)]["spaces"]
        res = ways(n[str(i)]["seats"], n[str(i)]["people"], n[str(i)]["spaces"])
        # res = ways(seats, people, spaces)
        ans[str(i)] = res
    
    result = {"answers" : ans}
    # logging.info("result : {}".format(result))
    return jsonify(result)

def ways(seats, people, spaces):
    l = []
    count = 0
    for i in range(seats):
        l.append(i)
    comb = combinations(l, people)
    for i in list(comb): 
        correct = True
        for j in range(len(list(i))-1):
            if (i[j+1] - i[j] <= spaces):
                correct = False
        if (correct):
            print(i)
            count+=1
    return count
