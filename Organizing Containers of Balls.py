import math
import os
import random
#porblem link : https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
#time : O(n)

import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    if sorted([sum(i)  for i in container]) == sorted([sum(i) for i in zip(*container)]):
        return "Possible" 
    else: return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
