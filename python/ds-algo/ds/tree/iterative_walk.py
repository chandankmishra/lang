def preTrav(root):
    stack = [(root, False)]
    preOrder = []
    while stack:
        node, visited = stack.pop()
        if node:
            if not visited:
                stack.extend([(root.right, False), (root.left, False), (root, True)])
            else:
                preOrder.append(root.val)

def inTrav(root):
    stack = [(root, False)]
    inOrder = []
    while stack:
        node, visited = stack.pop()
        if node:
            if not visited:
                stack.extend([(root.right, False), (root, True), (root.left, False)])
            else:
                inOrder.append(root.val)

def postTrav(root):
    stack = [(root, False)]
    postOrder = []
    while stack:
        node, visited = stack.pop()
        if node:
            if not visited:
                stack.extend([(root, True), (root.right, False), (root.left, False)])
            else:
                postOrder.append(root.val)
