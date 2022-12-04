## Part 1
with open("day2_input.txt","r") as f:
    pts = 0
    for line in f:
        l = line.rstrip('\n').split(" ")
        l = [ord(x) for x in l]
        l[1] = l[1]-23

        if l[0] == l[1]:
            pts += l[0]-64 + 3
        elif l[1] == l[0] + 1:
            pts += l[1]-64 + 6
        elif l[0] == l[1] + 1:
            pts += l[1]-64 + 0
        elif l[1] < l[0]:
            pts += l[1]-64 + 6
        else:
            pts += l[1]-64 + 0

print(f"total points = {pts}")

## Part 2
with open("day2_input.txt","r") as f:
    pts = 0
    for line in f:
        l = line.rstrip('\n').split(" ")
        l = [ord(x) for x in l]
        l[1] = l[1]-23

        if l[1] == 66:
            pts += l[0] - 64 + 3
        elif l[1] == 67:
            if l[0] == 65:
                pts += 2 + 6
            elif l[0] == 66:
                pts += 3 + 6
            else:
                pts += 7
        else:
            if l[0] == 65:
                pts += 3
            elif l[0] == 66:
                pts += 1
            else:
                pts += 2

print(f"total points = {pts}")