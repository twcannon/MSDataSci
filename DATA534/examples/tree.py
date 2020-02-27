
class Node():
	def __init__(self,_index,_valLeft,_valRight,_nodeLeft,_nodeRight,_is_leaf=False,_label=None):
		self.index = _index
		self.valLeft = _valLeft
		self.valRight = _valRight
		self.nodeLeft = _nodeLeft
		self.nodeRight = _nodeRight
		self.is_leaf = _is_leaf
		self.label = _label

leaf0 = Node(None, None, None, None, None, True, 'Yes')
leaf1 = Node(None, None, None, None, None, True, 'No')
leaf2 = Node(None, None, None, None, None, True, 'No')
leaf3 = Node(None, None, None, None, None, True, 'Yes')

mid0 = Node(1,'Big', 'Small', leaf0, leaf1)
mid1 = Node(2,'Small', 'Big', leaf2, leaf3)

root = Node(0,'Sunny', 'Rainy', mid0, mid1)

input01 = ['Sunny','Big','Big']

currNode = root

while currNode.is_leaf is not True:
	if input01[currNode.index] == currNode.valLeft:
		currNode = currNode.nodeLeft
	else:
		currNode = currNode.nodeRight

print("the answer is " + currNode.label)