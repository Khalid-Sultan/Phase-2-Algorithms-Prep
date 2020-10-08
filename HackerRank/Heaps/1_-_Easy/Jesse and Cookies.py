#!/bin/python3

import os
import sys
from heapq import *
#
# Complete the cookies function below.
#
def cookies(k, A):
    #
    # Write your code here.
    #
    h = []
    for i in A:
        heappush(h, i)
    ctr = 0

    while True:
        if len(h)<=0:
            return -1
        min_1 = heappop(h)
        if min_1>=k:
            break
        if len(h)<=0:
            return -1
        min_2 = heappop(h)
        heappush(h, min_1 + 2*min_2)
        ctr+=1
    return ctr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
