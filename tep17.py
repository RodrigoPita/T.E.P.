'''
HACKER RANK 22
'''
import sys

def smallestSizeSubsequence(n, A):
    even = 0
    for k in A:
        if (k & 1) == 0:
            even += 1
    odd = n - even

    if (odd & 1) == 0:
        return 0
    elif even == 0:
        return -1
    else:
        return 1

    # Return the size of the smallest subsequence to remove

n = int(input().strip())
A = list(map(int, input().strip().split(' ')))
result = smallestSizeSubsequence(n, A)
print(result)
