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

# For the list of everyone's rucksack we need to find the items that are shared
# in each elf's rucksack, assign it a priority number and sum up the total
# priorities of the whole crew

# The Code:
# Read input file
with open("2022_day3_input.txt") as f:
    content = f.readlines()

content = [i for i in content]

def common_characters(rucksack):
    '''
    Not a great way to do this, but ah well - this takes the the rucksack's
    contents and splits it. It then checks the intersections of the two strings
    that result and gives the common character
    NOTE:// intersection in this usage is borrowed kindly from
    https://bobbyhadz.com/blog/python-find-common-characters-between-two-strings
    '''
    first_index = slice(0, len(rucksack)//2)
    second_index = slice(len(rucksack)//2, len(rucksack))

    first, second = rucksack[first_index], rucksack[second_index]
    
    common_characters = ''.join(set(first).intersection(second))
    
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
for x in content:
    total_priorities += priorities(common_characters(x))

print(total_priorities)


    












    

