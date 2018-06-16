def examRush(tm, t):
    tm.sort()
    count=0
    sum=0
    for j in tm:
        sum += j
        if sum<=t:
            count+=1
    return count

if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    tm = []
    tm_i = 0
    for tm_i in range(n):
       tm_t = int(input().strip())
       tm.append(tm_t)
    result = examRush(tm, t)
    print(result)