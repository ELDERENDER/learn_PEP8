import sys
import os
import math


def calculate(x, y):
    result = 0
    for i in range(10):
        if i % 2 == 0:
            result += math.pow(x, i) / math.factorial(i)
    return result + y
