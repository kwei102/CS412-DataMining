import numpy as np

# python evaluation.py
# change the parameter INPUT (line 34) before running.

balance_d = [[ 0,12,10],
             [ 8,66,28], 
             [25,11,65]]
balance_r = [[ 0,11,11],
             [ 1,77,24], 
             [ 3,16,82]]

nursery_d = [[1545,  40,  11,   0,   0],
             [  30,  97,   0,   0,   3],
             [  33,   0,1503,   0,   0],
             [   0,   0,   0,1605,   0],
             [   0,   0,   0,   0,   0]]	
nursery_r = [[1563,  11,  22,   0,   0],
             [  49,  81,   0,   0,   0],
             [  32,   0,1504,   0,   0],
             [   0,   0,   0,1605,   0],
             [   0,   0,   0,   0,   0]]

led_d = [[274, 77],
         [ 84,699]]
led_r = [[274, 77],
         [ 83,700]]

poker_d = [[365, 94],
           [156, 63]]
poker_r = [[457, 2],
           [216, 3]]

INPUT = led_r

def sensitivity(table):
	print 'sensitivity'
	for i in range(length):
		if float(sum(table[i])) == 0:
			print 0
			continue
		print float(table[i][i])/float(sum(table[i]))
	print '\n'


def specificity(table):
	print 'specificity'
	for i in range(length):
		TN = 0
		N = 0
		for j in range(length):
			if j == i:
				continue
			TN += sum(table[j]) - table[j][i]
			N += sum(table[j])
		if float(N) == 0:
			print 0
			continue
		print float(TN)/float(N)
	print '\n'

def precision(table):
	print 'precision'
	for i in range(length):
		TP = 0
		P_p = 0 
		for j in range(length):
			if i == j:
				TP += table[j][i]
			P_p += table[j][i]
		if float(P_p) == 0:
			print 0
			continue
		print float(TP)/float(P_p)
	print '\n'

def recall(table):
	print 'recall'
	for i in range(length):
		if float(sum(table[i])) == 0:
			print 0
			continue
		print float(table[i][i])/float(sum(table[i]))
	print '\n'

def F_1(table):
	print 'F_1'
	for i in range(length):
		TP = 0
		P_p = 0 
		for j in range(length):
			if i == j:
				TP += table[j][i]
			P_p += table[j][i]
		if float(P_p) == 0:
			print 0
			continue
		prc = float(TP)/float(P_p)
		if float(sum(table[i])) == 0:
			print 0
			continue
		rec = float(table[i][i])/float(sum(table[i]))
		if prc+rec == 0:
			print 0
			continue
		print float(2*prc*rec)/float(prc+rec)
	print '\n'

def F_b(table, b):
	print 'F_b_{}'.format(b)
	for i in range(length):
		TP = 0
		P_p = 0 
		for j in range(length):
			if i == j:
				TP += table[j][i]
			P_p += table[j][i]
		if float(P_p) == 0:
			print 0
			continue
		prc = float(TP)/float(P_p)
		if float(sum(table[i])) == 0:
			print 0
			continue
		rec = float(table[i][i])/float(sum(table[i]))
		if b*b*prc+rec == 0:
			print 0
			continue
		print float((b*b+1)*prc*rec)/float(b*b*prc+rec)
	print '\n'



if __name__ == '__main__':
	length = len(INPUT)
	sensitivity(INPUT)
	specificity(INPUT)
	precision(INPUT)
	recall(INPUT)
	F_1(INPUT)
	F_b(INPUT, 0.5)
	F_b(INPUT, 2)
