# --- AoC 2022 - Day 2: Rock, Paper, Scissors PART ONE --- #

# The Problem:
# You are given a 'strategy guide' to play rock, paper, scissors and have to
# determine the total score if you play to this guide

# The guide is formed by the opponents moves (A - Rock, B - Paper, C - Scissors)
# next to your moves (X - Rock, Y - Paper, Z - Scissors)

# The points are scored in 2 ways:

# (1) Winning, Losing or Drawing the round:
#   (a) Winning = 6 points
#   (b) Drawing = 3 points
#   (c) Losing  = 0 points

# (2) What you've played:
#   (a) Rock     (X)  = 1 points
#   (b) Paper    (Y)  = 2 points
#   (c) Scissors (Z)  = 3 points

# The total score is the summation of both points

# The Code:
# Read input file
with open("2022_day2_input.txt") as f:
    content = f.readlines()

# Each strategy_guide entry is a string of opponents and your move (e.g 'A X')
# This concatenation removes endlines and then splits each into a single list
# of opponents move and your move
strategy_guide = [i.strip().split() for i in content]

def points(moves):
    '''
    This takes a single element of strategy_guide (the moves for that round)
    and produces the expected points for winning, losing or drawing and for
    the shape played by the player
    '''
    total_score = 0
    
    # Troubleshooting redudancy
    win_loss_draw = 0
    shapes_points = 0

    oppo = moves[0]
    your = moves[1]

    # Played score
    if your == 'X':
        total_score += 1
        shapes_points = 1
        
    if your == 'Y':
        total_score += 2
        shapes_points = 2

    if your == 'Z':
        total_score += 3
        shapes_points = 3

    # Win, Lose, Draw
    # You play rock
    if your == 'X':
        if oppo == 'A':
            total_score += 3
            win_loss_draw = 3
        elif oppo == 'C':
            total_score += 6
            win_loss_draw = 6
            
    # You play paper
    if your == 'Y':
        if oppo == 'B':
            total_score += 3
            win_loss_draw = 3
        elif oppo == 'A':
            total_score += 6
            win_loss_draw = 6
    # You play scissors
    if your == 'Z':
        if oppo == 'C':
            total_score += 3
            win_loss_draw = 3
        elif oppo == 'B':
            total_score += 6
            win_loss_draw = 6

    return total_score, win_loss_draw, shapes_points

# Now we can scan through our data and predict the total points
grand_total = 0

# Troubleshooting redudancy
win_loss_draw_total = 0
shapes_points_total = 0

for i in strategy_guide:
    result = list(points(i))

    win_loss_draw_total += int(result[1])
    shapes_points_total += int(result[2])

    grand_total += int(result[0])

print('Total score: ', grand_total)


        









