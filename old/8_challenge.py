#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
n = 3
sum = 1
if n == 0:
    print(sum) 
else:        
    for i in range(1,n+1):
        sum = sum * i
        print("{} = {} * {}".format(sum,sum,i)) 
        return sum
print()