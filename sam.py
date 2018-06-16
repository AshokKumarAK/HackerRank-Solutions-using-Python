"""arr=[]
arr.append([])
arr.append([])
for i in range(2):
    for j in range(2):
        a = input("Enter the no:")
        arr[i].append(a)
ar=[]
ar.append([])
ar.append([])
for i in range(2):
    for j in range(2):
        a = input("Enter the no:")
        ar[i].append(a)
for i in range(2):
    for j in range(2):
        print (int(arr[i][j]) + int(arr[i][j]))
a=5
b=5
print(["False","True"][a!=b])
n = int(input().strip())
s=[]
for _ in range(n):
    t=input()
    s.append(t)
score=list(map(int,s))
max_score = score[0]
min_score = score[0]

ans1 = 0
ans2 = 0
for val in score:
    if val > max_score:
        max_score = val
        ans1 = ans1 + 1
    if val < min_score:
        min_score = val
        ans2 = ans2 + 1
print (ans1, ans2)
count = [0]*6
for t in map(int,input().strip().split()):
    count[t] += 1
print(count.index(max(count)))
from collections import Counter
n, arr = input(), Counter(map(int, input().split()))
print(arr)
height=0
for c in word:
        height = max(height, height_arr[ ord(c) - ord("a")]
import math as ma
n=5.14
print(ma.floor(n))
A=[3,2,1,3,2,3]
b=[]
for k in range(len(A)-1):
    for i in range(len(A)-k-1):
        j=i+k
        print("i=",i)
        print("j=",j)
        if i==j:
            b.append(A[i])
        else:
            b.append(max(A[i:j]))
import math
print(math.factorial(100))
import math
s=5.3
t=5.6
print(math.ceil(s))
print(math.ceil(t))
import collections
a=[1,2,3,4,4,4,5,5,5,6,6,7,7,7,7,7,7]
#b=int(collections.Counter(a).most_common()[0][1])
#print(b)
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)
a=[1,2,3,4,5]
for i in range(len(a)-1,0,-1):
        for j in range(i):
            print (a[i])
s="ashokkumar"
li=[i for i in s]
li.remove('a')
print(li)
res=[0]*100000000
res.insert(1,10)
print(res)
from string import*
s = input()
print(max(0,sum(not (set(st) & set(s))for st in (digits, ascii_lowercase, ascii_uppercase, "!@#$%^&*()-+"))))"""
def fac(a):
    if a==1 or a==0:
        return 0
    else:
        return fac(a-1)
res = fac(5)
print(res)
