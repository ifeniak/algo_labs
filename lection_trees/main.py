class Tree:

    def __init__(self):
        self.root = None

    def search(self, value: int):
        if self._search(self.root, value) is None:
            return False
        return True

    def delete(self, value):
        pass

    def max_value(self):
        pass

    def min_value(self):
        pass

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        self._insert(self.root, value)

    # def _insert_with_search(self, value):

    # found_node = self._search(self.root, value)

    # 2 scenarios
    # 1 scenario: no such value in the Tree
    # found_node.parent =

    def _insert(self, current_node, value):
        # Reminder: is equals to ==

        # go right
        if value > current_node.value:
            # add to the right leaf if absent
            if current_node.right is None:
                current_node.right = Node(value=value, parent=current_node)
                return
            # search for a proper postition in right branch
            return self._insert(current_node.right, value)
        else:
            # add to the left leaf if absent
            if current_node.left is None:
                current_node.left = Node(value=value, parent=current_node)
                return
            # search for a proper position in right branch
            return self._insert(current_node.left, value)

    def _search(self, node_to_check, value):

        # if no more nodes, parent = leaf
        # or we found: search value is equal to the node
        if (node_to_check is None) or (node_to_check.value == value):
            return node_to_check

        if value > node_to_check.value:
            # go right
            return self._search(node_to_check.right, value)
        if value < node_to_check.value:
            # go left
            return self._search(node_to_check.left, value)

    def print(self):
        self._print(self.root)

    def _print(self, node):
        if node is not None:
            print(node.value)
        if node.left is not None:
            self._print(node.left)
        if node.right is not None:
            self._print(node.right)
class Node:

    def __init__(self, value=None, left=None, right=None, parent=None):
        self.right = right
        self.left = left
        self.parent = parent
        self.value = value


tree = Tree()
tree.insert(15)
tree.insert(6)
tree.insert(7)
tree.insert(4)
tree.insert(5)
tree.insert(23)
tree.insert(71)
tree.insert(50)

print(tree.search(10))
print(tree.search(8))
print(tree.search(6))
print(tree.search(6000))
print(tree.search(1))

tree.print()