import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

@app.route('/pre-tick', methods=['POST'])
def main():
    data = request.get_json()
    df = pd.read_csv(data, delimiter='\n')
    df = df[-51:]
    df["Close"] = pd.to_numeric(df["Close"])
    df['SMA_50'] = df.iloc[:,df.columns == "Close"].rolling(window=50).mean()
    result = str(df['SMA_50'][-1]) 
    logging.info("data sent for evaluation {}".format(data))
    # result = {"result" : search(n, s)}
    # logging.info("result : {}".format(result))
    return jsonify(result)