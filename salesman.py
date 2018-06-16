def minimumTime(x):
    x.sort()
    sum=0
    for i in range(len(x)-1):
        sum+=x[i+1]-x[i];
    return sum
    #  Return the minimum time needed to visit all the houses.

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        x = list(map(int, input().strip().split(' ')))
        result = minimumTime(x)
        print(result)