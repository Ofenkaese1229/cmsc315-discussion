"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):

        # Store the node's value and initialize references
        self.value = value

        # The new node begins without any children
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):

        # Initialize an empty Binary Search Tree
        self.root = None


    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Begin recursive insertion at the root.
        # Smaller values are placed in the left subtree and
        # larger values are placed in the right subtree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # If this position is empty, the correct insertion
        # location has been found, so create a new node.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # If the value equals the current node, no new node is
        # created. This implementation ignores duplicate values.

        # Return the node so the recursive calls reconnect
        # the tree correctly.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Begin the recursive search at the root.
        # A BST can reduce the search space at each comparison
        # because only the left or right subtree needs searching.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reaching an empty position means the value was not found.
        if node is None:
            return False

        # If the current node matches, the search is successful.
        if value == node.value:
            return True

        # A smaller value can only exist in the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # A larger value can only exist in the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Create a list to store values in traversal order.
        values = []

        # Begin the traversal at the root.
        self._inorder_recursive(self.root, values)

        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Stop when an empty child is reached.
        if node is None:
            return

        # Visit all smaller values first.
        self._inorder_recursive(node.left, values)

        # Visit the current node after the left subtree.
        values.append(node.value)

        # Visit all larger values last.
        self._inorder_recursive(node.right, values)

        # Because a BST stores smaller values on the left and
        # larger values on the right, visiting left, node, then
        # right produces the values in sorted order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # Create an empty BST
    my_tree = BST()

    # Insert values that branch into both left and right subtrees.
    values = [40, 25, 95, 10, 50, 70, 80]
    for value in values:
        my_tree.insert(value)

    print("\nValues inserted: ", values)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # The values are sorted because in-order traversal visits
    # the left subtree, the current node, then the right subtree
    print("\nIn-order traversal: ", my_tree.inorder())


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    print("\nSearch for 40: ", my_tree.search(40))
    print("Search for 25: ", my_tree.search(25))
    print("Search for 100: ", my_tree.search(100))
    print("Search for 90: ", my_tree.search(90))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Edge case 1: search and traverse an empty tree
    empty_tree = BST()
    print("\nEmpty tree traversal:", empty_tree.inorder())
    print("Search empty tree for 50:", empty_tree.search(50))

    # Edge case 2: insert a duplicate value
    print("\nTree before duplicate insertion:", my_tree.inorder())
    my_tree.insert(50)
    print("Tree after inserting duplicate 50:", my_tree.inorder())



if __name__ == "__main__":
    main()