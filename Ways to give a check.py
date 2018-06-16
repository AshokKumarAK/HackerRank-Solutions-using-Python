if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        count = 0
        board = []
        for board_i in range(8):
           board_t = [str(board_temp) for board_temp in input().strip().split(' ')]
           board.append(board_t)
        tem=str(board[1])
        for i in tem:
            if 'P'== i :
                pcol=[0,tem.index(i)-2]
                pflag='W'
                break
            elif 'p' ==i:
                pcol=[0,tem.index(i)-2]
                pflag='B'
                break
        if pflag == 'W':
            for i in board:
                if 'k' in str(i):
                    row=int(board.index(i))
                    break
            temp=str(board[row])
            col=temp.index('k')-2
            king=[row,col]
            for i in board:
                if 'K' in str(i):
                    row=int(board.index(i))
                    break
            temp = str(board[row])
            col = temp.index('K') - 2
            myking=[row,col]
        else:
            for i in board:
                if 'K' in str(i):
                    row=int(board.index(i))
                    break
            temp = str(board[row])
            col = temp.index('K') - 2
            king=[row,col]
            for i in board:
                if 'k' in str(i):
                    row=int(board.index(i))
                    break
            temp=str(board[row])
            col=temp.index('k')-2
            myking=[row,col]
        knight=[]
        knight.append([2,pcol[1]+1])
        knight.append([2, pcol[1]-1])
        knight.append([1, pcol[1] + 2])
        knight.append([1, pcol[1] - 2])
        if king in knight:
            count+=1
        bcol=list(pcol)
        bisop=[]
        for i in range(7):
            bcol[0]+=1
            bcol[1]+=1
            bisop.append([bcol[0],bcol[1]])
        bcol=list(pcol)
        for j in range(7):
            bcol[0]+=1
            bcol[1]-=1
            bisop.append([bcol[0],bcol[1]])
        if king in bisop:
            count+=2
        rcol=list(pcol)
        rook=[]
        for i in range(7):
            rcol[1]+=1
            rook.append([rcol[0],rcol[1]])
        rcol=list(pcol)
        for i in range(7):
            rcol[1]-=1
            rook.append([rcol[0],rcol[1]])
        rcol=list(pcol)
        for i in range(7):
            rcol[0]+=1
            rook.append([rcol[0],rcol[1]])
        if king in rook:
            count+=2
        if king[0]==0 and myking[0]==0:
            if (king[1]<myking[1] and pcol[1]>myking[1]) or (king[1]>myking[1] and myking[1]>pcol[1]):
                print("0")
            else:
                print(count)
        else:
            print(count)

