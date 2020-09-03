#!/usr/bin/python3

import random, sys, re, numpy, scipy
from scipy.stats import mode

def init():
    global dice_results
    dice_results = []
    random.seed()

def dice_roll(dice_count = 2, dice_size = 6):
    for i in range(0, dice_count):
        dice_results.append(random.randint(1, dice_size))

def dice_mean(array_in):
    return int(numpy.mean(array_in).round())

def dice_median(array_in):
    return int(numpy.median(array_in))

def dice_mode(array_in):
    return scipy.stats.mode(array_in)[0][0]

def launch_args(i):
    if ('-r' in i) or ('--results' in i):
        print('Results: ' + str(dice_results))
    if ('-m' in i) or ('--mean' in i):
        print('Mean: ' + str(dice_mean(dice_results)))
    if ('-d' in i) or ('--median' in i):
        print('Median: ' + str(dice_median(dice_results)))
    if ('-o' in i) or ('--mode' in i):
        print('Mode: ' + str(dice_mode(dice_results)))
    if ('-g' in i) or ('--range' in i):
        print('[Debug] Range flag, no logic yet implemented.')

init()
dice_roll()
print('Sum: ' + str(sum(dice_results)))
launch_args(sys.argv[1:])