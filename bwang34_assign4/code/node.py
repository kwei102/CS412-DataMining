import random
import math

class node(object):
	"""docstring for node"""
	def __init__(self, data, tree_type):
		self.data = data
		self.type = tree_type
		# leaf
		self.is_leaf = False
		self.label = None
		self.label_set = set()
		# non-leaf
		self.attribute = None
		self.table = {}
		self.attr_num = {}
		self.value_num = {}
		self.label_num = {}
		self.gini = {}
		self.majority = 0
		# children
		self.children = {}
		self.connection = {}
		
		self.construct()
		if self.is_leaf is False:
			self.gini_split()
			self.split_child()

	def construct(self):
		if len(self.data[0]) == 1:
			self.is_leaf = True
			labels = {}
			for record in self.data:
				label = record[0]
				if label not in labels:
					labels[label] = 0
				labels[label] += 1
			self.label = sorted(labels, key=labels.get, reverse=True)[0]
			return

		majority = {}
		for record in self.data:
			label = record[0]
			if label not in majority:
				majority[label] = 0
			majority[label] += 1
			self.label_set.add(label)
			pairs = record[1:]
			for pair in pairs:
				index = pair[0]
				value = pair[1]
				if index not in self.attr_num:
					self.table[index] = {}
					self.attr_num[index] = 0
				if value not in self.table[index]:
					self.table[index][value] = set() 
				if (index, value) not in self.value_num:
					self.value_num[(index, value)] = 0
				if (index, value, label) not in self.label_num:
					self.label_num[(index, value, label)] = 0
				
				self.table[index][value].add(label)
				self.attr_num[index] += 1
				self.value_num[(index, value)] += 1
				self.label_num[(index, value, label)] += 1
		self.majority = sorted(majority, key=majority.get, reverse=True)[0]
		
		if len(self.label_set) == 1:
			self.is_leaf = True
			self.label = self.label_set.pop()

	def gini_split(self):
		if self.type == 'DT':
			for attr in self.table.keys():
				attr_freq = self.attr_num[attr]
				if attr not in self.gini:
					self.gini[attr] = 0
				for value in self.table[attr].keys():
					value_freq = self.value_num[(attr, value)]
					gini = 1.0
					for label in self.table[attr][value]:
						p = float(self.label_num[(attr,value,label)])/float(self.value_num[(attr,value)])
						gini -= p*p
					self.gini[attr] += (float(value_freq)/float(attr_freq))*gini
		else:
			attrs = self.table.keys()
			attrs = random.sample(attrs, int(math.ceil(math.sqrt(len(attrs)))))
			for attr in attrs:
				attr_freq = self.attr_num[attr]
				if attr not in self.gini:
					self.gini[attr] = 0
				for value in self.table[attr].keys():
					value_freq = self.value_num[(attr, value)]
					gini = 1.0
					for label in self.table[attr][value]:
						p = float(self.label_num[(attr,value,label)])/float(self.value_num[(attr,value)])
						gini -= p*p
					self.gini[attr] += (float(value_freq)/float(attr_freq))*gini

	def split_child(self):
		self.attribute = sorted(self.gini, key=self.gini.get)[0]
		for i, record in enumerate(self.data):
			record_output = [record[0]]
			target_group = 0
			for pair in record[1:]:
				index = pair[0]
				value = pair[1]
				if index != self.attribute:
					record_output.append(pair)
				else:
					target_group = value
			if target_group not in self.children:
				self.children[target_group] = []
			self.children[target_group].append(record_output)



		

























