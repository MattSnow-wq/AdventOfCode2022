# --- AoC 2022 - Day 4: Camp Cleanup PART ONE --- #

# The Problem:
# Elves are clearing an area and working in pairs. The input is a list of these
# pairs areas (e.g. 2-4, 6-8)

# Our job is to assess how many pairs have one elf's range fully contained in
# the other (e.g. find the pairs like 2-8, 3-7)


# The Code:
# Read input file
with open("2022_day4_input.txt") as f:
    content = f.readlines()

content = [i.strip() for i in content]

def complete_coverage(instruction):
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

   
    if first_start <= secon_start and secon_end <= first_end:
        return True
    elif secon_start <= first_start and first_end <= secon_end:
        return True
    else:
        return False


total = 0
for x in content:
    if complete_coverage(x):
        total += 1


print(total)
    







    

