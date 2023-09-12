class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def deleteBinaryTree(root):
    if not root:
        return

    queue = [root]  
    tree_deleted = False 

    while queue:
        current_node = queue.pop(0)  

       
        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

        del current_node

    tree_deleted = True  

    return tree_deleted

root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)

if deleteBinaryTree(root):
    print("The binary tree has been successfully deleted.")
else:
    print("The binary tree was not deleted.")

