## Puzzle 1
with open("day3_input.txt","r") as f:
    s = 0
    for line in f:
        l = [line[:len(line)//2], line[len(line)//2:]]
        l[1] = l[1].replace('\n',"")

        overlap = set(l[0]).intersection(set(l[1])).pop()

        if not overlap.isupper(): 
            s += ord(overlap) - 96 
        else:
            s += ord(overlap) - 64 + 26

print(f"Total sum = {s}")
        
## Puzzle 2
ts = 0
with open("day3_input.txt","r") as f:
    l = []
    for line in f:
        l.append(line.replace('\n',""))
        print(f"List = {l}")
        if len(l) == 3:
            overlap = set(l[0]) & set(l[1]) & set(l[2])
            print(f"overlap is {overlap}")
            overlap = overlap.pop()
            if not overlap.isupper(): 
                print(f"Value is {ord(overlap)-96}")
                ts += ord(overlap) - 96
            else:
                print(f"Value is {ord(overlap) - 64 + 26}")
                ts += ord(overlap) - 64 + 26
            print(f"Sum is {ts}")
            l = []

print(f"Priority = {ts}")