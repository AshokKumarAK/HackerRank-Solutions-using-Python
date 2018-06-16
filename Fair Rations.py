N = int(input().strip())
B = list(map(int, input().strip().split(' ')))
sum=0
count=0
for i in B:
    sum+=i
    if sum%2 ==1:
        count+=2
if sum%2==0:
    print("NO")
else:
    print(count)