class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.right = right
        self.left = left

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):

        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        if key > node.key:
            if node.right is Node:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, node, key):

        if node.key == key:
            return True

        else:
            self.search(node.left, key)
            self.search(node.right, key)


    def delete(self, node, key):
        pass
    
            

        
        