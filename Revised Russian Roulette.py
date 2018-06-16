def revisedRussianRoulette(doors):
    count=[0,0]
    count[1] = doors.count(1)
    doors.append(0)
    for i in doors:
        if i==0:
            continue
        elif i == 1:
            inde=doors.index(i)
            doors[inde]=0
            count[0]+=1
            if doors[inde+1]==1:
                doors[inde+1]=0
    print(" ".join(map(str, count)))
if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)