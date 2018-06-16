s=input()
n=int(input())
for i in range(n):
    l,r=input().split()
    l,r=[int(l),int(r)]
    t=s[l-1:r]
    tem=set(t)
    if len(t) == len(tem):
        print("0")
    else:
        pass
#failed not completed
