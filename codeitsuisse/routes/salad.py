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
    result = search(n, s)
    logging.info("result :{}".format(result))
    return json.dumps(result);

def search(n, street_map):
    res = []
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
                if length >= n:
                    res.append(cnt)
    if not res:
        return 0
    return min(res)

# result = search(n, street_map)
# print(result)