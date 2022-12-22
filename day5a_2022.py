# --- AoC 2022 - Day 5: Supply StacksPART ONE --- #

# The Problem:
# There are stacks of crates [A] [B] etc. that are arranged like on a container
# ship with columns.

# Input is a starting configuration of the crates, and a set of instructions.

# The instructions are on the form of:
# Move n crates from column a to b

# NOTE:// STACKS WOULD HAVE MADE THIS 1000% EASIER I THINK

# The Code:
# Read input file
with open("2022_day5_input.txt") as f:
    content = f.readlines()

# This is going to be a challenge of sorting out the input file into the
# containers and the instructions first and foremost

# To store the data of the containers let's setup a list of lists for columns
# (e.g. column 8 is represented by a list with elements [B, J, T]

# Just extracting the grid and instructions in their raw form
raw_grid = content[0:8]
instructions = content[10::]

# --- Columns with their data --- #
# List of lists for each columns
cols = []
newcols = []
for i in range(0,9):
    cols.append([])
    newcols.append([])

# Each element of raw_grid[n] is the nth row of the original picture as a long
# string. Each 4th character (1,5,9, etc.) is where a letter will be placed

# Let's create a list of the row positions crates could be
row_pos = [i for i in range(1,37,4)]

# Now we go through our raw_grid by row, adding the values in the row_pos
# positions to their respective columns

for x in range(0,8):
    for i in range(0,9):
        cols[i].append(raw_grid[x][row_pos[i]])

# Made a foolish error and forgot to remove the empty strings at the front of
# columns so have gotten hacky with 'newcols'
print(cols)
print('----------------------')
for i in range(len(cols)):
    for j in range(len(cols[i])):
        if cols[i][j] != ' ':
            newcols[i].append(cols[i][j])
#print(newcols)
#print('----------------------')
cols = newcols # BRINING IT BACK TO COLS

# So now cols[n] has the crates in descending order for the nth column (i.e.
# cols[0][0] has the topmost crate in the 1st column, cols[0][1] has the next
# crate down for the 1st column)

# --- Instructions --- #
# We can firstly note that each instruction being on the form of
# "move n from a to b" can equally be written as:
# "move 1 from a to b, n times".

# So we can create a function that will move 1 crate from a to b and just run it
# n times to complete one instruction!

# Firstly, moving around the instructions to get a list of lists
# (clean) that just has the n-times value, the start column, & the
# end column

sep_instructions = [i.split() for i in instructions]
#print(sep_instructions[0])

clean = []
for i in range(0,len(sep_instructions)):
    clean.append([])
    
for j in range(0,len(sep_instructions)):
    for k in range(1,6,2):
        clean[j].append(int(sep_instructions[j][k]))

#print(clean[0])

# --- Move function ---#
# This is the tricky part. We create a function that will take in the 3 values
# from the clean instruction (n-times, start column, end column), and will be
# able to:
# (1) Put the value at the top of the start column to the top of the end column
# (2) Remove the top value from the start column
# (3) Repeat this process n-times and output the new modified columns


# EXAMPLE OF INSERTION AND DELETION
#test = cols[4]
#print(test)

#test.insert(0,'x')
#print(test)

#del test[0]
#print(test)

# Default to move 1 item from start to end column
def move_func(cols, start, end):
    '''
    Returns the modified columns after the 1 move has taken place
    '''
    x = cols[end-1]
    x.insert(0,cols[start-1][0])
    del cols[start-1][0]

    return cols

def move_ntimes(cols, ntimes, start, end):
    '''
    Perform the move function ntimes
    '''
    for n in range(0,ntimes):
        move_func(cols,start,end)

    return cols

#print(cols)
#print('-----------------------------------')
#print(move_func(cols,1,2))
#print('-----------------------------------')
#print(move_ntimes(cols,3,1,2))

# --- Putting it together --- #
# We now have a function that will move our grid n times and follow the
# instructions, so all that's left is to get our clean instructions into a for
# loop and get our final grid out
for i in range(0,len(clean)):
    ntimes, start, end = clean[i][0], clean[i][1], clean[i][2]

    cols = move_ntimes(cols, ntimes, start, end)

print(cols)

# The final bit for the challenge is to put together the top crates in all of
# stacks (e.g. if the 1st, 2nd and 3rd stacsk had [C] [M] and [Z] on top then
# that would be the code)
code = ''
for i in range(0,len(cols)):
    code += cols[i][0]

print(code)













