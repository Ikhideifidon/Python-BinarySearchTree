from Abstract_Data_Types import ArrayStack, ArrayQueue


class BinarySearchTree:
    # ............................A lightweight, nonpublic class for storing a node.................

    class _Node:
        __slots__ = "key", "left", "right", "parent"

        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        """The height of a tree is the length of the path from the deepest node in the tree.

        The height of a root node (single node tree) is 0.

        The height of an empty tree is -1.
        """
        if node is None:
            node = self.root
        if self.root is None:
            return -1
        leftHeight = self._height(node.left)
        rightHeight = self._height(node.right)
        return max(leftHeight, rightHeight)

    def findMin(self, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            print("Tree is Empty")
            return None
        else:
            if node.left:
                return self.findMin(node.left)
            else:
                return node.key
        return

    def findMax(self, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            print("Tree is Empty")
        else:
            if node.right:
                return self.findMax(node.right)
            else:
                return node.key
        return

    def countChildren(self, node=None):
        """Return the number of children in the Binary Tree."""
        if node is None:
            node = self.root
        if self.root is None:
            print("Tree is Empty")
            return 0
        else:
            count = 0
            if node.left:
                count += 1
            if node.right:
                count += 1
            return count

    def insert(self, key, node=None):
        """Insert a given integer in the proper position in the tree."""
        if not isinstance(key, (int, float)):
            raise TypeError("key must be an integer or a float")
        if node is None:
            node = self.root
        if self.root is None:
            self.root = self._Node(key)
        else:
            # Check if the key to be inserted is less than or equal to the root key
            if key <= node.key:
                if node.left is None:
                    node.left = self._Node(key)
                    node.left.parent = node
                else:
                    self.insert(key, node.left)
            # Check if the key to be inserted is greater than the root key
            else:
                if node.right is None:
                    node.right = self._Node(key)
                    node.right.parent = node
                else:
                    self.insert(key, node.right)
        self.size += 1

    def search(self, key, node=None):
        """Find a given key in a Binary Search Tree and return it if present.

        Otherwise return None.
        """
        if not isinstance(key, (int, float)):
            raise TypeError("key must be an integer or a float")
        if node is None:
            node = self.root
        if self.root is None:
            print("Tree is Empty")
            return None
        # Check if the root of the tree has the desired key
        if self.root.key == key:
            print("key is at the root")
            return self.root
        else:
            if node.key == key:
                print("key exists")
                return node

            elif key < node.key and node.left is not None:
                return self.search(key, node.left)

            elif key > node.key and node.right is not None:
                return self.search(key, node.right)

            else:
                print("Key does not exist")
                return None

    def delete_node(self, node, key):
        """Delete and return the node of a given key."""
        if node is None:
            return node

        # Search for the given key to be deleted

        # if the key is less than the key of the given node:
        if key < node.key:
            node.left = self.delete_node(node.left, key)

        # If the key is greater than the key of the given node:
        elif key > node.key:
            node.right = self.delete_node(node.right, key)

        # If the key is equal to the key of the given node:
        else:
            # case 1 : delete node with no child or only one child node
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # case 2 : Have 2 child nodes: then assign this node to the minimum available node in the right subtree.
            # Find the minimum available key in the right subtree
            # Assign this key to the given node
            temp = self.findMin(node.right)

            node.key = temp
            node.right = self.delete_node(node.right, temp.key)
        return node

    def delete(self, key):
        return self.delete_node(self.root, key)



    def inOrder(self, node=None):
        """Traverse the Left subtree Inorder.

        Visit the root.
        Traverse the Right subtree Inorder.
        """
        if node is None:
            node = self.root
        if self.root is None:
            return None
        stack = ArrayStack()
        result = []
        while stack or node:
            if node:
                stack.push(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.key)
                node = node.right
        return result

    def preOrder(self, node=None):
        """Visit the root.

        Traverse the Left subtree in Preorder.
        Traverse the Right subtree in Preorder.
        """
        if node is None:
            node = self.root
        if self.root is None:
            return None
        result = []
        stack = ArrayStack()
        stack.push(node)
        while stack:
            node = stack.pop()
            result.append(node.key)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)
        return result

    def postOrder(self, node=None):
        """Traverse the Left subtree in Postorder.

        Traverse the Right subtree in Postorder.
        visit the root
        """
        if node is None:
            node = self.root
        if self.root is None:
            return None
        visited = set()
        result = []
        stack = ArrayStack()
        while node or stack:
            if node:
                stack.push(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and node.right not in visited:
                    stack.push(node)
                    node = node.right
                else:
                    visited.add(node)
                    result.append(node.key)
                    node = None
        return result

    def _levelOrderTraversal(self, node):
        """This is also known as Breadth First Traversal.
        Visit the root.

        While traversing level l, keep all the elements at level l+1 in queue.
        Go to the next level and visit all the nodes at that level.
        Repeat this until all levels are completed.
        """
        if node is None:
            return None
        Q = ArrayQueue()
        result = []
        Q.enqueue(node)
        while Q:
            node = Q.dequeue()
            result.append(node.key)
            if node.left:
                Q.enqueue(node.left)
            if node.right:
                Q.enqueue(node.right)
        return result

    def levelOrderTraversal(self):
        return self._levelOrderTraversal(self.root)

    def inorderSuccessor(self, key, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            print("Tree is Empty")
        temp = self.search(key)
        if temp:
            if temp.right:
                return self.findMin(temp.right)
            else:
                successor = self._Node(None)
                ancestor = self.root
                while ancestor != temp:
                    if temp.key < ancestor.key:
                        successor = ancestor
                        ancestor = ancestor.left
                    else:
                        ancestor = ancestor.right
                return successor.key


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(8)
    bst.insert(12)
    bst.insert(4)
    bst.insert(13)
    bst.insert(11)
    bst.insert(15)
    bst.insert(9)


    print(bst.inOrder())
    print(bst.preOrder())
    print(bst.postOrder())
    print(bst.search(12))
    print(bst.levelOrderTraversal())
    print(bst.inorderSuccessor(150))
    print(bst.delete(4))
    print(bst.delete(78))
    print(bst.inOrder())
    print(bst.preOrder())
    print(bst.postOrder())
