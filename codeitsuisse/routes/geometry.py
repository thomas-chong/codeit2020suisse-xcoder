import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])
def geometry_main():
    data = request.get_json()
    #logging.info("data sent for evaluation {}".format(data))

    s = data.get("shapeCoordinates")
    l = data.get("lineCoordinates")

    result = res(s,l)

    #logging.info("result : {}".format(result))
    return jsonify(result)

def res(s, l):
    result = []
    for i in range(len(s)):
        line1 = [[int(s[i-1]["x"]), int(s[i-1]["y"])], [int(s[i]["x"]), int(s[i]["y"])]]
        line2 = [[int(l[0]["x"]),int(l[0]["y"])], [int(l[1]["x"]),int(l[1]["y"])]]
        temp = line_intersection(line1,line2)
        if temp:
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
    if (x <= max(line1[0][0],line1[1][0]) and x >= min(line1[0][0],line1[1][0]) and y <= max(line1[0][1], line1[1][1]) and y >= min(line1[0][1], line1[1][1])):
        return [x, y]