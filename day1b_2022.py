# --- AoC 2022 - Day 1: Calorie Counting PART TWO --- #

# The Problem:
# Input is a list of food items by their calories, where there is a line break
# this a new elf's backpack

# Find the elves in the top three for total calories per elf

# The Code:
# Read input file
with open("2022_day1_input.txt") as f:
    content = f.readlines()

# Removing the endline characters from each entry
stock_take = [i.strip() for i in content]

# Seperating the stock_take into seperate elves
# Thanks to stackoverflow for the information on itertools
# https://stackoverflow.com/questions/52943558/splitting-lists-by-empty-element
from itertools import groupby
elves = [list(g) for k, g in groupby(stock_take, key=bool) if k]

# Create empty list and place in the summation of each elf's stock
backpack_totals = []
for i in elves:
    backpack = [int(j) for j in i]
    calories = sum(backpack)
    backpack_totals.append(calories)

# Using the default sorting to get decending order 
backpack_totals = sorted(backpack_totals, reverse=True)

podium = backpack_totals[0:3]
print(sum(podium))











