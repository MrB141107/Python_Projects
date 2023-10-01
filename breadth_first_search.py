class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def breadth_first_search(root) -> None:

    if root is None:
        print("# No output as the tree is empty.")
        return

    queue = []
    queue.append(root)
    result = []

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.value)
        print(current_node.value, end=" ")

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    print("Breadth-First Search traversal:")
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    # Constructing the search tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Running the breadth-first search
    breadth_first_search(root)

    # Test with an empty tree
    root = None
    breadth_first_search(root)
