x1, v1, x2, v2 = map(int, input().split())
X = [x1, v1]
Y = [x2, v2]
back = X
fwd = Y
dist = fwd[0] - back[0]
while back[0] < fwd[0]:
    back[0] += back[1]
    fwd[0] += fwd[1]
    if fwd[0] - back[0] >= dist:
        break
print( ["No", "YES"][back[0] == fwd[0]])
"""x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
n = 0
if x2 > x1 and v2 > v1:
    print("NO")
elif x1==x2 and v1==v2:
    print("YES")
elif (x1 - x2) % (v2 - v1) == 0:
    print ("YES")
else:
    print("NO")
    while n!=1000:
        x1 = x1+v1
        x2 = x2+v2
        if x1==x2:
            print ("YES")
            break
        n+=1"""