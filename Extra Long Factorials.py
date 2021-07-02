#time : O(1)
#problem link : https://www.hackerrank.com/challenges/extra-long-factorials/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    x = 1
    for i in range(n):
        x*=i+1
    return x
if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))
