def super_reduced_string(s):
    res = []
    for c in s:
        if res and res[-1] == c:
            res.pop()
        else:
            res.append(c)
    res = ''.join(res)
    return res or "Empty String"

s = input().strip()
result = super_reduced_string(s)
print(result)