import os
import re

# Puzzle 1
class FileSystemNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def to_integer(val):
    try:
        return int(val)
    except ValueError:
        return val

def build_file_system_tree(commands):
    root = FileSystemNode("/")
    current_node = root

    for command in commands:
        if command[0] == "cd":
            # Change the current directory
            if command[1] == "..":
                # Go up one directory
                current_node = current_node.parent
            else:
                # Go down into a subdirectory
                found = False
                for child in current_node.children:
                    if child.name == command[1]:
                        current_node = child
                        found = True
                        break
                if not found:
                    # Create a new subdirectory
                    new_node = FileSystemNode(command[1], current_node)
                    current_node.add_child(new_node)
                    current_node = new_node
        elif command[0].startswith("ls"):
            # Add files to directory size
            for x in range(1,len(command)):
                if type(to_integer(command[x])) is int:
                    current_node.size += to_integer(command[x])

    return root

min_sizes = set()

def DFSSizes(node):
    res = node.size
    if node.children is not None:
        for x in node.children:
            res += DFSSizes(x)
    
    node.size = res
    print(f"Node {node.name} has size {res}")
    if res <= 100000:
        min_sizes.add((node.name, node.size))
    return res

def main():
    commands = []
    with open("day7_input.txt", "r") as f:
        text = f.read().split("$")
        for line in text:
            # Split the line into the command and its argument
            parts = re.split('\s|\n',line.strip())
            commands.append(parts)
        
    r = build_file_system_tree(commands)
    DFSSizes(r)
    print(min_sizes)
    print(sum([x[1] for x in min_sizes]))

if __name__ == "__main__":
    main()
