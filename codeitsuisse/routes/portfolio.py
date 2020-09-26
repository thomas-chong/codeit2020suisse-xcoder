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

    portfolio = data.get("inputs")
    val = []
    sd_s = []
    for i in range(len(portfolio)):
        val[data.get("Portfolio").get("Name")] = data.get("Portfolio").get("Value")
        sd_s[data.get("Portfolio").get("Name")] = data.get("Portfolio").get("SpotPrcVol")
        index = data.get("IndexFutures")
        coefficient = []
        sd_f = []
        price = []
        ratio = []
        numContracts = []
        for j in range(len(index)):
            coefficient[index[j].get("Name")] = index[j].get("CoRelationCoefficient")
            sd_f[index[j].get("Name")] = index[j].get("FuturePrcVol")
            price[index[j].get("Name")] = index[j].get("IndexFuturePrice")
            notional[index[j].get("Name")] = index[j].get("Notional")

            ratio[index[j].get("Name")] = coefficient[index[j].get("Name")] * sd_s[data.get("Portfolio").get("Name")] / sd_f[index[j].get("Name")]
            numContracts[index[j].get("Name")] = ratio[index[j].get("Name")] * val[data.get("Portfolio").get("Name")] / (price[index[j].get("Name")]*notional[index[j].get("Name")])

        ans = {"Name": index[0].get("Name"), "OptimalHedgeRatio": ratio[index[0].get("Name"), "Notional": numContracts[index[0].get("Name")]}
        for j in range(len(index)):
            if (ratio[j] < ans_ratio):
                ans = {"Name": index[j].get("Name"), "OptimalHedgeRatio": ratio[index[j].get("Name"), "Notional": numContracts[index[j].get("Name")]}
        
    result.append(ans)

    output = {"outputs": result}
    #logging.info("result : {}".format(result))
    return jsonify(output)