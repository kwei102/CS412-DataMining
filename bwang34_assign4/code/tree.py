from node import *
import Queue

class tree(object):
	"""docstring for tree"""
	def __init__(self, data):
		self.data = data
		self.root = None
		self.construct()

	def construct(self):
		queue = Queue.Queue()
		if self.root is None:
			self.root = node(self.data)
			queue.put(self.root)

		while queue.empty() is False:
			cur_node = queue.get()
			if cur_node.is_leaf is True:
				continue
			for child in cur_node.children.keys():
				cur_node.connection[child] = node(cur_node.children[child])
				queue.put(cur_node.connection[child])

	def test(self, data):
		correct = 0
		label_pair = []
		for i, record in enumerate(data):
			cur_node = self.root
			label_predicted = 0
			while cur_node.is_leaf is False:
				attribute = int(cur_node.attribute)
				if attribute >= len(record):
					break
				value = record[attribute]
				if value not in cur_node.connection:
					break
				cur_node = cur_node.connection[value]
			if cur_node.is_leaf:
				label_predicted = cur_node.label
			else:
				label_predicted = cur_node.majority
			if label_predicted == record[0]:
				correct += 1
			label_pair.append((record[0], label_predicted))
		return correct, label_pair





		
