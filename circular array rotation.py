n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
d = a[n-(k%n):n]+a[0:n-(k%n)]
for a0 in range(q):
    m = int(input().strip())
    print(d[m])