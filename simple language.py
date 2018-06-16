#!/bin/python3
n=int(input())
ma = 0
for i in range(n):
    te,va=input().split()
    te,va=[str(te),int(va)]
    if te=="add":
        if ma+va>ma:
            ma=ma+va
    else:
        if va>ma:
            ma=va
print(ma)


