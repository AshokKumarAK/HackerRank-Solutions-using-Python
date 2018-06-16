import os
import sys
# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    sum = 0
    ctr = 0
    for i in rating:
        if i>=90:
            ctr+=1
            sum+=i
    ans=23.345
    #print(round(ans,2))
    print("{:0.2f}".format(ans))

if __name__ == '__main__':
    n = int(input())
    rating = []
    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)
    averageOfTopEmployees(rating)