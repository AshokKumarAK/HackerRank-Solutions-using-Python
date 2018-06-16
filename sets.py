from functools import reduce
from fractions import gcd
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
A = map(int,input().strip().split(' '))
B = map(int,input().strip().split(' '))

def LCM(a, b):
    return (a*b) //gcd(a,b)

lcm = reduce(LCM, A, 1)
print(lcm)
gcd = reduce(gcd, B)
print(gcd)