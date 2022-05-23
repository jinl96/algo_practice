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

# https://leetcode.cn/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        size = len(s)
        is_Palindrome = [[True] * size for _ in range(0, size)]
        for start in range(size - 1, -1, -1):
            for end in range(start + 1, size):
                is_Palindrome[start][end] = (s[start] == s[end]) and (is_Palindrome[start + 1][end - 1])

        def dfs(cur, size, res, ans):
            if cur == size:
                ans.append(res[:])
                return
            for i in range(cur, size):
                if is_Palindrome[cur][i]:
                    res.append(s[cur: i + 1])
                    dfs(i + 1, size, res, ans)
                    res.pop()

        res = []
        ans = []
        dfs(0, size, res, ans)
        return ans