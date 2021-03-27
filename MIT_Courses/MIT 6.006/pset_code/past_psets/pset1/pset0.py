def summ(n):
    s = 0
    for i in range(1, n+1):
        s += 1.0/((i**2)+ i)
    return s

def common(l:list):
    if len(l) == 0: return 0
    if len(l) == 1: return len(l[0])

    s = set(l[0])
    for idx in range(1, len(l)):
        s = s.intersection(l[idx])

    return len(s)

print(common([[]]))
