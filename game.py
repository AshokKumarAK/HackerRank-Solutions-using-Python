n=input()
s=[]
b=0
w=0
for i in range(int(n)):
    t=input()
    s.append(t)
res=list(map(int,s))
largest=res[0]
for large in res:
    if large > largest:
        largest=large
        b+=1
smallest=res[0]
for small in res:
    if small < smallest:
        smallest=small
        w+=1
print(b,w)