#29
t = []
for a in range(2,101):
    for b in range(2,101):
        if a**b not in t:
            t.append(a**b)

print(len(t))