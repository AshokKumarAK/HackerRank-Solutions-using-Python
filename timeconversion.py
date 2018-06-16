n = int(input())
grades=[]
for _ in range(n):
    t=int(input())
    grades.append(t)
for i in range(n):
    if grades[i]<=37:
        continue
    else:
        if grades[i]%5==0 :
            continue
        else:
            qui = grades[i] / 5
            qui=int(qui)+1
            nval = 5 * int(qui)
            tem=int(nval) - grades[i]
            if tem<3:
                grades[i]=nval
            else:
                continue
print ("\n".join(map(str,grades)))



