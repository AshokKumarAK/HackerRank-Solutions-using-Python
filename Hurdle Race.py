n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
height.sort(reverse=True)
if k >=height[0]:
    print("0")
else:
    print(height[0]-k)
