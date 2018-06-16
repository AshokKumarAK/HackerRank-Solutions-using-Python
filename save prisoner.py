t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    if (m+s-1)%n==0:
        print(m+s-1)
    else:
        print(((m+s-1) % n)+1)
