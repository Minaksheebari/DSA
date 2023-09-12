class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min(node):
    while node.left:
        node = node.left
    return node

def delete_node(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = find_min(root.right)

        root.val = temp.val

        root.right = delete_node(root.right, temp.val)

    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


root = TreeNode(100)
root.left = TreeNode(50)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

print("Inorder traversal before deletion:")
inorder_traversal(root)
print()

key_to_delete = 30
root = delete_node(root, key_to_delete)

print(f"Node {key_to_delete} deleted.")
print("Inorder traversal after deletion:")
inorder_traversal(root)
