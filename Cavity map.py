"""n = int(input())
a = []
for i in range(n):
    a.append(list(input()))
for i in range(1,n-1):
    for j in range(1,n-1):
        if a[i][j] > a[i+1][j] and a[i][j] > a[i-1][j] and a[i][j] > a[i][j+1] and a[i][j] > a[i][j+1] and a[i][j]!='X' and a[i][j]!='X' and a[i][j]!='X' and a[i][j]!='X':
            a[i][j]="X"
for i in range(n):
    print("".join(str(x) for x in a[i]))"""
def transformCavity(arr, n):
    for idx_tb in range(1, n - 1):
        for idx_lr in range(1, n - 1):
            if arr[idx_tb - 1][idx_lr] != 'X' and int(arr[idx_tb - 1][idx_lr]) < int(arr[idx_tb][idx_lr]) and arr[idx_tb + 1][idx_lr] != 'X' and int(arr[idx_tb + 1][idx_lr]) < int( arr[idx_tb][idx_lr]) and arr[idx_tb][idx_lr - 1] != 'X' and int(arr[idx_tb][idx_lr - 1]) < int(arr[idx_tb][idx_lr]) and arr[idx_tb][idx_lr + 1] != 'X' and int(arr[idx_tb][idx_lr + 1]) < int(arr[idx_tb][idx_lr]):
                arr[idx_tb][idx_lr] = 'X'
if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        line = list(input())
        arr.append(line)
    transformCavity(arr, n)
    for line in arr:
        print(''.join(line))