n,k=input().strip().split()
n,k=[int(n),int(k)]
c=list(map(int, input().strip().split(' ')))
sum=0
b=int(input())
c.pop(k)
for i in c:
    sum += i
actual=sum/2
if actual==b:
    print("Bon Appetit")
else:
    rem=b-actual
    print(int(rem))