# Script to prepare the data for GPT-3
# Take 9 random samples from the data

import random

with open('../data/pairs/groenwold.txt', 'r') as f:
    with open('../data/pairs/groenwold_mini.txt', 'w') as f2:

        for i in random.sample(f.readlines(), 10):
            f2.write(i)