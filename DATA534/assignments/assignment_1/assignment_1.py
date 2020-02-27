import pandas as pd

class Node:
    def __init__(self, _index=None, _valLeft=None, _valRight=None, _nodeLeft=None, _nodeRight=None, _is_leaf=False, _label=None):
        self.index = _index
        self.valLeft = _valLeft
        self.nodeLeft = _nodeLeft
        self.nodeRight = _nodeRight
        self.is_leaf = _is_leaf
        self.label = _label


class MyInput:
    def __init__(self,_outlook,_company,_sailboat_size):
        self.as_list=[_outlook,_company,_sailboat_size]


def evalTree(current_node,input):
    while True:
        if current_node.is_leaf:
            print("When outlook is " + input[0] + ", and company is " +input[1] + ", and when sailboat size is " + input[2] +" the answer is " + current_node.label)
            break
        else:
            if input[current_node.index] == current_node.valLeft:
                current_node = current_node.nodeLeft
            else:
                current_node = current_node.nodeRight


leaf0 = Node(_is_leaf=True, _label='Yes')
leaf1 = Node(_is_leaf=True, _label='No')
leaf2 = Node(_is_leaf=True, _label='No')
leaf3 = Node(_is_leaf=True, _label='Yes')

mid0 = Node(1, 'Big', 'Small', leaf0, leaf1)
mid1 = Node(1, 'Small', 'Big', leaf2, leaf3)

root0 = Node(0, 'Sunny', 'Rainy', mid0, mid1)

all_inputs = pd.DataFrame([{'outlook': 'Sunny', 'Company': 'Big', 'Sailboat': 'Big'},
                           {'outlook': 'Rainy', 'Company': 'Big', 'Sailboat': 'Big'},
                           {'outlook': 'Sunny', 'Company': 'Small', 'Sailboat': 'Big'},
                           {'outlook': 'Rainy', 'Company': 'Small', 'Sailboat': 'Small'}])

new_input = []
for index, rows in all_inputs.iterrows():
    my_list = [rows.outlook, rows.Company, rows.Sailboat]
    new_input.append(my_list)


for i in new_input:
    evalTree(root0, i)