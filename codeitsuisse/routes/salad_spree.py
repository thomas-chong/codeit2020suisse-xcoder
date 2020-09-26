import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def evaluateSecretMessage():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    n = data.get("number_of_salads");
    street_map = data.get("salad_prices_street_map");
    #print()
    result = street_map


    logging.info("result :{}".format(result))
    
    return jsonify(result)

# def search():
#     res = []
#     for i in range(len(street_map)):
#         cnt = 0
#         length = 0
#         for j in range(len(street_map[0])):
#             if street_map[i][j] == ‘X’:
#                 cnt = 0
#             else:
#                 cnt += street_map[i][j]
# 			    length += 1
# 	    if length >= n:
# 		    res.append(cnt)
#     if not res:
#         return 0
#     return min(res)
    

    
    
    
    


