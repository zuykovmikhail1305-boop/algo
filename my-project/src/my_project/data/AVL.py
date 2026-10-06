class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.root = None
        self.height = 0
        self.wieght = 0

class BinarySearchTree():
    def __init__(self):
        self.head = None


    def insert(self, value):
        if self.head == None:
            self.head = Node()
            self.head.value = value
        else:
            self._insert_recursive(self.head, value)
         

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left == Node()
                node.left.value = value
                node.left.root = node
                self._update_hieght(node.left, 1)
                check = self._check_balance(node.left)
                self._insert_recursive(node.left, value)
                
        if value > node.value:
            if node.right == None:
                node.right == Node()
                node.right.value = value
                node.right.root = node
                self._update_hieght(node.left, 1)
                check = self._check_balance(node.left)
            else:
                self._insert_recursive(node.right, value)

    def _update_hieght(self, node, new_height):
        if node.root.height < new_height:
            node.root.height = new_height
            self._update_hieght(node.root, new_height + 1)


    def _check_balance(self, node):
        left = 0 if node.left is None else node.left.heigt
        right = 0 if node.right is None else node.right.heigt

        if abs(left - right) <= 1:
            if node.root == None:
                return abs(left - right)
            else:
                self._check_balance(node.root)
        else:
            return left - right

    def _right_small_turn(self, node):
        pass


    def search(self, value):
        if self.head.value == value:
            return self.head
        else:
            self._search_recursive(self.head.value)


    def _search_recursive(self, node, value):
        if value < node.value:
            
            if node.left.value == value:
                return node.left
            elif node.left.value == None:
                return False
            else:
                self._search_recursive(node.left, value)
        
        if value > node.value:
            
            if node.right.value == value:
                return node.right
            elif node.right.value == None:
                return False
            else:
                self._search_recursive(node.right, value)

    
    def _min_right(self, node):
        if node.right == None:
            node.root.right = None
            return node.value
        else:
            self._min_right(node.right)
    
    
    def delete(self, value):
        for_delete = self.search(value)
        self._delete(for_delete)
        

    def _delete(self, node):

        if node.right == None and node.left == None:
            root = node.root

            if root.left.value == node.value:
                node = None
                root.left = None
            
            if root.right.value == node.value:
                node = None
                root.right = None

        elif node.right != None and node.left == None:

                if root.left.value == node.value:
                    root.left = node.right

                if root.right.value == node.value:
                    root.right = node.right
        
        elif node.right == None and node.left != None:

                if root.left.value == node.value:
                    root.left = node.left

                if root.right.value == node.value:
                    root.right = node.left

        else:
            min_right = self._min_right(node)
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
            results.append(node.values)
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
        result.append(self.head.value) 
        self._level_oreder(self.head, result)
        return result


    def _lever_order(self, node, result):
        if node.left:
            result.append(node.left.value)
            self._level_order(node.left, result)
        if node.right:
            result.append(node.right.value)
            self._level_order(node.right, result)
             