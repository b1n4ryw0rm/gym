#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    size = len(a)
    numSwap = 0
    for i in range(size):
        for j in range(size - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numSwap += 1
        
        if numSwap == 0:
            break
    
    print(f"Array is sorted in {numSwap} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[size - 1]}")
                

