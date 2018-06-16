from functools import reduce
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
"""count=collections.Counter(a)
for i in count:
    if count[i]==1:
        print(i)
        break"""
answer =reduce(lambda x,y:x^y,a)
print(answer)