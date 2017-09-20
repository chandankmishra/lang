# A class that represet single node in the binary tree
class Node(object):
    def __init__(self, key=None):
        self.val = key
        self.left = None
        self.right = None


def printPreorder(root):
    if root:
        # Print the node value
        print("{0} ".format(root.val), end='')

        # Recursively walk on the left node
        printPreorder(root.left)

        # Recursively walk on the right node
        printPreorder(root.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder traversal of binary tree")
    printPreorder(root)


if __name__ == "__main__":
    main()

# root.left.left = Node(4)
