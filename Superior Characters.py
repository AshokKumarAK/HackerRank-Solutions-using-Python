from itertools import permutations
n=int(input())
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(n):
    st=""
    for j,x in enumerate(input().split()):
        x=int(x)
        if x!=0:
            st+=al[j]*x
    per=permutations(st)
    per=set(per)
    max=0
    for k in per:
        ctr=0
        lent=len(k)
        for l in range(lent):
            if l==0:
                continue
            elif l == lent-1:
                break
            else:
                if ord(k[l-1]) < ord(k[l]) and ord(k[l+1]) < ord(k[l]):
                    ctr+=1
        if ctr>max:
            max=ctr
    print(max)


