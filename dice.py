#!/usr/bin/python3

import random

# Flow:
# Input
    # Validate arguments if any
        # Throw error if it's invalid
    # Roll dice based on arguments
        # if no args just do a 1d6
    # Add stuff based on arguments
        # Plus/minus
        # High/low
    # if flags:
        # results
        # mean
        # median
        # average
# Output
dice_results = []
random.seed()

def dice_roll(dice_count = 1, dice_size = 6):
    for i in range(0, dice_count):
        dice_results.append(random.randint(1, dice_size))

dice_roll()
print(dice_results)
dice_results = []
dice_roll(4,20)
print(dice_results)