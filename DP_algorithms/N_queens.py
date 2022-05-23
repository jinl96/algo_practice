from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter


# https://leetcode.cn/problems/eight-queens-lcci/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(cur, size, board, dia, reverse_dia, col, res):
            # cur = current column
            if cur == size:
                ans = []
                # update current board into res
                for i in range(0, n):
                    ans.append(''.join(board[i]))
                res.append(ans)
            for row in range(0, n):
                if not col[row] and not dia[cur + row] and not reverse_dia[size - row + cur - 1]:
                    board[cur][row] = 'Q'
                    col[row] = dia[cur + row] = reverse_dia[size - row + cur] = True
                    dfs(cur + 1, size, board, dia, reverse_dia, col, res)
                    board[cur][row] = '.'
                    col[row] = dia[cur + row] = reverse_dia[size - row + cur] = False
        res = []
        board = [['.' for _ in range(0, n)] for _ in range(0, n)]
        dia = [False for _ in range(0, 2 * n - 1)]
        reverse_dia = [False for _ in range(0, 2 * n - 1)]
        col = [False for _ in range(0, n)]
        dfs(0, n, board, dia, reverse_dia, col, res)
        return res

