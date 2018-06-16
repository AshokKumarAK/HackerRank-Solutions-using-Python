"""from collections import Counter
n = input()
arr = Counter(map(int, input().split()))
print (arr.most_common(1)[0][0])"""
n=int(input())
for num in range(n):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num, end=' ')
