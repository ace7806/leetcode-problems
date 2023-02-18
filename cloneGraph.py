class Node:
       def __init__(self, val) -> None:
              self.val = val
              self.neighbors: list[Node] = []

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.extend([node2,node4])
node3.neighbors.extend([node2,node4])
node2.neighbors.extend([node1,node3])
node4.neighbors.extend([node1,node3])



'''
if node.val in seen return nodeCopy
createCopy of node and add it to seen
loop through nodes neighbors, dfs on neighbor, append neighborCopy to nodeCopy
return nodeCopy
'''
seen : dict[Node] = {}
def cloneGraph(node:Node):
       val= node.val
       if val in seen: return seen[val]
       nodeCopy = Node(val)
       seen[val] = nodeCopy
       for neighbor in node.neighbors:
              nodeCopy.neighbors.append(cloneGraph(neighbor))
       return nodeCopy
looked = set()
def printGraph(node:Node):
       if node in looked: return
       looked.add(node)
       print(node.val,end='')
       for x in node.neighbors:
              printGraph(x)

printGraph(node1)
print()
printGraph(cloneGraph(node1))


