r = 0
s = 0
with open('input/d1', 'r') as f:
    for line in f:
        l = line.rstrip()
        if len(l) == 0:
            r = max(r, s)
            s = 0
            continue
        num = int(l)
        s += num

print(r)
