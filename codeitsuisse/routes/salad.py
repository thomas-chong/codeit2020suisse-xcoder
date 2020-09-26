import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/salad-spree', methods=['POST'])
def main():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    n = data.get("number_of_salads");
    s = data.get("salad_prices_street_map")
    result = {"result" : search(n, s)}
    logging.info("result : {}".format(result))
    return jsonify(result)

def search(n, street_map):
    if not street_map:
        return 0
    res = float('inf')
    for i in range(len(street_map)):
        cnt = 0
        length = 0
        for j in range(len(street_map[0])):
            if street_map[i][j] == 'X':
                cnt = 0
                length = 0
            else:
                cnt += int(street_map[i][j])
                length += 1
                if length == n:
                    res = min(res, cnt)
                if length > n:
                    cnt -= int(street_map[i][j-n])
                    res = min(res, cnt)
                    length = n
    if res == float('inf'):
        return 0
    return res

# result = search(n, street_map)
# print(result)

