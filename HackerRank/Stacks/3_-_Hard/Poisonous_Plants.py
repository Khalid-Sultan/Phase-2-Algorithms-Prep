#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


# Complete the poisonousPlants function below.
def poisonousPlants(p):
    stack = deque()
    count = 0
    for i in p:
        streak = 0
        while stack and stack[-1][0] >= i:
            streak = max(streak, stack.pop()[1])
        streak += 1
        if not stack:
            streak = 0
        count = max(count, streak)
        stack.append((i, streak))
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
