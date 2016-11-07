import csv
import numpy as np
from scipy import stats

with open('data.online.scores') as f:
    reader = csv.reader(f, delimiter='\t')
    data = [(int(col1), int(col2), int(col3)) for col1, col2, col3 in reader]
    midterm = []
    final = []
    for score in data:
    	midterm.append(score[1])
    	final.append(score[2])
    score = np.vstack((midterm,final))
    print(np.cov(score))

    
