#!/bin/python3

import sys

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m, k = input().strip().split(' ')
        n, m, k = [int(n), int(m), int(k)]
        h = []
        for h_i in range(n):
        	h_t = [int(h_temp) for h_temp in input().strip().split(' ')]
        	h.append(h_t)
        # Write Your Code Here
        a = min(n, m)
        if (a & 1) == 0:
            a /= 2
            (a-1)^2 + 1
        else:
            a^2 + 1
            a += 1
            a /= 2
        maxHeight = int(a)

        memo = {}
        def maxBlocos(x):
            result_from_memo = memo.get(x)
            if result_from_memo is not None:
                return result_from_memo
            elif x == 0:
                return 0
            elif x == 1:
                return 1
            elif (x & 1) == 1:
                resultImpar = x**2 + maxBlocos(x-2)
                return resultImpar
            else:
                resultPar = (x-1)**2 + maxBlocos(x-3)
                return resultPar
                
