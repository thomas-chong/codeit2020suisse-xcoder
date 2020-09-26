import logging
import json
import re 

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/intelligent-farming', methods=['POST'])
def main():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    for i in range(len(data['list'])):
        data['list'][i]['geneSequence'] = reOrder(data['list'][i]['geneSequence'])
    #logging.info("answer : {}".format(answer))
    return jsonify(data)


def reOrder(s):
    res = []
    freq = {}
    freq["A"] = len(re.findall("A", s))
    freq["C"] = len(re.findall("C", s))
    freq["G"] = len(re.findall("G", s))
    freq["T"] = len(re.findall("T", s))
    print(freq["A"])    
    print(freq["C"])
    print(freq["G"])
    print(freq["T"])
        
    i = 1
    while (freq["A"] != 0):
        if (i % 3 == 0 and i != 0):
            if (freq["G"] != 0):
                res.append("G")
                freq["G"] -= 1
            elif (freq["T"] != 0):
                res.append("T")
                freq["T"] -= 1
            elif (freq["A"] != 0):
                res.append("A")
                freq["A"] -= 1
        else:
            res.append("A")
            freq["A"] -= 1
        i += 1

    count_c = int(freq["C"])
    while (count_c != 0):
        res.append("CC")
        freq["C"] -= 2
        count_c -= 2

    while (min([freq["A"],freq["C"],freq["G"],freq["T"]]) > 0):
        res.append("ACGT")
        freq["A"] -= 1
        freq["C"] -= 1
        freq["G"] -= 1
        freq["T"] -= 1
        
    while (freq["C"] != 0):
        res.append("C")
        freq["C"] -= 1
    while (freq["G"] != 0):
        res.append("G")
        freq["G"] -= 1
    while (freq["T"] != 0):
        res.append("T")
        freq["T"] -= 1
    
    return ''.join(res)



