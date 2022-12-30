# --- AoC 2022 - Day 8: Tuning Trouble PART TWO --- #

# The Problem:
# Given a large grid of numbers, each number if the height of a tree (0-9)

# Trees are visible or not-visible from different diretions if the tree in that
# direction is the same height or taller

# Now we need to find a 'scenic score': this is where we take a tree and
# calculate how many trees it can see before it's blocked. In one direction this
# is called the 'viewing distance'.Take the number of trees it can see in the 
# 4 cardinal directions and multiply each together

# Calculate the maximum scenic score for any tree (don't need to know which tree)

# The Code:
from pprint import pprint

# Read input file
with open("2022_day8_input.txt") as f:
    content = f.readlines()

# data[y][x] = yth row, xth column
data = [i.strip() for i in content]

def get_north(grid,row,col):
    '''
    Return the values north of the point in the grid
    '''
    x = []
    for i in range(0,row):
        x.append(grid[i][col])

    return x

def get_south(grid,row,col):
    '''
    Return the values south of the point in the grid
    '''
    x = []
    for i in range(row+1,99):
        x.append(grid[i][col])

    return x
              
def get_west(grid,row,col):
    '''
    Return the values west of the point in the grid
    '''
    x = []
    for i in range(0,col):
        x.append(grid[row][i])

    return x

def get_east(grid,row,col):
    '''
    Return the values east of the point in the grid
    '''
    x = []
    for i in range(col+1,99):
        x.append(grid[row][i])

    return x

# North viewing distance
def north_view(data,row,col):
    '''
    Return the 'viewing distance' in the North direction (how many trees can be seen)
    '''
    x = get_north(data,row,col)
    x.reverse() # hacky way to get counting 'outwards' to the edge of forest

    val = data[row][col]
    i = 1
    while i < len(x):
        if val > x[i-1]:
            i += 1
        else:
            break
    
    return i

# South viewing distance
def south_view(data,row,col):
    '''
    Return the 'viewing distance' in the South direction (how many trees can be seen)
    '''
    x = get_south(data,row,col)
    
    val = data[row][col]
    i = 1
    while i < len(x):
        if val > x[i-1]:
            i += 1
        else:
            break
    
    return i

# West viewing distance
def west_view(data,row,col):
    '''
    Return the 'viewing distance' in the West direction (how many trees can be seen)
    '''
    x = get_west(data,row,col)
    x.reverse()
    
    val = data[row][col]
    i = 1
    while i < len(x):
        if val > x[i-1]:
            i += 1
        else:
            break
    
    return i

# East viewing distance
def east_view(data,row,col):
    '''
    Return the 'viewing distance' in the East direction (how many trees can be seen)
    '''
    x = get_east(data,row,col)
    
    val = data[row][col]
    i = 1
    while i < len(x):
        if val > x[i-1]:
            i += 1
        else:
            break
    
    return i


# --- Testing ---#
trow, tcol = 3,3
#pprint(north_view(data,trow,tcol))
#pprint(south_view(data,trow,tcol))
#pprint(west_view(data,trow,tcol))
#pprint(north_view(data,trow,tcol))

# --- Applying to loop --- #
scores = []
for i in range(0,len(data)): #rows
    for j in range(0,len(data[0])): #cols

        val = data[i][j] # value at that row and column

        # Remove the outer layer of visible trees
        if i == 0 or i == 98:
            pass
        elif j == 0 or j == 98:
            pass
        else:
            n = int(north_view(data,i,j))
            e = int(east_view(data,i,j))
            s = int(south_view(data,i,j))
            w = int(west_view(data,i,j))

            scores.append(n*e*w*s)

        

pprint(max(scores))








            
