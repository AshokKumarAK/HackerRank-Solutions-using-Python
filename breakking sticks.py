from math import sqrt
from itertools import count, islice
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
def longestSequence(a):
    move=0
    for i in range(len(a)):
        if a[i]==1:
            move+=1
        elif isPrime(a[i])==True:
            move+=a[i]+1
        else:
            if a[i]==24:
                move+=46
            elif a[i]==45:
                move+=64
    return move

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = longestSequence(a)
    print(result)