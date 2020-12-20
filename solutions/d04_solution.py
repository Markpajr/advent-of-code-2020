import re
import os

dirname = os.path.dirname(os.path.abspath(''))
filename = os.path.join(dirname,'inputs','d04_input.txt')
with open(filename,"r") as f:
    passports = f.read().split('\n\n')
    passports = [passport.replace('\n',' ') for passport in passports]


# Passport dictionary
ppdict = {}
i = 0
for passport in passports:
    ppmatch = re.findall('(\S+):(\S+)',passport)
    ppdict[i] = dict(ppmatch)
    i += 1
# Part 1 Answer
validpp = 0
required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
for pp in ppdict.values():
    if all(req in pp for req in required_fields):
        validpp+=1
print(validpp)

# Part 2 Answer
validpps = {}
i = 0
required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
for pp in ppdict.values():
    if all(req in pp for req in required_fields):
        if (
            (len(pp['byr'])==4 and (1920<= int(pp['byr'])<=2002)) and
            (len(pp['iyr'])==4 and (2010<= int(pp['iyr'])<=2020)) and
            (len(pp['eyr'])==4 and (2020<= int(pp['eyr'])<=2030)) and
            ((pp['hgt'][-2:] == 'cm' and 150 <= int(pp['hgt'][:-2]) <= 193) or
             (pp['hgt'][-2:] == 'in' and 59 <= int(pp['hgt'][:-2]) <= 76)) and
            (re.match(r'#[\da-f]{6}',pp['hcl'])) and
            (pp['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and
            (len(pp['pid'])==9 and re.match(r'\d{9}',pp['pid']))
            
           ):
            validpps[i]=pp
            i+=1
print(len(validpps))
    