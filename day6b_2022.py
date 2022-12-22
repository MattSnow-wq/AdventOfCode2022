# --- AoC 2022 - Day 6: Tuning Trouble PART TWO --- #

# The Problem:
# This is a signal processing problem. We are given a long stream of
# characters and need to find the first instance where the
# 'start-of-packet marker' is in this signal.

# The start of packet marker is indicated by 4 characters that are all different

# Once found, we need to report the number of characters that are processed
# before the marker is found

# E.g. nppdvjthqldpwncqszvftbrmjlhg - first marker after character 6 [pdvj]

# PART TWO:
# Now we are searching for a 'start-of-message marker' where 14 distinct
# characters are needed. Only needed to change the 4 --> 14 in the function
# (sensible programming would have been to make the function take a variable
# like 'distinct letters' so that I could feed 4, or 14 - but problem solved
# none the less)

# The Code:
# Read input file
with open("2022_day6_input.txt") as f:
    content = f.readlines()

data = content[0]

def find_message(data):
    '''
    Will return the position of the first message marker and the 14
    distinct characters
    '''
    i = 0 # while loop to increase this later

    while True:
        test_string = []
        for x in range(i,i+14):
            test_string.append(data[x])

        set_string = set(test_string)

        if len(set_string) == len(test_string): # if there's no duplicates
            print('No duplicates found!')
            break            
        else:
            i += 1
        

    return test_string, set_string, i+14 # i+4 as the final marker character

print(find_message(data))
     




        
        
