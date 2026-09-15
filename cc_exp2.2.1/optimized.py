class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):

    # Base case
    if root is None or root == p or root == q:
        return root

    # Search in left subtree
    left = lowestCommonAncestor(root.left, p, q)

    # Search in right subtree
    right = lowestCommonAncestor(root.right, p, q)

    # If both sides contain a node,
    # current node is the LCA
    if left and right:
        return root

    # Return whichever side contains p or q
    return left if left else right


# Creating the Binary Tree
#
#          3
#        /   \
#       5     1
#      / \   / \
#     6   2 0   8
#        / \
#       7   4

root = TreeNode(3)

root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)


# p = 5, q = 1
p = root.left
q = root.right


answer = lowestCommonAncestor(root, p, q)

print("Optimized Approach")
print("p =", p.val)
print("q =", q.val)
print("Lowest Common Ancestor =", answer.val)