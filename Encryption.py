#time= O(n)
#link:https://www.hackerrank.com/challenges/encryption/problem



#!/bin/python3

import math as mt
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):

  n = mt.ceil(mt.sqrt(len(s)))
  x=['']*n

  for i in range(len(s)):
    y = (i)%n
    x[y]+=s[i]
  print(*x)
    

if __name__ == '__main__':

    s = input()

    encryption(s)

