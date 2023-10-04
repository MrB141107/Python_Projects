class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

def depth_first_search(root) -> None:
    if root is None:
        print("# No output as the tree is empty.")
        return

    stack = []
    stack.append(root)
    result = []

    while stack:
        current_node = stack.pop()
        result.append(current_node.value)
        print(current_node.value, end=" ")

        # Reverse the order of children to explore in a specific order (e.g., left to right).
        for child in reversed(current_node.children):
            stack.append(child)

    print("Depth-First Search traversal:")
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    # Constructing a tree with arbitrary structure
    root = Node(1)
    root.children = [Node(2), Node(3), Node(4)]
    root.children[0].children = [Node(5), Node(6)]
    root.children[1].children = [Node(7)]
    root.children[2].children = [Node(8), Node(9)]

    # Running the depth-first search
    depth_first_search(root)

    # Test with an empty tree
    root = None
    depth_first_search(root)
