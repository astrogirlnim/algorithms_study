import re

## Puzzle 1
with open("day4_input.txt","r") as f:
    c = 0
    for line in f:
        line = line.replace("\n","")
        line = [x.split('-') for x in line.split(",")]

        if int(line[0][0]) <= int(line[1][0]) and int(line[0][1]) >= int(line[1][1]):
            c += 1
        elif int(line[1][0]) <= int(line[0][0]) and int(line[1][1]) >= int(line[0][1]):
            c += 1 
    
print(f"Fully overlapped schedules = {c}")

with open("day4_input.txt","r") as f:
    c = 0
    for line in f:
        line = line.replace("\n","")
        line = [x.split('-') for x in line.split(",")]
        if int(line[0][1]) >= int(line[1][0]) and int(line[0][1]) <= int(line[1][1]):
            c += 1
        elif int(line[1][1]) >= int(line[0][0]) and int(line[1][1]) <= int(line[0][1]):
            c += 1

print(f"Overlapped schedules = {c}")