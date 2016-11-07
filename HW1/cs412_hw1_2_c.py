import csv
import numpy as np
from scipy import stats

with open('data.online.scores') as f:
    reader = csv.reader(f, delimiter='\t')
    data = [(int(col1), int(col2), int(col3)) for col1, col2, col3 in reader]
    final = []
    for score in data:
    	final.append(score[2])
    index = final.index(90)
    a = np.array(final)
    a = stats.zscore(a)
    print(a[index])

    
