# --- AoC 2022 - Day 1: Calorie Counting PART ONE --- #

# The Problem:
# Input is a list of food items by their calories, where there is a line break
# this a new elf's backpack

# Find the elf with the most total calories and find the sum of their calories

# The Code:
# Read input file
with open("2022_day1_input.txt") as f:
    content = f.readlines()

# Removing the endline characters from each entry
stock_take = [i.strip() for i in content]

# Seperating the stock_take into seperate elves
# Thanks to stackoverflow for information onf itertools
# https://stackoverflow.com/questions/52943558/splitting-lists-by-empty-element
from itertools import groupby
elves = [list(g) for k, g in groupby(stock_take, key=bool) if k]

record = 0
for i in elves:
    backpack = [int(j) for j in i]
    calories = sum(backpack)

    if calories > record:
        record = calories

print(record)










