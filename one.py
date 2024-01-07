class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def depth_first_traversal(node, encoded_tree):
    # Encode the current node
    encoded_tree.append(0)  # '0' represents the current node

    # Recursively encode each child
    for child in node.children:
        depth_first_traversal(child, encoded_tree)

    # Add a '1' to indicate the end of children
    encoded_tree.append(1)

def tree_to_dfuds(root):
    encoded_tree = []
    depth_first_traversal(root, encoded_tree)
    return encoded_tree

def dfuds_to_tree(encoded_tree):
    stack = []
    root = TreeNode(0)  # Assuming the root has a value of 0

    current_node = root
    for bit in encoded_tree:
        if bit == 0:
            # Add a new child to the current node
            new_child = TreeNode(len(current_node.children))
            current_node.children.append(new_child)
            stack.append(current_node)
            current_node = new_child
        elif bit == 1:
            # Move back to the parent node
            current_node = stack.pop()

    return root

def visualize_tree(node, depth=0):
    if node is not None:
        print("  " * depth + f"Node {node.value}")
        for child in node.children:
            visualize_tree(child, depth + 1)

# Example Usage:
# Construct a sample tree
root_node = TreeNode(0)
root_node.children.append(TreeNode(1))
root_node.children.append(TreeNode(2))
root_node.children[0].children.append(TreeNode(3))
root_node.children[0].children.append(TreeNode(4))

# Convert the tree to DFUDS representation
encoded_tree = tree_to_dfuds(root_node)
print("DFUDS Representation:", encoded_tree)

# Reconstruct the tree from DFUDS representation
reconstructed_tree = dfuds_to_tree(encoded_tree)

# Visualize the original tree
print("\nOriginal Tree:")
visualize_tree(root_node)

# Visualize the reconstructed tree
print("\nReconstructed Tree:")
visualize_tree(reconstructed_tree)
