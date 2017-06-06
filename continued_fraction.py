#
#   Author: Ruby Abrams
#   Description:
#       This is a math tool. This will return the continued fraction
#       list that represents any given number. A given number
#       inputted should be a floating point number.
#       (decimal representation)
#
#       Usage:
#           python continued_fraction.py <decimal number>
#
#
import sys
import numpy as np
from pprint import pprint
from timer import time_this

# @time_this
def continued_fraction_representation_of_(num, error=10**(-5)):
    x = float(num)      # a real number x
    a = []              # sequence of integers
    t = []              # sequence of decimal parts
    a0 = np.int(x)
    t0 = np.abs(x-a0)
    a = np.append(a, a0)
    t = np.append(t, t0)
    while np.abs(t0) >= error:
        a1 = np.int(1/t0)
        t1 = np.abs(a1 - 1/t0)
        a = np.append(a, a1)
        t = np.append(t, t1)
        a0 = a1
        t0 = t1
    return a

if __name__ == '__main__':
    arg = sys.argv[1]
    real_number = float(arg)

    cf = continued_fraction_representation_of_(real_number)
    print(cf)
