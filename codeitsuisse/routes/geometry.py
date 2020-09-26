import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def main():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    s = data.get("shapeCoordinates")
    l = data.get("lineCoordinates")

    result = res(s,l)

    logging.info("result : {}".format(result))
    return jsonify(result)

def res(s, l):
    result = []
    for i in range(len(s)):
        line1 = [s[i-1],s[i]]
        line2 = [l[0],l[1]]
        temp = line_intersection(line1,line2)
        if not temp:
           return
        else:
            result.append({"x" : temp[0], "y" : temp[1]})
    return result



def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return []

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return [x, y]