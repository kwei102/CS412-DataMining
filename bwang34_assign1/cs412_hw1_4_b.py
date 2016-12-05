import csv
import numpy as np
from scipy import spatial
from scipy import stats

with open('data.supermarkets.inventories') as f:
    reader = csv.reader(f, delimiter='\t')
    data = []
    for row in reader:
    	data.append(row)
    JS = []
    for item in data[0]:
    	JS.append(int(item))
    KK = []
    for item in data[1]:
    	KK.append(int(item))
    print(spatial.distance.minkowski(JS, KK, 1))
    print(spatial.distance.minkowski(JS, KK, 2))
    print(spatial.distance.minkowski(JS, KK, float('inf')))
    print(1-spatial.distance.cosine(JS, KK))
    print(stats.entropy(JS, KK, base=None))
