n=int(input())
ar=[]
r1=r2=r3=r4=r5=0
for _ in range(n):
    t=int(input())
    ar.append(t)
for val in ar:
    if val==1:
        r1+=1
    elif val==2:
        r2+=1
    elif val==3:
        r3+=1
    elif val==4:
        r4+=1
    else:
        r5+=1
if r1>=r2 and r1>=r3 and r1>=r4 and r1>=r5:
    print("1")
elif r2>r1 and r2>=r3 and r2>=r4 and r2>=r5:
    print("2")
elif r3>r1 and r3>r2 and r3>=r4 and r3>=r5:
    print("3")
elif r4>r2 and r4>r3 and r4>r1 and r4>=r5:
    print("4")
elif r5>r2 and r5>r3 and r5>r4 and r5>r1:
    print("5")
