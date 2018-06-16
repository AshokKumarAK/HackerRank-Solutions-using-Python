n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.sort()
while len(arr)>0:
    l=len(arr)
    print(l)
    a=arr[0]
    for i in range(l):
        arr[i]-=a
    arr=[x for x in arr if x != 0]