t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if x==y:
        tem=(b+w)*x
    elif x<y:
        if (x+z)<=y:
            tem=b*x+w*(x+z)
        else:
            tem=b*x+w*y
    elif x>y:
        if (y+z)<=x:
            tem=w*y+b*(y+z)
        else:
            tem=b*x+w*y
    print(tem)