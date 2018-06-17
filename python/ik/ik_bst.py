
class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def _get_max_node(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.val


def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left and root.right:
            root.key = _get_max_node(root.left)
            root.left = delete_node(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
    return root


def insert_node(root, key):
    if root is None:
        return BST(key)

    if key < root.val:
        root.left = insert_node(root.left, key)
    else:
        root.right = insert_node(root.right, key)
    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)


def preorder(root):
    if root is None:
        return
    print(root.val, end=' ')
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=' ')


root = None
root = insert_node(root, 20)
root = insert_node(root, 10)
root = insert_node(root, 30)

inorder(root)
print('')
preorder(root)
print('')
postorder(root)
print('')


# def _delete_single(root, val):
#     if root == None:
#         return None

#     if root.left == None:
#         return root.right
#     elif root.right == None:
#         return root.left
#     return None
