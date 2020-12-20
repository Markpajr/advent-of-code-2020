import os

# Part 1: Find 2 numbers that add to 2020 and multiply them

dirname = os.path.dirname(os.path.abspath(''))
filename = os.path.join(dirname,'inputs','d01_input.txt')
with open(filename, "r") as f:
    lines = f.read().splitlines()

for num in lines:
    current_number = int(num)
    #print(current_number)
    for num2 in lines:
        #print(num2)
        if (current_number + int(num2)) == 2020:
            answer = current_number * int(num2)
            print(f'Answer is {current_number}+{num2}={answer}')
            break
        else:
            continue

# Part 2: Find 3 numbers that add to 2020 and multiply them
for x in lines:
    num1 = int(x)
    #print(current_number)
    for y in lines:
        num2 = int(y)
        for z in lines:
            num3 = int(z)
            if (num1 + num2+num3) == 2020:
                answer = num1*num2*num3
                print(f'Answer is {num1}+{num2}+{num3}={answer}')
                break
            else:
                continue