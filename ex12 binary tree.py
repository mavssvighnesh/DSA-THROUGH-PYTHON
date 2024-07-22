class binarySearchTree: 
    def __init__(self, val=None): 
        self.val = val 
        self.left = None 
        self.right = None 

    def insert(self, val): 
        if self.val == None: 
            self.val = val 
        else: 
            if val == self.val: 
                return 'no duplicates allowed in binary search tree'
            if val < self.val: 
                if self.left: 
                    self.left.insert(val) 
                else: 
                    self.left = binarySearchTree(val) 
            else: 
                if self.right: 
                    self.right.insert(val) 
                else: 
                    self.right = binarySearchTree(val) 

    def breadthFirstSearch(self): 
        currentNode = self 
        bfs_list = [] 
        queue = [] 
        queue.insert(0, currentNode) 
        while len(queue) > 0: 
            currentNode = queue.pop() 
            bfs_list.append(currentNode.val) 
            if currentNode.left: 
                queue.insert(0, currentNode.left) 
            if currentNode.right: 
                queue.insert(0, currentNode.right) 
        return bfs_list 

    def depthFirstSearch_INorder(self): 
        return self.traverseInOrder([]) 

    def depthFirstSearch_PREorder(self): 
        return self.traversePreOrder([]) 

    def depthFirstSearch_POSTorder(self): 
        return self.traversePostOrder([]) 

    def traverseInOrder(self, lst): 
        if self.left: 
            self.left.traverseInOrder(lst) 
        lst.append(self.val) 
        if self.right: 
            self.right.traverseInOrder(lst) 
        return lst 

    def traversePreOrder(self, lst): 
        lst.append(self.val) 
        if self.left: 
            self.left.traversePreOrder(lst) 
        if self.right: 
            self.right.traversePreOrder(lst) 
        return lst 

    def traversePostOrder(self, lst): 
        if self.left: 
            self.left.traversePostOrder(lst) 
        if self.right: 
            self.right.traversePostOrder(lst) 
        lst.append(self.val) 
        return lst 

    def findNodeAndItsParent(self, val, parent=None): 
        if val == self.val: 
            return self, parent 
        if val < self.val: 
            if self.left: 
                return self.left.findNodeAndItsParent(val, self) 
            else: 
                return 'Not found' 
        else: 
            if self.right: 
                return self.right.findNodeAndItsParent(val, self) 
            else: 
                return 'Not found' 

    def delete(self, val): 
        if self.findNodeAndItsParent(val) == 'Not found': 
            return 'Node is not in tree'
        deleteing_node, parent_node = self.findNodeAndItsParent(val)
        nodes_effected = deleteing_node.traversePreOrder([]) 
        if len(nodes_effected) == 1: 
            if parent_node.left.val == deleteing_node.val: 
                parent_node.left = None
            else: 
                parent_node.right = None 
            return 'Successfully deleted' 
        else: 
            if parent_node == None: 
                nodes_effected.remove(deleteing_node.val) 
                self.left = None 
                self.right = None 
                self.val = None 
                for node in nodes_effected: 
                    self.insert(node) 
                return 'Successfully deleted' 
            nodes_effected = parent_node.traversePreOrder([]) 
            if parent_node.left == deleteing_node: 
                parent_node.left = None
            else: 
                parent_node.right = None 
            nodes_effected.remove(deleteing_node.val) 
            nodes_effected.remove(parent_node.val) 
            for node in nodes_effected: 
                self.insert(node) 
            return 'Successfully deleted' 

bst = binarySearchTree() 
bst.insert(7) 
bst.insert(4) 
bst.insert(9) 
bst.insert(0) 
bst.insert(5) 
bst.insert(8) 
bst.insert(13) 

print('IN order: ', bst.depthFirstSearch_INorder()) 
print('PRE order:', bst.depthFirstSearch_PREorder()) 
print('POST order:', bst.depthFirstSearch_POSTorder()) 
print(bst.delete(5)) 
print(bst.delete(9)) 
print(bst.delete(7)) 
print('IN order: ', bst.depthFirstSearch_INorder()) 
print('PRE order:', bst.depthFirstSearch_PREorder()) 
print('POST order:', bst.depthFirstSearch_POSTorder()) 
