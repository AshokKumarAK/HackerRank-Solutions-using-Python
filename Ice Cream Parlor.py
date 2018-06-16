def icecreamParlor(m, arr):
    ans=[]
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[i]+arr[j]==m:
                if i >=j:
                    ans.append(j+1)
                    ans.append(i+1)
                else:
                    ans.append(i+1)
                    ans.append(j+1)
                return ans
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr)
        print (" ".join(map(str, result)))