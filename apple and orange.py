import sys
s,t = input().strip().split(' ')
a,b = input().strip().split(' ')
m,n = input().strip().split(' ')
ap=0
org=0
ad=[]
od=[]
for _ in range(int(m)):
    tem =input()
    ad.append(tem)
for _ in range(int(n)):
    tem=input()
    od.append(tem)
for i in range(int(m)):
    temp = int(a) + int(ad[i])
    if int(temp) >= int(s) and int(temp) <= int(t):
        ap+=1
for i in range(int(n)):
    temp = int(a) + int(ad[i])
    if int(temp) >= int(s) and int(temp) <= int(t):
        org+=1
print(ap)
print(org)

