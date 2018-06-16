def printShortestPath(n, i_start, j_start, i_end, j_end):
    a,b,c,d=i_start,j_start,i_end,j_end
    ans=[]
    if (i_start%2==0 and i_end%2!=0) or (i_start%2!=0 and i_end%2==0):
        print("Impossible")
    elif i_start==i_end:
        if (j_end-j_start)==2:
            print("R")
        else:
            print("Impossible")
    elif abs(i_start - i_end) % 4 == 0 and (j_start == j_end):
        val = abs(i_start - j_end) - 1
        print(val)
        for i in range(val):
            if i % 2 != 0:
                print("LL", end=" ")
            else:
                print("LR", end=" ")
    else:
        val=abs(i_start-j_end)-1
        print(val)
        for i in range(val):
            if i_start>i_end and j_start>j_end:
                ans.append("UL")
                i_start-=2
                j_start-=1
            elif i_start<i_end and j_start>j_end:
                ans.append("UR")
                i_start-=2
                j_start+=1
            elif i_start==i_end and (j_end-j_start)>0 and (j_end-j_start)%2==0:
                ans.append("R")
                j_start+=2
            elif i_start>i_end and j_start>j_end:
                ans.append("LR")
                i_start+=2
                j_start+=1
            elif i_start<i_end and j_start>j_end:
                ans.append("LL")
                i_start+=2
                j_start-=1
            elif i_start==i_end and (j_end-j_start)<0 and (j_end-j_start)%2==0:
                ans.append("L")
                j_start-=2
        if i_end==c and j_end==d:
            print(" ".join(ans))
        else:
            print("Impossible")
if __name__ == "__main__":
    n = int(input().strip())
    i_start, j_start, i_end, j_end = input().strip().split(' ')
    i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
    printShortestPath(n, i_start, j_start, i_end, j_end)