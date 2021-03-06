from itertools import islice
from pprint import pprint as p
from matplotlib import pyplot as plt
import numpy as np
from math import *

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
    # normalizegit
    m = max(weights)
    return [v / m for v in weights]

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

if __name__ == "__main__":
    table = get_pattern_table("01010101000001011110010110010101001000010111101011001010000010111110111111001010101001010101011")
    sample = "000001111010101010000"
    visualize_samples([shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample), shuffle(sample)], table)