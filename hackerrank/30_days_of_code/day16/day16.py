#!/bin/python3

import sys

S = input().strip()
try:
    temp = int(S)
    print(temp)
except Exception as e:
    print('Bad String')
