# Puzzle 1
with open("day6_input.txt","r") as f:
    l = f.readline()
    i = 0
    s = list(l[i:i+4])
    while i < len(l)-4:
        s.pop(0)
        i += 1
        s += l[i+3]
        if len(set(s)) == 4:
            print(f"marker set = {s}, i = {i}")
            break

    print(f"Marker begins at {i+4}")

# Puzzle 2
with open("day6_input.txt","r") as f:
    l = f.readline()
    i = 0
    s = list(l[i:i+14])
    while i < len(l)-14:
        s.pop(0)
        i += 1
        s += l[i+13]
        if len(set(s)) == 14:
            print(f"marker set = {s}, i = {i}")
            break

    print(f"Marker begins at {i+14}")