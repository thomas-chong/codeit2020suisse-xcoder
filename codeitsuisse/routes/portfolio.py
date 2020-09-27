import logging
import json

from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/optimizedportfolio', methods=['POST'])
def main():
    data = request.get_json()
    print(data)

    result = []

    inputs = data.get("inputs")       
    val = dict()
    sd_s = dict()
    for i in range(len(inputs)):
        print(inputs[i])
        ans = dict()
        val[inputs[i].get("Portfolio").get("Name")] = inputs[i].get("Portfolio").get("Value")
        print(val[inputs[i].get("Portfolio").get("Name")])
        sd_s[inputs[i].get("Portfolio").get("Name")] = inputs[i].get("Portfolio").get("SpotPrcVol")
        print(sd_s[inputs[i].get("Portfolio").get("Name")])
        index = inputs[i].get("IndexFutures")
        coefficient = dict()
        sd_f = dict()
        price = dict()
        ratio = dict()
        numContracts = dict()
        notional = dict()
        for j in range(len(index)):
            coefficient[index[j].get("Name")] = index[j].get("CoRelationCoefficient")
            print(coefficient[index[j].get("Name")])
            sd_f[index[j].get("Name")] = index[j].get("FuturePrcVol")
            print(sd_f[index[j].get("Name")])
            price[index[j].get("Name")] = index[j].get("IndexFuturePrice")
            print(price[index[j].get("Name")])
            notional[index[j].get("Name")] = index[j].get("Notional")
            print(notional[index[j].get("Name")])

            ratio[index[j].get("Name")] = coefficient[index[j].get("Name")] * sd_s[inputs[i].get("Portfolio").get("Name")] / sd_f[index[j].get("Name")]
            print(ratio[index[j].get("Name")])
            numContracts[index[j].get("Name")] = ratio[index[j].get("Name")] * val[inputs[i].get("Portfolio").get("Name")] / (price[index[j].get("Name")]*notional[index[j].get("Name")])

        for key, value in ratio.items(): 
            if value == min(ratio.values()):
                ans["HedgePositionName"] = key
                ans["OptimalHedgeRatio"] = float("{:.3f}".format(value))
                ans["NumFuturesContract"] = int(numContracts[key])

        
        result.append(ans)

    output = {"outputs": result}
    #logging.info("result : {}".format(result))
    return jsonify(output)