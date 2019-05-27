'''
Design file system for Zookeepr system
APIs:
- create_node(path, value)
- set_value(path, value)

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.children = {}
		self.callback = None

class ZooKeeper:
	def __init__(self):
		self.root = Node(None)

	def get_path(self, path):
		# plist = [p for p in path.split('/') if p.strip() != '' ]
		plist = []
		for p in path.split('/'):
			if p.strip() != '':
				plist.append(p)
		return plist

	def function_callback(self, plist, path, value):
		node = self.root
		for word in plist[:-1]:
			node = node.children[word]
			if node.callback is not None:
				node.callback(path, value)

	def create_node(self, path, value):
		plist = self.get_path(path)
		if len(plist) == 0:
			raise ValueError()

		node = self.root
		for word in plist[:-1]:
			if word not in node.children:
				raise ValueError()
			node = node.children[word]
		node.children[plist[-1]] = Node(value)

		self.function_callback(plist, path, value)

	def set_value(self, path, value):
		plist = self.get_path(path)
		if len(plist) == 0:
			raise ValueError()

		node = self.root
		for word in plist:
			if word not in node.children:
				raise ValueError()
			node = node.children[word]
		node.data = value

		self.function_callback(plist, path, value)

	def get_value(self, path):
		plist = self.get_path(path)
		if len(plist) == 0:
			raise ValueError()

		node = self.root
		for word in plist:
			if word not in node.children:
				raise ValueError()
			node = node.children[word]
		return node.data

	def watch(self, path, cb):
		plist = self.get_path(path)
		if len(plist) == 0:
			raise ValueError()

		node = self.root
		for word in plist:
			if word not in node.children:
				raise ValueError()
			node = node.children[word]
		node.callback = cb

def dummy_func(path, val):
	print ("dummy_func", path, val)

obj = ZooKeeper()
# TC #1
obj.create_node('/a', 10)
try:
	val = obj.get_value('/a')
	print("GET TEST PASS", val)
except:
	print("TEST FAIL")

# TC #2
obj.watch('/a', dummy_func)
obj.create_node('/a/b', 20)
obj.watch('/a/b', dummy_func)
try:
	val = obj.get_value('/a/b')
	print("GET TEST PASS", val)
except:
	print("TEST FAIL")


# Tc3
obj.create_node('/a/b/c', 30)
try:
	val = obj.get_value('/a/b/c')
	print("GET TEST PASS", val)
except:
	print("GET TEST FAIL")

#Tc4
obj.set_value('/a/b/c', 60)
try:
	val = obj.get_value('/a/b/c')
	print("GET TEST PASS", val)
except:
	print("GET TEST FAIL")

# Tc4
try:
	val = obj.get_value('/d')
	print("GET TEST PASS", val)
except:
	print("GET TEST FAIL")







