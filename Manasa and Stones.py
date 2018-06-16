T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    for x in range(n):
        t=x * a + (n - 1 - x) * b
        print(t)


