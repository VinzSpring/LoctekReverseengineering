from itertools import islice
from pprint import pprint as p
from matplotlib import pyplot as plt
import numpy as np
from math import *
from data_prepare import *
import string 

import random

def shuffle(s):
    ls = list(s)
    random.shuffle(ls)
    return "".join(ls)

def all_substrings(s):
    l = len(s)
    for i in range(l):
        for j in range(i + 1, l):
            yield i, j, s[i: j]

def get_pattern_table(bits: str) -> {}:
    table = {}
    for _, _, pattern in all_substrings(bits):
        table[pattern] = bits.count(pattern)
    return table

        
def weight_string(bits: str, table):
    weights = [0 for i in range(len(bits))]
    for i, j, pattern in all_substrings(bits):
        if pattern in table:
            score = table[pattern]
            for x in range(i, j):
                weights[x] += score
    # normalize
    m = max(weights)
    return [v / m for v in weights] if m else weights

def visualize_samples(samples, table):
    l = len(samples)
    fig, sub_plots = plt.subplots(ceil(sqrt(l)), ceil(sqrt(l)), sharex=False)
    for i, sub in enumerate(sub_plots.reshape(-1)):
        if i >= l:
            break
        x = list(range(len(samples[i])))
        y = weight_string(samples[i], table)
        sub.set_xticks(x, minor=False)
        sub.set_xticklabels([s for s in samples[i]], fontdict=None, minor=False)
        sub.bar(x, y, width=1)
    plt.show()

def encode(hex):
    return hex.decode("latin-1")

if __name__ == "__main__":


    with open("./going_down_75_71_no_btn_R.txt") as f:
        ls = get_packets(f.readlines())

    table = get_pattern_table("".join(["".join(l) for l in ls]))
    sample = "".join(ls[0])
    visualize_samples("".join(["".join(l) for l in ls]), table)