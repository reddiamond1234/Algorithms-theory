class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_network = False


def insert_into_trie(root, binary_string):
    node = root
    for bit in binary_string:
        if bit not in node.children:
            node.children[bit] = TrieNode()
        node = node.children[bit]
    node.is_end_of_network = True


def construct_fixed_stride_trie(networks):
    root = TrieNode()

    # Sort networks based on prefixes
    sorted_networks = sorted(networks)

    # Insert each network into the trie
    for network in sorted_networks:
        insert_into_trie(root, network)

    return root


def print_trie_structure(node, level=0, prefix=""):
    if node.is_end_of_network:
        print(f"{'  ' * level} {prefix} (End)")

    for bit, child in node.children.items():
        print_trie_structure(child, level + 1, f"{prefix}{bit}")


# Given networks
networks = ["100*", "01*", "001*", "11*", "1011*", "1*"]

# Construct fixed stride trie
root = construct_fixed_stride_trie(networks)

# Print the trie structure
print_trie_structure(root)
