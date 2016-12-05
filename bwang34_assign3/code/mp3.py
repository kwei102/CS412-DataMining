import numpy as np
import operator
import csv

def combPattern(remaining_k, pruning_k, basic):
    ret = {}
    remainPattern = remaining_k.keys()
    for pattern in remainPattern:
    	for item in basic:
    		if item in pattern:
    			continue
    		newPattern = pattern.split(' ')
    		newPattern.append(item)
    		newPattern = sorted(newPattern)
    		prunFlag = False
    		for limit in pruning_k:
    			if set(limit.split(' ')) < set(newPattern):
    				prunFlag = True
    				break
    		if prunFlag is False:
    			ret[' '.join(newPattern)] = 0
    return ret



def nextLevel(remaining_k, pruning_k, basic, length, frequentPattern, paper):
	min_support = int(0.005 * len(paper))
	print 'Calculate {}-itemsets with min_support {}'.format(length, min_support)
	diction = {}
	diction = combPattern(remaining_k, pruning_k, basic)

	for title in paper:
		for key in diction:
			words = key.split(' ')
			if set(words) < set(title):
				diction[key] += 1
	keys = diction.keys()
	remaining = {}
	for key in keys:
		if diction[key] > min_support:
			remaining[key] = diction[key]
			frequentPattern[key] = diction[key]
		else:
			pruning_k.append(key)
	return remaining


def patternMining(name):
	with open(name, 'r') as f:
		pattern = {}
		paper = []
		for line in f:
			title = line.strip().split(' ')
			paper.append(title)
			for word in title:
				if word not in pattern:
					pattern[word] = 1
				else:
					pattern[word] +=1
		
		keys = pattern.keys()
		basic = []
		remaining = {}
		pruning = []
		frequentPattern = {}
		min_support = int(0.005 * len(paper))
		# min_support = 700
		print name
		print 'Calculate 1-itemsets with min_support {}'.format(min_support)
		for key in keys:
			if pattern[key] > min_support:
				basic.append(key)
				remaining[key] = pattern[key]
				frequentPattern[key] = pattern[key]
		index = 2
		while len(remaining) > 0:
		# for i in range(1):
			remaining = nextLevel(remaining, pruning, basic, index, frequentPattern, paper)
			index += 1
	return list(reversed(sorted(frequentPattern.items(), key=operator.itemgetter(1))))


vocab = dict()
vocab_order = dict()
titles = []
with open('paper.txt', 'r') as file:
	count = 0
	for line in file:
		record = line.strip().split('\t')
		for i in range(1,len(record)):
			titles.append(record[i])
			title = record[i].split(' ')
			for word in title:
				if word not in vocab:
					vocab[word] = count
					vocab_order[count] = word
					count += 1

with open('vocab.txt', 'w') as dictionary:
	for i in range(len(vocab)):
		dictionary.write(vocab_order[i] + '\n')

with open('title.txt', 'w') as titleFile:
	for title in titles:
		wordCount = {}
		title = title.split(' ')
		for word in title:
			if word not in wordCount:
				wordCount[word] = 1
			else:
				wordCount[word] += 1
		titleFile.write(str(len(wordCount)) + ' ')
		for key in wordCount.keys():
			titleFile.write(str(vocab[key]) + ':' + str(wordCount[key]) + ' ')
		titleFile.write('\n')

with open('result/word-assignments.dat', 'r') as result:
	topic = []
	for i in range(5):
		topic.append([])
	for line in result:
		record = line.strip().split(' ')[1:]
		temp = []
		for i in range(5):
			temp.append([])
		for item in record:
			item = item.split(':')
			temp[int(item[1])].append(item[0])
		for i in range(5):
			if temp[i]:
				topic[i].append(' '.join(temp[i]))
	for i in range(5):
		with open('topic-' + str(i) + '.txt', 'w') as topicFile:
			topicFile.write('\n'.join(topic[i]))

for i in range(5):
	freqPattern = patternMining('topic-' + str(i) + '.txt')
	with open('patterns/pattern-' + str(i) + '.txt', 'w') as patternFile:
		for record in freqPattern:
			patternFile.write(str(record[1]) + ' ' + record[0] + '\n')

dictionary = []
for i in range(5):
	temp = {}
	dictionary.append(temp)

pattern = []
for i in range(5):
	temp = []
	pattern.append(temp)


collection = []
for i in range(5):
	temp = set()
	collection.append(temp)

for i in range(5):
	with open('patterns/pattern-' + str(i) + '.txt', 'r') as patternFile:
		for line in patternFile:
			record = line.strip().split(' ')
			num = int(record[0])
			key = ' '.join(sorted(record[1:]))
			dictionary[i][key] = num
			pattern[i].append(key)
			collection[i].add(key)
		with open('patterns/pattern-' + str(i) + '.txt.phrase', 'w') as patternFileWord:
			for item in pattern[i]:
				words = item.split(' ')
				output = ''
				for word in words:
					output = output + ' ' + vocab_order[int(word)]
				patternFileWord.write(str(dictionary[i][item]) + ' ' + output + '\n')
		with open('max/max-' + str(i) + '.txt', 'w') as maxFile:
			maxed = []
			for item in pattern[i]:
				flag = False
				for other in pattern[i]:
					if item == other:
						continue
					if item != other and item in other:
						flag = True
						break
				if flag is False:
					maxFile.write(str(dictionary[i][item]) + ' ' + item + '\n')
					maxed.append(item)
			with open('max/max-' + str(i) + '.txt.phrase', 'w') as maxFileWord:
				for item in maxed:
					words = item.split(' ')
					output = ''
					for word in words:
						output = output + ' ' + vocab_order[int(word)]
					maxFileWord.write(str(dictionary[i][item]) + ' ' + output + '\n')
		with open('closed/closed-' + str(i) + '.txt', 'w') as closedFile:
			closed = []
			for item in pattern[i]:
				flag = False
				for other in pattern[i]:
					if item == other:
						continue
					if item != other and item in other and dictionary[i][item] == dictionary[i][other]:
						flag = True
						break
				if flag is False:
					closedFile.write(str(dictionary[i][item]) + ' ' + item + '\n')
					closed.append(item)
			with open('closed/closed-' + str(i) + '.txt.phrase', 'w') as closedFileWord:
				for item in closed:
					words = item.split(' ')
					output = ''
					for word in words:
						output = output + ' ' + vocab_order[int(word)]
					closedFileWord.write(str(dictionary[i][item]) + ' ' + output + '\n')

other = np.arange(5)
for i in range(5):
	with open('purity/purity-' + str(i) + '.txt', 'w') as puriFile:
		purity = []
		for item in pattern[i]:
			part1 = np.log2(float(dictionary[i][item])/float(len(collection[i])))
			f_tp = []
			for j in other:
				if i == j:
					continue
				if item in dictionary[j]:
					otherValue = dictionary[j][item]
				else:
					otherValue = 0
				f_tp.append(float(dictionary[i][item] + otherValue)/float(len(collection[i] | collection[j])))
			maxValue = max(f_tp)
			part2 = np.log2(maxValue)
			purity.append((part1-part2, dictionary[i][item], item))
		purity = sorted(purity)[::-1]
		for record in purity:
			puriFile.write(str(record[0]) + ' ' + record[2] + '\n')
		with open('purity/purity-' + str(i) + '.txt.phrase', 'w') as puriFileWord:
			for record in purity:
				words = record[2].split(' ')
				output = ''
				for word in words:
					output = output + ' ' + vocab_order[int(word)]
				puriFileWord.write(str(record[0]) + ' ' + output + '\n')



