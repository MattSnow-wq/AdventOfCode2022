# --- AoC 2022 - Day 8: Tuning Trouble PART ONE --- #

# The Problem:
# Given a large grid of numbers, each number if the height of a tree (0-9)

# Trees are visible or not-visible from different diretions if the tree in that
# direction is the same height or taller

# For the grid we're given, how many trees are visible from outside the grid?


# The Code:
from pprint import pprint

# Read input file
with open("2022_day8_input.txt") as f:
    content = f.readlines()

# data[y][x] = yth row, xth column
data = [i.strip() for i in content]

pprint(data)

def get_north(grid,row,col):
    '''
    Return the values north of the point in the grid
    '''
    x = []
    for i in range(0,row):
        x.append(grid[i][col])

    return x

def visible_north(grid,row,col,val):
    '''
    Returns True if the point is visible viewing from north
    '''
    vis = 0
    x = get_north(grid,row,col)

    for j in x:
        if j < val:
            vis += 1

    if vis == len(x):
        return True
    else:
        return False

def get_south(grid,row,col):
    '''
    Return the values south of the point in the grid
    '''
    x = []
    for i in range(row+1,99):
        x.append(grid[i][col])

    return x

def visible_south(grid,row,col,val):
    '''
    Returns True if the point is visible viewing from south
    '''
    vis = 0
    x = get_south(grid,row,col)

    for j in x:
        if j < val:
            vis += 1

    if vis == len(x):
        return True
    else:
        return False
              
def get_west(grid,row,col):
    '''
    Return the values west of the point in the grid
    '''
    x = []
    for i in range(0,col):
        x.append(grid[row][i])

    return x

def visible_west(grid,row,col,val):
    '''
    Returns True if the point is visible viewing from west
    '''
    vis = 0
    x = get_west(grid,row,col)

    for j in x:
        if j < val:
            vis += 1

    if vis == len(x):
        return True
    else:
        return False


def get_east(grid,row,col):
    '''
    Return the values east of the point in the grid
    '''
    x = []
    for i in range(col+1,99):
        x.append(grid[row][i])

    return x

def visible_east(grid,row,col,val):
    '''
    Returns True if the point is visible viewing from east
    '''
    vis = 0
    x = get_east(grid,row,col)

    for j in x:
        if j < val:
            vis += 1

    if vis == len(x):
        return True
    else:
        return False

def visible_any(north,east,south,west):
    '''
    If visible from any direction returns True. Only False if visible from
    no direction
    '''
    if (north | east | south | west):
        return True
    return False
    
visibles = 0

for i in range(0,len(data)): #rows
    for j in range(0,len(data[0])): #cols

        val = data[i][j] # value at that row and column

        # Remove the outer layer of visible trees
        if i == 0 or i == 98:
            visibles += 1
            pass
        elif j == 0 or j == 98:
            visibles += 1
            pass
        else:

            n = visible_north(data,i,j,val)
            e = visible_east(data,i,j,val)
            s = visible_south(data,i,j,val)
            w = visible_west(data,i,j,val)

            if visible_any(n,e,s,w):
                visibles += 1

pprint(visibles)




            
