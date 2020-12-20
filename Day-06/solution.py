import os

dirname = os.path.abspath('')
filename = os.path.join(dirname,'input.txt')
with open(filename,"r") as f:
    groups = f.read().split('\n\n')
    groups = [group.replace('\n',' ') for group in groups]

# Part 1
group_yes = []
for group in groups:
    group_yes.append(len(set(group.replace(' ',''))))
print(sum(group_yes))

# Part 2
group_all_yes = []
for group in groups:
    all_questions = set(group.replace(' ',''))
    people = group.split()
    all_yes = []
    for q in all_questions:
        if all(q in person for person in people):
            all_yes.append(q)
    group_all_yes.append(len(all_yes))
print(sum(group_all_yes))