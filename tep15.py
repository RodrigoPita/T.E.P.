#!/bin/python3
'''
import sys


N = int(input().strip())
C = input().strip()

strokes = 1
status = C[0]
for k in C:
    if k != status:
        strokes += 1
        status = k
print(strokes)
'''
from math import ceil

arr = [4, 1, 0, 1, 1, 0, 1]
def arrSplit(arr):
    if len(arr) <= 1:
        return 0
    goal = ceil(sum(arr)/2)
    testSum = 0
    count = 0
    cut = "cut"
    step = -1
    for k in arr:
        testSum += k
        step += 1
        print("testSum:", testSum, "goal:", goal)
        if testSum == goal:
            print("step:", step)
            cut = step
            print("cut:", cut)
            count += 1
            break
    if cut != "cut":
        arrA = [arr[k] for k in range(0, cut+1)]
        arrB = [arr[k] for k in range(cut+1, len(arr))]
        
        arrMax = max(arrA, arrB)
        if arrMax == arr:
            return 0
        arrMin = min(arrA, arrB)
        print("arrMax:", arrMax)
        print("arrMin:", arrMin)
        
        tamMax = len(arrMax)
        tamMin = len(arrMin)

        countMax = arrSplit(arrMax)
        countMin = arrSplit(arrMin)

        count += max(countMax, countMin)
    return count
