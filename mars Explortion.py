s = input().strip()
count=0
st="SOS"
for i in range(len(s)):
    if s[i]!=st[i%3]:
        count+=1
print(count)