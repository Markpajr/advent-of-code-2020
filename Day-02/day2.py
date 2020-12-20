import re

with open(r"C:\Users\MPatr\OneDrive\Documents\Coding Projects\Advent-of-Code\Day-02\puzzle.txt","r") as f:
    lines = f.read().splitlines()

regmatch = "(\d+)-(\d+)\s+(\w+):\s+(\w+)"

matchSum = 0
for puzzle in lines:
    for minmatch,maxmatch,letter,password in re.findall(regmatch,puzzle):
        if int(minmatch)<=password.count(letter)<=int(maxmatch):
            matchSum+=1

print(matchSum)

match2Sum = 0
for puzzle in lines:
    for pos1,pos2,letter,password in re.findall(regmatch,puzzle):
        if (password[int(pos1)-1]==letter or password[int(pos2)-1]==letter) and password[int(pos1)-1]!=password[int(pos2)-1] :
            match2Sum+=1
print(match2Sum)