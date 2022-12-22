# --- AoC 2022 - Day 4: Camp Cleanup PART TWO --- #

# The Problem:
# Elves are clearing an area and working in pairs. The input is a list of these
# pairs areas (e.g. 2-4, 6-8)

# Our job this time is to find out how many pairs overlap (doesn't have to be
# fully overlapping this time


# The Code:
# Read input file
with open("2022_day4_input.txt") as f:
    content = f.readlines()

content = [i.strip() for i in content]

def partial_coverage(instruction):
    '''
    For an input of pairs (2-4,5-8) this function returns the int values for
    the first elf and the second elf (e.g. [2,4], [5,8])

    Then it returns True if there is complete coverage
    '''
    # Removing comma
    raw = instruction.split(sep=',')

    # Splitting into first and second elf
    first = raw[0].split(sep='-')
    secon = raw[1].split(sep='-')

    # Finding the start and end for each elf
    first_start, first_end = int(first[0]), int(first[1])
    secon_start, secon_end = int(secon[0]), int(secon[1])

    # Simplifying terminology (probably could've done this earlier ah well
    a, b = first_start, first_end
    c, d = secon_start, secon_end

    # The inequalities logic determine if overlaps occur
    if a <= c and c <= b and b <= d:
        return True
    elif a <= c and c <= d and d <= b:
        return True
    elif c <= a and a <= b and b <= d:
        return True
    elif c <= a and a <= d and d <=b:
        return True
    else:
        return False

# Trial run with some of the content
#total = 0
#minicontent = content[0:10]
#for x in minicontent:
#    print(x)
#    if partial_coverage(x):
#        print('True')
#        total += 1
#    else:
#        print('False')

#    print(total)

grand_total = 0
for y in content:
    if partial_coverage(y):
        grand_total += 1


print(grand_total)







    

