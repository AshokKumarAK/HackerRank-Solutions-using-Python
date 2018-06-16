from collections import Counter
n = int(input().strip())
ar = Counter(list(map(int, input().strip().split(' '))))
result = sockMerchant(n, ar)
def sockMerchant(n, ar):
    p=0
    for s in ar: 
        p+= ar[s]//2
    print(p)
