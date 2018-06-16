import math
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
arr = list(map(int, input().strip().split(' ')))
count=0
page_no=1
for i in arr:
    page_count=math.ceil((i/k))
    chap=[int(i) for i in range(1,i+1)]
    for j in range(page_no,page_count+page_no):
        if j in chap[:k]:
            count+=1
        del chap[:k]
    page_no+=page_count
print(count)