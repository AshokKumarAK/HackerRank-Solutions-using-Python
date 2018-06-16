import sys

def dig(a):
    for i in a:
        if i.isdigit():
            return 0
    else:
        return 1
def low(l):
    for i in l:
        if i.islower():
            return 0
    else:
        return 1
def upp(u):
    for i in u:
        if i.isupper():
            return 0
    else:
        return 1
def spec(p):
    if "!" in p or "@" in p or "#" in p or "$" in p or "%" in p or "^" in p or "&" in p or "*" in p or "(" in p or ")" in p or "-" in p or "+" in p:
        return 0
    else:
        return 1

if __name__ == "__main__":
    n = int(input().strip())
    c=0
    password = input().strip()
    c+=low(password)
    c+=upp(password)
    c+=dig(password)
    c+=spec(password)
    if c+len(password)<6:
        print(6-(c+n)+c)
    else:
        print(c)