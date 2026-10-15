from collections import deque



class Node():
    def __init__(self, value = None):
        self.value = value
        self.right = None
        self.left = None
        self.root = None


class BST():
    def __init__(self):
        self.head = None


    def insert(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            self._insert_recursive(self.head, value)
         

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
                node.left.root = node
            else:
                self._insert_recursive(node.left, value)
        if value > node.value:
            if node.right == None:
                node.right = Node(value)
                node.right.root = node
            else:
                self._insert_recursive(node.right, value)

    
    def search(self, value):
        if self.head == None:
            return False
        else:
            if self.head.value == value:
                return self.head
            else:
                return self._search_recursive(self.head, value)


    def _search_recursive(self, node, value):
        if node == None:
            return False
        
        if value < node.value:

            if node.left == None:
                return False
            elif node.left.value == value:
                    return node.left
            else:
                return self._search_recursive(node.left, value)
        
        if value > node.value:

            if node.right == None:
                return False
            elif node.right.value == value:
                return node.right
            else:
                return self._search_recursive(node.right, value)


    def _min_right(self, node):
        if node.left == None:
            tmp = node
            node.root.right = tmp.right
            if tmp.right != None:
                tmp.right.root = node.root
            return tmp.value
        else:
            return self._min_right_recursive(node.left)

            
    def _min_right_recursive(self, node):
        if node.left == None:
            tmp = node
            if tmp.right != None:
                node.root.left = tmp.right
                tmp.right.root = node.root
            else:
                node.root.left = None
            return tmp.value
        else:
            return self._min_right_recursive(node.left)


    def delete(self, value):
        for_delete = self.search(value)
        if for_delete == False:
            return False
        else:
            self._delete(for_delete)
        

    def _delete(self, node):

        root = node.root
        if root == None and (node.right == None or node.left == None):
            if node.right != None:
                self.head = node.right
                self.head.root = None

            elif node.left != None:
                self.head = node.left
                self.head.root = None

            else:
                self.head = None


        elif root == None and node.right != None and node.left != None:
            new_value = self._min_right(node.right)
            node.value = new_value
            node.root = None

        else:
            if node.right == None and node.left == None:
            
                if root.left and root.left.value == node.value:
                    node = None
                    root.left = None
                
                if root.right and node != None and root.right.value == node.value:
                    node = None
                    root.right = None
                

            elif node.right != None and node.left == None:
            

                if root.left and root.left.value == node.value:
                    root.left = node.right
                    root.left.root = root

                if root.right and node != None and root.right.value == node.value:
                    root.right = node.right
                    root.right.root = root
            
            elif node.right == None and node.left != None:
        
                if root.left and root.left.value == node.value:
                    root.left = node.left
                    root.left.root = root

                if root.right and node != None and root.right.value == node.value:
                    root.right = node.left
                    root.right.root = root

            else:
                min_right = self._min_right(node.right)
                node.value = min_right


    def inorder(self):
        result = []
        self._inorder(self.head, result)
        return result


    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)


    def preroder(self):
        results = []
        self._preoder(self.head, results)
        return results


    def _preoder(self, node, results):
        if node:
            results.append(node.value)
            self._preoder(node.left, results)
            self._preoder(node.right, results)

            
    def postorder(self):
        result = []
        self._postoreder(self.head, result)
        return result


    def _postoreder(self, node, results):
        if node:
            self._postoreder(node.left, results)        
            self._postoreder(node.right, results)
            results.append(node.value)

    def level_order(self):
        
        result = []

        if self.head == None:
            return result

        queue = deque()
        queue.append(self.head)

        while queue:
            node = queue.popleft()
            result.append(node.value)

            if node.left:
                queue.append(node.left) 

            if node.right:
                queue.append(node.right)       

        return result