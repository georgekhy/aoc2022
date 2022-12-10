res = 0

with open('input/d2', 'r') as f:
    for rawline in f:
        line = rawline.rstrip()
        if len(line) == 0:
            continue
        op, me = line.split(' ')
        op = ord(op) - ord('A') + 1
        me = ord(me) - ord('X') + 1
        res += me
        sub = (me - op) % 3
        if sub == 0:
            res += 3
        elif sub == 1:
            res += 6

print(res)
