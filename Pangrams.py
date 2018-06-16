"""from collections import Counter
s=input()
s=s.replace(" ","")
s=s.lower()
l=Counter(s)
if len(l)==26:
    print("pangram")
else:
    print("not pangram")"""
from string import ascii_lowercase
s = raw_input().lower() # lowercase input
s = list(set(s)-set(' ')) # remove ' ' spaces
s = ''.join(sorted(s)) # joined the sorted list of unique charaters
print (["not pangram", "pangram"][ascii_lowercase == s])