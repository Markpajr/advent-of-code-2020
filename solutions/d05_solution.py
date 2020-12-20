import os
from statistics import median

dirname = os.path.dirname(os.path.abspath(''))
filename = os.path.join(dirname,'inputs','d05_input.txt')
with open(filename,"r") as f:
    seats = f.read().splitlines()

# Part 1
def find_seat(seat):
    rhalf = [0,127]
    chalf = [0,7]
    for char in seat:
        if char == 'F':
            rhalf = [rhalf[0],int(median(rhalf))]
        elif char == 'B':
            rhalf = [int(median(rhalf))+1,rhalf[1]]
        elif char == 'R':
            chalf = [int(median(chalf))+1,chalf[1]]
        elif char == 'L':
            chalf = [chalf[0],int(median(chalf))]
    row = rhalf[0]
    col = chalf[0]
    seat_id = row*8+col
    return seat_id
    
seat_ids = []
for seat in seats:
    seat_ids.append(find_seat(seat))
print(max(seat_ids))

# Part 2
seat_ids.sort()
def find_missing(lst): 
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]
print(find_missing(seat_ids)[0])
