from aoclib import *

inp = grab(1)

text_nums = 'one, two, three, four, five, six, seven, eight, nine'.split(', ')

def find_nums_in_string(inp):
    nums = []
    # Find the first number in a string
    for i in range(len(inp)):
        if inp[i].isdigit():
            nums.append(int(inp[i]))
        else:
            for j in text_nums:
                try:
                    if inp[i:i+len(j)] == j:
                        nums.append(text_nums.index(j) + 1)
                except:
                    pass
    
    return str(nums[0]) + str(nums[-1])

nums = [int(find_nums_in_string(i)) for i in inp.split('\n')]

print(sum(nums))

