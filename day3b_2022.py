# --- AoC 2022 - Day 3: Rucksack Reorganisation  PART ONE --- #

# The Problem:
# The elves have large rucksacks each and have loaded them all up with items
# (represented by letters a-z and A-Z)

# Each rucksack is split into 2 compartments with equal numbers of items in
# each. We are provided with a string of characters that represents the whole
# number of items in a single rucksack.

# Items are ranked by priority:
#  (i) a - z (lowercase) 1  - 26
# (ii) A - Z (uppercase) 27 - 52

# This is the same as before but now we take each rucksack in groups of 3. We
# need to find the common character within all 3 rucksacks (so compartments are
# not that useful)

# We need to find the common character between the 3 of them and then convert
# to their priority

# The Code:
# Read input file
with open("2022_day3_input.txt") as f:
    content = f.readlines()

content = [i.strip() for i in content]

def common_characters(trio):
    '''
    For the 3 elves' rucksacks returns the common characters
    '''
    first, second, third = trio[0], trio[1], trio[2]
    sets = [set(s) for s in trio] 
    
    common_characters = set.intersection(*sets)

    return common_characters

# Now we can find the common characters between the compartments we just need
# to convert those into the alphabet numbers. A hacky and lazy way I've gone
# about this is to convert to ord() then just scale down or up to the values
# from the question

def priorities(char):
    '''
    Return the priority number for the common character (a-z, 1-26, A-Z, 25-52)
    '''
    i = ord(char)
    
    # Lowercase
    if i > 96:
        return i-96
    else:
        return i-38

total_priorities = 0
for i in range(0,len(content),3):
    trio = content[i:i+3]
    char = common_characters(trio)
    x = list(char)
    character = x[0]
    total_priorities += priorities(character)

print(total_priorities)
        
    
    
    
    












    

