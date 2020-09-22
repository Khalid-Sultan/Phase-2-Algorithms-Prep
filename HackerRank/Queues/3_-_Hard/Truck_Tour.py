#!/bin/python3

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps):
    #
    # Write your code here.
    #
    # From what I understood is that we have to choose an index where at each step we subtract the distance from the capacity 
    # while ensuring that we don't drop below zero and reaching our starting point all over again
    # Also we should return the minimum index if there are multiple possiblilities
    # I am sure there is a better code out there, but i'll be looking into improving this solution later on
    for start in range(len(petrolpumps)):
        found = False
        i = start
        prev = 0
        while i<len(petrolpumps):
            prev += petrolpumps[i][0] - petrolpumps[i][1]
            if prev<0:
                found = not found
                break
            i+=1
        if found: continue
        i = 0
        while i<start:
            prev += petrolpumps[i][0] - petrolpumps[i][1]
            if prev<0:
                found = not found
                break
            i+=1
        if found: continue
        return start
    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    
    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
