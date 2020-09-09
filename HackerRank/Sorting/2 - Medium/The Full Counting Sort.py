#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the countSort function below.
def countSort(arr):
    #Dash it up hehe
    for i in range(len(arr)//2):
        arr[i][1]='-'
    #Built in sorting
    #arr.sort(key=lambda x: int(x[0]))
    count_sort(arr)
    res = " ".join(arr)
    print(res)
def count_sort(arr):
    res = [deque() for i in range(100)]
    for i in arr:
        res[int(i[0])].append(i[1])
    cnt = 0
    for i in res:
        while i:
            arr[cnt] = i.popleft()
            cnt+=1
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
