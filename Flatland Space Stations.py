def calc(n, arr):
    dp = [0] * n
    for i in range(n):
        if arr[i] == 1:
            dp[i] = 0
        else:
            if i == 0:
                dp[i] = 10**9
            else:
                dp[i] = dp[i - 1] + 1
    return dp

n, m = map(int, input().split())
arr = map(int, input().split())
flag = [0] * n
for val in arr:
    flag[val] = 1
d1 = calc(n, flag)
flag = flag[::-1]
d2 = calc(n, flag)
d2 = d2[::-1]
ans = 0
for i in range(n):
    ans = max(ans, min(d1[i], d2[i]))
print (ans)