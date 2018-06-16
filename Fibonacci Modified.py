def fibonacciModified(t1, t2, n):
    bp=[]
    bp.insert(0,0)
    bp.insert(1,t1)
    bp.insert(2,t2)
    for i in range(3,n+1):
        bp.insert(i,((bp[i-1]**2)+bp[i-2]))
    return bp[n]
if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print(result)