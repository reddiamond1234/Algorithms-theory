class CardinalTreeNode:
    def __init__(self, value, cardinality):
        self.value = value
        self.cardinality = cardinality
        self.children = []

def cardinal_depth_first_traversal(node, encoded_tree):
    encoded_tree.append(0)  # '0' represents the current node
    for _ in range(node.cardinality):
        encoded_tree.append(1)
    for child in node.children:
        cardinal_depth_first_traversal(child, encoded_tree)
    encoded_tree.append(1)

def cardinal_tree_to_dfuds(root):
    encoded_tree = []
    cardinal_depth_first_traversal(root, encoded_tree)
    return encoded_tree

def parent(node, root):
    if node == root:
        return None
    stack = [root]
    while stack:
        current_node = stack.pop()
        if node in current_node.children or node == current_node:
            return current_node
        stack.extend(current_node.children)
    return None


def first_child(node):
    if node.children:
        return node.children[0]
    return None

def child(node, i):
    if i < len(node.children):
        return node.children[i]
    return None

def visualize_cardinal_tree(node, depth=0):
    if node is not None:
        print("  " * depth + f"Node {node.value} (Card: {node.cardinality})")
        for child in node.children:
            visualize_cardinal_tree(child, depth + 1)

# Example Usage:
# Construct a different sample cardinal tree
root_cardinal_node = CardinalTreeNode("A", 3)
root_cardinal_node.children.append(CardinalTreeNode("B", 2))
root_cardinal_node.children.append(CardinalTreeNode("C", 0))
root_cardinal_node.children.append(CardinalTreeNode("D", 1))
root_cardinal_node.children[0].children.append(CardinalTreeNode("E", 0))
root_cardinal_node.children[0].children.append(CardinalTreeNode("F", 2))
root_cardinal_node.children[0].children[1].children.append(CardinalTreeNode("G", 0))
root_cardinal_node.children[0].children[1].children.append(CardinalTreeNode("H", 1))

# Convert the new cardinal tree to DFUDS representation
new_cardinal_encoded_tree = cardinal_tree_to_dfuds(root_cardinal_node)
print("DFUDS Cardinal Representation (Different Tree):", new_cardinal_encoded_tree)

# Test the Parent, FirstChild, and Child functions with the new tree
new_node_to_test = root_cardinal_node.children[0].children[1].children[1]
print("Parent of Node H:", parent(new_node_to_test, root_cardinal_node).value)
print("First Child of Node F:", first_child(root_cardinal_node.children[0].children[1]).value)
print("Second Child of Node A:", child(root_cardinal_node, 1).value)

# Visualize the new cardinal tree
print("\nDifferent Cardinal Tree:")
visualize_cardinal_tree(root_cardinal_node)