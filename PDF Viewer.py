from string import ascii_lowercase as al
dic = {x:i for i, x in enumerate(al, 0)}
h = list(map(int, input().strip().split(' ')))
word = input().strip()
l=len(word)
word=set(word)
val=[]
t=[]
for i,key in zip(word,dic):
        val.append(dic[i])
for i,j in zip(val,h):
    t.append(h[i])
t.sort(reverse=True)
print(l*t[0])


