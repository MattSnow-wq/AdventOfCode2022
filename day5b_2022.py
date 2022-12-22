# --- AoC 2022 - Day 5: Supply Stacks PART TWO --- #

# The Problem:
# There are stacks of crates [A] [B] etc. that are arranged like on a container
# ship with columns.

# Input is a starting configuration of the crates, and a set of instructions.

# The instructions are on the form of:
# Move n crates from column a to b

# The second part to this turns the n-times part a bit on it's head. Now,
# instead of moving the crates one after another you pick up and drop the whole
# stack of ntimes

# The Code:
# Read input file
with open("2022_day5_input.txt") as f:
    content = f.readlines()

raw_grid = content[0:8]
instructions = content[10::]

# --- Columns with their data --- #
cols = []
newcols = []
for i in range(0,9):
    cols.append([])
    newcols.append([])

row_pos = [i for i in range(1,37,4)]

# Now we go through our raw_grid by row, adding the values in the row_pos
# positions to their respective columns

for x in range(0,8):
    for i in range(0,9):
        cols[i].append(raw_grid[x][row_pos[i]])

# Removing the empty entries of the columns
for i in range(len(cols)):
    for j in range(len(cols[i])):
        if cols[i][j] != ' ':
            newcols[i].append(cols[i][j])

cols = newcols 

# So now cols[n] has the crates in descending order for the nth column (i.e.
# cols[0][0] has the topmost crate in the 1st column, cols[0][1] has the next
# crate down for the 1st column)

# --- Instructions --- #

sep_instructions = [i.split() for i in instructions]

clean = []
for i in range(0,len(sep_instructions)):
    clean.append([])
    
for j in range(0,len(sep_instructions)):
    for k in range(1,6,2):
        clean[j].append(int(sep_instructions[j][k]))


# --- Move function ---#

def new_move(cols, n, start, end):
    '''
    Using the new definition of the move, takes the grid input and the 3
    instruction variables and produces the end state of the grid
    '''
    start, end = start-1, end-1 # fence post

    to_be_moved = cols[start][0:n] # the section to be moved
    to_be_moved.reverse()
    x = cols[end]
    
    for i in to_be_moved:
        x.insert(0,i)

    del cols[start][0:n]

    return cols



print(cols)
print('---------------------------')
#print(new_move(cols,3,1,2))


# --- Putting it together --- #
for i in range(0,len(clean)):
    n, start, end = clean[i][0], clean[i][1], clean[i][2]
    cols = new_move(cols, n, start, end)

print(cols)

code = ''
for i in range(0,len(cols)):
    code += cols[i][0]

print(code)

















