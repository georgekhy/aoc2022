res = 0

with open('input/d.input', 'r') as f:
    for rawline in f:
        line = rawline.rstrip()
        if len(line) == 0:
            continue

print(res)
