if __name__ == "__main__":
    n = int(input().strip())
    res=[0,1,2,3,4,5,6,7,8,9]
    tickets = []
    tickets_i = 0
    for tickets_i in range(n):
       tickets_t = str(input().strip())
       tickets.append(tickets_t)
    x=0
    for i in range(n):
        for j in range(i+1,n):
            for k in str(tickets[i]):
                if res[x] == int(k):
                    x+=1
            for l in str(tickets[j]):
                if res[x] == int(l):
                    x+=1
            print(x)