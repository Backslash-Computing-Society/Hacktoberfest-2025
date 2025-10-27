"""
Binary Tree Traversal

Implementation of different traversal methods for a binary tree:
- Inorder (Left, Root, Right)
- Preorder (Root, Left, Right)
- Postorder (Left, Right, Root)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Perform inorder traversal of a binary tree.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of values in inorder sequence
    """
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result

def preorder_traversal(root):
    """
    Perform preorder traversal of a binary tree.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of values in preorder sequence
    """
    result = []
    
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return result

def postorder_traversal(root):
    """
    Perform postorder traversal of a binary tree.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of values in postorder sequence
    """
    result = []
    
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
    
    postorder(root)
    return result

# Test cases
if __name__ == "__main__":
    # Create a sample binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Inorder traversal:", inorder_traversal(root))  # [4, 2, 5, 1, 3]
    print("Preorder traversal:", preorder_traversal(root))  # [1, 2, 4, 5, 3]
    print("Postorder traversal:", postorder_traversal(root))  # [4, 5, 2, 3, 1]