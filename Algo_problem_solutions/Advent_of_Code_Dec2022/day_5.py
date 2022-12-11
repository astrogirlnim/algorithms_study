## Puzzle 1 
import re
import collections
with open("day5_input.txt","r") as f:
    stacks = collections.defaultdict(list)
    for line in f:
        if line != "\n" and line[0:4] != 'move':
            # Reading input
            line = line.replace("\n","")
            l = re.split(r"\s\s\s\s|\]\s\[|\s\s\[|]\s\s",line)
            l = [re.findall(r"[A-Z]",x) for x in l]
 
            if len(l) > 1:
                for i in range(len(l)):
                    if l[i]:
                        stacks[i+1].append(l[i][0])
        elif line[0:4] == "move":
            l = re.findall(r"[0-9][0-9]*",line)
            l = [int(x) for x in l]
            stacks[l[2]] = stacks[l[1]][:l[0]][::-1] + stacks[l[2]]
            stacks[l[1]] = stacks[l[1]][l[0]:]

    for i in range(1,max(stacks.keys())+1):
        print(stacks[i][0])

## Puzzle 2
with open("day5_input.txt","r") as f:
    stacks = collections.defaultdict(list)
    for line in f:
        if line != "\n" and line[0:4] != 'move':
            # Reading input
            line = line.replace("\n","")
            l = re.split(r"\s\s\s\s|\]\s\[|\s\s\[|]\s\s",line)
            l = [re.findall(r"[A-Z]",x) for x in l]
 
            if len(l) > 1:
                for i in range(len(l)):
                    if l[i]:
                        stacks[i+1].append(l[i][0])
        elif line[0:4] == "move":
            l = re.findall(r"[0-9][0-9]*",line)
            l = [int(x) for x in l]
            stacks[l[2]] = stacks[l[1]][:l[0]] + stacks[l[2]]
            stacks[l[1]] = stacks[l[1]][l[0]:]

    print("Part 2:")
    for i in range(1,max(stacks.keys())+1):
        print(stacks[i][0])
