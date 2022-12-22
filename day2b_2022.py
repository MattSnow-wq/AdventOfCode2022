# --- AoC 2022 - Day 2: Rock, Paper, Scissors PART TWO --- #

# The Problem:
# You are given a 'strategy guide' to play rock, paper, scissors and have to
# determine the total score if you play to this guide

# The strategy guide was previously thought to show opponents moves and then
# your own - but in fact it shows your opponents move and the required result
# of the round (X - you lose, Y - you draw, Z - you win)

# The points are the same system as before

# The points are scored in 2 ways:

# (1) Winning, Losing or Drawing the round:
#   (a) Winning = 6 points
#   (b) Drawing = 3 points
#   (c) Losing  = 0 points

# (2) What you've played:
#   (a) Rock       = 1 points
#   (b) Paper      = 2 points
#   (c) Scissors   = 3 points

# The total score is the summation of both points

# The Code:
# Read input file
with open("2022_day2_input.txt") as f:
    content = f.readlines()

# Each strategy_guide entry is a string of opponents and outcome (e.g 'A X')
# This concatenation removes endlines and then splits each into a single list
# of opponents move and your move
strategy_guide = [i.strip().split() for i in content]

def what_wins(opposition):
    '''
    Produces what will beat an opposition move (A, B, C)
    '''
    if opposition == 'A':
        return 'paper'

    if opposition == 'B':
        return 'scissors'

    if opposition == 'C':
        return 'rock'

def what_draws(opposition):
    '''
    Produces what will draw an opposition move (A, B, C)
    '''
    if opposition == 'A':
        return 'rock'

    if opposition == 'B':
        return 'paper'

    if opposition == 'C':
        return 'scissors'

def what_loses(opposition):
    '''
    Produces what will lose to an opposition move (A, B, C)
    '''
    if opposition == 'A':
        return 'scissors'

    if opposition == 'B':
        return 'rock'

    if opposition == 'C':
        return 'paper'


def points(moves):
    '''
    This takes a single element of strategy_guide (the opponent's move
    for that round and the required result) and produces the points scored
    by your move shape and the outcome of the round
    '''
    total_score = 0
    
    opposition = moves[0]
    result = moves[1]

    # Get the your move and add the outcome points to total score
    if result == 'X':
        your_move = what_loses(opposition)

    if result == 'Y':
        your_move = what_draws(opposition)
        total_score += 3

    if result == 'Z':
        your_move = what_wins(opposition)
        total_score += 6

    # Calculate the shape points from your_move
    if your_move == 'rock':
        total_score += 1

    if your_move == 'paper':
        total_score += 2

    if your_move == 'scissors':
        total_score += 3

    return total_score


grand_total = 0

for i in strategy_guide:
    grand_total += int(points(i))

print(grand_total)
        









