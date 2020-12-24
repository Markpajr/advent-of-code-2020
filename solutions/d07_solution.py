import os
import re

#dirname = os.path.dirname(os.path.abspath(''))
dirname = os.path.abspath('')
filename = os.path.join(dirname,'inputs','d07_input.txt')

with open(filename,"r") as f:
    luggage_rules = f.read().splitlines()
    
luggage_rules = [rule.replace('bags','bag') for rule in luggage_rules]
luggage_rules = [rule.replace('.','') for rule in luggage_rules]

bag_re = '(\d+)\s(.+)'

all_bags = {}

for rule in luggage_rules:
    rule_split = rule.split(' contain ')
    sub_bags = {}
    for bag in rule_split[1].split(', '):
        bag_info = re.match(bag_re,bag)
        if bag_info == None:
            continue
        bag_num = bag_info.group(1)
        bag_type = bag_info.group(2)
        
        sub_bags[bag_type] = int(bag_num)  
    all_bags[rule_split[0]] = sub_bags
    
    
def check_bag(all_bags, target_bag, current_bag):
    if current_bag == target_bag:
        return 1
    if all_bags.get(current_bag) == {}:
        return 0
    else:
        bag_count = []
        for k_bag,v in all_bags[current_bag].items():
            bag_count.append(check_bag(all_bags,target_bag,k_bag))
        return max(bag_count)
    
bag_count = 0
target = 'shiny gold bag'
for k,v in all_bags.items():
    if k != target:
        bag_count += check_bag(all_bags,target,k)
print(bag_count)

bag_contents = {}
for k,v in all_bags.items():
    bag_contents[k] = []
    try:
        for kk,vv in v.items():
            bag_contents[k]+=[kk]*int(vv)
    except:
        pass
    
    
def count_bags(current_bag):
    if current_bag ==" " or bag_contents.get(current_bag) is None:
        return 0
    count = len(bag_contents[current_bag])
    counts = []
    for k in bag_contents[current_bag]:
        counts.append(count_bags(k))
    return sum(counts) + count

print(count_bags(target))