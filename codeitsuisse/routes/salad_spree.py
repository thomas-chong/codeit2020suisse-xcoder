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
    print()
    result = street_map


    logging.info("result :{}".format(result))
    
    return jsonify(result)

#def search():
    

    
    
    
    


