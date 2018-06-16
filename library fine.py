a,b,c=map(int,input().strip().split())
x,y,z=map(int,input().strip().split())
if c==z:
    if b==y:
        if a==x:
            print(0)
        else:
            val=15*(a-x)
            if val>0:
                print(val)
            else:
                print(0)
    elif b>y:
        print(500*(b-y))
    else:
        print(0)
elif c<z:
    print(0)
else:
    print(10000)