import csv
import numpy as np
from scipy import spatial
from scipy import stats

table = np.array([[1346, 430], [133, 32974]])
print(stats.chisquare(table))