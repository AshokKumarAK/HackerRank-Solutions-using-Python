n=input()
s=input().strip().split()
print(s)
flag=0
count=0
for i in s:
    if i.lower()=='u':
        flag+=1
    else:
        flag-=1
print(count)