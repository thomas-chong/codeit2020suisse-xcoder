import logging
import json

from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/olympiad-of-babylon', methods=['POST'])
def main():
    data = request.get_json()
    print(data)

    numBook = data.get("numberOfBooks")
    numDay = data.get("numberOfDays")
    books = data.get("books")
    days = data.get("days")

    result = {"optimalNumberOfBooks": optimalNum(numBook, numDay, books, days)}
    #logging.info("result : {}".format(result))
    return jsonify(result)

def optimalNum(numBook, numDay, books, days):
    count = 0
    remain_books = books
    for i in range(len(days)):
        targetTime = days[i]
        res = []
        ans = []
        #print(remain_books)
        dfs(remain_books, targetTime, 0, res, [])
        for j in range(len(res)):
            if (sum(res[j]) > targetTime):
                res[j].remove(res[j][-1])
        #print(res)
        
        max_length = len(res[0])
        min = targetTime - sum(res[0])
        target = res[0]
        for j in range(len(res)):
            diff = targetTime - sum(res[j])
            length = int(len(res[j]))
            if (length > max_length):
                target = res[j]
                max_length = length
            elif (diff < min and diff >= 0 and res[j] == max_length):
                min = diff
                target = res[j]
        #print(target)
        
        count += len(target)
        for j in range(len(target)):
            remain_books.remove(target[j])
        #print(remain_books)
        #print("---------------------")
    return count

def dfs(nums, temp, index, res, path):
    if (temp < 0):
        return
    elif (temp == 0):
        return
    else:
        if (len(path)==1):
            res.append(path)
        elif (len(path)>1):
            res.append(path)
           
    for i in range(index, len(nums)):
        dfs(nums, temp - nums[i], i + 1, res, path + [nums[i]])