import sys
import numpy as np
from tree import *


# python DecisionTree.py ../data/balance-scale.train ../data/balance-scale.test
# python DecisionTree.py ../data/nursery.data.train ../data/nursery.data.test
# python DecisionTree.py ../data/led.train.new ../data/led.test.new
# python DecisionTree.py ../data/poker.train ../data/poker.test


TRAIN = sys.argv[1]
TEST = sys.argv[2]

def read_train():
	data = []
	with open(TRAIN, 'r') as train_file:
		count = 0
		for line in train_file:
			line = line.strip().split(' ')
			record = []
			label = line[0]
			record.append(label)
			attrs = line[1:]
			for attr in attrs:
				index, value = attr.split(':')
				record.append((index,value))
			data.append(record)
	return data

def read_train():
	data = []
	with open(TRAIN, 'r') as train_file:
		for line in train_file:
			line = line.strip().split(' ')
			record = []
			label = line[0]
			record.append(label)
			attrs = line[1:]
			for attr in attrs:
				index, value = attr.split(':')
				record.append((index,value))
			data.append(record)
	return data

def read_test():
	test = []
	count = 0
	with open(TEST, 'r') as test_file:
		for line in test_file:
			line = line.strip().split(' ')
			record = []
			label = line[0]
			record.append(label)
			attrs = line[1:]
			for attr in attrs:
				index, value = attr.split(':')
				record.append(value)
			test.append(record)
			count += 1
	return test, count


if __name__ == '__main__':
	data = read_train()
	test, num = read_test()
	decision_tree = tree(data)
	correct_num, label_pair = decision_tree.test(test)
	print 'accuracy: {}'.format(float(correct_num)/float(num))



