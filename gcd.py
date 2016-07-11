# GCD calculator
import sys

def gcd(a,b):
    while a%b != 0:
        r = a%b
        p = (a-r)/b
        a = b
        b = r
    return b

def main(a,b):
    return gcd(a,b)

main(sys.argv[1], sys.argv[2])
