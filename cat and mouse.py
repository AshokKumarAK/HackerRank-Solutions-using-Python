q=int(input())
for _ in range(q):
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]
    cata=abs(x-z)
    catb=abs(y-z)
    if cata==catb:
        print("Mouse C")
    elif cata>catb:
        print("Cat B")
    else:
        print("Cat A")
