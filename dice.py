#!/usr/bin/python3

import random, sys, re, numpy
from scipy.stats import mode

def init():
    global dice_results
    dice_results = []
    random.seed()

def dice_roll(dice_count = 1, dice_size = 6):
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
        print('[Debug] Results flag')
    if ('-m' in i) or ('--mean' in i):
        print('[Debug] Mean flag')
    if ('-d' in i) or ('--median' in i):
        print('[Debug] Median flag')
    if ('-o' in i) or ('--mode' in i):
        print('[Debug] Mode flag')
    if ('-g' in i) or ('--range' in i):
        print('[Debug] Range flag')

init()
dice_roll()
print(sum(dice_results))
launch_args(sys.argv[1:])
print(sys.argv[1:])