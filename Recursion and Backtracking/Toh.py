"""
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks
and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.
"""

def toh(n, from_tower, to_tower, temp):
    if n == 1:
        print("Move 1 tower form " +from_tower+" to "+ to_tower)
        return
    toh(n-1, from_tower, temp, to_tower)
    print("Move "+str(n)+" tower form " +from_tower+" to "+ to_tower)
    toh(n-1, temp, to_tower, from_tower)

toh(3, "A", "C", "temp")