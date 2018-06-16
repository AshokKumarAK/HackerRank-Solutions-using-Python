n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c=c[::k]
zero=c.count(0)
one=c.count(1)
print(100-(one*3)-zero)