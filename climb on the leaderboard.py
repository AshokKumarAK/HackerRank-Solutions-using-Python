from bisect import bisect
n = int(input())
scores = sorted(set(map(int,input().split())))
m = int(input())
alice = map(int,input().split())
for i in alice:
    print(scores)
    print(bisect(scores,i))
"""scores=list(set(scores))
scores.sort(reverse=True)
flag=True
for j in alice:
    for i in scores:
        if j > i:
            scores.insert(scores.index(i),j)
            scores = list(set(scores))
            scores.sort(reverse=True)
            print(scores.index(j)+1)
            flag=False
            break
    if flag:
        scores.append(j)
        l = len(scores)
        print(l)"""


