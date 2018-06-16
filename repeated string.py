s=str(input())
n=int(input())
#s1=s*(n//len(s))
print(s.count('a')*(n//len(s))+ s[:n%len(s)].count('a'))
