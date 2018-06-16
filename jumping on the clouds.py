n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
count=0
i=0
while i!=(n-1):
    if i==(n-2):
        i+=1
        count+=1
    elif c[i+2]!=1:
        count+=1
        i+=2
    else:
        count+=1
        i+=1
print(count)