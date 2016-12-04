import sys
import numpy as np
from tree import *
import random

# time python RandomForest.py ../data/balance-scale.train ../data/balance-scale.test
# time python RandomForest.py ../data/nursery.data.train ../data/nursery.data.test
# time python RandomForest.py ../data/led.train.new ../data/led.test.new
# time python RandomForest.py ../data/poker.train ../data/poker.test

TRAIN = sys.argv[1]
TEST = sys.argv[2]
SAMPLE = 0.5
TREE = 200

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
	for i in range(TREE):
		data.append([])
	max_label = 0
	with open(TRAIN, 'r') as train_file:
		for line in train_file:
			line = line.strip().split(' ')
			record = []
			label = line[0]
			max_label = max(max_label, int(label))
			record.append(label)
			attrs = line[1:]
			for attr in attrs:
				index, value = attr.split(':')
				record.append((index,value))
			for i in range(TREE):
				if random.random() < SAMPLE:
					data[i].append(record)
	return data, max_label

def read_test():
	test = []
	labels = []
	count = 0
	with open(TEST, 'r') as test_file:
		for line in test_file:
			line = line.strip().split(' ')
			record = []
			label = line[0]
			labels.append(label)
			record.append(label)
			attrs = line[1:]
			for attr in attrs:
				index, value = attr.split(':')
				record.append(value)
			test.append(record)
			count += 1
	return test, count, labels

def calculate_confusion_matrix(num, labels, labels_predicted):
	selected_label = []
	length = len(labels)
	correct = 0
	for i in range(length):
		selected_label.extend(sorted(labels_predicted[i], key=labels_predicted[i].get, reverse=True)[0])
	confusion_matrix = np.zeros((num, num))
	for j in range(length):
		confusion_matrix[int(labels[j])-1][int(selected_label[j])-1] += 1
		if labels[j] == selected_label[j]:
			correct += 1
	return confusion_matrix, correct

def print_confusion_matrix(confusion_matrix):
	for row in confusion_matrix:
		string = [str(int(x)) for x in row]
		print ' '.join(string)

if __name__ == '__main__':
	data, class_num = read_train()
	test, data_num, labels = read_test()
	output = []
	for i in range(data_num):
		output.append({})
	for i in range(TREE):
		decision_tree = tree(data[i], 'RF')
		labels_predicted = decision_tree.test(test)
		for j, label in enumerate(labels_predicted):
			if label not in output[j]:
				output[j][label] = 0
			output[j][label] += 1
	confusion_matrix, correct = calculate_confusion_matrix(class_num, labels, output)
	print_confusion_matrix(confusion_matrix)
	# print 'accuracy: {}'.format(float(correct)/float(data_num))
