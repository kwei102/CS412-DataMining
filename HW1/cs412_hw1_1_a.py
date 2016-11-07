import csv

with open('data.online.scores') as f:
    reader = csv.reader(f, delimiter='\t')
    data = [(int(col1), int(col2), int(col3)) for col1, col2, col3 in reader]
    midterm_max = 0
    midterm_min = 200
    for student in data:
    	midterm_max = max(midterm_max, student[1])
    	midterm_min = min(midterm_min, student[1])
    print(midterm_max)
    print(midterm_min)
