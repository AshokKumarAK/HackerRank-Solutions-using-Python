import sys

def strangeCode(t):
    t1=1
    val=3
    res=[]
    tem=True
    while len(res)+1<=t:
        if tem==True:
            mul=val
            tem=False
        res.append(val)
        val-=1
        t1+=1
        if val==1:
            res.append(val)
            val=2*mul
            tem=True
    return res[t-1]

if __name__ == "__main__":
    t = int(input().strip())
    result = strangeCode(t)
    print(result)