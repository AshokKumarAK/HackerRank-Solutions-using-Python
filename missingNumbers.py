from collections import Counter
def missingNumbers(arr, brr):
    a=Counter(arr)
    b=Counter(brr)
    res=[]
    for i,j in zip(a,b):
        if(a[i]!=b[j]):
            res.append(i)
    return res
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    brr = list(map(int, input().strip().split(' ')))
    result = missingNumbers(arr, brr)
    print(" ".join(map(str, result)))