from numpy import inf
import heapq

## Part 1
# Get the elf carrying the maximum number of calories
elfheap = []
elf_number, cals, max_cal_elf = 0, 0, [0, -inf] 
with open("./day1_input.txt","r") as f:
    for l in f:
        if l == '\n':
            max_cal_elf = max(max_cal_elf, [elf_number, cals], key=lambda x: x[1])
            elfheap.append(cals)
            elf_number += 1
            cals = 0
        else:
            cals += int(l)
        

print(f"Maximum calorie elf = {max_cal_elf[0]+1} with {max_cal_elf[1]} calories")

## Part 2 
print(f"Sum of three largest is {sum(heapq.nlargest(3, elfheap))}")