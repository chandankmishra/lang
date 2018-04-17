# A class that represet single node in the binary tree
class Node(object):
    def __init__(self, key=None):
        self.val = key
        self.left = None
        self.right = None


# Root, Left, Right
def printPreorder(root):
    if root:
        # Print the node value
        print("{0} ".format(root.val), end='')

        # Recursively walk on the left node
        printPreorder(root.left)

        # Recursively walk on the right node
        printPreorder(root.right)


# Left, Root, Right
def printInorder(root):
    if root:
        printInorder(root.left)

        print("{0} ".format(root.val), end='')

        printInorder(root.right)


# Left, Right, Root
def printPostorder(root):
    if root:
        printInorder(root.left)

        printInorder(root.right)

        print("{0} ".format(root.val), end='')


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder traversal of binary tree : ", end='')
    printPreorder(root)
    print()

    print("Inorder traversal of binary tree : ", end='')
    printInorder(root)
    print()

    print("Postorder traversal of binary tree : ", end='')
    printPostorder(root)
    print()


if __name__ == "__main__":
    main()

# root.left.left = Node(4)
