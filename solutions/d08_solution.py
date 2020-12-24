import os

#dirname = os.path.dirname(os.path.abspath(''))
dirname = os.path.abspath('')
filename = os.path.join(dirname,'inputs','d08_input.txt')

with open(filename,"r") as f:
    game_rules = f.read().splitlines()
    
def challenge_1(rules):
    acc = 0
    ran_rules = set()
    current_rule = 0
    solution = True
    
    while True:
        # Check if current rule is = to last rule in list
        if len(rules) - 1 == current_rule:
            solution = False
        
        # Checks if current rule has already been ran
        if current_rule in ran_rules:
            solution = False
            return acc,solution
        
        rule_type,rule_value = rules[current_rule].split(' ')
        rule_value = int(rule_value)
        ran_rules.add(current_rule)
        
        if rule_type == 'nop':
            current_rule += 1
        if rule_type == 'acc':
            acc += rule_value
            current_rule +=1
        if rule_type == 'jmp':
            current_rule += rule_value
        
        if solution == False:
            return acc, True
    return acc,False

print(challenge_1(game_rules))

def challenge_2(rules):
    acc = 0
    ran_rules = []
    current_rule = 0
    valid_rules = rules.copy()
    for current_rule in range(1, len(valid_rules)):   
        rule_type, rule_value = rules[current_rule].split(" ")
        rule_value = int(rule_value)

        if rule_type == "nop":
            rule_type = "jmp"
        elif rule_type == "jmp":
            rule_type = "nop"

        ran_rules = []
        valid_rules = rules.copy()
        valid_rules[current_rule] = " ".join((rule_type, str(rule_value)))
        acc, valid = challenge_1(valid_rules)
        if valid:
            return acc
print(challenge_2(game_rules))