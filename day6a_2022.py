# --- AoC 2022 - Day 6: Tuning Trouble PART ONE --- #

# The Problem:
# This is a signal processing problem. We are given a long stream of
# characters and need to find the first instance where the
# 'start-of-packet marker' is in this signal.

# The start of packet marker is indicated by 4 characters that are all different

# Once found, we need to report the number of characters that are processed
# before the marker is found

# E.g. nppdvjthqldpwncqszvftbrmjlhg - first marker after character 6 [pdvj]


# The Code:
# Read input file
with open("2022_day6_input.txt") as f:
    content = f.readlines()

data = content[0]

def find_marker(data):
    '''
    Will return the position of the first marker and the 4 distinct characters
    '''
    i = 0 # while loop to increase this later

    while True:
        test_string = []
        for x in range(i,i+4):
            test_string.append(data[x])

        set_string = set(test_string)

        if len(set_string) == len(test_string): # if there's no duplicates
            print('No duplicates found!')
            break            
        else:
            i += 1
        

    return test_string, set_string, i+4 # i+4 as the final marker character

print(find_marker(data))
     




        
        
