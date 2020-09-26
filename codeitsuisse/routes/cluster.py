import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def cluster_main():
    board = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '1':
                cnt += 1
                dfs(board, i, j)
    
    answer = {"answer" : cnt}

    logging.info("answer : {}".format(answer))
    return jsonify(answer)

def dfs(board, i, j):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '*':
        return
    temp = board[i][j]
    board[i][j] = '*'
    dfs(board, i-1, j-1)
    dfs(board, i-1, j)
    dfs(board, i-1, j+1)
    dfs(board, i, j+1)
    dfs(board, i+1, j+1)
    dfs(board, i+1, j)
    dfs(board, i+1, j-1)


